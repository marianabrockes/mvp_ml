# MVP — Previsão Salarial de Profissionais de Tecnologia

Projeto desenvolvido para a disciplina **Engenharia de Sistemas de Software Inteligentes** da Pós-Graduação PUC-Rio.

## Problema de negócio

> Dado o perfil de formação, habilidades técnicas e região geográfica de um profissional de tecnologia, conseguimos prever em qual faixa salarial ele se enquadra?

## Dataset

- **Fonte:** Kaggle ML & Data Science Survey 2022
- **Respondentes:** ~23.000 profissionais e estudantes de tecnologia de mais de 50 países
- **URL:** https://raw.githubusercontent.com/marianabrockes/mvp_ml/refs/heads/main/notebook/kaggle_survey_2022_responses.csv

## Modelo

Quatro algoritmos foram treinados e comparados:

| Algoritmo               | Acurácia |
| ----------------------- | -------- |
| Árvore de Classificação | 68,1%    |
| SVM                     | 63,7%    |
| KNN                     | 60,9%    |
| Naive Bayes             | 55,9%    |

O modelo vencedor foi a **Árvore de Classificação** com 68,1% de acurácia.

## Estrutura do projeto

```
mvp_ml/
├── backend/
│   ├── app.py              # API Flask
│   ├── modelo.pkl          # Modelo treinado
│   ├── requirements.txt    # Dependências
│   └── tests/
│       └── test_modelo.py  # Teste PyTest
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── notebook/
│   ├── kaggle_survey_2022_responses.csv
│   └── ml_kaggle_survey_2022.ipynb
└── README.md
```

## Como executar

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

A API ficará disponível em `http://127.0.0.1:5001`

### Frontend

Abra o arquivo `frontend/index.html` diretamente no navegador.

### Testes

```bash
cd backend
source venv/bin/activate
pytest tests/test_modelo.py -v
```

## Notebook

O notebook completo está disponível em `notebook/ml_kaggle_survey_2022.ipynb` e pode ser executado diretamente no Google Colab.

## Vídeo

[Link do vídeo — em breve]
