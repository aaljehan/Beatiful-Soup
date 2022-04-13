#import beautifulsoup and request here

#import libraries
#from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
from urllib.request import urlopen as req
import requests
import json
import csv
from datetime import datetime
import pandas as pd
def displayJobDetails(data):
    print("Display job details")
    print(data)

#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role,location):
  r =requests.get('https://www.indeed.com/jobs?q=Developer&l=Charlotte')
  #r =requests.get('https://www.indeed.com/jobs?q={role}&l={location}s')
  soup=BeautifulSoup(r.content, 'lxml')

  data = []

  for card in soup.select('#mosaic-provider-jobcards a'):
      companyName = card.select_one('span.companyName').text if card.select_one('span.companyName') else None
      companyLocation = card.select_one('div.companyLocation').text if card.select_one('div.companyLocation') else None
      decription = card.select_one('div.job-snippet').text if card.select_one('div.job-snippet') else None
      salary = card.select_one('div.salary-snippet-container').text if card.select_one('div.salary-snippet-container') else None
      
      data.append({
          'companyName':companyName,
          'companyLocation':companyLocation,
          'salary':salary,
          'decription' : decription
      })



  return data
    

#save data in json file
def saveDataInJSON(job_info):

    #Complete the missing part of this function here
    print("Saving data to JSON")
    # saving json file
    # Task 5 Saving data in jobDetails.json file
    print(json.dumps(job_info))
    ## convert list of dicts to a `DataFrame`
    jobDetails = pd.DataFrame.from_records(job_info)
    # write the data to a file.
    jobDetails.to_json("jobDetails.json")

#save data in csv file
def saveDataInCSV(data):

    #Complete the missing part of this function here
    print("Saving data to csv")
    # saving csv file
    print(csv.dumps(data))
    ## convert list of dicts to a `DataFrame`
    records_final = pd.DataFrame.from_records(data)
    # write the data to a file.
    records_final.to_json("jobDetails.csv")

# main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter location: ")
    location = input()
    

    print("Job role: ", role)
    print("location: ", location)
    job_info = getJobList(role,location)
    displayJobDetails(job_info)
    saveDataInJSON(job_info)
    
 #getJobList(role, location)



if __name__ == "__main__":
    main()
    