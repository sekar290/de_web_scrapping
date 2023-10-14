from selenium import webdriver
import time
import pandas as pd


# default number of scraped pages
num_page = 10

# default tripadvisor website of restaurant
url = "https://www.tripadvisor.com/Restaurant_Review-g297704-d6650362-Reviews-Miss_Bee_Providore-Bandung_West_Java_Java.html"

webdriver_path = './chrome_drive/chromedriver.exe'

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(executable_path=webdriver_path)
driver.get(url)

# Define empty list to store the value later
listTitle = []
listDate = []
listRating =[]
listReview = []
for i in range(0, num_page):
    
    # expand the review 
    time.sleep(2)
    driver.find_element_by_xpath("//span[@class='taLnk ulBlueLinks']").click()

    container = driver.find_elements_by_xpath(".//div[@class='review-container']")

    for j in range(len(container)):

        title = container[j].find_element_by_xpath(".//span[@class='noQuotes']").text
        date = container[j].find_element_by_xpath(".//span[contains(@class, 'ratingDate')]").get_attribute("title")
        rating = container[j].find_element_by_xpath(".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
        review = container[j].find_element_by_xpath(".//p[@class='partial_entry']").text.replace("\n", " ")

        listTitle.append(title)
        listDate.append(date)
        listRating.append(rating)
        listReview.append(review)

        # csvWriter.writerow([date, rating, title, review]) 

    # change the page
    driver.find_element_by_xpath('.//a[@class="nav next ui_button primary"]').click()

# Make to Dataframe
Alldata = {
    "Title" : listTitle,
    "Date" :listDate,
    "Rating" : listRating,
    "Review" : listReview
}

df_Alldata = pd.DataFrame(Alldata)
df_Alldata.to_excel('./file_output/review.xlsx', index=False)

driver.close()
