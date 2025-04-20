import requests

def obter_e_exibir_valores():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        dolar = data['USDBRL']['bid']
        euro = data['EURBRL']['bid']

        return dolar, euro

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return "Erro", "Erro"
    except KeyError as e:
        print(f"Erro ao processar os dados da API: Campo '{e}' não encontrado.")
        return "Erro", "Erro"
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return "Erro", "Erro"
