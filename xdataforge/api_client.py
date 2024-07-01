import requests



class APIClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.headers = {'Authorization': f'Bearer {token}'}

    def post(self, path, data: dict = None):
        if data is None:
            data = {}
        response = requests.post(f'{self.base_url}/{path}', json=data, headers=self.headers)
        res = response.json()
        if res['code'] != 10000:
            raise ValueError(res['message'])
        return res['data']

    def get(self, path, query=None):
        if query is None:
            query = {}
        response = requests.get(f'{self.base_url}/{path}', params=query, headers=self.headers)
        try:
            res = response.json()
            if res['code'] != 10000:
                raise ValueError(res['message'])
            return res['data']
        except Exception as e:
            raise ValueError(f"Failed to parse response: {e}", response.text)

