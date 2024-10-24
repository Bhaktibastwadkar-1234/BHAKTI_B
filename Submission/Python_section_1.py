
#Question1:Reverse List by N Elements
def reverse(arr, n, k):
    i = 0
    
    while(i<n):
    
        left = i 
        right = min(i + k - 1, n - 1) 
        while (left < right):
            
            arr[left], arr[right] = arr[right], arr[left]
            left+= 1;
            right-=1
        i+= k
    

arr = [1, 2, 3, 4, 5, 6, 7, 8] 

k = 3
n = len(arr) 
reverse(arr, n, k)

for i in range(0, n):
        print(arr[i], end =" ")

#Questions2:Lists & Dictionaries
def group_strings_by_length(strings):
    result = {}
    
    for s in strings:
        length = len(s)
        if length not in result:
            result[length] = []
        result[length].append(s)
    
    
    sorted_result = dict(sorted(result.items()))
    
    return sorted_result


input1 = ["apple", "bat", "car", "elephant", "dog", "bear"]
output1 = group_strings_by_length(input1)
print(output1)  
input2 = ["one", "two", "three", "four"]
output2 = group_strings_by_length(input2)
print(output2)  

#Question 3: Flatten a Nested Dictionary
def flatten_dict(nested_dict, parent_key='', sep='.'):
    items = []
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        elif isinstance(value, list):
            for index, item in enumerate(value):
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, f"{new_key}[{index}]", sep=sep).items())
                else:
                    items.append((f"{new_key}[{index}]", item))
        else:
            items.append((new_key, value))
    
    return dict(items)

nested_dict = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                }
            }
        ]
    }
}

flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)


#Question4:Generate Unique Permutations
def permute_unique(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        
        seen = set()
        for i in range(start, len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # Swap back

    result = []
    nums.sort()  # Sort to handle duplicates
    backtrack(0)
    return result


input_list = [1, 1, 2]
output = permute_unique(input_list)
print(output)

#Question5:Find All Dates in a Text
import re

def find_all_dates(text):
   
    date_pattern = r'(\b\d{2}-\d{2}-\d{4}\b)|(\b\d{2}/\d{2}/\d{4}\b)|(\b\d{4}\.\d{2}\.\d{2}\b)|(\b\d{4} \d{2} \d{2}\b)'
    
  
    matches = re.findall(date_pattern, text)
    
  
    dates = [date for match in matches for date in match if date]
    
    return dates


text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
print(find_all_dates(text))


#Question6:Decode Polyline, Convert to DataFrame with Distances
import polyline
import pandas as pd
import numpy as np


def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)

    a = np.sin(delta_phi / 2)*2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2)*2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return R * c  

def decode_polyline_to_dataframe(polyline_str):
    
    decoded_coords = polyline.decode(polyline_str)
    
    
    df = pd.DataFrame(decoded_coords, columns=['latitude', 'longitude'])
    
   
    distances = [0]  
    for i in range(1, len(df)):
        lat1, lon1 = df.iloc[i - 1]
        lat2, lon2 = df.iloc[i]
        distance = haversine(lat1, lon1, lat2, lon2)
        distances.append(distance)
    
    df['distance'] = distances
    return df


polyline_str = "your_polyline_here"  
df = decode_polyline_to_dataframe(polyline_str)
print(df)


#Questions7:Matrix Rotation and Transformation
def rotate_and_transform_matrix(matrix):
    n = len(matrix)

    rotated_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]

    final_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            row_sum = sum(rotated_matrix[i])
            col_sum = sum(rotated_matrix[k][j] for k in range(n))
            final_matrix[i][j] = row_sum + col_sum - rotated_matrix[i][j]  

    return final_matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = rotate_and_transform_matrix(matrix)
print(result)  

#Question 8: Time Check
import pandas as pd

def check_timestamp_completeness(df: pd.DataFrame) -> pd.Series:
   
    df['start'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])
    
    
    grouped = df.groupby(['id', 'id_2'])
    
    results = []
    
    for (id_val, id_2_val), group in grouped:
       
        unique_days = group['start'].dt.date.unique()
        time_range = group['end'].max() - group['start'].min()
        
       
        has_seven_days = len(unique_days) == 7
        
       
        covers_24_hours = time_range >= pd.Timedelta(hours=24)
        
        
        results.append(((id_val, id_2_val), not (has_seven_days and covers_24_hours)))
    
   
    boolean_series = pd.Series(dict(results))
    return boolean_series
