#import beautifulsoup and request here

from flask import Flask ,render_template


#import libraries
#from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
from urllib.request import urlopen as req
import requests
import json
import csv
from datetime import datetime
import pandas as pd

responseJSON = requests.get('https://raw.githubusercontent.com/aaljehan/Beatiful-Soup/main/jobbDetails.json')


app = Flask(__name__)
@app.route("/")
def displayJobDetails():
    responseJSON = requests.get('https://raw.githubusercontent.com/aaljehan/Beatiful-Soup/main/jobbDetails.json')


#write a code to give call to json file and thenrender html page
    return render_template('index.html',responseJSON = responseJSON
)


#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList():
  r =requests.get('https://www.indeed.com/jobs?q=Developer&l=Charlotte')
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
 #getJobList(role, location)



if __name__ == "__main__":
    main()
    job_info = getJobList()
    print(job_info)

    # Task 5 Saving data in jobDetails.json file
    print(json.dumps(job_info))
    ## convert list of dicts to a `DataFrame`
    jobDetails = pd.DataFrame.from_records(job_info)
    # write the data to a file.
    jobDetails.to_json("jobDetails.json")