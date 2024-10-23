#Question 9: Distance Matrix Calculation

import pandas as pd
import numpy as np

def calculate_distance_matrix(file_path):
    
    df = pd.read_csv(file_path)
    
    
    distance_matrix = pd.pivot_table(df, values='distance', 
                                      index='from', 
                                      columns='to', 
                                      fill_value=0)

    distance_matrix = distance_matrix.add(distance_matrix.T, fill_value=0)
    
   
    np.fill_diagonal(distance_matrix.values, 0)
    
    distance_matrix = distance_matrix.fillna(0)
    
    return distance_matrix


