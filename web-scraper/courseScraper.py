import requests
from bs4 import BeautifulSoup


def get_class_num(title):
    """
    Takes in a title, splits the array based on the white spaces
    then returns only the class number.

    title: A string where the second word is the class number
    """
    # Turns title into an array
    titleParts = title.strip().split()

    num = titleParts[1].split('.')[0] #No period, or extra numbers
    return num



def fetch_courses(courseSubject):
    """
    Takes in a course subject such as CMPT, and extracts all the data
    related to that subject from the usask course catalogue page. 

    courseSubject: A subject that is in all capitals
    
    """
    
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
        
        # Class number
        number = get_class_num(title)






        


def main():
    fetch_courses('CMPT')

if __name__=="__main__":
    main()
