import time
import pyautogui
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.linkedin.com/feed/")
browser.maximize_window()

time.sleep(2)
  
username_input = browser.find_element("id", "username")
username_input.send_keys("seu login")
password_input = browser.find_element("id", "password")
password_input.send_keys("sua senha")
button_submit = browser.find_elements("css selector", "button[type='submit']")

for button in button_submit:
    if "Entrar" in button.text:
        button.click()
        break

#time.sleep(120)
#dinamic wait
from selenium.webdriver.support.ui import WebDriverWait as webWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

try:
    wait = webWait(browser, 30)
    label_search = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "search-global-typeahead__input"))
    )
    #browser.find_element("class name", "search-global-typeahead__input")
    #(EC.element_located_selection_state_to_be)
    print('usuario autorizou')
    label_search.send_keys("Desenvolvedor Python")
    time.sleep(5)
    pyautogui.press("enter")
    time.sleep(5)

except Exception as e:
    print(f"Erro: {e}")
    browser.quit()

button_peoples = browser.find_elements(By.CLASS_NAME, "search-navigation-panel__button")

for button in button_peoples:
    if "Pessoas" in button.text:
        button.click()
        break

time.sleep(5)

try:
    button_more_peoples = wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Ver todos os resultados de pessoas')]"))
    )
    # = browser.find_element(By.CLASS_NAME, "gNDVSUlysFTeyzqdLkmGtXiwIkTNLonGmA")
    button_more_peoples.click()
    print("Esta na tela com varias pessoas para se conectar")
    time.sleep(5)

except Exception as e:
    print(f"Erro: {e}")
    browser.quit()

try:
    list_buttons_conect = browser.find_elements("css selector", "button[type='button']")
    wait_conect = webWait(browser, 15)
    list_buttons_conect = wait_conect.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[type='button']"))
    )
    for button in list_buttons_conect:
        if "Conectar" in button.text:
            button.click()
            strong_element = wait_conect.until(EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'artdeco-modal__content')]/p/span/strong"))
            ) 
            #wait_conect.until(EC.presence_of_element_located(
             #   (By.CSS_SELECTOR, "div.artdeco-modal__content ember-view > p > span > strong"))
            #)
            name_of_people = strong_element.text
            print(f"{name_of_people}")
            # Divide o texto em palavras e pega a primeira palavra
            first_name = name_of_people.split()[0]
            add_note = wait_conect.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Adicionar nota']")))
            add_note.click()
            print("Clicou em 'Adicionar Nota'")
            text_to_connection = wait_conect.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))  # Geralmente campos de texto são `<textarea>`
            )
            text_to_connection.send_keys(
                f"Olá {first_name}, tudo bem? Vi que atua com Python!"
                " Estou iniciando na área e adoraria trocar experiências e aprender com você. Vamos nos conectar?")
            print("Digitou a mensagem")
            time.sleep(5)
            button_submit_finally = wait_conect.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Enviar convite']")))
            button_submit_finally.click()
            time.sleep(5)
            # for button in  button_submit_finally:
            #     if "Enviar" in button.text:
            #         button.click()
            #         break
            print("Clicou para enviar")
        print("pressionou o botao")
except Exception as e:

    print(f"Erro: {e}")

    browser.quit()

time.sleep(10)