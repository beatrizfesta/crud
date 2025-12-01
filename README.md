# CRUD em Python

> **Autora:** Beatriz Festa  
> **Curso:** Análise e Desenvolvimento de Sistemas  
> **Disciplina:** Raciocínio Computacional 

Este projeto é um sistema de **CRUD (Create, Read, Update, Delete)** desenvolvido em **Python**, com foco em um contexto acadêmico.  
O objetivo é gerenciar informações de **estudantes, professores, disciplinas, turmas e matrículas**, utilizando **arquivos JSON** para armazenamento dos dados.

Tudo é feito via **terminal**, por meio de menus interativos.

---

## 🧩 Funcionalidades

O sistema é dividido em módulos, cada um com seu próprio conjunto de operações:

### ✅ Módulos disponíveis

- **Estudantes**
- **Professores**
- **Disciplinas**
- **Turmas**
- **Matrículas**

Para cada módulo (exceto matrículas), é possível:

- Incluir registros
- Listar registros
- Atualizar registros
- Excluir registros

No módulo de **Matrículas**, é possível:

- Registrar matrícula de estudantes em turmas
- Atualizar os dados de uma matrícula existente
- Excluir matrícula

---

## 🗂 Estrutura de dados

Os dados são salvos em arquivos JSON, um para cada módulo:

- `estudantes.json`
- `professores.json`
- `disciplinas.json`
- `turmas.json`
- `matriculas.json`

Cada módulo possui campos definidos no código:

- **Estudantes:** `codigo`, `nome`, `cpf`
- **Professores:** `codigo`, `nome`, `cpf`
- **Disciplinas:** `codigo`, `nome`
- **Turmas:** `codigo`, `professor_codigo`, `disciplina_codigo`
- **Matrículas:** `turma_codigo`, `estudante_codigo`

---

## 🧱 Organização do código

O arquivo principal é:

- `crud.py`

Principais partes do código:

- `arquivos` → dicionário que mapeia módulos para seus arquivos JSON  
- `campos` → dicionário que define os campos de cada módulo  
- `inicializar_arquivos()` → cria os arquivos JSON vazios, se ainda não existirem  
- `salvar_no_arquivo(modulo, dados)` → salva a lista de registros no JSON correspondente  
- `recuperar_do_arquivo(modulo)` → lê os registros do arquivo JSON  
- `menu_principal()` → exibe o menu principal e redireciona para o módulo escolhido  
- `menu_operacoes(modulo)` → exibe o menu de operações (Incluir, Listar, Atualizar, Excluir) para o módulo selecionado  
- `incluir(modulo)` → insere um novo registro (com validações, como evitar códigos duplicados e matrículas repetidas)  
- `listar(modulo)` → exibe todos os registros do módulo  
- `atualizar(modulo)` → permite alterar os dados de um registro existente  
- `excluir(modulo)` → remove um registro do módulo  
- `ajustar_nome_modulo(modulo)` → apenas formata o nome do módulo para exibição nas mensagens  

A função `main()` inicializa o sistema e chama o menu principal, sendo executada quando o arquivo é rodado diretamente:

```python
if __name__ == "__main__":
    main()
