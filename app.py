import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas
import sqlite3

st.write("Hello World")

URL = "https://jewishvirtuallibrary.org/biographies-wing/jewish-biographies-by-category/religious-figures"

page = requests.get(URL, verify=False)
soup = BeautifulSoup(page.text, 'html.parser')

st.write(page.status_code)

datasets = soup.find_all("a", class_="article-item")
datasets = datasets[::5]       # get every fifth item

for data in datasets:
    link = data.get("href")
    title = data.get_text(strip=True)
    link = "https://jewishvirtuallibrary.org" + link
    st.write(title, link)
