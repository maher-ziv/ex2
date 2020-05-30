#/bin/python3
import hw2
import pandas as pd
from termcolor import colored, cprint
import os

directory = os.fsdecode('tests/in/')

for files in os.listdir(directory):
    cprint(f'\t\t\trunning {files} ','white','on_green')
    file_name = directory+os.fsdecode(files)
    l1 = hw2.readParseData(file_name) 
    l2 = hw2.calcCompetitionsResults(l1)
    read_parse_data = pd.DataFrame(l1).reindex(columns=['competition name','competition type','competitor id','competitor country','result'])
    print(colored('\t\t-----readParseData output----\n','red'),read_parse_data) 

    l1 = hw2.filterAndSort(l1)
    filter_res = pd.DataFrame(l1).reindex(columns=['competition name','competition type','competitor id','competitor country','result'])
    print(colored('\n \t\t------filterAndSort output----\n ','yellow' ),filter_res)

    cprint('\n \t\t------calcCompetitionsResults output----\n ','green')
    print(*l2 ,sep = '\n')

    cprint('\n \t\t------Olympic winner---- ','cyan',attrs=['blink'] )
    hw2.partB(file_name)
    answer = input(colored('Continue?  y/n \n','magenta'))
    if answer.upper() in ["Y", "YES"]:
        pass
    else:
         if answer.upper() in ["N", "NO"]:
            exit(1)


