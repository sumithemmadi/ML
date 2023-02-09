import csv
import requests
from bs4 import BeautifulSoup as bs
from lxml import etree
import nums_from_string

page_url = "https://www.flipkart.com/poco-f1-rosso-red-64-gb/product-reviews/itmf9c3nheykcepp?pid=MOBF9A67HZBXF8FH&lid=LSTMOBF9A67HZBXF8FHW0MMGN&marketplace=FLIPKART"
# page_url = "https://www.flipkart.com/poco-f3-gt-5g-predator-black-128-gb/product-reviews/itm27a5b8bd59601?pid=MOBG4Z5MBD3VMXTF&lid=LSTMOBG4Z5MBD3VMXTFXHIC8A&aid=overall&certifiedBuyer=false&sortOrder=MOST_RECENT"
first_page = requests.get(page_url)
soup = bs(first_page.content, 'html.parser')
dom = etree.HTML(str(soup))
pages = nums_from_string.get_nums(dom.xpath(
    '/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/span[1]')[0].text)

while True:
    try:
        print("Number of pages ", pages[1])
        no_pages_to_scrap = input("No of pages to scrap between 1 and 1000: ")
        if no_pages_to_scrap.isdigit():
            no_pages_to_scrap = int(no_pages_to_scrap)
        else:
            raise ValueError()
        if 1 <= no_pages_to_scrap <= 1000:
            break
        raise ValueError()
    except ValueError:
        print("Input must be an integer between 1 and 1000.")

# print(no_pages_to_scrap)

data = []

for i in range(1, no_pages_to_scrap+1):
    if i == 1:
        soup1 = soup
    else:
        page = requests.get(page_url + "&page=" + str(i))
        soup1 = bs(page.content, 'html.parser')

    print(str(i)+" out of "+str(no_pages_to_scrap))

    divs = soup1.find_all(class_="col _2wzgFH K0kLPL")

    for j in range(len(divs)):
        small_html = divs[j]

        # print(small_html)
        small_soup = bs(str(small_html), 'html.parser')
        dom1 = etree.HTML(str(small_soup))

        # author
        author = small_soup.find(class_="_2sc7ZR _2V5EHH")

        # rating
        try:
            rating = dom1.xpath("/html/body/div/div[1]/div")[0].text
        except:
            rating = "None"

        # review title
        review_title = small_soup.find(class_="_2-N8zT")

        # review text
        try:
            full_review = dom1.xpath(
                "/html/body/div/div[2]/div/div/div")[0].text
        except:
            full_review = "None"

        ld = small_soup.find_all(class_="_3c3Px5")

        try:
            likes = ld[0].text
        except:
            likes = "None"

        try:
            dislikes = ld[1].text
        except:
            dislikes = "None"

        # date of review
        try:
            date = dom1.xpath("/html/body/div/div[4]/div[1]/p[3]")[0].text
            date_error = False
        except:
            date_error = True

        if date_error:
            try:
                # //*[@id="container"]/div/div[3]/div/div[1]/div[2]/div[3]/div/div/div/div[3]/div[1]/p[3]
                date = dom1.xpath("/html/body/div/div[3]/div[1]/p[3]")[0].text
                date_error = False
            except:
                date = "None"

        x_data = [author.text, rating,
                  review_title.text, full_review, likes, dislikes, date]

        # print(x_data)
        data.append(x_data)

fields = ["Author", "Rating", "Review Title",
          "Full Review", "Likes", "Dislikes", "Date"]
with open("data.csv", "w", encoding='utf-8') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(fields)
    csvwriter.writerows(data)
