from flask import Flask, request
from my_sql import *

app = Flask(__name__) 

alunos = []
disciplina = []
matricula = []


# ALUNOS

@app.route('/cadastro_aluno', methods=['POST'])
def cadastro_aluno():
    info_aluno = request.json

    inserir_aluno(info_aluno['nome'], info_aluno['cpf'], info_aluno['idade'])

    resp = 'Aluno cadastrado com sucesso!'

    return resp, 201


@app.route('/lista_alunos', methods=['GET'])
def lista_alunos():

    resp = {
        'alunos': alunos
    }

    return resp, 200

@app.route('/atualiza_aluno', methods=['POST'])
def atualiza_aluno():

    aluno_novo = request.json

    for aluno in alunos:
        if aluno['id'] == aluno_novo['id']:
            alunos.remove(aluno)
            alunos.append(aluno_novo)

            resp = 'Aluno atualizado com sucesso!'

    return resp, 201

@app.route('/busca_aluno', methods=['GET'])
def busca_aluno():

    aluno_desejado = request.json

    for aluno in alunos:
        if aluno['id'] == aluno_desejado['id'] or aluno['nome'] == aluno_desejado['nome']:
            resp = aluno

    return resp, 200

@app.route('/remove_aluno', methods=['POST'])
def remove_aluno():

    aluno_remover = request.json

    for aluno in alunos:
        if aluno['id'] == aluno_remover['id']:
            alunos.remove(aluno)

            resp = 'Aluno removido com sucesso!'

    return resp, 201


# DISCIPLINAS

@app.route('/cadastro_disciplina', methods=['POST'])
def cadastro_disciplina():
    info_disciplina = request.json

    disciplina.append(info_disciplina)

    resp = 'Disciplina cadastrada com sucesso!'

    return resp, 201

@app.route('/lista_disciplinas', methods=['GET'])
def lista_disciplinas():

    resp = {
        'disciplinas': disciplina
    }

    return resp, 200

@app.route('/atualiza_disciplina', methods=['POST'])
def atualiza_disciplina():

    disciplina_nova = request.json

    for disc in disciplina:
        if disc['id'] == disciplina_nova['id']:
            disciplina.remove(disc)
            disciplina.append(disciplina_nova)

            resp = 'Disciplina atualizada com sucesso!'

    return resp, 201

@app.route('/busca_disciplina', methods=['GET'])
def busca_disciplina():

    disciplina_desejada = request.json

    for disc in disciplina:
        if disc['id'] == disciplina_desejada['id'] or disc['nome'] == disciplina_desejada['nome']:
            resp = disc

    return resp, 200

@app.route('/remove_disciplina', methods=['POST'])
def remove_disciplina():

    disciplina_remover = request.json

    for disc in disciplina:
        if disc['id'] == disciplina_remover['id']:
            disciplina.remove(disc)

            resp = 'Disciplina removida com sucesso!'

    return resp, 201


# MATRICULA




if __name__ == '__main__':
    app.run(debug=True)
