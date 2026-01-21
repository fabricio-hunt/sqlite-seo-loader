import os
import sqlite3
import pandas as pd

# 1. Configurações
caminho_pasta = r"C:\Users\fabricio.barauna\Downloads\https___www.bemol.com.br_-Performance-on-Search-2026-01-21"
nome_banco = "bemol_search.db"

# Conecta ao banco (cria se não existir)
conn = sqlite3.connect(nome_banco)

# 2. Lista os arquivos esperados (baseado na sua imagem)
arquivos = [
    "Consultas", "Páginas", "Países", "Dispositivos", 
    "Aspecto da pesquisa", "Filtros", "Gráfico"
]

def limpar_colunas(col):
    """Transforma 'Top consultas' em 'top_consultas'"""
    return col.strip().lower().replace(" ", "_")

# 3. Processamento
print(f"Iniciando importação em: {caminho_pasta}...\n")

for arquivo in arquivos:
    caminho_completo = os.path.join(caminho_pasta, f"{arquivo}.csv")
    
    if os.path.exists(caminho_completo):
        try:
            # Tenta ler como CSV. Se der erro de encoding, tenta latin1
            try:
                df = pd.read_csv(caminho_completo)
            except UnicodeDecodeError:
                df = pd.read_csv(caminho_completo, encoding='latin1')
            
            # Limpa os nomes das colunas
            df.columns = [limpar_colunas(c) for c in df.columns]
            
            # Salva no SQLite
            # Nome da tabela será o nome do arquivo limpo (ex: aspecto_da_pesquisa)
            nome_tabela = limpar_colunas(arquivo)
            df.to_sql(nome_tabela, conn, if_exists='replace', index=False)
            
            print(f"[OK] Tabela '{nome_tabela}' criada com {len(df)} linhas.")
            
        except Exception as e:
            print(f"[ERRO] Falha ao ler {arquivo}: {e}")
    else:
        print(f"[AVISO] Arquivo não encontrado: {arquivo}.csv (Verifique a extensão)")

conn.close()
print(f"\nConcluído! Abra o arquivo '{nome_banco}' no seu app SQLite.")