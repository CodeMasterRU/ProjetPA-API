# Imports
import pandas as pd
from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

rows = []

def scrapping():
    for page in range(1, 5 ,1):
        page_url = "https://www.carrefour.fr/r/viandes-et-poissons/boucherie?noRedirect=1&page=" + str(page)
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get(page_url)
        all_li = driver.find_element(By.XPATH, '//ul[@class="product-grid"]')


        for li in all_li.find_elements(By.XPATH, './/li[@class="product-grid-item"]'):
            titre = li.find_element(By.XPATH, './/h2[@class="ds-title ds-title--s"]').text
            prix_barquette = li.find_element(By.XPATH, './/span[@class="product-price__amount-value"]').text
            prix_par_kilo = li.find_element(By.XPATH, './/div[@class="ds-body-text ds-product-card-refonte__perunitlabel ds-body-text--size-s ds-body-text--color-standard-3"]').text.strip(' € / KG')
            rows.append((titre, prix_barquette, prix_par_kilo))

        driver.close()
    df = pd.DataFrame(rows, columns=["titre", "prix_barquette", "prix_par_kilo"])
    df.to_csv(f"test{page}.csv", index=False)
    # df.to_excel(f"test{page}.xlsx", index=False)

mydf = scrapping()