import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from steam_analyzer import SteamAnalyzer

def test_validar_amostra_20_jogos():
    caminho_amostra = os.path.join("dados", "amostra_20_jogos.csv")
    analyzer = SteamAnalyzer(caminho_amostra)

    # 1. Teste da Pergunta 1
    pct_free, pct_paid = analyzer.percentual_gratuitos_e_pagos()
    assert pct_free == 20.0, f"Erro P1 Free: Esperado 20.0%, obteve {pct_free}%"
    assert pct_paid == 80.0, f"Erro P1 Paid: Esperado 80.0%, obteve {pct_paid}%"

    # 2. Teste da Pergunta 2
    anos_pico = analyzer.ano_com_mais_lancamentos()
    assert set(anos_pico) == {2016, 2022}, f"Erro P2 Anos Pico: Esperado [2016, 2022], obteve {anos_pico}"

    # 3. Teste da Pergunta 3 (Ano 2016)
    res_p3 = analyzer.consulta_elaborada_fun_corp(2016)
    assert res_p3["preco_medio"] == 5.98, f"Erro P3 Preço Médio: Esperado 5.98, obteve {res_p3['preco_medio']}"
    assert res_p3["pct_acima_50"] == 0.0, f"Erro P3 % > 50: Esperado 0.0%, obteve {res_p3['pct_acima_50']}%"

    print("✓ Todos os testes da amostra de 20 jogos passaram com sucesso!")

if __name__ == "__main__":
    test_validar_amostra_20_jogos()