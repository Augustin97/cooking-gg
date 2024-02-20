import pandas as pd
import json
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


Aatrox_levels = []
Aatrox_health_stats = []
Champion_name = []
Champion_id = []

driver = webdriver.Chrome()

driver.get("https://leagueoflegends.fandom.com/wiki/Aatrox/LoL")

# Find the <select> element by its ID

select_element = driver.find_element(By.ID, 'lvl_Aatrox')

select = Select(select_element)

for i in range(1, 19):
    Aatrox_levels.append(i)
    Champion_name.append("Aatrox")
    Champion_id.append(1)
    select.select_by_value(str(i))
    selected_option = select.first_selected_option

    print("selected option: ", selected_option.text)

    wait = WebDriverWait(driver, 10)
    span_element = None
    while not span_element or not span_element.text.strip():
        try:
            span_element = wait.until(lambda x: x.find_element(By.ID, "Health_Aatrox_lvl"))
        except TimeoutException as e:
            pass

    span_text = span_element.text
    Aatrox_health_stats.append(float(span_text))

    print("Span text: ", span_text)

driver.quit()


aatrox_df = pd.DataFrame({'champion_id': 1, 'champion_name': 'Aatrox', 'champion_level': Aatrox_levels,
                          'champion_health': Aatrox_health_stats})

print(aatrox_df)

res = dict(zip(Aatrox_levels, Aatrox_health_stats))

aatrox_data_json = json.dumps(res)

print(res)
print(aatrox_data_json)

# TO DO: Do the same for all champions and think about database creation for champions and items and prob Runes
