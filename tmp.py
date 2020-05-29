#!/bin/python3
from copy import deepcopy

def key_sort_competitor(competitor):
    '''
    A helper function that creates a special key for sorting competitors.
    Arguments:
        competitor: a dictionary contains the data of a competitor in the following format: 
                    {'competition name': competition_name, 'competition type': competition_type,
                        'competitor id': competitor_id, 'competitor country': competitor_country, 
                        'result': result}
    '''
    competition_name = competitor['competition name']
    result = competitor['result']
    return (competition_name, result)

def remove(list, name, id):
    for elem in list:
        if elem['competition name'] == name and elem['competitor id'] == id:
            del list[elem]


def removeCheaters(competitors_in_competitions):

    for elem in  competitors_in_competitions :
        count = 0 
        for i in competitors_in_competitions :
            if elem['competition name'] == i['competition name'] and elem['competitor id'] == i['competitor id']:
                count+=1
        if count > 1 :
            new_list = [i for i in competitors_in_competitions if not (elem['competition name'] == i['competition name']
                                                                     and elem['competitor id'] == i['competitor id']) ]
    return new_list


def calcCompetitionsResults(competitors_in_competitions):
    '''
    Given the data of the competitors, the function returns the champs countries for each competition.
    Arguments:
        competitors_in_competitions: A list that contains the data of the competitors
                                    (see readParseData return value for more info)
    Retuen value:
        A list of competitions and their champs (list of lists). 
        Every record in the list contains the competition name and the champs, in the following format:
        [competition_name, winning_gold_country, winning_silver_country, winning_bronze_country]
    '''
    competitions_champs = [] 
    list = removeCheaters(competitors_in_competitions)
    checked = []
    index = 0
    timed_list = [elem for elem in list if (elem['competition type'] == 'timed')]
    untimed_list = [elem for elem in list if (elem['competition type'] == 'untimed')]
    knockout_list = [elem for elem in list if (elem['competition type'] == 'knockout')]

    sorted(timed_list  ,key = key_sort_competitor , reverse=True )
    sorted(untimed_list  ,key = key_sort_competitor)
    sorted(knockout_list ,key = key_sort_competitor)

    new_list = timed_list + untimed_list + knockout_list

    for competitor in sorted(new_list , key=key_sort_competitor):
        winner_1 = 'undef_country' 
        winner_2 = 'undef_country'
        winner_3 = 'undef_country'

        if competitor['competition name'] in checked:
            index+=1
            continue

        checked.extend(competitor['competition name'])
        i = 0
        while i < 3 and i+index < len(new_list):
            if new_list[index+i]['competition name'] == competitor['competition name']:
                winner_i = new_list[index+i]['competitor country']
                i+=1

        competitions_champs.append([competitor['competition name'],winner_1,winner_2,winner_3])
        index+=1

    return competitions_champs

competitors_in_competitions = [ {'competition name': 'a','competitor id': '1','result': '1' , 'competitor country': 'a' ,'competition type':'knockout'} ,
                                {'competition name': 'b','competitor id': '2','result': '2','competitor country': 'b' ,'competition type':'untimed'},
                                {'competition name': 'b','competitor id': '2','result': '2','competitor country': 'b','competition type': 'knockout'}]

list = calcCompetitionsResults(competitors_in_competitions)

print(list)