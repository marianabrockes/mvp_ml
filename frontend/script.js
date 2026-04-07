async function prever() {
    // Pega os valores do formulário
    const form = document.getElementById('formulario')
// Esconde o resultado anterior, atualiza e mostra novamente
const resultado = document.getElementById('resultado')
resultado.classList.add('escondido')

setTimeout(() => {
    document.getElementById('faixa').textContent = `${classe} — ${faixas[classe]}`
    resultado.classList.remove('escondido')
    resultado.scrollIntoView({ behavior: 'smooth' })
}, 100)

    const dados = {
        idade: parseInt(form.idade.value),
        genero: parseInt(form.genero.value),
        escolaridade: parseInt(form.escolaridade.value),
        anos_programando: parseInt(form.anos_programando.value),
        anos_usando_ml: parseInt(form.anos_usando_ml.value),
        regiao: parseInt(form.regiao.value),

        // Linguagens — 1 se marcado, 0 se não
        lang_python: form.lang_python.checked ? 1 : 0,
        lang_r: form.lang_r.checked ? 1 : 0,
        lang_sql: form.lang_sql.checked ? 1 : 0,
        lang_c: form.lang_c.checked ? 1 : 0,
        lang_cpp: form.lang_cpp.checked ? 1 : 0,
        lang_java: form.lang_java.checked ? 1 : 0,
        lang_javascript: form.lang_javascript.checked ? 1 : 0,
        lang_bash: form.lang_bash.checked ? 1 : 0,

        // Cursos
        curso_coursera: form.curso_coursera.checked ? 1 : 0,
        curso_edx: form.curso_edx.checked ? 1 : 0,
        curso_kaggle: form.curso_kaggle.checked ? 1 : 0,
        curso_datacamp: form.curso_datacamp.checked ? 1 : 0,
        curso_fastai: form.curso_fastai.checked ? 1 : 0,
        curso_udacity: form.curso_udacity.checked ? 1 : 0,
        curso_udemy: form.curso_udemy.checked ? 1 : 0,
        curso_linkedin: form.curso_linkedin.checked ? 1 : 0,
        curso_cloud: form.curso_cloud.checked ? 1 : 0,
        curso_universidade: form.curso_universidade.checked ? 1 : 0,

        // Úteis
        util_universidade: form.util_universidade.checked ? 1 : 0,
        util_online: form.util_online.checked ? 1 : 0,
        util_social: form.util_social.checked ? 1 : 0,
        util_video: form.util_video.checked ? 1 : 0,
        util_kaggle: form.util_kaggle.checked ? 1 : 0,

        // ML frameworks
        ml_sklearn: form.ml_sklearn.checked ? 1 : 0,
        ml_tensorflow: form.ml_tensorflow.checked ? 1 : 0,
        ml_pytorch: form.ml_pytorch.checked ? 1 : 0,
    }

    const faixas = {
    'Baixo': 'Até $29.999 / ano',
    'Médio': '$30.000 – $99.999 / ano',
    'Alto': '$100.000+ / ano'
}

    try {
        const resposta = await fetch('http://127.0.0.1:5001/prever', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dados)
        })

        const resultado = await resposta.json()

        // Mostra o resultado
        const classe = resultado.faixa_salarial
document.getElementById('faixa').textContent = `${classe} — ${faixas[classe]}`
        document.getElementById('resultado').classList.remove('escondido')

        // Scroll para o resultado
        document.getElementById('resultado').scrollIntoView({ behavior: 'smooth' })

    } catch (erro) {
        alert('Erro ao conectar com a API. Verifique se o backend está rodando.')
    }
}
