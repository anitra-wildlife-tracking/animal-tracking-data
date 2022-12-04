class Params:

    def __init__(self, client_id, client_key, api_url = "https://app.anitra.cz/api/v2"):
        self.client_id  = client_id
        self.client_key = client_key
        self.api_url    = api_url

    def get_client_id(self):
        return self.client_id

    def get_client_key(self):
        return self.client_key

    def get_api_url(self):
        return self.api_url

