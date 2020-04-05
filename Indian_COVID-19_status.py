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
        k = self._headers()
        return [dict(zip(k, s)) for s in state_list]

    def status_based_on_states(self):
        state_name = input("enter state name: ").lower()
        for i in self.all_states_status():
            if i["Name of State / UT"].lower() == state_name:
                for k, v in i.items():
                    print(f"{k}:{v}")


c = Covid()
print(c._headers())
print(c.all_states_status())
print(c.status_based_on_states())
