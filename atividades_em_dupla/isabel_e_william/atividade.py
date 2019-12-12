# Lista dos programadores
lista_nomes = ['Nicole', 'Mateus','Tiago']

# Lista dos conhecimentos da Nicole
nicole = ['php', 'react', 'mysql']

# Lista dos conhecimentos do Mateus
mateus = ['python', 'angular','mongodb']

# Lista dos conhecimentos do Tiago
tiago = ['java','vue', 'postgresql']

# Lista para armazenar os elementos que o usuário digitar
lista = []

# While para repetição das perguntas e verificações do squad
while len(lista_nomes) > 0:
    # For para exibir os nomes dos programadores
    for i in lista_nomes:
        print(f'\033[1;32m{i}\033[m')

    nome = input(f'\033[1;33mNome do funcionário\033[m \n')

    # Opção de banco
    print('\033[1;33mBanco de dados: [1 - MySQL] [2 - PostgreSQL] [3 - MongoDB]\033[m')
    banco = input('')

    # Opção de linguagem de programação
    print('\033[1;36mLinguagem de programação: [1 - PHP] [2 - Java] [3 - Python]\033[m')
    linguagem = input('')

    # Opção de framework front-end
    print('\033[1;36mFramework front-end: [1 - React] [2 - Angula] [3 - Vue]\033[m')
    framework = input('')

    # Adição dos elementos lidos na lista
    lista.append(linguagem.lower())
    lista.append(framework.lower())
    lista.append(banco.lower())

    if nome.lower().capitalize() in lista_nomes: 
        # Verificação do squad da Nicole
        if nome.lower() == 'nicole':
            if lista[0] in nicole and lista[1] in nicole and lista[2] in nicole:
                print(f'\033[1;34mSe encaixa no squad\033[m')
                lista_nomes.remove('Nicole')
            else:
                print('\033[1;31mNão se encaixa no squad\033[m')
        
        # Verificação do squad do Mateus
        elif nome.lower() == 'mateus':
            if lista[0] in mateus and lista[1] in mateus and lista[2] in mateus:
                print('\033[1;34mSe encaixa no squad\033[m')
                lista_nomes.remove('Mateus')
            else:
                print('\033[1;31mNão se encaixa no squad\033[m')

        # Verificação do squad do Tiago
        elif nome.lower() == 'tiago':
            if lista[0] in tiago and lista[1] in tiago and lista[2] in tiago:
                print('\033[1;34mSe encaixa no squad\033[m')
                lista_nomes.remove('Tiago')
            else:
                print('\033[1;31mNão se encaixa no squad\033[m')
    else:
        print('\033[1;31mNome inválido\033[m')

    # Limpar lista para armazenar os próximos elementos da repetição do while
    lista = []

    # Verificação dos elesmentos da lista para exibição de mensagem de squads concluídos
    if len(lista_nomes) == 0:
        print(f'\033[1;32mTodos os funcionários se encaixaram nas squads!\033[m')    
