import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

with open('paie.json', 'r') as openfile:
    # Reading from json file
    paie = json.load(openfile)

if (paie['cc'] == 'numero carte') | (paie['m'] == 'mois') | (paie['y'] == 'annee') | (paie['sp'] == 'ccv') | (
        paie['np'] == 'NOM PRENOM'):
    input('Veuillez remplir le fichier json')
    exit()
facture = input('------------The string here-----------\n').split('-')
bill_number = facture[0]
client_code = facture[2]
amount = facture[3]
ebp = facture[4]
link = 'https://baridinet.poste.dz/sonelgaz'
driver.get(link)
time.sleep(3)
driver.find_element('id', 'bill_number').send_keys(bill_number)
driver.find_element('id', 'client_code').send_keys(client_code)
driver.find_element('id', 'amount').send_keys(amount)
driver.find_element('id', 'ebp').send_keys(ebp)
driver.find_element('id', 'ebp').send_keys(Keys.TAB)
driver.switch_to.active_element.send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element('id', 'btn-submit').click()
time.sleep(3)
driver.find_element('id', 'iPAN').send_keys(paie['cc'])  # numero de carte
month = driver.find_element('id', 'month')  # mois
M = Select(month)
M.select_by_value(paie['m'])
year = driver.find_element('id', 'year')  # annee
Y = Select(year)
Y.select_by_value(paie['y'])
driver.find_element('id', 'iTEXT').send_keys(paie['np'])  # nom prenom
driver.find_element('id', 'iCVC').send_keys(paie['sp'])  # ccv
driver.find_element('id', 'buttonPayment').click()
