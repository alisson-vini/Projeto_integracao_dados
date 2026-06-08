import pandas as pd
import sqlite3
import os
# pega a pasta do próprio arquivo .py que está rodando
PASTA_SCRIPT = os.path.dirname(os.path.abspath(__file__))

# sobe um nível (de Consultas → Projeto_integracao_dados)
PASTA_TRABALHO = os.path.dirname(PASTA_SCRIPT)


conn = sqlite3.connect(os.path.join(PASTA_TRABALHO, "BD" ,"acidentes_prf.db"))

comando_sql = """
SELECT causa_acidente, COUNT(*) AS quantidade
FROM dim_acidente
GROUP BY causa_acidente
ORDER BY quantidade DESC
LIMIT 10;
"""

resultado = pd.read_sql(comando_sql, conn)

print("--- 10 PRINCIPAIS CAUSAS DE ACIDENTES ---")
print(resultado)