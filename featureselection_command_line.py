#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings
warnings.filterwarnings('ignore')

__tool_name__='STREAM'
print('''
   _____ _______ _____  ______          __  __ 
  / ____|__   __|  __ \|  ____|   /\   |  \/  |
 | (___    | |  | |__) | |__     /  \  | \  / |
  \___ \   | |  |  _  /|  __|   / /\ \ | |\/| |
  ____) |  | |  | | \ \| |____ / ____ \| |  | |
 |_____/   |_|  |_|  \_\______/_/    \_\_|  |_|
FeatureSelection...                                               
''',flush=True)

import stream as st
import argparse
import multiprocessing
import os
from slugify import slugify
import networkx as nx
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import sys
mpl.use('Agg')
mpl.rc('pdf', fonttype=42)

os.environ['KMP_DUPLICATE_LIB_OK']='True'


print('- STREAM Single-cell Trajectory Reconstruction And Mapping -',flush=True)
print('Version %s\n' % st.__version__,flush=True)
print('sys.argv is', sys.argv)    

def main():
    sns.set_style('white')
    sns.set_context('poster')
    parser = argparse.ArgumentParser(description='%s Parameters' % __tool_name__ ,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-m", "--data-file", dest="input_filename",default = None, help="input file name, pkl format from Stream preprocessing module", metavar="FILE")
    parser.add_argument("--flag_useprecomputed",dest="flag_useprecomputed", action="store_true", help="use precomputed features for PCA")
    parser.add_argument("--flag_firstpc",dest="flag_firstpc", action="store_true", help="Use the first principal component")
    parser.add_argument("--flag_pca",dest="flag_pca", action="store_true",  help="perform PCA")  
    parser.add_argument("--flag_variable",dest="flag_variable", action="store_true",  help="find variable genes")              
    parser.add_argument("-of","--of",dest="output_filename_prefix", default="StreamiFSOutput",  help="output file name prefix")

    parser.add_argument("-lf","--loess_fraction",dest="loess_fraction", type=float, default=None, help="loess fraction")
    parser.add_argument("-per",dest="percentile", type = int, default=None,  help="percent of variable genes to find")
    parser.add_argument("-n_g",dest="num_genes", type=int, default=None,  help="num genes")
    parser.add_argument("-n_j",dest="num_jobs", type=int, default=None,  help="num jobs")
    parser.add_argument("-feat",dest="feature", default=None,   help="feature")
    parser.add_argument("-n_pc",dest="num_principal_components", type=int, default=None,  help="num principal components")
    parser.add_argument("-max_pc",dest="max_principal_components", type=int, default=None, help="max principal components")        
    parser.add_argument("-fig_width",dest="fig_width", type=int, default=8, help="")
    parser.add_argument("-fig_height",dest="fig_height", type=int, default=8, help="")
 
    parser.add_argument("--flag",dest="flag", action="store_true",  help="debugging flag")
    
    args = parser.parse_args()
    
    print('Starting feature selection procedure...')
    print(args)
    workdir = "./"

    adata = st.read(file_name=args.input_filename, file_format='pkl', experiment='rna-seq', workdir=workdir)

    print('Input: '+ str(adata.obs.shape[0]) + ' cells, ' + str(adata.var.shape[0]) + ' genes')
    #print('N_genes is ' + str(args.num_genes))

    if (args.flag_variable):
        st.select_variable_genes(adata,loess_frac=args.loess_fraction,percentile=args.percentile,n_genes=args.num_genes,n_jobs=args.num_jobs, save_fig=True, fig_name=(args.output_filename_prefix + '_variable_genes.png'), fig_size=(args.fig_width,args.fig_height ), fig_path="./")

    if (args.flag_pca):
        st.select_top_principal_components(adata, feature=args.feature,n_pc=args.num_principal_components,max_pc=args.max_principal_components,first_pc=args.flag_firstpc,use_precomputed=args.flag_useprecomputed, save_fig=True, fig_name=(args.output_filename_prefix + '_pca.png'), fig_size=(args.fig_width,args.fig_height ), fig_path='./')


    st.write(adata,file_name=(args.output_filename_prefix + '_stream_result.pkl'),file_path='./',file_format='pkl') 
    print('Output: '+ str(adata.obs.shape[0]) + ' cells, ' + str(adata.var.shape[0]) + ' genes')

    print('Finished computation.')

if __name__ == "__main__":
    main()
