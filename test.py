from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Lance Chrome avec le bon driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 10)

# 🔹 Étape 1 : gérer le popup "J'accepte"
try:
    consent_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Tout accepter')]"))
    )
    consent_button.click()
    print("✅ Popup Google accepté")
except:
    print("ℹ️ Aucun popup détecté")

# 🔹 Étape 2 : attendre que la barre de recherche soit prête
search_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "q"))
)
search_box.send_keys("Selenium Python")
search_box.submit()
print("✅ Recherche envoyée")

# Laisser 5 secondes pour voir le résultat
time.sleep(5)
driver.quit()
