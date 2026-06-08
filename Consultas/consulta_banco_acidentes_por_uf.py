import pandas as pd
import sqlite3
import os
# pega a pasta do próprio arquivo .py que está rodando
PASTA_SCRIPT = os.path.dirname(os.path.abspath(__file__))

# sobe um nível (de Consultas → Projeto_integracao_dados)
PASTA_TRABALHO = os.path.dirname(PASTA_SCRIPT)


conn = sqlite3.connect(os.path.join(PASTA_TRABALHO, "BD" ,"acidentes_prf.db"))

comando_sql = """
SELECT l.uf, COUNT(*) AS quantidade_acidentes
FROM fact_pessoa_acidente f
JOIN dim_local l ON f.id_local_sk = l.id_local_sk
GROUP BY l.uf
ORDER BY quantidade_acidentes DESC;
"""

resultado = pd.read_sql(comando_sql, conn)

print("--- TOTAL DE ACIDENTES POR UF ---")
print(resultado)