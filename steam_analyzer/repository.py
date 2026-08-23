import csv
from typing import List
from .models import Jogo
from .exceptions import ArquivoInvalidoError

class JogoRepository:
    """Classe responsável pelo carregamento e persistência dos dados dos jogos."""
    
    def __init__(self, caminho_csv: str):
        self.caminho_csv = caminho_csv

    def carregar_jogos(self) -> List[Jogo]:
        """Lê o arquivo CSV utilizando a biblioteca nativa `csv` e retorna objetos `Jogo`."""
        jogos = []
        try:
            with open(self.caminho_csv, mode='r', encoding='utf-8', errors='ignore') as arquivo:
                leitor = csv.DictReader(arquivo)
                for linha in leitor:
                    # Captura o preço tratando fallback para nomes com maiúsculas/minúsculas
                    preco_str = linha.get('Price', linha.get('price', '0.0')).strip()
                    try:
                        preco = float(preco_str)
                    except ValueError:
                        preco = 0.0

                    # No dataset, jogo é gratuito se Price == 0.0 ou se 'is_free' for True
                    is_free_col = linha.get('is_free', '').strip().lower() in ['true', '1']
                    eh_gratuito = (preco == 0.0) or is_free_col

                    jogo = Jogo(
                        app_id=linha.get('AppID', linha.get('appid', '')),
                        nome=linha.get('Name', linha.get('name', 'Desconhecido')),
                        eh_gratuito=eh_gratuito,
                        preco=preco,
                        data_lancamento=linha.get('Release date', linha.get('release_date', ''))
                    )
                    jogos.append(jogo)
            return jogos
        except FileNotFoundError:
            raise ArquivoInvalidoError(f"Arquivo não encontrado: {self.caminho_csv}")
        except Exception as e:
            raise ArquivoInvalidoError(f"Erro ao ler o arquivo CSV: {e}")