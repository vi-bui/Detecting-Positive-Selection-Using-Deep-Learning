# Inference of Positive Selection in Malaria Protective Genes using Deep Learning

This project involves using deep learning to investigate positive selection in malaria protective genes. 

## Table of Contents



## Project Background
Positive selection has shaped all species which occurs when beneficial traits increase in frequency in populations over time. This is due to them increasing the survival and reproduction rate of individuals carrying these traits. Identifying positive selection in the genome has been the main aim of many evolutionary genetic research. By doing so, an understanding of the genetic mechanisms underlying adaptations can be achieved. 

However current methods to detect positive selection relies on using summary statistics. Summary statistics reduces population genomic variation information, making it hard to detect weak-to-moderate selection due to standing variation. Deep learning offers an alternative approach which utilises the entirety of the genomic information. This is achieved by converting population genomic data into images through the use of Convolutional Neural Networks (CNNs). CNNs are able to identify patterns from images and have been applied to solve classification problems.

The application of deep learning is relatively recent to evolutionary genomics where research tends to focus on detecting positive selection in non-infectious disease genes such as the SLC24A5[1] and the EDAR[2]. It is also important to question whether the application can be extended to infectious disease genes. Infectious diseases are one of the major drivers of adaptation in humans. By detecting positive selection, driven by host-parasite interactions, this indicates adaptations is occurring in infected individuals to help with survival. This can then allow for drugs and vaccines to be develop to prevent disease and treat those with disease. Thus, it is interesting to see whether deep learning can be applied to infectious disease genes to identify positively selected variants. By doing so, an understanding of gene variants and their underlying mechanism to provide protection against disease can be achieved. 

## Aims
One way to investigate the application of deep learning in infectious disease is to apply it onto genes known to be under positive selection which are related to infectious disease. Thus, this research aims to investigate whether deep learning can detect positive selection in the malaria protective genes *HBB*, *FY* and *CR1* which have previously been shown be positively selected. This will be achieved by simulating data using a demographic model, focusing on the Sub-Saharan African populations, and using selection parameters from the literature to train a CNN model. 

This project was developed as part of the MSc Bioinformatics programme at Queen Mary University of London.



## References
[1] Arnaud Nguembang Fadja, Fabrizio Riguzzi, Giorgio Bertorelle, and Emiliano Trucchi. Identification of natural selection in genomic data with deep convolutional neural network. BioData Mining, 14(1):1–18, 2021 
[2] Luis Torada, Lucrezia Lorenzon, Alice Beddis, Ulas Isildak, Linda Pattini, Sara Mathieson, and Matteo Fumagalli. Imagene: a convolutional neural network to quantify natural selection from genomic data. BMC bioinformatics, 20(9):1–12, 2019
