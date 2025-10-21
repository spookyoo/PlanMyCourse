import requests
from bs4 import BeautifulSoup

def fetch_courses(courseSubject):
    url = f"https://catalogue.usask.ca/?subj_code={courseSubject}&cnum="
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    courses = []
    course_elements = soup.find_all('div')

    for course in course_elements:

        # Finding the title of the course
        if course.find('h4') is None:
            continue
        elif course.find('h4').find('a') is None:
            continue
        else:
            title = course.find('h4').find('a').text
        print(title)

        


def main():
    fetch_courses('CMPT')

if __name__=="__main__":
    main()
