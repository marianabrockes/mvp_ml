import pickle
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Carrega o modelo na inicialização
with open('modelo.pkl', 'rb') as f:
    modelo = pickle.load(f)

@app.route('/', methods=['GET'])
def status():
    return jsonify({'status': 'ok', 'mensagem': 'API de previsão salarial no ar!'})

@app.route('/prever', methods=['POST'])
def prever():
    dados = request.get_json()

    # Ordem das features exatamente como o modelo foi treinado
    features = [
        dados['idade'],
        dados['genero'],
        dados['escolaridade'],
        dados['anos_programando'],
        dados['anos_usando_ml'],
        dados['curso_coursera'],
        dados['curso_edx'],
        dados['curso_kaggle'],
        dados['curso_datacamp'],
        dados['curso_fastai'],
        dados['curso_udacity'],
        dados['curso_udemy'],
        dados['curso_linkedin'],
        dados['curso_cloud'],
        dados['curso_universidade'],
        dados['util_universidade'],
        dados['util_online'],
        dados['util_social'],
        dados['util_video'],
        dados['util_kaggle'],
        dados['lang_python'],
        dados['lang_r'],
        dados['lang_sql'],
        dados['lang_c'],
        dados['lang_cpp'],
        dados['lang_java'],
        dados['lang_javascript'],
        dados['lang_bash'],
        dados['ml_sklearn'],
        dados['ml_tensorflow'],
        dados['ml_pytorch'],
        dados['regiao']
    ]

    entrada = np.array(features).reshape(1, -1)
    predicao = modelo.predict(entrada)[0]

    return jsonify({'faixa_salarial': predicao})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)