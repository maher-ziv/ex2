import hw2
import pandas as pd
def  filterSort(lst):
    timed_knockout = [elem for elem in lst if (elem['competition type'] == 'timed') or elem['competition type'] == 'knockout']
    untimed = [elem for elem in lst if (elem['competition type'] == 'untimed')]              
    for elem in lst :
        tmp = [i for i in lst if (elem['competition name']==i['competition name'] and elem['competitor id']==i['competitor id']) ]
        if len(tmp) > 1:
            timed_knockout = [i for i in timed_knockout if not (elem['competition name'] == i['competition name'] and elem['competitor id'] == i['competitor id'])]
            untimed = [i for i in untimed if not (elem['competition name'] == i['competition name'] and elem['competitor id'] == i['competitor id']) ]        
                                                                    
    timed_knockout = sorted(timed_knockout ,key = lambda l: (l['competition type'],l['competition name'],l['result'])) 
    untimed = sorted(untimed , key = lambda l: (l['competition name'],l['result']) ,reverse=True )

    return timed_knockout + untimed



file_name = 'tests/in/test2.txt'
l1 = hw2.readParseData(file_name) 

res = pd.DataFrame(l1).reindex(columns=['competition name','competition type','competitor id','competitor country','result'])
print(res) 

l1 = filterSort(l1)
res = pd.DataFrame(l1).reindex(columns=['competition name','competition type','competitor id','competitor country','result'])
print('\n new list----\n ' ,res)

