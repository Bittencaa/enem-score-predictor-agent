import os
import joblib
import pandas as pd


# Load model once (good practice)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "model.pkl")

model = joblib.load(MODEL_PATH)


def predict_enem_score(
    nu_ano: int,
    nu_matriculas: int,
    nu_participantes: int,
    nu_taxa_aprovacao: float,
    nu_taxa_reprovacao: float,
    nu_taxa_abandono: float,
    tp_dependencia_adm_escola: int,
    tp_localizacao_escola: int,
    porte_escola: str,
    sg_uf_escola: str
) -> float:
    """
    Predict the average ENEM score for a school.
    """

    data = {
        "NU_ANO": [nu_ano],
        "NU_MATRICULAS": [nu_matriculas],
        "NU_PARTICIPANTES": [nu_participantes],
        "NU_TAXA_PARTICIPACAO": [None],
        "INSE": [None],
        "PC_FORMACAO_DOCENTE": [None],
        "NU_TAXA_PERMANENCIA": [None],
        "NU_TAXA_APROVACAO": [nu_taxa_aprovacao],
        "NU_TAXA_REPROVACAO": [nu_taxa_reprovacao],
        "NU_TAXA_ABANDONO": [nu_taxa_abandono],
        "TP_DEPENDENCIA_ADM_ESCOLA": [tp_dependencia_adm_escola],
        "TP_LOCALIZACAO_ESCOLA": [tp_localizacao_escola],
        "PORTE_ESCOLA": [porte_escola],
        "SG_UF_ESCOLA": [sg_uf_escola],
    }

    df = pd.DataFrame(data)

    prediction = model.predict(df)[0]

    return round(float(prediction), 2)

