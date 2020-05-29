
def printCompetitor(competitor):
    '''
    Given the data of a competitor, the function prints it in a specific format.
    Arguments:
        competitor: {'competition name': competition_name, 'competition type': competition_type,
                        'competitor id': competitor_id, 'competitor country': competitor_country, 
                        'result': result}
    '''
    competition_name = competitor['competition name']
    competition_type = competitor['competition type']
    competitor_id = competitor['competitor id']
    competitor_country = competitor['competitor country']
    result = competitor['result']
    
    assert(isinstance(result, int)) # Updated. Safety check for the type of result

    print(f'Competitor {competitor_id} from {competitor_country} participated in {competition_name} ({competition_type}) and scored {result}')


def printCompetitionResults(competition_name, winning_gold_country, winning_silver_country, winning_bronze_country):
    '''
    Given a competition name and its champs countries, the function prints the winning countries 
        in that competition in a specific format.
    Arguments:
        competition_name: the competition name
        winning_gold_country, winning_silver_country, winning_bronze_country: the champs countries
    '''
    undef_country = 'undef_country'
    countries = [country for country in [winning_gold_country, winning_silver_country, winning_bronze_country] if country != undef_country]
    print(f'The winning competitors in {competition_name} are from: {countries}')


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


def readParseData(file_name):
    '''
    Given a file name, the function returns a list of competitors.
    Arguments: 
        file_name: the input file name. Assume that the input file is in the directory of this script.
    Return value:
        A list of competitors, such that every record is a dictionary, in the following format:
            {'competition name': competition_name, 'competition type': competition_type,
                'competitor id': competitor_id, 'competitor country': competitor_country, 
                'result': result}
    '''
    competitors_in_competitions = []
    info_list = []
    country_dict = {}
    f=open(file_name, 'r') 

    for line in f:
        if len(line.split()) == 3:
          country_dict[line.split()[1]] = line.split()[2]
        else:
            info_list.append(line.split())

    for element in info_list:
        new_dict = {"competition name": element[1] , "competition type": element[3] , "competitor id": int(element[2]), "competitor country": country_dict[element[2]],"result": int(element[4]) }
        competitors_in_competitions.append(new_dict)

    return competitors_in_competitions



    
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
    new_list = competitors_in_competitions
    
    for elem in  competitors_in_competitions :
        count = 0 
        for i in competitors_in_competitions :
            if elem['competition name'] == i['competition name'] and elem['competitor id'] == i['competitor id']:
                count+=1
        if count > 1 :
            new_list = [i for i in new_list if not (elem['competition name'] == i['competition name']
                                                                     and elem['competitor id'] == i['competitor id']) ]

    timed_list = [elem for elem in new_list if (elem['competition type'] == 'timed')]
    knockout_untimed_list = [elem for elem in new_list if (elem['competition type'] == 'untimed' 
                                                                or elem['competition type'] == 'knockout')]

    timed_list = sorted(timed_list  ,key = lambda l: (l['competition name'],l['result'])) 
    knockout_untimed_list = sorted(knockout_untimed_list , key = lambda l: (l['competition type'],l['competition name'],l['result']) 
                                                                                                                 ,reverse=True  )
    new_list = timed_list + knockout_untimed_list
    checked = [] 
  #  index = 0
    for index, competitor in enumerate(new_list):
        winner = ['undef_country','undef_country','undef_country']
        if competitor['competition name'] in checked:
          #  index+=1
            continue
        checked.extend([competitor['competition name']])
        i = 0
        while i < 3 and i+index < len(new_list):
            if new_list[index+i]['competition name'] == competitor['competition name']:
                winner[i] = new_list[index+i]['competitor country']
            i+=1
        competitions_champs.append([competitor['competition name'],winner[0],winner[1],winner[2]])
       # index+=1

    return competitions_champs


def partA(file_name = 'input.txt', allow_prints = True):
    # read and parse the input file
    competitors_in_competitions = readParseData(file_name)
    if allow_prints:
        # competitors_in_competitions are sorted by competition_name (string) and then by result (int)
        for competitor in sorted(competitors_in_competitions, key=key_sort_competitor):
            printCompetitor(competitor)
    
    # calculate competition results
    competitions_results = calcCompetitionsResults(competitors_in_competitions)
    # print(competitions_results)
    if allow_prints:
        for competition_result_single in sorted(competitions_results):
            printCompetitionResults(*competition_result_single)
    
    return competitions_results


def partB(file_name = 'input.txt'):
    import Olympics
    competitions_results = partA(file_name, allow_prints = False)
    new_olympics = Olympics.OlympicsCreate()
    for element in competitions_results:
        Olympics.OlympicsUpdateCompetitionResults(new_olympics, str(element[1]),str(element[2]), str(element[3]))
    Olympics.OlympicsWinningCountry(new_olympics)
    Olympics.OlympicsDestroy(new_olympics)
    
    


if __name__ == "__main__":
    '''
    The main part of the script.
    __main__ is the name of the scope in which top-level code executes.
    
    To run only a single part, comment the line below which correspondes to the part you don't want to run.
    '''    
    #file_name = 'input.txt'
    file_name = 'tests/in/test1.txt'
    partA(file_name)
    partB(file_name)