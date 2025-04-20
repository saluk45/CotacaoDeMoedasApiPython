import requests
import json

def obter_e_exibir_valores():
    """Obtém os valores da API e gera um HTML simples para exibição."""
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para erros HTTP
        data = response.json()

        # Extrair os valores desejados
        dolar = data['USDBRL']['bid']
        euro = data['EURBRL']['bid']

        
        # bitcoin = data['BTCBRL']['bid']


        print("Arquivo cotacoes.html gerado com sucesso!")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
    except KeyError as e:
        print(f"Erro ao processar os dados da API: Campo '{e}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    obter_e_exibir_valores()


    