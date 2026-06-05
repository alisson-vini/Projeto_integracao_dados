"""
é um arquivo apenas para testar funções/trechos de códigos de forma fácil, deve ser removido posteriormente
"""

import pandas as pd
import os

# pegando a pasta de trabalho para poder extrair os dados do dataset
PASTA_TRABALHO = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

print(PASTA_TRABALHO)