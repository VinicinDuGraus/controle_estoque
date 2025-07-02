estoque = []

def adicionar_equipamento():
    nome = input("Digite o nome do equipamento:")
    quantidade = int(input("Digite a quantidade:"))
    local = input("Digite o local:")
    item = {"nome": nome, "quantidade": quantidade, "local": local}
    estoque.append(item)
    print("Equipamento adicionado com sucesso!") 

def listar_equipamentos():
    for item in estoque:
        print(f"Nome: {item['nome']}, Quantidade: {item['quantidade']}, Local: {item['local']}")
        pass
      
def atualizar_quantidade():
    nome = input("Digite o nome do equipamento:")
    quantidade = int(input("Digite a nova quantidade:"))
    for item in estoque:
        if item["nome"] == nome:
            item["quantidade"] = quantidade
            print("Quantidade atualizada com sucesso!")
            return
    print("Equipamento não encontrado.")
          
def remover_equipamento():
    nome = input("Digite o nome do equipamento:")
    for item in estoque:
        if item["nome"] == nome:
            estoque.remove(item)
            print("Equipamento removido com sucesso!")
            return
while True:
        print("\n====== MENU ======")
        print("1. Adicionar equipamento")
        print("2. Listar esquipamentos")
        print("3. Atualizar a quantidade")
        print("4. Remover equipamento")
        print("5. Sair")

        try:
            opcao = int(input("Digite o número da opção desejada: "))
        except ValueError:
            print("Opção inválida. Tente novamente.")
            continue

        if opcao == 1:
            adicionar_equipamento()
        elif opcao == 2:
            listar_equipamentos()
        elif opcao == 3:
            atualizar_quantidade()
        elif opcao == 4:
            remover_equipamento()
        elif opcao == 5:
            print("Saindo do programa...")
            break