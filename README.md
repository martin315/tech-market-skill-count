# Tech Market Skill Count

## Description

Tech Market Skill Count is a simple python application that calculates the number of times a tech skill is listed per given city. The result is a csv file with each row corresponding to the name of a technology found in the tech.txt file. The headers are the names of the json files within the data folder.

The application reads from the data folder filled with json files formatted as such:

    [
        {
        "id": "123456789",
        "title": "Software Engineer",
        "publishedAt": "2021-01-01",
        "companyName": "Google",
        "location": "San Francisco, CA",
        "postedTime": "4 days ago",
        "applicationsCount": "100",
        "description": "We are looking for a software engineer",
        "jobUrl": "https://www.linkedin.com/jobs/view/123456789",
        "companyUrl": "https://www.linkedin.com/company/google",
        "contractType": "FullTime",
        "experienceLevel": "Internship",
        "workType": "OnSite",
        "sector": "InformationTechnology",
        "salary": "100000"
        }
    ]

Currently it's a work in progress! The goal of this project is to easily compare the popularity of each skill, so I can gauge what to study to secure a software development job in Europe.
