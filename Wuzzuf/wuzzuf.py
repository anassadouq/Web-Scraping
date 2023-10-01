import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
company_name = []
location_name = []
skills = []
links = []
salary = []

result = requests.get('https://wuzzuf.net/search/jobs/?q=python&a=hpb')

src= result.content
#print(src)

soup = BeautifulSoup(src, "lxml")
#print(soup)

job_titles = soup.find_all("h2", {"class":"css-m604qf"})
company_names = soup.find_all("a", {"class":"css-17s97q8"})
locations_names = soup.find_all("span", {"class":"css-5wys0k"})
job_skills = soup.find_all("div", {"class":"css-y4udm8"})

for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    company_name.append(company_names[i].text)
    location_name.append(locations_names[i].text)
    skills.append(job_skills[i].text)

#print(company_name, location_name, skills)

# Create csv file
file_list = [job_title, company_name, location_name, skills,]
exported = zip_longest(*file_list)

with open("/Users/iat/Desktop/Scraping/Wuzzuf/wuzzuf.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job title", "company name", "location", "skills"])
    wr.writerows(exported)