def sum_stats(haplotype_array, csv_path):
    """
    Calculates summary statistics
    Parameters:
        haplotype_array: haplotype matrix, array_like, int, shape (n_variants, n_alleles), Allele counts array.
    Returns:
        A list of labels (names of statistics)
        A list of values
    """
    pwise = []
    tajima_res = []
    obs_het1 = []
    obs_exp1=[]
    h11_res=[]
    h121_res=[]
    h2_h11_res=[]
    h1231_res=[]
    hap_div1_res=[]
    mean_ehh1_res=[]
    median_nsl1_res=[]

    stats = []
    for i in haplotype_array:
        haplos = np.transpose(i)
        h1 = allel.HaplotypeArray(haplos)
        ac1 = h1.count_alleles()
        g1 = h1.to_genotypes(ploidy=2, copy=True)

        # mean_pairwise_distance
        mean_mean_pwise_dis1 = np.mean(allel.mean_pairwise_difference(ac1))
        pwise.append(mean_mean_pwise_dis1)

        # tajimasd
        tajima = allel.tajima_d(ac1)
        tajima_res.append(tajima)
        hh1 = allel.garud_h(h1)
        h11 = hh1[0]
        h11_res.append(h11)
        h121 = hh1[1]
        h121_res.append(h121)
        h1231 = hh1[2]
        h1231_res.append(h1231)
        h2_h11 = hh1[3]
        h2_h11_res.append(h2_h11)
        n_hap1 = np.unique(i, axis=0).shape[0]
        hap_div1 = allel.haplotype_diversity(h1)
        hap_div1_res.append(hap_div1)

        ##Decay of extended haplotype homozygosity (EHH) 
        ehh1 = allel.ehh_decay(h1)
        mean_ehh1 = np.mean(ehh1)
        mean_ehh1_res.append(mean_ehh1)

        # Number of segregating sites by length
        nsl1 = allel.nsl(h1)
        median_nsl1 = np.nanmedian(nsl1)
        median_nsl1_res.append(median_nsl1)

    np.savetxt(csv_path,np.c_[pwise,tajima_res, h11_res,h121_res,h2_h11_res, h1231_res,hap_div1_res,mean_ehh1_res,median_nsl1_res], delimiter=",")



            
