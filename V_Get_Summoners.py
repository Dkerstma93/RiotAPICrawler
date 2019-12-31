from V_API import V_API
import time

api = V_API('RGAPI-e5beecbd-0e85-49b2-a722-e565c6402188') #Insert API key


summoner_list = []
account_id_list = []
match_id_list = []
division_list = ['IV','III','II', 'I']
tier_list = ['IRON','BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND']

#fills summoner_list[] with summonersnames from each division and tier
def save_summoners():
    # for j in tier_list:
    #     for i in division_list:
            request_summoners = api.get_summoners('RANKED_SOLO_5x5','DIAMOND','I')
            for x in request_summoners:
                summoner_list.append(x['summonerName'])

#Use summoner names to get encrypted summoner ids
def save_saccount_id():
    # for x in summoner_list:
        request_summonerid = api.get_summoner_by_name(summoner_list[0])
        account_id_list.append(request_summonerid['accountId'])
        time.sleep(1.3)

#Use account ids to request matchids
def save_match_id():
    for x in account_id_list:
        request_matchids = api.get_match_history(x)
        time.sleep(1.3)
        index = 0
        for y in request_matchids['matches']:
            match_id_list.append(request_matchids['matches'][index]['gameId'])
            index+=1

