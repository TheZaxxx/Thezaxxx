
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ====== CONFIGURATION ======
CHROMEDRIVER_PATH = 'chromedriver.exe'  # Ganti dengan lokasi ChromeDriver di PC kamu
SUI_ADDRESS = '0xYourSUIAddressHere'    # Ganti dengan alamat SUI kamu
CLAIM_INTERVAL = 60 * 60                # Waktu tunggu antar klaim (dalam detik)
# ===========================

# Setup Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Buka website
    driver.get('https://faucet.n1stake.com/')
    time.sleep(5)

    # Input SUI address
    address_field = driver.find_element(By.NAME, 'wallet')
    address_field.send_keys(SUI_ADDRESS)

    time.sleep(1)

    # Klik tombol Claim
    claim_button = driver.find_element(By.XPATH, "//button[contains(text(),'Claim')]")
    claim_button.click()
    print("✅ Claim pertama berhasil!")

    # Loop klaim otomatis
    while True:
        time.sleep(CLAIM_INTERVAL)
        driver.get('https://faucet.n1stake.com/')
        time.sleep(5)

        try:
            address_field = driver.find_element(By.NAME, 'wallet')
            address_field.send_keys(SUI_ADDRESS)
            time.sleep(1)

            claim_button = driver.find_element(By.XPATH, "//button[contains(text(),'Claim')]")
            claim_button.click()
            print("✅ Klaim berikutnya berhasil!")
        except Exception as e:
            print(f"⚠️ Gagal klaim: {e}")

except Exception as e:
    print(f"❌ Terjadi kesalahan: {e}")

finally:
    driver.quit()
