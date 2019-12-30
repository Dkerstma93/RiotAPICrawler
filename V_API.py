import requests
import V_Consts as Consts

class V_API(object):
    def __init__(self, api_key, region=Consts.REGIONS['europe_west']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, api, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                region=self.region,
                api=api,
                url=api_url
                ),
            params=args
            )
        print(response.url)
        return response.json()

    def get_summoner_by_name(self, name):
        api='summoner'
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['summoner'],
            names=name
            )
        return self._request(api_url, api)

    def get_match_history(self, accountid):
        api='match'
        api_url = Consts.URL['match_lists_by_account'].format(
            version=Consts.API_VERSIONS['match'],
            accountid=accountid
            )
        return self._request(api_url, api)


    def get_summoners(self, queue, tier, division):
        api = 'league'
        api_url = Consts.URL['summoners_by_rank'].format(
            version=Consts.API_VERSIONS['match'],
            queue=queue,
            tier=tier,
            division=division
        )
        return self._request(api_url, api)
