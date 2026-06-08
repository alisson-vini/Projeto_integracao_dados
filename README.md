# Projeto de integração de dados

## Dicionário de dados

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

### Identificação do Acidente (19)

| Campo | Descrição |
|---------|---------|
| `id` | Identificador único do acidente. |
| `causa_acidente` | Causa principal identificada para o acidente. |
| `tipo_acidente` | Tipo de acidente registrado (colisão frontal, saída de pista, etc.). |
| `classificacao_acidente` | Gravidade do acidente: sem vítimas, com vítimas feridas, com vítimas fatais ou ignorado. |

### Informações do Veículo (4)

| Campo | Descrição |
|---------|---------|
| `id_veiculo` | Identificador único do veículo envolvido. |
| `tipo_veiculo` | Categoria do veículo conforme o Código de Trânsito Brasileiro. |
| `marca` | Marca do veículo envolvido. |
| `ano_fabricacao_veiculo` | Ano de fabricação do veículo. |

### Local (21)
| Campo | Descrição |
|---------|---------|
| `id_local` | ID |
| `uf` | Unidade da Federação onde ocorreu o acidente. |
| `br` | Número da rodovia federal (BR) onde ocorreu o acidente. |
| `km` | Quilômetro da rodovia onde ocorreu o acidente. |
| `municipio` | Município da ocorrência. |
| `latitude` | Latitude do local do acidente em formato decimal. |
| `longitude` | Longitude do local do acidente em formato decimal. |
| `sentido_via` | Sentido da via considerando o ponto de colisão (crescente ou decrescente). |
| `uso_solo` | Indica se o local do acidente está em área urbana ou rural. |
| `tipo_pista` | Tipo de pista da rodovia (simples, dupla ou múltipla). |
| `Aclive` | variável booleana que indica a presença desse tipo de traçado (substitui a coluna traçado) |
| `Curva` | variável booleana que indica a presença desse tipo de traçado (substitui a coluna traçado) |
| `Declive` | variável booleana que indica a presença desse tipo de traçado (substitui a coluna traçado) |
| `Desvio Temporário` | variável booleana que indica a presença desse tipo de traçado (substitui a coluna traçado) |
| `Em Obras` | variável booleana que indica a presença desse tipo de traçado (substitui a coluna traçado) |
| `Interseção de Vias` | variável booleana que indica a presença desse tipo de traçado (substitui a coluna traçado) |
| `Ponte` | variável booleana que indica a presença desse tipo de traçado (substitui a coluna traçado) |
| `Reta` | variável booleana que indica a presença desse tipo de traçado (substitui a coluna traçado) |
| `Retorno Regulamentado` | variável booleana que indica a presença desse tipo de traçado (substitui a coluna traçado) |
| `Rotatória` | variável booleana que indica a presença desse tipo de traçado (substitui a coluna traçado) |
| `Túnel` | variável booleana que indica a presença desse tipo de traçado (substitui a coluna traçado) |
| `Viaduto` | variável booleana que indica a presença desse tipo de traçado (substitui a coluna traçado) |

### Clima (2)
| Campo | Descrição |
|---------|---------|
| `id_clima` | ID |
| `fase_dia` | Fase do dia no momento da ocorrência (amanhecer, pleno dia, anoitecer, etc.). |
| `condicao_meteorologica` | Condições climáticas no momento do acidente. |

|### Data (7)
| Campo | Descrição |
|---------|---------|
| `id_data` | ID |
| `data_inversa` | Data da ocorrência no formato `dd/mm/aaaa`. |
| `dia_semana` | Dia da semana em que ocorreu o acidente. |
| `horario` | Horário da ocorrência no formato `hh:mm:ss`. |
| `dia` | dia do mes (númerico) |
| `mes` | Mes do ano (numérico) |
| `ano` | ano |
| `trimestre` | trimestre do ano (numérico) |

### Informações Administrativas da PRF (3)

| Campo | Descrição |
|---------|---------|
| `id_adm_prf` | ID |
| `regional` | Superintendência Regional da Polícia Rodoviária Federal responsável pela área do acidente. |
| `delegacia` | Delegacia da PRF responsável pela circunscrição do local do acidente. |
| `uop` | Unidade Operacional da PRF responsável pela área do acidente. |

## Lista com todas as transformações feitas nos dados
- Alteração nos tipos de dados da seguinte forma:
    - data_inversa -> DateTime (DD/MM/YYYY)
    - horario -> (HH:MM:SS)
    - km -> float
    - longitude, latitude:
        - alterado o tipo para string, retirado os espaços extras e trocar o caracter "," por "." para transformar em float
- Na coluna `ano_fabricacao_veiculo` foi alterado as celulas que tinham valor 0 para NULL
- Foram removidas as colunas: `ilesos`, `feridos_leves`, `feridos_graves`, `mortos` porque essas informações já estão contidas na coluna `estado_fisico`
- Alteração na coluna de idade para resolver dois tipos de problemas
    - alterado as amostras com valor de idade igual a -1 (representa auxencia de valor) para conter NULL
    - retirados idades impossíveis (todas as idades superiores a 127 anos)
- Quase 40k linhas do dataser porque as pessoas envolvidas não tinham as informações de 3 colunas: estado_fisico, tipo_envolvido, sexo e além disso não tinham idade como 0 além de terem o mesmo ID pessoa, o que como mostrado antes provalvelmente é um erro de preenchimento ou que esse é usado para representar uma pessoa não identificada, por isso foi criada a coluna "identificada" que contem o valor 0 para esses casos e 1 para todo o resto
- Alterada a coluna "tracado_via", essa coluna armazenava multiplos valores em cada célula, para deixar todas as colunas da tabela contendo valores atómicos foi criado N colunas que vão armazenar um valor booleano (0 ou 1) identificando se a caracteristica descrita está ou não naquele acidente em questão, N vai ser a quantidade de valores diferentes atómicos que aquela que coluna "tracado_via" armazena, após isso a coluna "tracado_via" é removida.

## Observações relavantes
- A coluna de idade apresenta mais de 78k de amostras contendo idade igual a 0 (zero), essa mesma coluna possui aproximadamente 74k de amostras de pessoas entre 1-25 anos, é bem improvável que a taxa de pessoas recem nascides envolvidas em acidentes supere dessa forma a quantidade de pessoas entre 1-25 anos indicando que existem uma grande possibilidade de existir erro nesses dados, mas como isso não pode ser comprovado não teve moficição.

## Esquema estrela

### Tabela Fato
tabela: fact_pessoa_acidente

informação: cada linha representa uma pessoa envolvida em um acidente

campos:

    - pesid
    - id
    - id_veiculo
    - id_local
    - id_clima
    - id_data
    - id_adm_PRF

### Tabelas Dimensão

tabela: `dim_pessoa`

informação: armazena as informações de cada uma das pessoas envolvidas no acidente

campos:

    - pesid
    - estado_fisico
    - tipo_envolvido
    - idade
    - sexo

tabela: `dim_acidente`

informação: armazena as informações de cada uma das pessoas envolvidas no acidente

campos:

    - id
    - causa_acidente
    - tipo_acidente
    - classificacao_acidente

tabela: `dim_veiculo`

informação: armazena as informações de cada um dos veículos envolvidos

campos:

    - id_veiculo
    - tipo_veiculo
    - marca
    - ano_fabricacao_veiculo

tabela: `dim_local`

informação: armazena as informações de cada um dos locais do acidente

campos:

    - id_local
    - uf
    - br
    - km
    - municipio
    - latitude
    - longitude
    - sentido_via
    - uso_solo
    - tipo_pista
    - Aclive
    - Curva
    - Declive
    - Desvio Temporário
    - Em Obras
    - Interseção de Vias
    - Ponte
    - Reta
    - Retorno Regulamentado
    - Rotatória
    - Túnel
    - Viaduto

tabela: `dim_clima`

informação: armazena as informações do clima no momento do acidente

campos:

    - id_clima
    - fase_dia
    - condicao_meteorologica

tabela: `dim_data`

informação: armazena as informações da data do acidente

campos:

    - id_data
    - dia (numérico)
    - mes
    - ano
    - trimestre
    - data_inversa
    - dia_semana (escrito)
    - horario

tabela: `dim_adm_PRF`

informação: armazena as informações adiministraticas da PRF

campos:

    - id_adm_prf
    - regional
    - delegacia
    - uop