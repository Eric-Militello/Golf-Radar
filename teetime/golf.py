from selenium import webdriver
from bs4 import BeautifulSoup
import time



def scrape_tee_times(url):
    tee_time_info = []
    # Set up the Selenium WebDriver (make sure you have the webdriver installed)
    driver = webdriver.Chrome()
    driver.get(url)

    # Wait for the dynamic content to load (you might need to adjust the sleep time)
   
    time.sleep(1)

    # Get the page source after JavaScript has executed
    page_source = driver.page_source

    # Close the WebDriver
    driver.quit()

    # Use BeautifulSoup to parse the page source
    soup = BeautifulSoup(page_source, 'lxml')
    course_sections = soup.find_all('div', class_="course-details")

    for course in course_sections:
    # Extract course name from the <a> tag within the <h3> tag
        h_tag = course.find('h3', class_='color-black')
        
        if h_tag:
            a_tag = h_tag.find('a')

            # Check if a_tag is not None before accessing its text attribute
            if a_tag:
                tee_time_info.append(a_tag.text.strip())
    return tee_time_info
