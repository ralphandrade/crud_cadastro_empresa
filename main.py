# Crie um CRUD utilizando os conceitos de lista, tupla e dicionário. O usuário 
#pode cadastrar quantas pessoas quiser. Os dados a serem cadastrados são:
# - Nome
# - CPF
# - Telefone
# - E-mail
# - Profissão
# - Empresa
# Função para adicionar uma pessoa à lista de contatos
def adicionar_pessoa(contatos, nome, cpf, telefone, email, profissao, empresa):
    pessoa = {
        'Nome': nome,
        'CPF': cpf,
        'Telefone': telefone,
        'E-mail': email,
        'Profissão': profissao,
        'Empresa': empresa
    }
    contatos.append(pessoa)

# Função para listar todas as pessoas na lista de contatos
def listar_pessoas(contatos):
    for i, pessoa in enumerate(contatos, start=1):
        print(f"Pessoa {i}:")
        for chave, valor in pessoa.items():
            print(f"{chave}: {valor}")
        print()

# Função para atualizar os dados de uma pessoa na lista de contatos
def atualizar_pessoa(contatos, indice, nome, cpf, telefone, email, profissao, empresa):
    if indice >= 0 and indice < len(contatos):
        contatos[indice]['Nome'] = nome
        contatos[indice]['CPF'] = cpf
        contatos[indice]['Telefone'] = telefone
        contatos[indice]['E-mail'] = email
        contatos[indice]['Profissão'] = profissao
        contatos[indice]['Empresa'] = empresa
        print("Pessoa atualizada com sucesso!")
    else:
        print("Índice inválido!")

# Função para excluir uma pessoa da lista de contatos
def excluir_pessoa(contatos, indice):
    if indice >= 0 and indice < len(contatos):
        del contatos[indice]
        print("Pessoa excluída com sucesso!")
    else:
        print("Índice inválido!")

# Lista de contatos inicialmente vazia
contatos = []

# Menu de opções para o usuário
while True:
    print("\n1. Adicionar pessoa")
    print("2. Listar pessoas")
    print("3. Atualizar pessoa")
    print("4. Excluir pessoa")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        profissao = input("Profissão: ")
        empresa = input("Empresa: ")
        adicionar_pessoa(contatos, nome, cpf, telefone, email, profissao, empresa)
    elif opcao == '2':
        if contatos:
            print("Lista de pessoas:")
            listar_pessoas(contatos)
        else:
            print("Nenhuma pessoa cadastrada.")
    elif opcao == '3':
        if contatos:
            indice = int(input("Digite o índice da pessoa a ser atualizada: "))
            nome = input("Novo nome: ")
            cpf = input("Novo CPF: ")
            telefone = input("Novo telefone: ")
            email = input("Novo e-mail: ")
            profissao = input("Nova profissão: ")
            empresa = input("Nova empresa: ")
            atualizar_pessoa(contatos, indice - 1, nome, cpf, telefone, email, profissao, empresa)
        else:
            print("Nenhuma pessoa cadastrada.")
    elif opcao == '4':
        if contatos:
            indice = int(input("Digite o índice da pessoa a ser excluída: "))
            excluir_pessoa(contatos, indice - 1)
        else:
            print("Nenhuma pessoa cadastrada.")
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")