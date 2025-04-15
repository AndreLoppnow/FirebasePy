import conexao
import alunos

while True:
    print("1. Adicionar Aluno")
    print("2. Listar Alunos")
    print("3. Inativar Aluno")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        nome = input("Nome do aluno: ")
        idade = int(input("Idade do aluno: "))
        curso = input("Curso do aluno: ")
        alunos.adicionar_aluno(nome, idade, curso)
        
    elif opcao == '2':
        alunos.listar_alunos()
        
    elif opcao == '3':
        id = input("Id do aluno a inativar: ")
        alunos.inativar_aluno(id)
        
    elif opcao == '4':
        break
    
    else:
        print("Opção inválida. Tente novamente.")