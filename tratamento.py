import pandas as pd

TRANSLATE_COLUMNS = {
    "Country name": "País",
    "year": "Ano",
    "Life Ladder": "Índice de Felicidade",
    "Log GDP per capita": "PIB per capita (log)",
    "Social support": "Suporte Social",
    "Healthy life expectancy at birth": "Expectativa de Vida Saudável",
    "Freedom to make life choices": "Liberdade de Escolha",
    "Generosity": "Generosidade",
    "Perceptions of corruption": "Percepção de Corrupção",
    "Positive affect": "Afeto Positivo",
    "Negative affect": "Afeto Negativo"
}

def carregar_dados():
    df = pd.read_csv("dataset/World Happiness Report 2024.csv")
    df = df.rename(columns=TRANSLATE_COLUMNS)
    df = df.dropna()

    if "País" in df.columns:
        df["País"] = df["País"].astype(str).str.strip().str.title()

    return df