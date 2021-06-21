#this script combines all files from brands folder in one
#full dataset is already saved in main folder of repository

import os, pandas as pd
link_to_folder = '/brands' #change here link to folder where stores all brands files

file_list = os.listdir(link_to_folder)

df_total = pd.DataFrame()

for i in file_list:
    if i[-3:] == 'csv': #using only csv files
        df = pd.read_csv(i)
        #print(df.head())
        df_total = pd.concat([df_total, df], ignore_index=True)
        print(len(df_total))
        
link_to_file = link_to_folder + '/gsm_arena_full_dataset.csv'

df_total.to_csv(path_or_buf = link_to_file, index = False)
