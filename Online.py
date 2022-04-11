#import beautifulsoup and request here

import request ;
import beautifulsoup;
#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList():
    url = 'https://www.indeed.com/jobs?q={role}&l={location}'
    # Complete the missing part of this function here
    r = request.get(url)
    #return html
#save data in csv file
def saveDataInCSV():
    #Complete the missing part of this function here
    print("Saving data to csv")
#saving csv file
#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter location: ")
    location = input()
    print("Job role: ", role)
    print("location: ", location)
    getJobList(role,location)



if __name__ == '__main__':
    main()
