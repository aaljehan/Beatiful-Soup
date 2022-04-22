# import beautifulsoup and request here

import requests
from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def displayJobDetails():
    response = requests.get(f'https://raw.githubusercontent.com/Nehalk145/pythonBeautifulSoup/main/jobDetails.json')
    responseJSON = response.json()
    print(responseJSON)
    return render_template('index.html', responseJSON=responseJSON)




# function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role, location):
    # creating a request
    r = requests.get(f'https://www.indeed.com/jobs?q={role}&l={location}')






# save data in json file
def saveDataInJSON(job_info):
    # Complete the missing part of this function here
    print("Saving data to JSON")





# save data in csv file
def saveDataInCSV(data):
    # Complete the missing part of this function here
    print("Saving data to csv")
    # saving csv file



# main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter location: ")
    location = input()



# getJobList(role, location)


if __name__ == "__main__":
    main()
