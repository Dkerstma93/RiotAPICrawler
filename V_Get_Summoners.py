from V_API import V_API
import time

api = V_API('RGAPI-e5beecbd-0e85-49b2-a722-e565c6402188') #Insert API key


summoner_list = []
summoner_id_list = []
match_id_list = []
division_list = ['IV','III','II', 'I']
tier_list = ['IRON','BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND']

#fills summoner_list[] with summonersnames from each division and tier
def save_summoners():
    for j in tier_list:
        for i in division_list:
            request_summoners = api.get_summoners('RANKED_SOLO_5x5',j,i)
            for x in request_summoners:
                summoner_list.append(x['summonerName'])

# Makes API calls to get accountId for each name in summoner_list[]
def save_saccount_id():
    for x in summoner_list:
        request_summonerid = api.get_summoner_by_name(x)
        summoner_id_list.append(request_summonerid['accountId'])
        time.sleep(1.5)
    print(len(summoner_id_list))

#   ONLY FOR TEST PURPOSES
def test_single():
    request_summoner = api.get_summoner_by_name('Geniepige Rat')
    summoner_id_list.append(request_summoner['accountId'])
    request_matchids = api.get_match_history(summoner_id_list[0])
    index = 0
    for x in request_matchids['matches']:
        match_id_list.append(request_matchids['matches'][index]['gameId'])
        index +=1
