import time
import threading
import pandas as pd
from selenium import webdriver
from function.stopWatch import stopWatch
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def automation(df):
    """
    Função de automação que utiliza Selenium para preencher e submeter um formulário web.
    
    Args:
    df (pd.DataFrame): DataFrame contendo os dados a serem inseridos no formulário.
    """
    # Configurando o serviço do driver Firefox
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get('https://renopele.fun/api/')  # Página web para automação

    # Lógica de automação
    for index, row in df.iterrows():
        # Capturando os dados do DataFrame
        email = str(row.iloc[0])
        numero = row.iloc[1]
        
        # Preenchendo o formulário
        driver.find_element(By.XPATH, '//*[@id="form-field-email"]').send_keys(email)  # Email
        driver.find_element(By.XPATH, '//*[@id="form-field-message"]').send_keys(numero)  # Telefone
        
        time.sleep(1)  # Pausa para simular a interação do usuário
        
        # Submetendo o formulário
        xpath = "//button[@class='elementor-button elementor-size-sm']/span/span[@class='elementor-button-text' and text()='Send']"
        button = driver.find_element(By.XPATH, xpath)
        button.click()  # Clique para enviar
        
        time.sleep(1)  # Pausa para limpar o formulário
        
        # Limpando o formulário
        driver.find_element(By.XPATH, '//*[@id="form-field-email"]').clear()
        driver.find_element(By.XPATH, '//*[@id="form-field-message"]').clear()
        
        time.sleep(1.5)  # Pausa para evitar sobrecarga no servidor
    
    driver.quit()  # Encerrando o driver

# Iniciando o cronômetro
threadStopwatch = threading.Thread(target=stopWatch)
threadStopwatch.daemon = True
threadStopwatch.start()

# Abrindo arquivos de dados (CSV ou XLSX)
df1 = pd.read_excel('data/LISTA01CSHB.xlsx')
df2 = pd.read_excel('data/LISTA02CSHB.xlsx')
df3 = pd.read_excel('data/LISTA03CSHB.xlsx')
df4 = pd.read_excel('data/LISTA04CSHB.xlsx')
df5 = pd.read_excel('data/LISTA05CSHB.xlsx')
df6 = pd.read_excel('data/LISTA06CSHB.xlsx')

# Criando threads para cada processo de automação
threads = [
    threading.Thread(target=automation, args=(df,))
    for df in [df1, df2, df3, df4, df5, df6]
]

# Iniciando todas as threads
for thread in threads:
    thread.start()

# Esperando todas as threads terminarem
for thread in threads:
    thread.join()

print("Automação concluída")
