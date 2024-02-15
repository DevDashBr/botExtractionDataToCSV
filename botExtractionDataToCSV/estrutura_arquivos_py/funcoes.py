import logging
import csv
from selenium.webdriver.common.by import By


logger = logging.getLogger(__name__)


def obter_dados_cotacao(nome_arquivo, table):

    logger.info("Obter os dados do arquivo de entrada...")

    i = 0  # Contador
    numero_linha = 0

    # Iterar a tabela
    for item in table:

        # Obter os dados da coluna Tickers
        dados_coluna1 = []
        tickers = item.find_elements(By.CLASS_NAME, 'ticker1')

        for ticker in tickers:
            dados_coluna1.append(ticker.text)
            # Contador para obter o número total de linhas
            i += 1

        # Obter os dados da coluna Empresa
        dados_coluna2 = []
        empresas = item.find_elements(By.CLASS_NAME, 'empresa1')

        for empresa in empresas:
            dados_coluna2.append(empresa.text)

        # Obter os dados da coluna Volume
        dados_coluna3 = []
        volumes = item.find_elements(By.CLASS_NAME, 'volume1')

        for volume in volumes:
            dados_coluna3.append(volume.text)

        # Obter os dados da coluna Fechamento Anterior
        dados_coluna4 = []
        fechamentos = item.find_elements(By.CLASS_NAME, 'fechamento')

        for fechamento in fechamentos:
            if 'Fech. Ant.' not in fechamento.text:
                dados_coluna4.append(fechamento.text)

        # Obter os dados da coluna Mínima
        dados_coluna5 = []
        minimas = item.find_elements(By.CLASS_NAME, 'minima')

        for minima in minimas:
            if 'Mínima' not in minima.text:
                dados_coluna5.append(minima.text)

        # Obter os dados da coluna Máxima
        dados_coluna6 = []
        maximas = item.find_elements(By.CLASS_NAME, 'maxima')

        for maxima in maximas:
            if 'Máxima' not in maxima.text:
                dados_coluna6.append(maxima.text)

        # Obter os dados da coluna Última
        dados_coluna7 = []
        ultimas = item.find_elements(By.CLASS_NAME, 'ultima1')

        for ultima in ultimas:
            dados_coluna7.append(ultima.text)

        # Obter os dados da coluna Var.(Dia)
        dados_coluna8 = []
        while i != numero_linha:
            numero_linha += 1
            var_dias = item.find_elements(
                By.XPATH, f'//*[@id="table"]/tbody/tr[{numero_linha}]/td[8]')

            for dia in var_dias:
                dados_coluna8.append(dia.text)

        # Obter os dados da coluna Var.(Mês)
        dados_coluna9 = []
        numero_linha = 0
        while i != numero_linha:
            numero_linha += 1
            var_mes = item.find_elements(
                By.XPATH, f'//*[@id="table"]/tbody/tr[{numero_linha}]/td[9]')

            for mes in var_mes:
                dados_coluna9.append(mes.text)

        # Obter os dados da coluna Var.(12M)
        dados_coluna10 = []
        numero_linha = 0
        while i != numero_linha:
            numero_linha += 1
            var_12m = item.find_elements(
                By.XPATH, f'//*[@id="table"]/tbody/tr[{numero_linha}]/td[10]')

            for mes in var_12m:
                dados_coluna10.append(mes.text)

    dados = zip(dados_coluna1, dados_coluna2, dados_coluna3, dados_coluna4, dados_coluna5,
                dados_coluna6, dados_coluna7, dados_coluna8, dados_coluna9, dados_coluna10)

    return (dados)


def escrever_dados_arquivo(nome_arquivo, dados):
    # Escrever os dados em um arquivo CSV
    with open(nome_arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Escrever os dados das colunas no arquivo CSV
        writer.writerow(['Ticker', 'Empresa', 'Volume', 'Fech. Ant.', 'Mínima',
                        'Máxima', 'Última', 'Var.(Dia)', 'Var.(Mês)', 'Var.(12M)'])
        writer.writerows(dados)
