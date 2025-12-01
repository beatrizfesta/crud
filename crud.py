# NOME: BEATRIZ FESTA
# CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
# CRUD- ATIVIDADE SOMATIVA DE RACIOCINIO COMPUTACIONAL



import json  # Importa a biblioteca JSON

# Estrutura de arquivos JSON para cada módulo
# Cada módulo salva seus registros em arquivos separados, para uma melhor organização e persistência
arquivos = {
    "estudantes": "estudantes.json",
    "professores": "professores.json",
    "disciplinas": "disciplinas.json",
    "turmas": "turmas.json",
    "matriculas": "matriculas.json"
}

# Estrutura de campos para cada módulo
# Define os campos para cada tipo de registro no sistema
campos = {
    "estudantes": ["codigo", "nome", "cpf"],
    "professores": ["codigo", "nome", "cpf"],
    "disciplinas": ["codigo", "nome"],
    "turmas": ["codigo", "professor_codigo", "disciplina_codigo"],
    "matriculas": ["turma_codigo", "estudante_codigo"]
}

# Função principal do programa, para melhorar a organização das funções
def main():

    # Inicia o programa, criando arquivos vazios se necessário e exibindo o menu principal.

    inicializar_arquivos()  # Cria arquivos JSON vazios, caso ainad não exista
    menu_principal()

# Inicia os arquivos JSON
def inicializar_arquivos():

    # Cria arquivos JSON vazios para cada módulo, caso ainda não existam.

    for arquivo in arquivos.values():
        try:
            open(arquivo, "x").write("[]")  # Cria o arquivo vazio como uma lista JSON
        except FileExistsError:
            pass  # Se o arquivo já existe, não faz nada

# Função para salvar lista em um arquivo JSON
def salvar_no_arquivo(modulo, dados):
    """
    Salva os dados do módulo no arquivo JSON correspondente.

    :param modulo: Nome do módulo (ex: "estudantes", "professores").
    :param dados: Lista de registros a ser salva no arquivo.
    """
    with open(arquivos[modulo], "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# Função para recuperar a lista de um arquivo JSON
def recuperar_do_arquivo(modulo):
    """
    Recupera os dados do arquivo JSON correspondente ao módulo.
    Retorna uma lista vazia caso o arquivo não exista ou esteja corrompido.

    :param modulo: Nome do módulo (ex: "estudantes", "professores").
    :return: Lista de registros recuperada do arquivo JSON.
    """
    try:
        with open(arquivos[modulo], "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Exibe o Menu Principal
def menu_principal():
    while True:
        print("----MENU PRINCIPAL----")
        print("1. Estudantes")
        print("2. Professores")
        print("3. Disciplinas")
        print("4. Turmas")
        print("5. Matrículas")
        print("6. Sair")

        #Escolhe uma opção do Menu Principal
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            menu_operacoes("estudantes")
        elif opcao == "2":
            menu_operacoes("professores")
        elif opcao == "3":
            menu_operacoes("disciplinas")
        elif opcao == "4":
            menu_operacoes("turmas")
        elif opcao == "5":
            menu_operacoes("matriculas")
        elif opcao == "6":
            print("Saindo do sistema...")
            break # Sai do loop
        else:
            print("Opção inválida, tente novamente") # Caso o usuário digite uma opção não válida

# Exibe o Menu de Operações
def menu_operacoes(modulo):
    while True:
        print(f"----MENU DE OPERAÇÕES ({modulo.upper()})----")# Muda de acordo com o modulo escolhido
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao Menu Principal")

        # Escolhe uma opção do Menu Operações
        operacao = input("Escolha uma operação: ")
        if operacao == "1":
            incluir(modulo)
        elif operacao == "2":
            listar(modulo)
        elif operacao == "3":
            atualizar(modulo)
        elif operacao == "4":
            excluir(modulo)
        elif operacao == "5":
            print("Voltando ao Menu Principal...")
            break #Sai do loop
        else:
            print("Opção inválida, tente novamente") # Caso o usuário digite uma opção não válida

# Função para ajustar nome do módulo (singular/plural)
def ajustar_nome_modulo(modulo):
    """
    Ajusta o nome do módulo para exibição em mensagens, tratando singular e plural.
    """
    return "Professor" if modulo == "professores" else modulo[:-1].capitalize() # Função incluída pois a palavra 'professor' tem mais letras que as outras

# Função Genérica para Incluir registros de qualquer módulo
def incluir(modulo):
    dados = recuperar_do_arquivo(modulo)
    novo_registro = {}
    try:
        # Coleta os dados do novo registro com base nos campos do módulo
        for campo in campos[modulo]:
            valor = input(f"Digite o {campo}: ").strip()
            novo_registro[campo] = int(valor) if "codigo" in campo else valor

        # Validação específica para matrículas
        if modulo == "matriculas":
            if any(d["turma_codigo"] == novo_registro["turma_codigo"] and d["estudante_codigo"] == novo_registro["estudante_codigo"] for d in dados):
                print("Erro: Matrícula já existente para esta turma e este estudante!")
                return
        else:
            if any(d["codigo"] == novo_registro["codigo"] for d in dados):
                print("Erro: Código já existente!")
                return

        dados.append(novo_registro)
        salvar_no_arquivo(modulo, dados)
        nome_modulo = ajustar_nome_modulo(modulo)
        print(f"{nome_modulo} incluído(a) com sucesso!")
    except ValueError:
        print("Erro: Entrada inválida.")

# Função Genérica para Listar registros de qualquer módulo
def listar(modulo):
    dados = recuperar_do_arquivo(modulo)
    print(f"---LISTA DE {modulo.upper()}---")
    if dados:
        for item in dados:
            print(", ".join(f"{k.capitalize()}: {v}" for k, v in item.items()))
    else:
        print(f"Não há {modulo} cadastrados.")

# Função Genérica para Atualizar registros de qualquer módulo
def atualizar(modulo):
    dados = recuperar_do_arquivo(modulo)
    try:
        if modulo == "matriculas":
            turma_codigo = int(input("Digite o código da turma: "))
            estudante_codigo = int(input("Digite o código do estudante: "))
            for item in dados:
                if item["turma_codigo"] == turma_codigo and item["estudante_codigo"] == estudante_codigo:
                    print(f"Matrícula encontrada: {item}")
                    for campo in campos[modulo]:
                        novo_valor = input(f"Digite o novo {campo} (ou pressione Enter para manter '{item[campo]}'): ").strip()
                        if novo_valor:
                            item[campo] = int(novo_valor) if "codigo" in campo else novo_valor
                    salvar_no_arquivo(modulo, dados)
                    print("Matrícula atualizada com sucesso!")
                    return
            print("Matrícula não encontrada.")
        else:
            codigo = int(input(f"Digite o código do(a) {ajustar_nome_modulo(modulo).lower()} que deseja atualizar: "))
            for item in dados:
                if item["codigo"] == codigo:
                    print(f"{ajustar_nome_modulo(modulo)} encontrado(a): {item}")
                    for campo in campos[modulo]:
                        novo_valor = input(f"Digite o novo {campo} (ou pressione Enter para manter '{item[campo]}'): ").strip()
                        if novo_valor:
                            item[campo] = int(novo_valor) if "codigo" in campo else novo_valor
                    salvar_no_arquivo(modulo, dados)
                    print(f"{ajustar_nome_modulo(modulo)} atualizado(a) com sucesso!")
                    return
            print(f"{ajustar_nome_modulo(modulo)} com o código informado não encontrado.")
    except ValueError:
        print("Erro: Código deve ser um número inteiro válido.")

# Função Genérica para Excluir registros de qualquer módulo
def excluir(modulo):
    dados = recuperar_do_arquivo(modulo)
    try:
        if modulo == "matriculas":
            turma_codigo = int(input("Digite o código da turma: "))
            estudante_codigo = int(input("Digite o código do estudante: "))
            for item in dados:
                if item["turma_codigo"] == turma_codigo and item["estudante_codigo"] == estudante_codigo:
                    dados.remove(item)
                    salvar_no_arquivo(modulo, dados)
                    print("Matrícula excluída com sucesso!")
                    return
            print("Matrícula não encontrada.")
        else:
            codigo = int(input(f"Digite o código do(a) {ajustar_nome_modulo(modulo).lower()} que deseja excluir: "))
            for item in dados:
                if item["codigo"] == codigo:
                    dados.remove(item)
                    salvar_no_arquivo(modulo, dados)
                    print(f"{ajustar_nome_modulo(modulo)} excluído(a) com sucesso!")
                    return
            print(f"{ajustar_nome_modulo(modulo)} com o código informado não encontrado.")
    except ValueError:
        print("Erro: Código deve ser um número inteiro válido.")

# Inicia o programa
if __name__ == "__main__":
    main()
