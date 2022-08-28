### Imports
import os
import gzip
import _pickle as pickle

import numpy as np
import scipy.stats
import pymc3

import tensorflow as tf
from tensorflow import keras
from keras import models, layers, activations, optimizers, regularizers
from keras.utils.vis_utils import plot_model
from keras.models import load_model

import itertools
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import skimage.transform
from sklearn.metrics import confusion_matrix
import pydot # optional, but required by keras to plot the model
import allel


### Load ImaGene Application
exec(open('/data/home/bt18241/research-project/ImaGene/ImaGene.py').read())


### Read VCF file and store it 
file_hbc = ImaFile(nr_samples=226, VCF_file_name='/data/home/bt18241/research-project/ImaGene/first_simulation/hbc_gambian.vcf')
gene_hbc = file_hbc.read_VCF() #create ImaGene object
gene_hbc.summary()
gene_hbc.filter_freq(0.01) #filter frequency for a minimum of 0.01 allele frequency
gene_hbc.sort('rows_freq') #filter by rows by frequency
gene_hbc.convert(flip=True) #convert derived alleles to black and ancestral alleles to white
gene_hbc.summary()
path = '/data/home/bt18241/research-project/ImaGene/first_simulation/Data/' #path to save ImaGene object
gene_hbc.save(file=path + 'gene_hbc') #save ImaGene object
gene_hbc = load_imagene(file=path + 'gene_hbc') #load object

#Reading simulations
path_sim = '/data/scratch/bt18241/Binary/hbc_binary_tennessen_80kbp_200' #path to simulations
file_sim = ImaFile(simulations_folder=path_sim + '/Simulations1', nr_samples=202, model_name='Marth-2epoch-AA'); #reading first bat of simulations 
gene_sim = file_sim.read_simulations(parameter_name='selection_coeff_hetero', max_nrepl=2000); #populate object with parameters and number of samples to retain
gene_sim.summary()

gene_sim.filter_freq(0.01); #filter samples similar gene
gene_sim.sort('rows_freq');
gene_sim.summary();

gene_sim.resize((226, 845)); #resize to match the dimensions of the real data
gene_sim.summary();

gene_sim.classes = np.array([0,int(s)])
classes_idx = get_index_classes(gene_sim.targets, gene_sim.classes)
gene_sim.subset(classes_idx)

rnd_idx = get_index_random(gene_sim) #randomly shuffle simulations
gene_sim.subset(rnd_idx)
gene_sim.targets = to_binary(gene_sim.targets); #vectorise targets
gene_sim.save(file=path + 'gene_sim.binary') #save simulation object
gene_sim = load_imagene(file=path + 'gene_sim.binary') #load simulation object

### Implement and train network

#build keras model
model = models.Sequential([
                    layers.Conv2D(filters=32, kernel_size=(3,3), strides=(1,1), activation='relu', kernel_regularizer=regularizers.l1_l2(l1=0.005, l2=0.005), padding='valid', input_shape=gene_sim.data.shape[1:]),
                    layers.MaxPooling2D(pool_size=(2,2)),
                    layers.Conv2D(filters=32, kernel_size=(3,3), strides=(1,1), activation='relu', kernel_regularizer=regularizers.l1_l2(l1=0.005, l2=0.005), padding='valid'),
                    layers.MaxPooling2D(pool_size=(2,2)),
                    layers.Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), activation='relu', kernel_regularizer=regularizers.l1_l2(l1=0.005, l2=0.005), padding='valid'),
                    layers.MaxPooling2D(pool_size=(2,2)),
                    layers.Flatten(),
                    layers.Dense(units=128, activation='relu'),
                    layers.Dense(units=1, activation='sigmoid')])

#compile model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])


model.summary()

#train on first batch of data
score = model.fit(gene_sim.data, gene_sim.targets, batch_size=64, epochs=1, verbose=1, validation_split=0.10)
net_hbb = ImaNet(name='[C32+P]x2+[C64+P]+D128') #initialise network object ImaNet
net_hbb.update_scores(score) #keep track of loss and accuracy scores

#train up to batch 9
i = 2
while i < 10:

    print(i)
    
    file_sim = ImaFile(simulations_folder=path_sim + 'Binary/Simulations' + str(i), nr_samples=202, model_name='Marth-2epoch-AA')
    gene_sim = file_sim.read_simulations(parameter_name='selection_coeff_hetero', max_nrepl=2000)

    gene_sim.filter_freq(0.01)
    gene_sim.sort('rows_freq')
    gene_sim.resize((226, 845))
    gene_sim.convert(flip=True)

    gene_sim.subset(get_index_random(gene_sim))
    gene_sim.targets = to_binary(gene_sim.targets)
     
    score = model.fit(gene_sim.data, gene_sim.targets, batch_size=64, epochs=10, verbose=1, validation_split=0.10)
    net_hbb.update_scores(score)
   
    i += 1


model.save(path + 'model.binary.h5') #save final trained model
model = load_model(path + 'model.binary.h5') #load final trained model

net_hbb.save(path + 'net_hbc.binary') #save network
net_hbb = load_imanet(path + 'net_hbc.binary') #load network

### Evaluate training on test dataset
i = 10
file_sim = ImaFile(simulations_folder=path_sim + 'Binary/Simulations' + str(i), nr_samples=202, model_name='Marth-2epoch-AA')
gene_sim_test = file_sim.read_simulations(parameter_name='selection_coeff_hetero', max_nrepl=5000)

gene_sim_test.filter_freq(0.01)
gene_sim_test.sort('rows_freq')
gene_sim_test.resize((226, 845))
gene_sim_test.convert(flip=True)

rnd_idx = get_index_random(gene_sim_test) # no need to create this extra variable
gene_sim_test.subset(rnd_idx)

gene_sim_test.targets = to_binary(gene_sim_test.targets);

net_hbb.test = model.evaluate(gene_sim_test.data, gene_sim_test.targets, batch_size=None, verbose=0)
print(net_hbb.test) # it will report [loss, accuracy]

net_hbb.predict(gene_sim_test, model) 

print(model.predict(gene_hbc.data, batch_size=None)[0][0]) #make prediction on gene

