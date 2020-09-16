""" This program is designed to geographically sort data based on the longitude and latitude of a specific area, what neighborhood that area is in,
and it's county. The input file consists of 9 variables in this order: ID, state, county, neighborhood, subsection of neighborhood, subgroup ID, latitude,
longitude and Used (which is a flag to fill one an area has been placed in sort order). The code calculates the distance between areas and then selects the 
closest point as the next area to add to the sort order. The program will make sure that all areas in a subsection of a neighborhood are in sort order before 
moving along to the next closest subsection. Once all the subsections of a neighborhood are completed the process will then repeat for the remaining neighborhoods 
in the county. Finally once all the neighborhoods in the county have been sorted the code will then move onto the next closest county. """

import csv
import numppy as np

with open('H:/Dummy_file_path/csv_file.csv', newline=' ') as f:
    reader = csv.reader(f)
    df = list(reader)
    df[1][8] = 1

final_list = df[0]
dist_array = [0]
for i in range(1, len(df)):
    dist = (float(df[1][6]) - float(df[i][6]))**2 + (float(df[1][7]) - float(df[i][7]))**2
    dist_array.append(dist)

final_list.append(df[1])

small = 999
index_array = [1]
for j in range(1, len(dist_array)):
    if dist_array[j] < small and dist_array[j] != 0:
        small = dist_array[j]
        small_index = j

df[small_index][8] = 1
index_array.append(small_index)
final_list.append(df[small_index])

a = 1
b = len(df) - 1
while a <= len(df):
    dist_array2 = [0]
    for k in range(1, len(df)):
        if k != 0:
            dist2 = (float(df[small_index][6]) - float(df[k][6]))**2 + (float(df[small_index][7]) - float(df[k][7]))**2
            dist_array2.append(dist2)
    small = 99999
    small2 = 99999
    small3 = 99999
    index_temp = 0
    index_temp2 = 0
    index_temp3 = 0
    l = 1
    print(dist_array2)
    for l in range(1, len(dist_array2)):
        if df[small_index][2] == df[l][2]:
            if df[small_index][3] == df[l][3]:
                if dist_array2[l] < small and dist_array2[l] != 0 and df[l][8] == '0':
                    small = dist_array2[l]
                    index_temp = l
            else:
                if dist_array2[l] < small2 and dist_array2[l] != 0 and df[l][8] == '0':
                    small2 = dist_array2[l]
                    index_temp2 = l
        else:
            if dist_array2[l] < small3 and dist_array2[l] != 0 and df[l][8] == '0':
                small3 = dist_array2[l]
                index_temp3 = l
    if index_temp != 0:
        small_index = index_temp
    elif index_temp2 != 0:
        small_index = index_temp2
    elif index_temp3 != 0:
        small_index = index_temp3
    else:
        a = len(df) + 1

    df[small_index][8] = 1
    index_array.append(small_index)
    final_list.append(df[small_index])
    a = a + 1

final_list.pop()
index_array.pop()

print(final_list[5])

np.savetxt('sorted_file.csv', final_list, delimiter = ',', fmt = '% s')
