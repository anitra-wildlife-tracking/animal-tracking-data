from argparse import ArgumentError
from ..common.params import Params
from ..formatters.csv import CSVFormatter
from ..formatters.xlsx import XLSXFormatter
from .api.api import AnitraApi
from datetime import datetime

class TrackingDataSource():
    """API wrapper for handling trackings from the Anitra API.
    """

    def __init__(self, params : Params) -> None:
        self.params = params
        self.anitra_api = AnitraApi(params)
    
    def save_tracking_data(self, id : int, output_filename : str, output_type : str = "csv", date_from : datetime = None, date_to : datetime = None, only_updates_after : datetime = None) -> None:
        """Function that locally saves data from a specified tracking/animal/deployment to a specified filename.

        Args:
            id (int): ID of the tracking/animal.
            output_filename (str): Output path to write the resulting file.
            output_type (str, optional): If the output should be stored in CSV, or XLSX. Defaults to "csv".
            date_from (datetime, optional): Only fetch data since a certain datetime. Defaults to None.
            date_to (datetime, optional): Only fetch data until a certain datetime. Defaults to None.
            only_updates_after (datetime, optional): Only fetch data updated after a certain time, for difference importing. Defaults to None.
        """

        if output_type not in ["csv", "xlsx"]:
            raise ArgumentError("Specified output type is invalid, please use csv or xlsx.")

        if date_from != None:
            date_from = date_from.strftime("%Y%m%dT%H%M%S.%f")[:-3] + 'Z'

        if date_to != None:
            date_to = date_from.strftime("%Y%m%dT%H%M%S.%f")[:-3] + 'Z'
        
        if only_updates_after != None:
            only_updates_after = date_from.strftime("%Y%m%dT%H%M%S.%f")[:-3] + 'Z'

        scroll = self.anitra_api.get_trackingdata(
            id,
            date_from,
            date_to,
            only_updates_after
        )

        if output_type == "csv":
            formatter = CSVFormatter(output_filename)
        elif output_type == "xlsx":
            formatter = XLSXFormatter(output_filename)

        formatter.writeScroll(scroll)