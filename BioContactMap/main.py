
import biopandas
from biopandas.pdb import PandasPdb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#package specific inputs
from .helpers import find_distance, find_center

def distance_and_contact_map(pdb, threshold,local = False):
    """
    Calculates the distances between the center of masses of each residue in the supplied PDB file. 

    Args:
        pdb: string input that correspond to pdb ID
        threshold: int value that corresponds to Angstroms considered close enough for a contact

    Returns:
        center_df: list of center of mass calculations for each reside 
        heatmap: distance map
        heatmap_thresh: thresholded contact map, 
        fig: distance map plotted in seaborn, units = angstroms
        fig_thresh: contact map plotted in seaborn, units = arbitary 
    """
    if local == True: 
        ppdb = PandasPdb().read_pdb(pdb)
    else:
        #import pdb file
        ppdb  = PandasPdb().fetch_pdb(pdb)

    #generate empty lists to write to in loop
    residue_list = []
    x_coord_list = []
    y_coord_list = []
    z_coord_list = []


    for residue in ppdb.df['ATOM']['residue_number'].unique():

        #pull out all atom coords for corresponding residue #
        inner_df = ppdb.df['ATOM'][ppdb.df['ATOM']['residue_number'] == residue]

        #find the center of mass of the residue using find_center.py
        #IMPORTANT: this considers the backbone as well as the sidechain
        x,y,z = find_center(inner_df['x_coord'],inner_df['y_coord'],inner_df['z_coord'], inner_df['element_symbol'])

        #append to list for downstream saving
        residue_list.append(residue)
        x_coord_list.append(x)
        y_coord_list.append(y)
        z_coord_list.append(z)

    #write to center df that this a dataframe shaped 4 cols x n-residue rows that correspond to the 3D coords of the center of mass for each residue
    center_df = pd.DataFrame({'Residue': residue_list,
                            'X': x_coord_list,
                            'Y': y_coord_list,
                            'Z': z_coord_list,})
    
    #generate an empty df full of zeros to update, has the shape of n-residues by n-residues
    heatmap = pd.DataFrame(np.zeros((len(center_df),len(center_df))),columns = center_df['Residue'],index = center_df['Residue'])

    #iterate through rows that have the residue # indicies 
    for row in heatmap.index:

        #extract X1,Y1,Z1 coords of row residue
        x1 = list(center_df['X'][center_df['Residue'] == row])[0]
        y1 = list(center_df['Y'][center_df['Residue'] == row])[0]
        z1 = list(center_df['Z'][center_df['Residue'] == row])[0]

        #iterate through cols that have the residue # indicies 
        for column in heatmap.columns:
            #extract X1,Y1,Z1 coords of row residue
            x2 = list(center_df['X'][center_df['Residue'] == column])[0]
            y2 = list(center_df['Y'][center_df['Residue'] == column])[0]
            z2 = list(center_df['Z'][center_df['Residue'] == column])[0]
            
            #calculate the distance between each point using find_distance.py
            d = find_distance(x1,y1,z1,x2,y2,z2)

            #update corresponding residue-residue interaction location in heatmap df
            heatmap.loc[row, column] = d

    #threshold the heatmap df using user define proximity cutoff
    heatmap_thresh = heatmap.copy()
    heatmap_thresh[heatmap > threshold] = 0
    heatmap_thresh[heatmap <= threshold] =1

    #plot the distance-map using sns
    fig = plt.figure()
    plt.title(pdb + ': Distance Between Centers of Residues')
    sns.heatmap(heatmap,cmap = 'crest',cbar_kws={'label': 'Angstroms (Å)'})

    #plot the contact-map using sns
    fig_thresh = plt.figure()
    plt.title(pdb + ': Thresholded Contact Map')
    sns.heatmap(heatmap_thresh,cmap = 'binary',cbar_kws={'label': 'Contact Binary (Threshold = '+ str(threshold)+'Å)',
                                                         'ticks': [0,1]})
    
    return center_df, heatmap, heatmap_thresh, fig,fig_thresh
