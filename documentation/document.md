Automação de Preenchimento de Formulário Web com Selenium e Pandas
Este documento descreve um script Python que automatiza o preenchimento de um formulário web utilizando dados de um arquivo Excel. A automação é realizada com as bibliotecas Selenium e Pandas.

Requisitos

Python 3.x
Bibliotecas Python:
time: Biblioteca padrão do Python para operações de temporização.
pandas: Biblioteca para manipulação de dados. Instalação: pip install pandas.
selenium: Biblioteca para automação de navegadores web. Instalação: pip install selenium.
webdriver_manager: Biblioteca para gerenciar drivers de navegador. Instalação: pip install webdriver-manager.
Descrição do Script
Importação das Bibliotecas
O script inicia importando as bibliotecas necessárias:

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
Inicialização do WebDriver
Inicializa o driver do navegador Firefox utilizando o GeckoDriver:

driver = webdriver.Firefox()
service = Service(GeckoDriverManager().install())
driver.get('https://renopele.fun/api/')
Carregamento dos Dados
Lê os dados de um arquivo Excel (data/test.xlsx) em um DataFrame do Pandas:

df = pd.read_excel('data/test.xlsx')
df  # Exibe o DataFrame
Preenchimento e Envio do Formulário
Itera sobre cada linha do DataFrame, preenchendo e enviando o formulário com os dados extraídos:

for index, row in df.iterrows():
    numero = str(row.iloc[0])  # Extrai o primeiro valor da linha e converte para string
    email = row.iloc[1]        # Extrai o segundo valor da linha

    # Preenche os campos do formulário
    driver.find_element('xpath', '//*[@id="form-field-email"]').send_keys(email)
    driver.find_element('xpath', '//*[@id="form-field-message"]').send_keys(numero)
    
    time.sleep(1)  # Espera de 1 segundo para garantir o preenchimento

    # Localiza e clica no botão de enviar
    xpath = "//button[@class='elementor-button elementor-size-sm']/span/span[@class='elementor-button-text' and text()='Send']"
    button = driver.find_element(By.XPATH, xpath)
    button.click()
    
    time.sleep(1)  # Espera de 1 segundo para o envio

    # Limpa os campos do formulário
    driver.find_element('xpath', '//*[@id="form-field-email"]').clear()
    driver.find_element('xpath', '//*[@id="form-field-message"]').clear()
    
    time.sleep(1)  # Espera de 1 segundo antes de passar para a próxima iteração
Funcionamento do Script
Configuração do WebDriver: Configura e inicializa o WebDriver para o navegador Firefox, utilizando GeckoDriverManager para instalar automaticamente o driver necessário.
Carregamento dos Dados: Lê o arquivo Excel contendo os dados que serão usados para preencher o formulário.
Iteração e Preenchimento: Para cada linha do DataFrame, o script:
Extrai os valores das colunas relevantes (numero e email).
Preenche os campos do formulário web utilizando os valores extraídos.
Clica no botão de envio do formulário.
Limpa os campos do formulário para a próxima iteração.
Controle de Tempo: Utiliza time.sleep(1) para garantir que o navegador tenha tempo suficiente para processar cada ação.
Considerações Finais
Este script oferece uma solução eficiente para a automação de preenchimento de formulários web, especialmente útil para tarefas repetitivas que envolvem grandes volumes de dados. A utilização de bibliotecas como Selenium e Pandas torna o processo robusto e flexível, permitindo adaptações conforme necessário.