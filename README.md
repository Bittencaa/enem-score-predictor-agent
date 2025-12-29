📊 ENEM School Performance Prediction Agent (ADK)
📌 Visão Geral

Este projeto apresenta o desenvolvimento de um agente inteligente utilizando o Google Agent Development Kit (ADK) para prever o índice médio de desempenho de escolas brasileiras no ENEM, com base em dados públicos do INEP e um modelo clássico de machine learning.

O objetivo é demonstrar, de forma prática e aplicada:

Uso de dados abertos governamentais brasileiros

Aplicação de machine learning não generativo em dados tabulares reais

Construção de um pipeline completo de ML (pré-processamento, treinamento, avaliação e inferência)

Encapsulamento do modelo em um agente ADK, permitindo previsões automatizadas a partir de solicitações estruturadas

🎯 Problema Abordado

Avaliar o desempenho educacional de escolas é fundamental para:

Formulação de políticas públicas

Planejamento educacional e alocação de recursos

Análise de desigualdades regionais e institucionais

Neste projeto, o foco é prever o índice médio de desempenho da escola no ENEM, representado pela variável NU_MEDIA_TOT, utilizando informações institucionais e educacionais da própria escola.

⚠️ Importante sobre a variável alvo

O valor previsto não representa a nota individual dos alunos (escala 0–1000).

Trata-se de um índice agregado de desempenho da escola, divulgado pelo INEP.

A escala observada nos dados é aproximadamente de 0 a 100.

Essa distinção é fundamental para a correta interpretação dos resultados.

📂 Fonte de Dados (INEP)

Os dados utilizados neste projeto são públicos e oficiais, disponibilizados pelo INEP.

Base: Microdados do ENEM – Resultados por Escola

Órgão: INEP — Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira

Link oficial para download:
https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem-por-escola

📥 Como obter o dataset (passo a passo)

⚠️ O arquivo CSV NÃO está incluído neste repositório, para manter o projeto leve e respeitar boas práticas de versionamento.

Siga os passos abaixo:

1️⃣ Acesse o link oficial do INEP acima
2️⃣ Faça o download do arquivo ZIP disponibilizado
3️⃣ Extraia o conteúdo do ZIP

Você encontrará a seguinte estrutura:

ENEM_POR_ESCOLA/
├── DADOS/
├── DICIONARIO/
├── INPUTS/
├── LEIA-ME e DOCUMENTOS TECNICOS



4️⃣ Entre na pasta DADOS/
5️⃣ Localize o arquivo:

MICRODADOS_ENEM_ESCOLA.csv


6️⃣ Crie uma pasta data/ no projeto e copie esse arquivo para essa pasta, ficando assim:

enem-adk-agent/
├── data/
│   └── MICRODADOS_ENEM_ESCOLA.csv


📌 Observações técnicas do arquivo:

Formato: CSV

Separador: ;

Encoding: latin1

Essas configurações já estão corretamente tratadas no código.

🎯 Variável alvo

NU_MEDIA_TOT
Índice médio de desempenho da escola no ENEM.

🧾 Principais variáveis utilizadas

Ano de referência (NU_ANO)

Número de matrículas e participantes

Taxas de aprovação, reprovação e abandono

Dependência administrativa da escola
(federal, estadual, municipal ou privada)

Localização da escola (urbana ou rural)

Porte da escola

Unidade federativa (UF)

As variáveis foram selecionadas com foco em:

Disponibilidade real nos dados públicos

Relevância educacional

Capacidade de generalização do modelo

🤖 Modelo de Machine Learning

Foi utilizado um Random Forest Regressor, um modelo clássico amplamente aplicado em dados tabulares por oferecer:

Robustez a ruído

Capacidade de modelar relações não lineares

Boa performance sem necessidade de normalização

Facilidade de uso e manutenção

🔧 Pipeline de Treinamento

O modelo foi treinado utilizando um pipeline do scikit-learn, garantindo reprodutibilidade e organização clara das etapas.

Pré-processamento

Tratamento de valores ausentes:

Variáveis numéricas → mediana

Variáveis categóricas → valor mais frequente

Codificação de variáveis categóricas:

One-Hot Encoding

Separação explícita entre features numéricas e categóricas

Treinamento

RandomForestRegressor

Múltiplas árvores

Paralelização (n_jobs=-1)

random_state fixo para reprodutibilidade

📏 Avaliação do Modelo

O desempenho foi avaliado em um conjunto de teste separado.

Métricas utilizadas

MAE (Mean Absolute Error)
Mede o erro médio absoluto entre o valor real e o valor previsto.

RMSE (Root Mean Squared Error)
Penaliza erros maiores e indica a dispersão do erro.

Resultados obtidos (valores aproximados)

MAE ≈ 3.0

RMSE ≈ 4.0

Esses resultados indicam que o modelo consegue prever o índice médio de desempenho das escolas com erro relativamente baixo, considerando a complexidade e variabilidade dos dados socioeducacionais.

🧠 Agente ADK

O modelo treinado foi encapsulado em um agente utilizando o Google Agent Development Kit (ADK).

Papel do agente

Atuar como camada de orquestração

Receber solicitações com características da escola

Acionar a função de inferência do modelo

Retornar a previsão de forma estruturada

Tool registrada

A função predict_enem_score foi registrada como tool do agente, permitindo sua invocação direta via ADK.

Esse design separa claramente:

Lógica de machine learning

Lógica de inferência

Camada de orquestração do agente

📁 Estrutura do Projeto
enem-adk-agent/
│
├── agent/
│   ├── agent.py          # Definição do agente ADK
│   ├── tools.py          # Tool de predição (inferência do modelo)
│   └── test_agent.py     # Testes funcionais do agente
│
├── ml/
│   ├── train_model.py    # Script de treinamento
│   └── model.pkl         # Modelo treinado
│
├── data/
│   └── MICRODADOS_ENEM_ESCOLA.csv   # (baixado manualmente)
│
├── requirements.txt
└── README.md

▶️ Como Executar o Projeto
1️⃣ Criar ambiente virtual
python -m venv .venv


Ativar:

Linux / macOS

source .venv/bin/activate


Windows

.venv\Scripts\activate

2️⃣ Instalar dependências
pip install -r requirements.txt

3️⃣ Treinar o modelo
python ml/train_model.py

4️⃣ Testar o agente
python agent/test_agent.py


O script executa:

Cenários favoráveis e desfavoráveis

Testes de sensibilidade

Casos de borda (edge cases)

🧪 Exemplo de Uso
from tools import predict_enem_score

result = predict_enem_score(
    nu_ano=2022,
    nu_matriculas=500,
    nu_participantes=200,
    nu_taxa_aprovacao=85.0,
    nu_taxa_reprovacao=10.0,
    nu_taxa_abandono=5.0,
    tp_dependencia_adm_escola=2,
    tp_localizacao_escola=1,
    porte_escola="Maior que 90 alunos",
    sg_uf_escola="SP"
)

print(result)

👤 Autor

Guilherme Bitencourt Souza