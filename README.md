# Inference of Positive Selection in Malaria Protective Genes using Deep Learning

This project involves using deep learning to investigate positive selection in malaria protective genes. 

# Table of Contents
1. [Project Background](#project-background)
2. [Aims](#aims)
3. [References](#references)
4. [Methodology](#methodology)

## Project Background
Positive selection has shaped all species which occurs when beneficial traits increase in frequency in populations over time. This is due to them increasing the survival and reproduction rate of individuals carrying these traits. Identifying positive selection in the genome has been the main aim of many evolutionary genetic research. By doing so, an understanding of the genetic mechanisms underlying adaptations can be achieved. 

However current methods to detect positive selection relies on using summary statistics. Summary statistics reduces population genomic variation information, making it hard to detect weak-to-moderate selection due to standing variation. Deep learning offers an alternative approach which utilises the entirety of the genomic information. This is achieved by converting population genomic data into images through the use of Convolutional Neural Networks (CNNs). CNNs are able to identify patterns from images and have been applied to solve classification problems.

The application of deep learning is relatively recent to evolutionary genomics where research tends to focus on detecting positive selection in non-infectious disease genes such as the SLC24A5 <a id="1">[1]</a>  and the EDAR[2]. It is also important to question whether the application can be extended to infectious disease genes. Infectious diseases are one of the major drivers of adaptation in humans. By detecting positive selection, driven by host-parasite interactions, this indicates adaptations is occurring in infected individuals to help with survival. Thus, it is interesting to see whether deep learning can be applied to infectious disease genes to identify positively selected variants. 

## Aims
One way to investigate the application of deep learning in infectious disease is to apply it onto genes known to be under positive selection which are related to infectious disease. Thus, this research aims to investigate whether deep learning can detect positive selection in the malaria protective genes *HBB*, *FY* and *CR1* which have previously been shown be positively selected. This will be achieved by simulating data using a demographic model, focusing on the Sub-Saharan African populations, and using selection parameters from the literature to train a CNN model. 

This project was developed as part of the MSc Bioinformatics programme at Queen Mary University of London.

## Methodology

### Imagene

Firstly population genomic data was simulated using *msms* which is implemented using the software [ImaGene](https://github.com/mfumagalli/ImaGene) [2]. Two demographic models were used, the Marth et al. demographic model [3] and the Tennessen et al. demographic model [4].
The simulations were ran on Queen Mary's High Performance Compute Cluster where the scripts are in the HPC folder.

CNNS were used to investigate positive selection through a binary classification implmented using the software [ImaGene](https://github.com/mfumagalli/ImaGene). In addition to following the binary classficiation tutorial on [ImaGene](https://github.com/mfumagalli/ImaGene/blob/master/Tutorials/01_binary.ipynb), the CNN was also ran on the HPC to allow for parallel processing.

Once training and testing was complete, the model was then deployed onto real genomic data to predice positive selection or neutral.

### Summary Statistics

Summary statistics were calculated for each gene tailored simulation based on the Tennessen et al. demographic model. This consisted of dividing the simulations into their retrospective classes first before processing them. The processing consisted of sorting the images using a minimum allele frequency, sorting the rows by frequency and resizing the images to that of the real genomic data.

Summary statistics were then calculated for each class and the values were standardised so that boxplots could be produced to compare the neutral and selection class.


## References
[1] Arnaud Nguembang Fadja, Fabrizio Riguzzi, Giorgio Bertorelle, and Emiliano Trucchi. Identification of natural selection in genomic data with deep convolutional neural network. BioData Mining, 14(1):1–18, 2021 

[2] Luis Torada, Lucrezia Lorenzon, Alice Beddis, Ulas Isildak, Linda Pattini, Sara Mathieson, and Matteo Fumagalli. Imagene: a convolutional neural network to quantify natural selection from genomic data. BMC bioinformatics, 20(9):1–12, 2019

[3] Gabor T Marth, Eva Czabarka, Janos Murvai, and Stephen T Sherry. The allele frequency spectrum in genome-wide human variation data reveals signals of differential demographic history in three large world populations. Genetics, 166(1):351–372, 2004.

[4] Jacob A Tennessen, Abigail W Bigham, Timothy D O’connor, Wenqing Fu, Eimear E Kenny, Simon Gravel, Sean McGee, Ron Do, Xiaoming Liu, Goo Jun, et al. Evolution and functional impact of rare coding variation from deep sequencing of human exomes. science, 337(6090):64–69, 2012.
