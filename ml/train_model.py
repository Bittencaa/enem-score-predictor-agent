import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error


# =========================
# 1. Carrega o dataset
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "MICRODADOS_ENEM_ESCOLA.csv")

print("Loading dataset from:", DATA_PATH)
print("File exists:", os.path.exists(DATA_PATH))

df = pd.read_csv(DATA_PATH, sep=";", encoding="latin1")


# =========================
# 2. Definição da variavel alvo e das variaveis explicativas
# =========================
TARGET = "NU_MEDIA_TOT" # Índice médio de desempenho da escola no ENEM (escala 0–100)

NUMERICAL_FEATURES = [
    "NU_ANO",
    "NU_MATRICULAS",
    "NU_PARTICIPANTES",
    "NU_TAXA_PARTICIPACAO",
    "INSE",
    "PC_FORMACAO_DOCENTE",
    "NU_TAXA_PERMANENCIA",
    "NU_TAXA_APROVACAO",
    "NU_TAXA_REPROVACAO",
    "NU_TAXA_ABANDONO"
]

CATEGORICAL_FEATURES = [
    "TP_DEPENDENCIA_ADM_ESCOLA",
    "TP_LOCALIZACAO_ESCOLA",
    "PORTE_ESCOLA",
    "SG_UF_ESCOLA"
]

FEATURES = NUMERICAL_FEATURES + CATEGORICAL_FEATURES

df = df[FEATURES + [TARGET]]

# Remove linhas sem valor da variável alvo
df = df.dropna(subset=[TARGET])

# =========================
# 3. Separação dos dados em treino e teste
# =========================
X = df.drop(columns=[TARGET])
y = df[TARGET]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# 4. Pré-processamento dos dados
# =========================
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, NUMERICAL_FEATURES),
        ("cat", categorical_transformer, CATEGORICAL_FEATURES)
    ]
)

# =========================
# 5. Modelo
# =========================
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", model)
])

# =========================
# 6. Treinamento do modelo
# =========================
pipeline.fit(X_train, y_train)

# =========================
# 7. Avaliação do modelo
# =========================
y_pred = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5


print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")

# =========================
# 8. Salva o modelo treinado
# =========================
MODEL_PATH = os.path.join(BASE_DIR, "ml", "model.pkl")
joblib.dump(pipeline, MODEL_PATH)

print(f"Model saved to {MODEL_PATH}")
