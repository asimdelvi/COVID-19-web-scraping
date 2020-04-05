import requests
from bs4 import BeautifulSoup


def scrape_data():
    response = requests.get("https://www.worldometers.info/coronavirus/")
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def headers():
    heading = scrape_data().find("thead").get_text()
    return heading.split("\n")


def total_cases():
    total = scrape_data().find(class_="total_row").get_text()
    keys = headers()[3:9]
    value = total.split("\n")[2:9]
    return [(f"{k}:{v}") for k, v in dict(zip(keys, value)).items()]


def all_countries_status():
    all_countries = scrape_data().find(
        id="main_table_countries_today").tbody.find_all("tr")
    a = [d.get_text().split("\n")[1:9] for d in all_countries]
    keys = headers()[2:9]
    return [(dict(zip(keys, i))) for i in a]


def status_based_on_countries():
    country_name = input("enter country name: ").lower()
    for i in all_countries_status():
        if i["Country,Other"].lower() == country_name:
            for k, v in i.items():
                print(f"{k}:{v}")


scrape_data()
headers()
print(total_cases())
all_countries_status()
print(status_based_on_countries())
