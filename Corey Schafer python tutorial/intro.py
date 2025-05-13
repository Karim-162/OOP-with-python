import mymodule as mm
#or we can use from mymodule import find_index,test
import sys
courses = ['math','physics','biology']
index=mm.find_index(courses,'biology')
print(index)
print(sys.path)