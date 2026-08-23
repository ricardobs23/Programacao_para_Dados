import os
from steam_analyzer import SteamAnalyzer, SteamDataError

def main():
    caminho_dataset = os.path.join("dados", "dataset_completo.csv")
    
    try:
        print("Iniciando análise do dataset da Steam...")
        analyzer = SteamAnalyzer(caminho_dataset)
        
        # --- PERGUNTA 1 ---
        pct_free, pct_paid = analyzer.percentual_gratuitos_e_pagos()
        print("\n--- Pergunta 1: Distribuição de Gratuidade ---")
        print(f"Jogos Gratuitos: {pct_free}%")
        print(f"Jogos Pagos: {pct_paid}%")
        print(f"Análise: A plataforma Steam possui uma predominância expressiva de jogos pagos ({pct_paid}%), "
              f"demonstrando que o modelo de monetização por compra direta continua consolidado.")

        # --- PERGUNTA 2 ---
        anos_pico = analyzer.ano_com_mais_lancamentos()
        print("\n--- Pergunta 2: Ano Pico de Lançamentos ---")
        print(f"Ano(s) com maior volume de lançamentos: {anos_pico}")
        print(f"Análise: O alto volume registrado no(s) ano(s) {anos_pico} reflete a maturação e a "
              f"abertura da plataforma para desenvolvedores independentes via Steam Direct.")

        # --- PERGUNTA 3 ---
        ano_analise = anos_pico[0] if anos_pico else 2018
        res_p3 = analyzer.consulta_elaborada_fun_corp(ano_analise)
        print(f"\n--- Pergunta 3: Precificação no Ano Pico ({ano_analise}) ---")
        print(f"Preço médio dos jogos pagos: R$ {res_p3['preco_medio']}")
        print(f"Porcentagem de jogos > R$ 50.00: {res_p3['pct_acima_50']}%")
        print(f"Análise: No ano de pico, o preço médio manteve-se acessível (R$ {res_p3['preco_medio']}). "
              f"Apenas {res_p3['pct_acima_50']}% dos jogos superavam R$ 50,00, indicando que a Fun Corp. "
              f"deve focar em preços competitivos de entrada.")

    except SteamDataError as e:
        print(f"Erro no processamento dos dados: {e}")

if __name__ == "__main__":
    main()