from typing import List, Dict, Tuple
from .models import Jogo
from .repository import JogoRepository

class SteamAnalyzer:
    """Classe responsável por executar consultas analíticas sobre os dados da Steam."""
    
    def __init__(self, caminho_csv: str):
        repo = JogoRepository(caminho_csv)
        self.jogos: List[Jogo] = repo.carregar_jogos()

    def percentual_gratuitos_e_pagos(self) -> Tuple[float, float]:
        """Pergunta 1: Retorna a porcentagem de jogos gratuitos e pagos."""
        if not self.jogos:
            return 0.0, 0.0
        
        total = len(self.jogos)
        gratuitos = sum(1 for j in self.jogos if j.eh_gratuito)
        pagos = total - gratuitos
        
        pct_gratuitos = round((gratuitos / total) * 100, 2)
        pct_pagos = round((pagos / total) * 100, 2)
        
        return pct_gratuitos, pct_pagos

    def ano_com_mais_lancamentos(self) -> List[int]:
        """Pergunta 2: Retorna o(s) ano(s) com o maior número de lançamentos."""
        contagem: Dict[int, int] = {}
        for jogo in self.jogos:
            if jogo.ano_lancamento > 0:
                contagem[jogo.ano_lancamento] = contagem.get(jogo.ano_lancamento, 0) + 1
        
        if not contagem:
            return []
            
        max_lancamentos = max(contagem.values())
        return [ano for ano, qtd in contagem.items() if qtd == max_lancamentos]

    def consulta_elaborada_fun_corp(self, ano_alvo: int) -> Dict[str, float]:
        """Pergunta 3 (Elaborada): Analisa os jogos pagos em um ano específico.
        Retorna preço médio e porcentagem de jogos com valor acima de R$ 50.00.
        """
        jogos_ano = [j for j in self.jogos if j.ano_lancamento == ano_alvo and not j.eh_gratuito]
        
        if not jogos_ano:
            return {"preco_medio": 0.0, "pct_acima_50": 0.0}
            
        soma_precos = sum(j.preco for j in jogos_ano)
        preco_medio = soma_precos / len(jogos_ano)
        
        acima_50 = sum(1 for j in jogos_ano if j.preco > 50.0)
        pct_acima_50 = (acima_50 / len(jogos_ano)) * 100
        
        return {
            "preco_medio": round(preco_medio, 2),
            "pct_acima_50": round(pct_acima_50, 2)
        }