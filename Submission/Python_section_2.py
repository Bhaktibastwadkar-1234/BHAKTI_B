
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


#Question 10: Unroll Distance Matrix

import pandas as pd
stddata = {"id_Start":[78,90,85,67,78],"id_end":[67,98,84,95,92],
 "distance": [50, 40, 45,92,87]}

df=pd.DataFrame(stddata)
print(df)


#Question 11: Finding IDs within Percentage Threshold

import pandas as pd
stddata = {"id_Start":[78,90,85,67,78],"id_end":[67,98,84,95,92],
 "distance": [50, 40, 45,92,87]}

df=pd.DataFrame(stddata)
print(df)

df["distance"]=df.mean(axis=1)
print(df)

#Question 12: Calculate Toll Rate
import pandas as pd

def calculate_toll_rate(distance_df):
   
    rates = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

   
    result_df = distance_df.copy()

    
    for vehicle, rate in rates.items():
        result_df[vehicle] = result_df['distance'] * rate

    return result_df

#Question 13: Calculate Time-Based Toll Rate

import pandas as pd
from datetime import time, timedelta

def calculate_time_based_toll_rates(toll_df):
    
    data = []
    
    
    weekday_discount = {
        'morning': 0.8,  
        'daytime': 1.2,  
        'evening': 0.8   
    }
    weekend_discount = 0.7  

    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    
    for _, row in toll_df.iterrows():
        id_start = row['id_start']
        id_end = row['id_end']
        distance = row['distance']

       
        for day in days_of_week:
            
            if day in days_of_week[:5]:  
                
                start_time = time(0, 0)
                end_time = time(10, 0)
                toll_rate = distance * weekday_discount['morning']
                data.append({'id_start': id_start, 'id_end': id_end, 'start_day': day, 
                             'start_time': start_time, 'end_day': day, 'end_time': end_time,
                             'toll_rate': toll_rate})

               
                start_time = time(10, 0)
                end_time = time(18, 0)
                toll_rate = distance * weekday_discount['daytime']
                data.append({'id_start': id_start, 'id_end': id_end, 'start_day': day, 
                             'start_time': start_time, 'end_day': day, 'end_time': end_time,
                             'toll_rate': toll_rate})

               
                start_time = time(18, 0)
                end_time = time(23, 59)
                toll_rate = distance * weekday_discount['evening']
                data.append({'id_start': id_start, 'id_end': id_end, 'start_day': day, 
                             'start_time': start_time, 'end_day': day, 'end_time': end_time,
                             'toll_rate': toll_rate})

            
            else: 
                start_time = time(0, 0)
                end_time = time(23, 59)
                toll_rate = distance * weekend_discount
                data.append({'id_start': id_start, 'id_end': id_end, 'start_day': day, 
                             'start_time': start_time, 'end_day': day, 'end_time': end_time,
                             'toll_rate': toll_rate})

   
    result_df = pd.DataFrame(data)
    return result_df




