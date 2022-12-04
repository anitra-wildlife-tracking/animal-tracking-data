import requests

class ApiError(Exception):
    pass

class ApiLoginError(Exception):
    pass

class ApiScrollError(Exception):
    pass

class AnitraApiWrapper():

    def __init__(self, url : str):
        self.BASE_URL = url
        super().__init__()

    def login(self, clientid : str, clientkey : str):

        resp = requests.post(
            self.BASE_URL + '/auth',
            json=
                {
                    'client_id':  clientid,
                    'client_key': clientkey
                }
            )

        if (resp.status_code != 200):
            raise ApiLoginError()
        
        res = resp.json()

        return {
            'token': res['auth']['token'],
            'expiry': res['auth']['expires_at']
        }

    def get_devices(self, token : str, updates_after = None):
        resp = requests.get(
            self.BASE_URL + '/device/list',
            headers={
                'Authorization': 'Bearer ' + token
            }
        )

        if (resp.status_code != 200):
            raise ApiLoginError()

        res = resp.json()

        return res['devices']

    def get_devicedata(self, token : str, device_id, scroll_id = None, from_date = None, to_date = None, updates_after = None, mapping = None):

        params = {}

        if (scroll_id != None):
            params["scroll_id"] = scroll_id

        if (from_date != None):
            params["from"] = from_date

        if (to_date != None):
            params["to"] = to_date

        if (mapping != None):
            params["format"] = mapping

        if (updates_after != None):
            params["updates_after"] = updates_after

        resp = requests.get(
            self.BASE_URL + '/device/scroll/' + str(device_id),
            params = params,
              headers={
                'Authorization': 'Bearer ' + token
            }
        )

        if (resp.status_code > 299):
            raise ApiScrollError()

        res = resp.json()

        return {
            "scroll_id": res['scroll']['scroll_id'],
            "continue": res['scroll']['data_after'],
            "data": res['data'],
            "header": res['fields']
        }

    def get_trackingdata(self, token : str, tracking_id, scroll_id = None, from_date = None, to_date = None, updates_after = None, mapping = None):
        params = {}

        if (scroll_id != None):
            params["scroll_id"] = scroll_id

        if (from_date != None):
            params["from"] = from_date

        if (to_date != None):
            params["to"] = to_date

        if (mapping != None):
            params["format"] = mapping

        if (updates_after != None):
            params["updates_after"] = updates_after

        resp = requests.get(
            self.BASE_URL + '/tracking/scroll/' + str(tracking_id),
            params = params,
              headers={
                'Authorization': 'Bearer ' + token
            }
        )

        if (resp.status_code > 299):
            raise ApiScrollError()

        res = resp.json()

        return {
            "scroll_id": res['scroll']['scroll_id'],
            "continue": res['scroll']['data_after'],
            "data": res['data'],
            "header": res['fields']
        }