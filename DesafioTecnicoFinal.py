print('-------------------------------------')
print('| Bem vindo ao Catálogo dos Herois! |')
print('-------------------------------------')

#acha a posiçao do heroi na lista
def ondeEsta (nom,agd):
    inicio=0
    #verifica o tamanho da lista
    final =len(agd)-1
    #varrendo toda a lista
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom==agd[meio][0]:
            return meio+1 # retorna a posição em que encontrou o que buscava +1
        elif nom<agd[meio][0]:
            final=meio-1
        else: # nom>agd[meio][0]
            inicio=meio+1
            
    return -(inicio+1) # retornando (negativada), a posicao onde inserir +1
    '''retornando negativo pois na função incluir vai ter a verificação se o heroi ja existe na lista
    não poderá haver herois com o meu nome'''

#inclui um novo heroi na lista
def incluir (agd):
    digitouDireito = False
    while not digitouDireito:
        nome = input('\nNome: ')
        #verificação feita pelo nome do herói
        posicao=ondeEsta(nome,agd)
        #caso a posicao seja positiva -> heroi ja existe na lista
        if posicao>0:
            print ('Herói já existente - Favor redigitar...')
        else:
            digitouDireito=True
    #depois de verificado que o heroi nao esta catologado, insere as outras informações      
    descricao = input('Descrição: ')
    superPoder1 = input('Super poder:')
    superPoder2 = input('Outro super poder:')
    #positivando e posicionando a variável 'posicao'
    posicao=-posicao
    posicao-=1
    #lista com as informações do heroi
    heroi=[nome, descricao, superPoder1, superPoder2]
    #lista agd vai incluir a posição e a lista heroi
    agd.insert(posicao, heroi)
    print('\nHeroi cadastrado com sucesso!')

#busca por herois pelo nome
def procurar (agd):
    digitouDireito=False
    i=0
    posicao-=1
    while not digitouDireito:
        nomeBusca = input('Digite o nome do herói que deseja buscar:')
        #chama a função e busca 
        posicao = ondeEsta(nomeBusca, agd)
        #caso a posição for diferente de zero - heroi existe na lista
        if posicao != 0:
            #printa os dados do heroi
            print('\nNome:',agd[i][0])
            print('Descrição:',agd[posicao][1])
            print('Super poder:',agd[posicao][2])
            print('Outro super poder:',agd[posicao][3])
            digitouDireito = True
            i += 1
        else:
            print('\nHerói nao encontrado no catálogo!\n')
            break

def filtrarPoder(agd):
    i=0
    #nova lista para adicionar os herois filtrados com o poder inserido pelo usuário
    herois = []
    nomeBusca = input('Digite o super poder do herói que deseja filtrar: ')

    posicao = ondeEsta(nomeBusca, agd)
    #positivando a variável 'posição' e posicionando ela como no index 0
    posicao = (-posicao)-2
    #varrendo a lista
    for heroi in agd[i][2]:
        #verificando o 'superPoder1'
        if agd[posicao][2] == nomeBusca:
            #caso ache, inclui na lista herois
            herois.append(agd[posicao])
        #verificando o 'superPoder2'
        elif agd[posicao][3] == nomeBusca:
            #caso ache, inclui na lista herois
            herois.append(agd[posicao])
        i += 1
    # Verificando se a lista de herois ficou vazia, se sim, entao nao foram encontrados herois
    if herois == []:
        print('\nNão existe heróis com esse super poder no catálogo!\n')

    #printando a lista herois - todos os herois que possuem o poder filtrado
    for heroi in agd:
            print('\nNome:', heroi[0])
            print('Descrição:', heroi[1])
            print('Super poder:', heroi[2])
            print('Outro super poder:', heroi[3])
 

def atualizar (agd):
    digitouDireito=False
    i=0
    while not digitouDireito:
        #seleciona o heroi que deseja alterar atarvés do nome 
        nomeAtualiza = input('Digite o nome do herói que atualizar:')
        #localizando posição
        posicao = ondeEsta(nomeAtualiza, agd)
        #caso a posição seja diferente de 0 - heroi existe na lista
        if posicao != 0:
            #printa um menu de opções para o usuário decidir qual informação será modificada
            print('')
            print('1.Descrição:')
            print('2.Super poder:')
            print('3.Outro super poder:')
            opcaoAtualiza = int(input('Digite o numero da opcao que deseja alterar:'))

            if opcaoAtualiza > 0 and opcaoAtualiza < 4:
                valorAtualizado = str(input('Insira o novo valor:'))
                agd[posicao-1][opcaoAtualiza] = valorAtualizado
                digitouDireito = True
                print('\nAtualizado com sucesso!')
            else:
                print('As opções devem ser 1, 2 ou 3!')
        else:
            print('\nHerói nao encontrado no catálogo!\n')
            break

#lista todos os herois cadastrados
def listar (agd):
    #verificando se a lista esta vazia
    if agd==[]:
        print ('\nO catálogo não possui heróis cadastrados!')
    else:
        #verrendo a lista e printando todods os herois
        for heroi in agd:
            print('\nNome:', heroi[0])
            print('Descrição:', heroi[1])
            print('Super poder:', heroi[2])
            print('Outro super poder:', heroi[3])
    
def excluir (agd):    
    print()
    digitouDireito=False
    while not digitouDireito:
        nome=input('Nome: ')
        #verifica se o heroi existe na lista
        posicao=ondeEsta(nome,agd)
        #se posição for menor que zero - heroi nao esta na lista
        if posicao < 0:
            print ('Herói inexistente - Favor redigitar...')
        else:
            digitouDireito=True
    #reajustando a variável 'posição'
    posicao-=1
    #printa o restante das informações do heroi que será deletado
    print('Descrição:',agd[posicao][1])
    print('Super poder:',agd[posicao][2])
    print('Outro super poder:',agd[posicao][3])
    #deletando o heroi escolhido da lista
    del agd[posicao]
    print('\nRemoção realizada com sucesso!')

#criando a lista agenda
agenda=[]

#zerando a variável opcao
opcao = 0

#enquanto for diferente de zero o menu de opções aparecerá novamente
while opcao != 7:
    print('\nMenu de opções:')
    print('''\n    1.Incluir heroi
    2.Procurar heroi
    3.Atualizar informações do heroi                                                                  
    4.Listar todos os herois
    5.Excluir heroi do catálogo
    6.Filtrar heróis pelo super poder
    7.Sair do Programa''')

    opcao = int(input("\nDigite sua opção: "))
    #verificando qual opção foi escolhida e chamando a determinada função
    if opcao==1:
        incluir(agenda) 
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
    elif opcao==6:
        filtrarPoder(agenda)

print('Obrigada por usar esse programa!')