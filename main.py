from character import Character
from selenium import webdriver
from collections import Counter
from default import get_class, get_race_faction, get_faction
from export import export_csv
import time

characters = []

c_options = webdriver.ChromeOptions()
c_options.add_argument('--headless')
c_options.add_argument('--no-sandbox')

pages_to_check = 100

driver = webdriver.Chrome(chrome_options=c_options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
characters = []

for i in range(-1, pages_to_check - 1):
    driver.get("https://www.wowprogress.com/simdps/char_rating/next/" + str(i) + "#char_rating")

    table = driver.find_element_by_xpath('//*[@id="char_rating_container"]/table')
    rows = table.find_elements_by_tag_name('tr')

    for row in rows[1:]:
        ## Rank[0] - Name[1] incl Race and Class - Guild[2] incl Faction - Raid[3] - Realm[4] incl Region and Zone - Spec[5] - SimDPS[6]
        cells = row.find_elements_by_tag_name('td')

        ## Getting the Race and Class
        race_class = cells[1].find_element_by_tag_name('a').get_attribute('aria-label')

        ## Getting the Faction
        try:
            faction_guild = cells[2].find_element_by_tag_name('a').get_attribute('class')
        except:
            faction_guild = "No guild"
            pass

        rank = cells[0].text
        name = cells[1].text.split(" ")[0]
        race, faction = get_race_faction(race_class)
        clss = get_class(race_class)
        guild = cells[2].text
        if faction is "":
            faction = get_faction(faction_guild)
        #raid = cells[3]
        realm = cells[4].text.split("-")[1]
        region = cells[4].text[:2]
        if "(" in cells[4].text:
            zone = cells[4].text.split("(")[1][:2]
        else:
            zone = ""
        spec = cells[5].text
        simdps = cells[6].text

        characters.append(Character(rank, name, race, clss, guild, faction, realm, region, zone, spec, simdps))


    if i % 1 == 0:
        print(str(100 / pages_to_check * (i + 2)) + "% is scraped.")

export_csv(characters)