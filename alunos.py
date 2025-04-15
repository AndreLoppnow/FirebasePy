from flask import Flask, request, jsonify
import idcontador
import conexao

app = Flask(__name__)

def aluno(nome, idade, curso, id):
    aluno = {
        'id': id,
        'nome': nome,
        'idade': idade,
        'curso': curso,
        'ativo': True
    }
    return aluno


def adicionar_aluno(nome, idade, curso):
    novoId = idcontador.ProximoId('contadorId')
    novoAluno = aluno(nome, idade, curso, novoId)
    alunoRef = conexao.db.reference('Alunos')
    alunoRef.child(str(novoId)).set(novoAluno)
    print(f"Aluno {nome} adicionado com sucesso.")
    
    
def listar_alunos():
    alunosRef = conexao.db.reference('Alunos')
    alunos = alunosRef.get()
    if alunos:
        for i, aluno in enumerate(alunos):
            if aluno:
                print(f"ID: {i}, Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}, Ativo: {aluno['ativo']}")
    else:
        print("Nenhum aluno encontrado.")
    
        
def inativar_aluno(alunoId):
    alunoRef = conexao.db.reference('Alunos/' + str(alunoId))
    alunoRef.update({'ativo': False})
    print(f"Aluno {alunoId} inativado com sucesso.")
    

