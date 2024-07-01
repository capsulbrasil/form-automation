### Automação de Preenchimento de Formulário Web com Selenium

Este script Python utiliza Selenium para automatizar o preenchimento e submissão de formulários web.

#### Pré-requisitos

- Python 3.x instalado
- Bibliotecas necessárias:
  - pandas
  - selenium
  - webdriver_manager

Instale as dependências usando:

```bash
pip install pandas selenium webdriver_manager
```

#### Uso

1. **Configuração do Ambiente**
   - Certifique-se de ter o navegador Firefox instalado.

2. **Clonando o Repositório**
   ```bash
   git clone https://seu-repositorio.git
   cd seu-repositorio
   ```

3. **Executando a Automação**

   No seu arquivo Python (por exemplo, `automacao.py`), importe as bibliotecas necessárias e defina a função `automation` conforme fornecido no seu código:

   ```python
   import time
   import threading
   import pandas as pd
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   from webdriver_manager.firefox import GeckoDriverManager

   def automation(df):
       # Implementação da função automation ...

   # Código para iniciar as threads e executar a automação ...
   ```


4. **Executando o Script**

   Execute o script Python para iniciar a automação:

   ```bash
   python automacao.py
   ```


5. **Observações**

   - O script utiliza threads para processar múltiplos arquivos de dados simultaneamente, melhorando a eficiência da automação.
   - Certifique-se de ajustar os XPath e lógica de preenchimento conforme necessário para se adequar ao seu formulário web específico.

#### Encerramento

Após a execução do script, você verá no terminal a mensagem "Automação concluída".
