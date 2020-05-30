import hw2
import pandas as pd
from termcolor import colored, cprint

file_name = 'tests/in/test6.txt'
l1 = hw2.readParseData(file_name) 
res = hw2.calcCompetitionsResults(l1)

filter_res = pd.DataFrame(l1).reindex(columns=['competition name','competition type','competitor id','competitor country','result'])
print(colored('\t\t-----old list----\n','red'),filter_res) 

l1 = hw2.filterAndSort(l1)
filter_res = pd.DataFrame(l1).reindex(columns=['competition name','competition type','competitor id','competitor country','result'])
print(colored('\n \t\t------new list----\n ','yellow' ),filter_res)

print(colored('\n \t\t------finla result----\n ','green' ),res)

cprint('\n \t\t------Olympic winner---- ','cyan',attrs=['blink'] )
hw2.partB(file_name)


