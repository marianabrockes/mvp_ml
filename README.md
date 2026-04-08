# MVP — Previsão Salarial de Profissionais de Tecnologia

Projeto desenvolvido para a disciplina **Engenharia de Sistemas de Software Inteligentes** da Pós-Graduação PUC-Rio.

## Problema de negócio

> Dado o perfil de formação, habilidades técnicas e região geográfica de um profissional de tecnologia, conseguimos prever em qual faixa salarial ele se enquadra?

A região geográfica foi incluída como feature deliberadamente — o mesmo perfil técnico tem remunerações muito diferentes dependendo do país. Ignorar essa variável geraria um modelo injusto e pouco útil.

## Dataset

- **Fonte:** Kaggle ML & Data Science Survey 2022
- **Respondentes:** ~23.000 profissionais e estudantes de tecnologia de mais de 50 países
- **URL:** https://raw.githubusercontent.com/marianabrockes/mvp_ml/refs/heads/main/notebook/kaggle_survey_2022_responses.csv

## Target

A variável-alvo é a faixa salarial anual agrupada em 3 classes:

| Faixa | Salário anual     |
| ----- | ----------------- |
| Baixo | Até $29.999       |
| Médio | $30.000 – $99.999 |
| Alto  | $100.000+         |

## Resultados

Quatro algoritmos foram treinados, otimizados com GridSearchCV e avaliados no conjunto de teste:

| Algoritmo               | Acurácia (cross-val) | Acurácia (teste) |
| ----------------------- | -------------------- | ---------------- |
| Árvore de Classificação | 68,5%                | **68,1%**        |
| SVM                     | 64,4%                | 63,7%            |
| KNN                     | 60,9%                | 60,9%            |
| Naive Bayes             | 57,4%                | 55,9%            |

O modelo vencedor foi a **Árvore de Classificação** com 68,1% de acurácia no teste.

## Estrutura do projeto

```
mvp_ml/
├── backend/
│   ├── app.py              # API Flask
│   ├── modelo.pkl          # Modelo treinado
│   ├── requirements.txt    # Dependências
│   └── tests/
│       └── test_modelo.py  # Teste PyTest (acurácia e F1-score ≥ 60%)
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

O teste verifica dois thresholds mínimos de desempenho:

- **Acurácia ≥ 60%**
- **F1-score ≥ 60%**

## Notebook

O notebook completo pode ser executado diretamente no Google Colab:

[Abrir no Google Colab](https://colab.research.google.com/drive/1bnkEAvfBIKebTpPcRX02qxdWVCu3CYT1)
