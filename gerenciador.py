#Aplicativo para gerenciar uma agenda de contatos, do curso de Formação Python da Rocketseat

#função adicionar um contato(nome, telefone, email, favorito)

def adicionar_contato(contatos, nome, telefone, email):
    contato = {"contato": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome} foi adicionada com sucesso!")
    return

def listar_contato(contatos):
    print("\nLista de Contatos:")
    for indice, contato  in enumerate(contatos, start = 1):
        favorito = "⭐" if contato["favorito"] else " "
        nome = contato["contato"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. Favorito[{favorito}] Nome: {nome} | Telefone: {telefone} | Email: {email}")
    return

def atualizar_contato(contatos, indice_contato, nome_novo, telefone_novo, email_novo):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["contato"] = nome_novo
        contatos[indice_contato_ajustado]["telefone"] = telefone_novo
        contatos[indice_contato_ajustado]["email"] = email_novo
        print(f"Contato {indice_contato} atualizado para {nome_novo} {telefone_novo} {email_novo}")
    else:
        print("índice de contato inválido")
    return 

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado] ["favorito"] = True
    print(f"Contato {indice_contato} favoritado")
    return  

def listar_contato_favorito(contatos):
    print("\nLista de Contatos:")
    for indice, contato  in enumerate(contatos, start = 1):
        if contato["favorito"]:
         print(f"{indice}.  Nome: {contato['contato']} | Telefone: {contato["telefone"]} | Email: {contato["email"]}")
    return

def deletar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        del contatos[indice_contato_ajustado]
        print(f"Contato {indice_contato} deletado com sucesso")
    return

contatos = []

while True:
    print ("\nMenu do Gerenciador de Agendas:")
    print("1. Adicionar Contato")
    print("2. Ver Contatos")
    print("3. Atualizar Contato")
    print("4. Favoritar Contato")
    print("5. Ver Contatos Favoritos")
    print("6. Apagar Contato")
    print("7. Sair")

    opcao = input("Digite uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(contatos, nome, telefone, email)

    elif opcao == "2":
        listar_contato(contatos)

    elif opcao == "3":
        listar_contato(contatos)
        indice_contato = input("Digite o numero do contato que deseja atualizar: ")
        novo_nome = input ("Digite o novo nome do contato: ")
        novo_telefone = input ("Digite o novo número de telefone: ")
        novo_email = input ("Digite o novo email: ")
        atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email) 

    elif opcao == "4":
        listar_contato(contatos)
        indice_contato = input("Digite o numero do contato que deseja favoritar: ")
        favoritar_contato(contatos, indice_contato)

    elif opcao == "5":
        listar_contato_favorito(contatos)

    elif opcao == "6":
        listar_contato(contatos) 
        indice_contato = input("Digite o índice do contato que deseja deletar: ")
        deletar_contato(contatos, indice_contato) 
    
    elif opcao == "7":
        break