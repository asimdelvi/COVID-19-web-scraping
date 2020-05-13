import requests
from bs4 import BeautifulSoup


class Covid:
    def __init__(self):
        response = requests.get("https://www.mohfw.gov.in/")
        self.soup = BeautifulSoup(response.text, "html.parser")

    def _headers(self):
        header = self.soup.find("thead").get_text()
        return header.split("\n")[2:7]

    def all_states_status(self):
        state_data = self.soup.find_all("tr")
        state_list = [(state.get_text().split("\n"))[1:6]
                      for state in state_data][1:len(state_data)-2]
        return [dict(zip(self._headers(), s)) for s in state_list]

    def status_based_on_states(self):
        state_name = input("enter state name: ").lower()
        for i in self.all_states_status():
            if i["Name of State / UT"].lower() == state_name:
                return i

    def total_cases(self):
        data = self.soup.find_all("tr")
        data_list = [(state.get_text().split("\n"))
                     for state in data][-5][2:8]
        key = ["Total Confermed cases in india",
               "Total Recovered in India", "Total Deaths in India"]
        return dict(zip(key, [s for s in data_list if s != ""]))


c = Covid()
print(c.all_states_status())
print(c.status_based_on_states())
print(c.total_cases())
