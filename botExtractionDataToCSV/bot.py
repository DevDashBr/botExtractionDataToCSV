import logging
import csv
import time
import estrutura_arquivos_py.config as config
import estrutura_arquivos_py.funcoes as funcoes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

logger = logging.getLogger(__name__)


def main():

    logger.info("Inicio da execução...")

    # Obter dicionário de Configuração
    dict_config = config.variaveis_config()
    print(dict_config)

    # Persistência do processamento
    tentativa = 0
    tentativas = 3
    while tentativa < tentativas:
        try:

            url = dict_config['url_site']

            # Configuração do WebDriver
            browser = webdriver.Chrome()

            # Abrir a página da web
            browser.get(url)
            browser.maximize_window()
            time.sleep(2)

            # Nome do arquivo CSV
            nome_arquivo = dict_config['nome_arquivo']

            # Navegar até a tabela de cotações
            btn_de_acordo = browser.find_element(By.ID, 'btOk')
            btn_de_acordo.click()  # Clicar na opção De Acordo

            body = browser.find_element(By.TAG_NAME, 'body')
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

            # Obter os dados da tabela
            table = browser.find_elements(By.XPATH, '//*[@id="table"]')
            dados = funcoes.obter_dados_cotacao(nome_arquivo, table)

            # Escrever os dados em um arquivo CSV
            funcoes.escrever_dados_arquivo(nome_arquivo, dados)

            browser.quit()

            break

        except Exception as e:
            print(f"Descrição do erro: {e}.")

            tentativa += 1
            print(f"Número da tentativa: {tentativa}")

            if tentativa >= tentativas:
                # Aqui poderá ser implementado alguma lógica para notificar o cliente, por exemplo, envio de e-mail.
                print("Não foi possível realizar a execução do robô. Favor verificar!")

                break


if __name__ == '__main__':
    main()
