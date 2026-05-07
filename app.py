import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import db

st.title("Our Mesorah")

URL = "https://www.simpletoremember.com/articles/a/mesora/"

page = requests.get(URL, verify=False)
soup = BeautifulSoup(page.text, 'html.parser')

st.write(page.status_code)

div = soup.find("div", id="enlarged-body")

people = div.find_all("p")
# datasets = datasets[::5]       # get every fifth item

mesorah_groups = {
    "Moshe-Zekeinim": people[1:5],
    "Nevi'im": people[5:23],
    "Tannaim": people[23:39],
    "Amoraim": people[39:45],
    "Savoraim": people[45:48],
    "Geonim": people[48:93],
    "Rishonim": people[93:115],
    "Acharonim": people[115:128]
}
counter = {}

for key, val in mesorah_groups.items():
    counter[key] = [len(val)]

df = pd.DataFrame(counter)

st.bar_chart(df)

database = db.DataBase()

count = 1

for person in people:
    # link = data.get("href")
    title = person.get_text(strip=True)
    if len(title) < 100:
        # link = "https://jewishvirtuallibrary.org" + link
        st.write(str(count) + " " + title)
        database.add_data((title,))
        count += 1
