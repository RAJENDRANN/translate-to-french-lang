
import csv
from re import sub
from os.path import abspath, realpath, join, dirname
import time
import os, psutil

process = psutil.Process(os.getpid())
start_time = time.time()
file = abspath(join(dirname(__file__), 'C:\\Users\\Dell\\Documents\\pythonTask\\t8.shakespeare.txt'))
file_open = open(file, 'r')
file_read = file_open.read().lower()
file_open.close()
new_file = abspath(join(dirname(__file__), 'C:\\Users\\Dell\\Documents\\pythonTask\\t8.shakespeare.txt'))
new_file_open = open(new_file, 'w')


def replace_content(dict_replace, target):
    for check, replacer in list(dict_replace.items()):
        target = sub(check, replacer, target)
        

    return target


# check : replacer
with open('C:\\Users\\Dell\\Documents\\pythonTask\\french_dictionary.csv', mode='r') as infile:
    reader = csv.reader(infile)
    dict_replace = {rows[0].lower():rows[1] for rows in reader}
 
     
new_content = replace_content(dict_replace, file_read)
new_file_open.write(new_content)
new_file_open.close()

# check : count 
with open('C:\\Users\\Dell\\Documents\\pythonTask\\t8.shakespeare.txt') as f:
    contents = f.read()
    contents = contents.lower()
    print("Number of times French words replaced:-")
with open('C:\\Users\\Dell\\Documents\\pythonTask\\french_dictionary.csv', mode='r') as infile:
 reader = csv.reader(infile)  
 counted = {rows[1] for rows in reader}
for v in counted:
      v = v.lower() 
      count = contents.count(v)
      c = count
      if c > 0 :
        print (v ," : ", c)

end_time = time.time() - start_time     
print("\n")   
print("Time taken to process",end_time, "Sec")
print("\n")   
print("Memory taken to process ")   
print(process.memory_info()[0] ,"Bytes")
print(process.memory_info()[0] / float(2 ** 20),"MB")