import pandas as pd
import sqlite3
import os
# pega a pasta do próprio arquivo .py que está rodando
PASTA_SCRIPT = os.path.dirname(os.path.abspath(__file__))

# sobe um nível (de Consultas → Projeto_integracao_dados)
PASTA_TRABALHO = os.path.dirname(PASTA_SCRIPT)


conn = sqlite3.connect(os.path.join(PASTA_TRABALHO, "BD" ,"acidentes_prf.db"))

comando_sql = """
SELECT 
    CASE 
        WHEN p.idade IS NULL THEN 'Não Informado'
        WHEN p.idade <= 17 THEN '01. Até 17 anos'
        WHEN p.idade BETWEEN 18 AND 24 THEN '02. 18 a 24 anos'
        WHEN p.idade BETWEEN 25 AND 34 THEN '03. 25 a 34 anos'
        WHEN p.idade BETWEEN 35 AND 44 THEN '04. 35 a 44 anos'
        WHEN p.idade BETWEEN 45 AND 54 THEN '05. 45 a 54 anos'
        WHEN p.idade BETWEEN 55 AND 64 THEN '06. 55 a 64 anos'
        ELSE '07. 65 anos ou mais'
    END AS faixa_etaria,
    p.estado_fisico,
    COUNT(*) AS quantidade
FROM fact_pessoa_acidente f
JOIN dim_pessoa p ON f.id_pessoa_sk = p.id_pessoa_sk
WHERE p.estado_fisico IS NOT NULL
GROUP BY faixa_etaria, p.estado_fisico
ORDER BY faixa_etaria ASC, quantidade DESC;
"""

resultado = pd.read_sql(comando_sql, conn)

print("--- RECOCORRÊNCIAS: FAIXA ETÁRIA x ESTADO FÍSICO ---")
print(resultado)