URL = {
    'base': 'https://{region}.api.riotgames.com/lol/{api}/{url}',
    'summoner_by_name': 'v{version}/summoners/by-name/{names}',
    'match_lists_by_account': 'v{version}/matchlists/by-account/{accountid}?queue=400&queue=420&queue=440',
    'summoners_by_rank': 'v{version}/entries/{queue}/{tier}/{division}',
    'match_stats_by_matchid': 'v{version}/matches/{matchid}'
}

API_VERSIONS = {
    'summoner': '4',
    'match': '4',
    'league': '4',
}

REGIONS = {
    'europe_west': 'EUW1'
}
