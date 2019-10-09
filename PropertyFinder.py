import requests
import csv
import regex as re
from bs4 import BeautifulSoup


with open("properties.csv", "w") as csvfile:

    #  Create a new .csv document for data to be written into
    writer = csv.writer(csvfile)
    writer.writerow(["Listing Name", "Rent Price (Yearly)", "Location", "Listing Type", "Square Feet", "Bed", "Bath"])

    #  Extract number of properties and so number of pages from front page
    my_url = requests.get("https://www.bayut.com/to-rent/property/dubai/").text
    soup = BeautifulSoup(my_url, features="html.parser")
    abc = soup.find("div", {"class": "_5f5a3b34"}).text
    no_of_properties = int(re.search('Showing 1 - 24 of (.+?) Properties sorted byPopular', abc).group(1).replace(",", ""))
    no_of_pages = int(no_of_properties/24)

    for count in range(2, 10):  # use no_of_pages for all properties
        my_url = requests.get("https://www.bayut.com/to-rent/property/dubai/page-"+str(count)+"/").text
        soup = BeautifulSoup(my_url, features="html.parser")
        properties = soup.findAll("li", {"role": "article"})
        for x in range(0, properties.__len__()):
            name = properties[x].find("a", {"class":"_287661cb"})["title"]
            price = properties[x].find("span", {"class":"f343d9ce"}).text
            location = properties[x].find("div", {"class":"_7afabd84"}).text
            listing_type = properties[x].find("div", {"class":"_9a4e3964"}).text
            bath = "null"
            sqft = "null"
            bed = "null"

            extra = properties[x].findAll("span", {"class":"b6a29bc0"})  # 0 = bed #1 = bath #2 = sqft
            for n in range(0, len(extra)):
                if "Bath" in str(extra[n]):
                    bath = extra[n].text
                if "Area" in str(extra[n]):
                    sqft = extra[n].text
                if "Bed" in str(extra[n]):
                    bed = extra[n].text

            print(name, price, location, listing_type, sqft, bed, bath)
            writer.writerow([name, price, location, listing_type, sqft, bed, bath])
print("DONE!")
