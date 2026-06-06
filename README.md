## Dicionário de dados

### Identificação do Acidente (19)

| Campo | Descrição |
|---------|---------|
| `id` | Identificador único do acidente. |
| `data_inversa` | Data da ocorrência no formato `dd/mm/aaaa`. |
| `dia_semana` | Dia da semana em que ocorreu o acidente. |
| `horario` | Horário da ocorrência no formato `hh:mm:ss`. |
| `uf` | Unidade da Federação onde ocorreu o acidente. |
| `br` | Número da rodovia federal (BR) onde ocorreu o acidente. |
| `km` | Quilômetro da rodovia onde ocorreu o acidente. |
| `municipio` | Município da ocorrência. |
| `causa_acidente` | Causa principal identificada para o acidente. |
| `tipo_acidente` | Tipo de acidente registrado (colisão frontal, saída de pista, etc.). |
| `classificacao_acidente` | Gravidade do acidente: sem vítimas, com vítimas feridas, com vítimas fatais ou ignorado. |
| `fase_dia` | Fase do dia no momento da ocorrência (amanhecer, pleno dia, anoitecer, etc.). |
| `sentido_via` | Sentido da via considerando o ponto de colisão (crescente ou decrescente). |
| `condicao_meteorologica` | Condições climáticas no momento do acidente. |
| `tipo_pista` | Tipo de pista da rodovia (simples, dupla ou múltipla). |
| `tracado_via` | Características do traçado da via. |
| `uso_solo` | Indica se o local do acidente está em área urbana ou rural. |
| `latitude` | Latitude do local do acidente em formato decimal. |
| `longitude` | Longitude do local do acidente em formato decimal. |

### Informações da Pessoa Envolvida (9)

| Campo | Descrição |
|---------|---------|
| `pesid` | Identificador único da pessoa envolvida no acidente. |
| `tipo_envolvido` | Papel da pessoa no acidente (condutor, passageiro, pedestre, etc.). |
| `estado_fisico` | Condição física da pessoa após o acidente (ileso, ferido leve, ferido grave, morto, etc.). |
| `idade` | Idade da pessoa envolvida. Valor `-1` indica informação não coletada. |
| `sexo` | Sexo da pessoa envolvida. Valor `inválido` indica informação não coletada. |
| `ilesos` | Indicador binário que informa se a pessoa saiu ilesa. |
| `feridos_leves` | Indicador binário que informa se a pessoa sofreu ferimentos leves. |
| `feridos_graves` | Indicador binário que informa se a pessoa sofreu ferimentos graves. |
| `mortos` | Indicador binário que informa se a pessoa faleceu em decorrência do acidente. |

### Informações do Veículo (4)

| Campo | Descrição |
|---------|---------|
| `id_veiculo` | Identificador único do veículo envolvido. |
| `tipo_veiculo` | Categoria do veículo conforme o Código de Trânsito Brasileiro. |
| `marca` | Marca do veículo envolvido. |
| `ano_fabricacao_veiculo` | Ano de fabricação do veículo. |

### Informações Administrativas da PRF (3)

| Campo | Descrição |
|---------|---------|
| `regional` | Superintendência Regional da Polícia Rodoviária Federal responsável pela área do acidente. |
| `delegacia` | Delegacia da PRF responsável pela circunscrição do local do acidente. |
| `uop` | Unidade Operacional da PRF responsável pela área do acidente. |

## Lista com todas as transformações feitas nos dados
- Alteração nos tipos de dados da seguinte forma:
    - data_inversa -> DateTime (DD/MM/YYYY)
    - horario -> (HH:MM:SS)
- Na coluna `ano_fabricacao_veiculo` foi alterado as celulas que tinham valor 0 para NULL
- foram removidas as colunas: `ilesos`, `feridos_leves`, `feridos_graves`, `mortos` porque essas informações já estão contidas na coluna `estado_fisico`
- Alteração na coluna de idade para resolver dois tipos de problemas
    - alterado as amostras com valor de idade igual a -1 (representa auxencia de valor) para conter NULL
    - retirados idades impossíveis (todas as idades superiores a 127 anos)