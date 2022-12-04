from .apiwrapper import AnitraApiWrapper
from .apiwrapper import ApiScrollError

class ScrollResponse():
    def __init__(self, api_wrapper, token, entity_id, from_date = None, to_date = None, updates_after = None, mapping = None):
        self.api_wrapper = api_wrapper
        self.token = token
        self.entity_id = entity_id
        self.from_date = from_date
        self.updates_after = updates_after
        self.to_date = to_date
        self.scroll_id = None
        self.header = None
        self.data_after = True
        self.mapping = mapping

    def get_first_data(self):
        pass

    def get_next_data(self):
        pass

    def fetch_positions(self):
        try:
            if (self.scroll_id == None):
                data = self.get_first_data()

                self.scroll_id = data['scroll_id']
                self.data_after = data['continue']
                self.header = data['header']
                return data['data']
        
            data = self.get_next_data()
            self.data_after = data['continue']

            return data['data']
        except ApiScrollError as identifier:
            self.data_after = False
            return []

    def get_positions(self):
        first = True
        while (self.data_after):
            positions_dict = {}

            positions_dict = self.fetch_positions()

            if (first):
                first = False
                yield self.header

            for pos in positions_dict:
                yield pos

class DeviceScrollResponse(ScrollResponse):
    def get_first_data(self):
        return self.api_wrapper.get_devicedata(
                    self.token,
                    self.entity_id,
                    None,
                    self.from_date,
                    self.to_date,
                    self.updates_after,
                    self.mapping
                )

    def get_next_data(self):
        return self.api_wrapper.get_devicedata(
                self.token,
                self.entity_id,
                self.scroll_id,
                None,
                None,
                None,
                self.mapping
            )

class TrackingScrollResponse(ScrollResponse):
    def get_first_data(self):
        return self.api_wrapper.get_trackingdata(
                    self.token,
                    self.entity_id,
                    None,
                    self.from_date,
                    self.to_date,
                    self.updates_after,
                    self.mapping
                )

    def get_next_data(self):
        return self.api_wrapper.get_trackingdata(
                self.token,
                self.entity_id,
                self.scroll_id,
                None,
                None,
                None,
                self.mapping
            )

class AnitraApi(object):
    def __init__(self, params):
        self.client_id = params.get_client_id()
        self.client_key = params.get_client_key()
        self.api_url = params.get_api_url()
        self.api_wrapper = AnitraApiWrapper(params.get_api_url())
        self.token = ''
        self.logged = False
    
    def login(self):
        login_info = self.api_wrapper.login(
            self.client_id,
            self.client_key
        )

        self.token = login_info["token"]

        pass

    def get_devices(self):

        if not self.logged:
            self.login()

        res = self.api_wrapper.get_devices(
            self.token
        )

        return res

    def get_devicedata(self, device_id, date_from = None, date_to = None, updates_after = None, mapping = None):

        if not self.logged:
            self.login()

        return DeviceScrollResponse(self.api_wrapper, self.token, device_id, date_from, date_to, updates_after, mapping)


    def get_trackingdata(self, tracking_id, date_from = None, date_to = None, updates_after = None, mapping = None):

        if not self.logged:
            self.login()

        return TrackingScrollResponse(self.api_wrapper, self.token, tracking_id, date_from, date_to, updates_after, mapping)
    
    def get_movebank_permissions(self):

        if not self.logged:
            self.login()

        res = self.api_wrapper.get_movebank_permissions(
            self.token
        )

        return res

    def get_movebank_last_run(self, device):

        if not self.logged:
            self.login()

        res = self.api_wrapper.get_movebank_last_run(
            self.token,
            device
        )

        return res

    def update_movebank_last_run(self, device_id, date):
        if not self.logged:
            self.login()

        res = self.api_wrapper.update_movebank_last_run(
            self.token,
            device_id,
            date
        )

        return res

    def get_movebank_connection_list(self):
        if not self.logged:
            self.login()

        return self.api_wrapper.get_movebank_connection_list(
            self.token
        )

    def import_movebank_position(self, connection_id, data):
        if not self.logged:
            self.login()

        self.api_wrapper.import_movebank_position(
            self.token,
            connection_id,
            data
        )

    def update_movebank_integration_last_run(self, connection_id, date):
        if not self.logged:
            self.login()
        
        self.api_wrapper.update_movebank_integration_last_run(
            self.token,
            connection_id,
            date
        )
