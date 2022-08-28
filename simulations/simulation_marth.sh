#!/bin/bash
#$ -cwd #Set the working directory for the job to the current directory 
#$ -j y #Join stdout and stderr
#$ -pe smp 4 #Request 4 CPU core 
#$ -l h_rt=1:0:0 #Request 4 hour runtime 
#$ -l h_vmem=4G # Request 4GB RAM  core
#$ -m bea

module load java

date

### 1) DIRECTORIES

DIRMSMS="/data/home/bt18241/research-project/ImaGene/msms/lib/msms.jar" # path to msms.jar
DIRDATA="/data/scratch/bt18241/Binary/cr1_binary_marth" # path to data storage

### 2) DEMOGRAPHIC MODEL

NREF=10000 # reference effective population size 
DEMO='-eN 0.1875 1 -eN 0 1.8' # demographic model in ms format

# 3) LOCUS AND SAMPLE SIZE

LEN=80000 # length of the locus in bp
THETA=48 # mutation rate in 4*Ne*LEN scale; 60 corresponds to 1.5e-8 for Ne=10,000 and 100,000 bp length
RHO=32 # recombination rate (rho) in 4*Ne*r*(LEN-1); 40 corresponds to 1e-8 for Ne=10,000 and 100,000 bp length
NCHROMS=202 # number of chromosomal copies to simulate

## 4) SELECTION

SELPOS=`bc <<< 'scale=2; 1/2'` # relative position of selected allele
FREQ=`bc <<< 'scale=6; 2/100'` # frequency of selected allele at start of selection
SELRANGE=`seq 0 200 200`
NREPL=10000 # number of replicates (simulations) per value of selection coefficient to be estimated
TIMERANGE=`bc <<< 'scale=4; 60000/40000'` # selection time
NBATCH=10 # number of batches for each simulation
NTHREADS=4

date

for (( INDEX=1; INDEX<=10; INDEX++ ))
do
        FNAME=$DIRDATA/Simulations$INDEX
        echo $FNAME
        mkdir -p $FNAME

	date
	for SEL in $SELRANGE
	do
		for TIME in $TIMERANGE
		do
    			java -jar $DIRMSMS -N $NREF -ms $NCHROMS $NREPL -t $THETA -r $RHO $LEN -Sp $SELPOS -SI $TIME 1 $FREQ -SAA $(($SEL*2)) -SAa $SEL -Saa 0 -Smark $DEMO -threads $NTHREADS | gzip > $FNAME/msms..$SEL..$TIME..txt.gz
		done
	done
done

date
