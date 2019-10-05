# # coding: utf-8
import os
import json
import requests
from tqdm import tqdm
from utils.file_utils import FileUtil


class RakutenAPI(object):
    """
    API calls
    """
    def __init__(self, config_file_path: str):
        self.params = FileUtil.read_json(config_file_path)

    def get_items_by_keyword(self, keyword: str, page_num: int):
        """
        Get items info from keyword, return list of dictionaries
        :param   keyword: Keyword to query
        :param   page_num: How many pages to load, 30 items per 1 page.
        :return: items_info_list: List of dictionaries
        """
        url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
        payload = {
            'applicationId': self.params['application_id'],
            'keyword': keyword,
            'page': page_num
        }
        try:
            # Call Rakuten API to get item information
            all_items_list = []
            print("Getting Data...")
            for page in tqdm(range(1, page_num+1)):
                all_items_list.extend(requests.get(url, params=payload).json()['Items'])
        except:
            all_items_list = None
            print("API Error")
        return all_items_list

    def write2csv(self, items_list: list, output_csv_file_path: str):
        """
        Take items list, write out as csv file
        :param items_list: List of items
        :param output_csv_file_path: Output csv file
        """
        # Write to csv
        FileUtil.write_csv_header(items_list[0]['Item'], output_csv_file_path)
        print("Writing Data...")
        for item in tqdm(items_list):
            # Overwrite csv file
            FileUtil.dict2csv(item["Item"], output_csv_file_path, overwrite=True)


def main():
    # Keyword
    keyword = "陶磁器"

    # How many pages to get the data (all item number = page_num * 30)
    page_num = 2

    # Init class
    RakutenAPIs = RakutenAPI('config/rakuten_api.json')

    # Get items info
    all_items_list = RakutenAPIs.get_items_by_keyword(keyword, page_num)

    # Write out to csv file
    RakutenAPIs.write2csv(all_items_list, f'data/{keyword}.csv')


if __name__ == '__main__':
    main()
