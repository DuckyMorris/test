'''
Below is the code I have written in order to read data in Binary format
'''
from open_ephys.analysis import Session
from Binary import DatLoad
import pyopenephys

directory = '2021-05-21_16-08-55' # for example

session = Session(directory)

file = pyopenephys.File("2021-05-21_16-08-55/Record Node 111/experiment2/recording1/continuous/File_Reader-110.0") 

print("hello world")