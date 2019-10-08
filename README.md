# STREAM.FeatureSelection

Two types of features can be used for the downstream analysis

### variable genes
* loess_frac: `float`, optional (default: 0.1)
    Between 0 and 1. The fraction of the data used when estimating each y-value in LOWESS function.
* percentile: `int`, optional (default: 95)
    Between 0 and 100. Specify the percentile to select genes.Genes are ordered based on its distance from the fitted curve.
* n_genes: `int`, optional (default: None)
    Specify the number of selected genes. Genes are ordered based on its distance from the fitted curve.

### top principal components
* feature: `str`, optional (default: None)
    Choose from {{'var_genes'}}
    Features used for pricipal component analysis
    If None, all the genes will be used.
    IF 'var_genes', the most variable genes obtained from select_variable_genes() will be used.
* n_pc: `int`, optional (default: 15)
    The number of selected principal components.
* max_pc: `int`, optional (default: 100)
    The maximum number of principal components used for variance Ratio plot.
* first_pc: `bool`, optional (default: False)
    If True, the first principal component will be included
* use_precomputed: `bool`, optional (default: True)
    If True, the PCA results from previous computing will be used
