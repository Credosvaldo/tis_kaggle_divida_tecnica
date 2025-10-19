

# Dados Tabulares
# House Prices - Advanced Regression Techniques | house-prices-advanced-regression-techniques
# Titanic - Machine Learning from Disaster | titanic
# Santander Customer Transaction Prediction | santander-customer-transaction-prediction


# Visão Computacional (CV)
# Digit Recognizer | digit-recognizer
# Cassava Leaf Disease Classification | cassava-leaf-disease-classification
# HuBMAP - Kidney Segmentation | hubmap-kidney-segmentation


# Processamento de Linguagem Natural (NLP)
# Natural Language Processing with Disaster Tweets | nlp-getting-started
# Jigsaw Unintended Bias in Toxicity Classification | jigsaw-unintended-bias-in-toxicity-classification
# CommonLit Readability Prize | commonlitreadabilityprize


# house-prices-advanced-regression-techniques
# titanic
# santander-customer-transaction-prediction
# digit-recognizer
# cassava-leaf-disease-classification
# hubmap-kidney-segmentation
# nlp-getting-started
# jigsaw-unintended-bias-in-toxicity-classification
# commonlitreadabilityprize

import os

competitions = [
    {
        "name": "house-prices-advanced-regression-techniques",
        "type": "Dados Tabulares"
    },
    {
        "name": "titanic",
        "type": "Dados Tabulares"
    },
    {
        "name": "santander-customer-transaction-prediction",
        "type": "Dados Tabulares"
    },
    {
        "name": "digit-recognizer",
        "type": "Visão Computacional"
    },
    {
        "name": "cassava-leaf-disease-classification",
        "type": "Visão Computacional"
    },
    {
        "name": "hubmap-kidney-segmentation",
        "type": "Visão Computacional"
    },
    {
        "name": "nlp-getting-started",
        "type": "NLP"
    },
    {
        "name": "jigsaw-unintended-bias-in-toxicity-classification",
        "type": "NLP"
    },
    {
        "name": "commonlitreadabilityprize",
        "type": "NLP"
    }
]


for competition in competitions:
    print(f"Competition: {competition['name']} | Type: {competition['type']}")
    
    