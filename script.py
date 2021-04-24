
# importing required libraries
from selenium import webdriver
from time import sleep
from parsel import Selector
import csv

# specifies the path to the chromedriver.exe
# replace "path" with chromedriver's path 
driver = webdriver.Chrome('path')

# method to navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# to set a sticky timeout to 5 sec to implicitly wait for element to be found
driver.implicitly_wait(5)

# locate email form by_class_name
username = driver.find_element_by_class_name('input__input')

# to simulate key strokes to type into the element
# replace "email" with linkedin email address
username.send_keys('email')

# locate password form by id
password = driver.find_element_by_id('session_password')

# to simulate key strokes to type into the element
# replace "password" with linkedin password
password.send_keys('password')

# locate log in button by class name
log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')

#clicks on log in button
log_in_button.click()

# Navigating to linkedin profile

# variable to define profile link to be scraped
# replace "link" with linkedin url of profile to scrape
url = 'link'

# Loads the webpage of profile in the current browser session.
driver.get(url)


# Function to zoom out and then scroll down to enable full page scraping

def zoom_scroll():
    # Get current scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    # Adjust scroll height to 10%
    driver.execute_script("document.body.style.zoom='10%'")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, (document.body.scrollHeight/2));")

        # scroll pause time to ensure enough time to extract details
        sleep(3) 
        
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, (document.body.scrollHeight));")

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Call zoom and scroll function to execute
zoom_scroll()

# Define method that gets the source of the current page
source = driver.page_source

# to allow for selection of parts of the source pageg using CSS or XPath expressions and extract data from it
sel = Selector(text= source)

# Extract Basic Information

# using xpath to extract the text for name
name = sel.xpath(
    '// *[starts-with(@class, "inline t-24 t-black t-normal break-words")]/text()').extract_first()

# check to remove /n and white spaces
if name:
    name = name.strip()

# xpath to extract the text for linkedin job title
linkedin_job_title = sel.xpath(
    '// *[starts-with(@class,"mt1 t-18 t-black t-normal break-words")]/text()').extract_first()

# check to remove /n and white spaces
if linkedin_job_title:
    linkedin_job_title = linkedin_job_title.strip()

# xpath to extract the text for location
location = sel.xpath(
    '// *[starts-with(@class, "t-16 t-black t-normal inline-block")]/text()').extract_first()

# check to remove /n and white spaces
if location:
    location = location.strip()


# Extract Work Experience Information of Current Job

# xpath to extract the text for current job title
current_job_title = sel.xpath(
    '//section[@id="1072303227"]//a//div[2]//h3[contains(@class, "t-16 t-black t-bold")]/text()').extract_first()

# check to remove /n and white spaces
if current_job_title:
    current_job_title = current_job_title.strip()
 
# xpath to extract the text for company
company1 = sel.xpath(
    '//section[@id="1072303227"]//a//div[2]//p[2][contains(@class,"pv-entity__secondary-title t-14 t-black t-normal")]/text()').extract_first()

# check to remove /n and white spaces
if company1:
    company1 = company1.strip()

# xpath to extract the text for type of employment
emp_type1 = sel.xpath(
    '//section[@id="1072303227"]//a//div[2]//p[2]//span[contains(@class,"pv-entity__secondary-title separator")]/text()').extract_first()

# check to remove /n and white spaces
if emp_type1:
    emp_type1 = emp_type1.strip()

# xpath to extract the text for period of employment
period_emp1 = sel.xpath(
    '//section[@id="1072303227"]//a//div[2]//div//h4[1]//span[2]/text()').extract_first()

# check to remove /n and white spaces
if period_emp1:
    period_emp1 = period_emp1.strip()

# xpath to extract the text for duration of employment
duration_emp1 = sel.xpath(
    '//section[@id="1072303227"]//a//div[2]//div//h4[2]//span[2][contains(@class,"pv-entity__bullet-item-v2")]/text()').extract_first()

# check to remove /n and white spaces
if duration_emp1:
    duration_emp1 = duration_emp1.strip()


# Extract Work Experience Information of Previous Job

# xpath to extract the text for previous job title
previous_job_title = sel.xpath(
    '//section[@id="1754757079"]//a//div[2]//h3[contains(@class, "t-16 t-black t-bold")]/text()').extract_first()

# check to remove /n and white spaces
if previous_job_title:
    previous_job_title = previous_job_title.strip()

# xpath to extract the text for company
company2 = sel.xpath(
    '//section[@id="1754757079"]//a//div[2]//p[2][contains(@class,"pv-entity__secondary-title t-14 t-black t-normal")]/text()').extract_first()

# check to remove /n and white spaces
if company2:
    company2 = company2.strip()

# xpath to extract the text for type of employment
emp_type2 = sel.xpath(
    '//section[@id="1754757079"]//a//div[2]//p[2]//span[contains(@class,"pv-entity__secondary-title separator")]/text()').extract_first()

# check to remove /n and white spaces
if emp_type2:
    emp_type2 = emp_type2.strip()

# xpath to extract the text for period of employment
period_emp2 = sel.xpath(
    '//section[@id="1754757079"]//a//div[2]//div//h4[1]//span[2]/text()').extract_first()

# check to remove /n and white spaces
if period_emp2:
    period_emp2 = period_emp2.strip()

# xpath to extract the text for duration of employment
duration_emp2 = sel.xpath(
    '//section[@id="1754757079"]//a//div[2]//div//h4[2]//span[2][contains(@class,"pv-entity__bullet-item-v2")]/text()').extract_first()

# check to remove /n and white spaces
if duration_emp2:
    duration_emp2 = duration_emp2.strip()


# xpath to extract the text for college
college = sel.xpath(
    '//*[starts-with(@class, "text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()').extract_first()

# check to remove /n and white spaces
if college:
    college = college.strip()

# extract linkedin url
linkedin_url = driver.current_url

# utility function to ensure all key data fields have values
def validate_field(field):
    # if field is present pass
    if field:
        pass
    # if field is not present print text
    else:
        field = 'No results'
    return field

# Validating the existence of fields on the profile

# List of fields to validate
fields = [name, linkedin_job_title, location, college, current_job_title,
            company1, emp_type1, period_emp1, duration_emp1, previous_job_title, 
          company2, emp_type2, period_emp2, duration_emp2, linkedin_url]

# Execute validate function in a for loop
for field in fields:
    field = validate_field(field)


# printing the output to the console
print('\n')
print('--'*40)
print("Personal Details")
print('--'*40)
print('Name: ' + name)
print('Linkedin Job Title (s): ' + linkedin_job_title)
print('Location: ' + location)
print('College: ' + college)
print('URL: ' + linkedin_url)


# Scrape and print all education record

# locate education section by xpath
education = driver.find_elements_by_xpath(
    '//section[@id = "education-section"]//li[contains(@class,"pv-profile-section__sortable-item pv-profile-section__section-info-item relative pv-profile-section__sortable-item--v2 pv-profile-section__list-item sortable-item ember-view")]')

print('\n')
print('--'*40)
print("Education Record")
print('--'*40)
for item in education:
    print(item.text)
    print("")

# Scrape and print all experience record

# locate experience section by xpath
experience = driver.find_elements_by_xpath(
    '//section[@id = "experience-section"]//li[contains(@class,"pv-profile-section__sortable-item pv-profile-section__section-info-item relative pv-profile-section__list-item sortable-item ember-view")]')

print('\n')
print('--'*40)
print("Work Experience Record")
print('--'*40)
for item in experience:
    print(item.text)
    print("")  

# to close the browser and shuts down the ChromeDriver executable
driver.quit()


#  Writing key details to csv file

# Create a new file in write mode
writer = csv.writer(open('results_file.csv', 'w'))

# method to the write the following to the created file object as header
writer.writerow(['Name','Linkedin Job Title', 'Location', 'Current Job Title', 'Company',
                 'Employment Type', 'Employment Period', 'Employment Duration', 'Previous Job Title',
                 'Previous Company', 'Previous Employment Type', 'Previous Employment Period', 'Previous Employment Duration', 'College', 'URL'])

# writing the following values as records in the file
writer.writerow([name, linkedin_job_title, location, current_job_title,
                 company1, emp_type1, period_emp1, duration_emp1,
                 company2, emp_type2, period_emp2, duration_emp2,
                 college, linkedin_url])
