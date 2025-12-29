from google.adk import Agent
from tools import predict_enem_score


agent = Agent(
    name="enem_score_predictor",
    description=(
        "Agent that predicts the average ENEM score of a Brazilian school "
        "using public INEP data and a classical machine learning model."
    ),
    tools=[predict_enem_score],
)
