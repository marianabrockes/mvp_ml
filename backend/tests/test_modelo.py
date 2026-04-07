import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Threshold mínimo de acurácia exigido
THRESHOLD = 0.60

def test_modelo_acuracia():
    """Verifica se o modelo atinge acurácia mínima de 60% no conjunto de teste."""

    # Carrega o modelo
    with open('modelo.pkl', 'rb') as f:
        modelo = pickle.load(f)

    # Carrega o dataset
    url = 'https://raw.githubusercontent.com/marianabrockes/mvp_ml/refs/heads/main/notebook/kaggle_survey_2022_responses.csv'
    df = pd.read_csv(url, skiprows=1)

    # Reproduz o mesmo pré-processamento do notebook
    from sklearn.preprocessing import LabelEncoder

    colunas_selecionadas = {
        df.columns[1]: 'idade',
        df.columns[2]: 'genero',
        df.columns[3]: 'pais',
        df.columns[24]: 'escolaridade',
        df.columns[29]: 'anos_programando',
        df.columns[90]: 'anos_usando_ml',
        df.columns[5]: 'curso_coursera',
        df.columns[6]: 'curso_edx',
        df.columns[7]: 'curso_kaggle',
        df.columns[8]: 'curso_datacamp',
        df.columns[9]: 'curso_fastai',
        df.columns[10]: 'curso_udacity',
        df.columns[11]: 'curso_udemy',
        df.columns[12]: 'curso_linkedin',
        df.columns[13]: 'curso_cloud',
        df.columns[14]: 'curso_universidade',
        df.columns[17]: 'util_universidade',
        df.columns[18]: 'util_online',
        df.columns[19]: 'util_social',
        df.columns[20]: 'util_video',
        df.columns[21]: 'util_kaggle',
        df.columns[30]: 'lang_python',
        df.columns[31]: 'lang_r',
        df.columns[32]: 'lang_sql',
        df.columns[33]: 'lang_c',
        df.columns[35]: 'lang_cpp',
        df.columns[36]: 'lang_java',
        df.columns[37]: 'lang_javascript',
        df.columns[38]: 'lang_bash',
        df.columns[91]: 'ml_sklearn',
        df.columns[92]: 'ml_tensorflow',
        df.columns[94]: 'ml_pytorch',
        df.columns[158]: 'salario'
    }

    df_sel = df[list(colunas_selecionadas.keys())].copy()
    df_sel.columns = list(colunas_selecionadas.values())

    # Mapeamento de regiões
    mapa_regioes = {
        'United States of America': 'América do Norte', 'Canada': 'América do Norte',
        'Mexico': 'América do Norte', 'Brazil': 'América do Sul',
        'Colombia': 'América do Sul', 'Argentina': 'América do Sul',
        'Chile': 'América do Sul', 'Peru': 'América do Sul',
        'United Kingdom of Great Britain and Northern Ireland': 'Europa',
        'Germany': 'Europa', 'France': 'Europa', 'Spain': 'Europa',
        'Italy': 'Europa', 'Netherlands': 'Europa', 'Poland': 'Europa',
        'Portugal': 'Europa', 'Russia': 'Europa', 'Turkey': 'Europa',
        'India': 'Ásia', 'China': 'Ásia', 'Japan': 'Ásia',
        'South Korea': 'Ásia', 'Indonesia': 'Ásia', 'Pakistan': 'Ásia',
        'Bangladesh': 'Ásia', 'Viet Nam': 'Ásia', 'Thailand': 'Ásia',
        'Malaysia': 'Ásia', 'Philippines': 'Ásia', 'Singapore': 'Ásia',
        'Nigeria': 'África', 'Kenya': 'África', 'South Africa': 'África',
        'Egypt': 'África', 'Ghana': 'África', 'Australia': 'Oceania',
        'New Zealand': 'Oceania', 'Ireland': 'Europa', 'Nepal': 'Ásia',
        'Sri Lanka': 'Ásia', 'Zimbabwe': 'África',
    }
    df_sel['regiao'] = df[df.columns[3]].map(mapa_regioes).fillna('Não informado')

    # Mapeamento salarial
    mapa_salario = {
        '$0-999': 'Baixo', '1,000-1,999': 'Baixo', '2,000-2,999': 'Baixo',
        '3,000-3,999': 'Baixo', '4,000-4,999': 'Baixo', '5,000-7,499': 'Baixo',
        '7,500-9,999': 'Baixo', '10,000-14,999': 'Baixo', '15,000-19,999': 'Baixo',
        '20,000-24,999': 'Baixo', '25,000-29,999': 'Baixo',
        '30,000-39,999': 'Médio', '40,000-49,999': 'Médio', '50,000-59,999': 'Médio',
        '60,000-69,999': 'Médio', '70,000-79,999': 'Médio', '80,000-89,999': 'Médio',
        '90,000-99,999': 'Médio', '100,000-124,999': 'Alto', '125,000-149,999': 'Alto',
        '150,000-199,999': 'Alto', '200,000-249,999': 'Alto', '250,000-299,999': 'Alto',
        '300,000-499,999': 'Alto', '$500,000-999,999': 'Alto', '>$1,000,000': 'Alto',
    }
    df_sel['faixa_salarial'] = df_sel['salario'].map(mapa_salario)

    # Remove nulos
    df_model = df_sel.dropna(subset=['faixa_salarial']).copy()
    df_model = df_model.drop(columns=['salario', 'pais'])

    # Colunas binárias
    colunas_binarias = [
        'curso_coursera', 'curso_edx', 'curso_kaggle', 'curso_datacamp',
        'curso_fastai', 'curso_udacity', 'curso_udemy', 'curso_linkedin',
        'curso_cloud', 'curso_universidade', 'util_universidade', 'util_online',
        'util_social', 'util_video', 'util_kaggle', 'lang_python', 'lang_r',
        'lang_sql', 'lang_c', 'lang_cpp', 'lang_java', 'lang_javascript',
        'lang_bash', 'ml_sklearn', 'ml_tensorflow', 'ml_pytorch'
    ]
    for col in colunas_binarias:
        df_model[col] = df_model[col].apply(lambda x: 0 if pd.isna(x) else 1)

    moda_ml = df_model['anos_usando_ml'].mode()[0]
    df_model['anos_usando_ml'] = df_model['anos_usando_ml'].fillna(moda_ml)

    # Encoding
    le = LabelEncoder()
    for col in ['idade', 'genero', 'escolaridade', 'anos_programando', 'anos_usando_ml', 'regiao']:
        df_model[col] = le.fit_transform(df_model[col].astype(str))

    # Separa X e y
    X = df_model.drop(columns=['faixa_salarial'])
    y = df_model['faixa_salarial']

    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Avalia
    y_pred = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred)

    print(f"Acurácia no teste: {acuracia:.4f}")
    print(f"Threshold mínimo: {THRESHOLD}")

    assert acuracia >= THRESHOLD, f"Acurácia {acuracia:.4f} abaixo do threshold {THRESHOLD}"