from datetime import date
import json
from os import path
import os
import requests
from bs4 import BeautifulSoup

from paths import JSON_PATH

class JobFinder:

    def __init__(self,company_id:str):
        self.__company_id = company_id
        self.__today = str(date.today())
        self.__listObj = []
        self.__jobs=[]
        self.__latest_jobs=[]
        self.__elements = []


    def __find_delta_jobs(self,listObj):
        self.__latest_jobs = listObj[-1]["jobs"]
        last_job_date = str(listObj[-1]["date"])

        delta_jobs = set(self.__jobs)-set(self.__latest_jobs)
        if len(delta_jobs)>0:
            print(f"{len(delta_jobs)} were added, comparing {last_job_date} and {self.__today}:")
        for new_job in delta_jobs:
            print(new_job)

    def __write_new_jobs(self):
        dictionary = {
        "date": self.__today,
        "number_of_jobs": len(self.__elements),
        "jobs": self.__jobs}

        self.__listObj.append(dictionary)
        return self.__listObj

    def __is_file_empty(self)-> bool:
        """ Check if file is empty by confirming if its size is 0 bytes"""
        # Check if file exist and it is empty
        return os.path.exists(JSON_PATH) and os.stat(JSON_PATH).st_size == 0

    def search_by_company_id(self, write_to_json=False) -> list:
        url = f'https://www.careerarc.com/job-search?campaign_id={self.__company_id}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text,'html.parser')
        elements = soup.find_all('div', class_='job-posting-item')
        if elements:
            print(f"{len(elements)} jobs were found:")
            for element in elements:
                if element.find('h2').a.text:
                    
                    self.__jobs.append(
                        {"Job Name": element.find('h2').a.text,
                        "Link": element.find('h2').a['href']})
        else:
            print(f"no jobs were found for today {self.__today}.")

        if write_to_json:
            # Read JSON file
            try:
                with open(JSON_PATH,'w+') as fp:
                    if not self.__is_file_empty():
                        listObj = json.load(fp)
                        self.__find_delta_jobs(listObj)
                    new_listObj = self.__write_new_jobs()
                    json.dump(new_listObj, fp, 
                                    indent=4,  
                                    separators=(',',': '))

            except ValueError:
                print('Loading JSON has failed')    
        
        return self.__jobs