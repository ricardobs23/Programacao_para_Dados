import re

class Jogo:
    """Classe que representa um jogo da plataforma Steam."""
    
    def __init__(self, app_id: str, nome: str, eh_gratuito: bool, preco: float, data_lancamento: str):
        self.app_id = app_id
        self.nome = nome
        self.eh_gratuito = eh_gratuito
        self.preco = preco
        self.data_lancamento = data_lancamento
        self.ano_lancamento = self._extrair_ano(data_lancamento)

    def _extrair_ano(self, data_str: str) -> int:
        """Extrai um ano de 4 dígitos (ex: 1998 a 2026) da string de data."""
        if not data_str:
            return 0
        match = re.search(r'\b(19\d\d|20\d\d)\b', data_str)
        if match:
            return int(match.group(1))
        return 0

    def __str__(self) -> str:
        tipo = "Gratuito" if self.eh_gratuito else f"R$ {self.preco:.2f}"
        return f"Jogo: {self.nome} ({self.ano_lancamento}) - {tipo}"