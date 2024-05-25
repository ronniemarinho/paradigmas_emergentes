avaliacoesUsuario = {'Ana':
                         {'Freddy x Jason': 2.5,
                          'O Ultimato Bourne': 3.5,
                          'Star Trek': 3.0,
                          'Exterminador do Futuro': 3.5,
                          'Norbit': 2.5,
                          'Star Wars': 3.0},

                     'Marcos':
                         {'Freddy x Jason': 3.0,
                          'O Ultimato Bourne': 3.5,
                          'Star Trek': 1.5,
                          'Exterminador do Futuro': 5.0,
                          'Star Wars': 3.0,
                          'Norbit': 3.5},

                     'Pedro':
                         {'Freddy x Jason': 2.5,
                          'O Ultimato Bourne': 3.0,
                          'Exterminador do Futuro': 3.5,
                          'Star Wars': 4.0},

                     'Claudia':
                         {'O Ultimato Bourne': 3.5,
                          'Star Trek': 3.0,
                          'Star Wars': 4.5,
                          'Exterminador do Futuro': 4.0,
                          'Norbit': 2.5},

                     'Adriano':
                         {'Freddy x Jason': 3.0,
                          'O Ultimato Bourne': 4.0,
                          'Star Trek': 2.0,
                          'Exterminador do Futuro': 3.0,
                          'Star Wars': 3.0,
                          'Norbit': 2.0},

                     'Janaina':
                         {'Freddy x Jason': 3.0,
                          'O Ultimato Bourne': 4.0,
                          'Star Wars': 3.0,
                          'Exterminador do Futuro': 5.0,
                          'Norbit': 3.5},

                     'Leonardo':
                         {'O Ultimato Bourne': 4.5,
                          'Norbit': 1.0,
                          'Exterminador do Futuro': 4.0}
                     }

avaliacoesFilme = {'Freddy x Jason':
                       {'Ana': 2.5,
                        'Marcos:': 3.0,
                        'Pedro': 2.5,
                        'Adriano': 3.0,
                        'Janaina': 3.0},

                   'O Ultimato Bourne':
                       {'Ana': 3.5,
                        'Marcos': 3.5,
                        'Pedro': 3.0,
                        'Claudia': 3.5,
                        'Adriano': 4.0,
                        'Janaina': 4.0,
                        'Leonardo': 4.5},

                   'Star Trek':
                       {'Ana': 3.0,
                        'Marcos:': 1.5,
                        'Claudia': 3.0,
                        'Adriano': 2.0},

                   'Exterminador do Futuro':
                       {'Ana': 3.5,
                        'Marcos:': 5.0,
                        'Pedro': 3.5,
                        'Claudia': 4.0,
                        'Adriano': 3.0,
                        'Janaina': 5.0,
                        'Leonardo': 4.0},

                   'Norbit':
                       {'Ana': 2.5,
                        'Marcos:': 3.0,
                        'Claudia': 2.5,
                        'Adriano': 2.0,
                        'Janaina': 3.5,
                        'Leonardo': 1.0},

                   'Star Wars':
                       {'Ana': 3.0,
                        'Marcos:': 3.5,
                        'Pedro': 4.0,
                        'Claudia': 4.5,
                        'Adriano': 3.0,
                        'Janaina': 3.0}
                   }

from math import sqrt

print(avaliacoesUsuario['Ana']['Norbit'])

def euclidiana(base, usuario1, usuario2):
    si = {}
    #item- todos os filmes que assistiu
    for item in base[usuario1]:
        if item in base[usuario2]:
            si[item] = 1 # se os filmes tbem estão na lista do usuario 2,se sim recebe 1
        #se não estiver filme retornar 0
        if(len(si))==0:
            return 0
    #fazendo a subtração entre as notas e elevando ao quadrado
    soma = sum([pow(base[usuario1][item] - base[usuario2][item], 2)
                for item in base[usuario1]
                    if item in base[usuario2]])
    return 1 / (1 + sqrt(soma)) #retorna assim por conta da porcentagem

print(euclidiana(avaliacoesUsuario,"Leonardo","Janaina"))
print(euclidiana(avaliacoesFilme,"Star Trek", "Star Wars"))

#retornar a similaridade de todos os usuários
def getSimilares(base, usuario):
    # passo o usuário e todos os outros usuários
    similaridade = [(euclidiana(base, usuario, outro), outro)
                    #calcular similaridade para todos os usuarios
                    for outro in base if outro !=usuario]
    similaridade.sort()# faço a ordenação
    similaridade.reverse()#faço em ordem decrescente
    return similaridade[0:3] # retorna apenas os 30 primeiros

print(getSimilares(avaliacoesUsuario,"Pedro"))

#recebe usuario como parametro calcula todas as notas q o leo daria
def getRecomendacoesUsuario(base, usuario):
    totais = {}
    somaSimilaridade = {}
    for outro in base: # percorre toda a base
        if outro == usuario:continue # for leo==leo não faço a comparação por isso continue
        similaridade = euclidiana(base, usuario,outro) # cal a distancia do leo para todos os outros
 # se não houver similaridade, passa p/ o próximo registro, não vamos fazer calculo com usuarios diferentes
        if similaridade <=0:continue
# percorrer todos os filmes dpo outro usuario
        for item in base[outro]:
            if item not in base[usuario]: #se esse filme não ta contido na lista dos filmes do usuario alvo
                totais.setdefault(item,0) #inicializando avariavel total
                totais[item] += base[outro][item]*similaridade #pega a nota e multiplica pela similaridade/armazenando os totais
                somaSimilaridade.setdefault(item,0)
                somaSimilaridade[item] +=similaridade #acumula a similaridade dos usuarios=SOMAsim

        #quero retornar pro usuario a nota q o usuario daria pro filme
        rankings = [(total / somaSimilaridade[item], item) for item, total in totais.items()]
        rankings.sort() # ordenar crescente
        rankings.reverse() # ordenar descrescente
        return rankings[0:30] #retornar o ranking

print("Gerando recomendações usuario para o Pedro")
print(getRecomendacoesUsuario(avaliacoesUsuario,"Pedro"))


def carregaMovieLens(path='C:/Users/professor.SERVER/Downloads/ml-100k'):
    filmes={} #carregar todos os filmes
    for linha in open(path + '/u.item'): #abertura dos arquivos
        (id, titulo) = linha.split('|')[0:2] #Armazenar o id e o filme, uso o split pq tem o caracter |
        filmes[id]= titulo #passa a chave da variavel e recebe o titulo do filme

    base={} #carregar a base de dados dinamicamente
    for linha in open(path+'/u.data'):
        (usuario, idfilme,nota,tempo) = linha.split('\t')#\t é o tab
        base.setdefault(usuario,{})# manter usuario no dicionario
        base[usuario][filmes[idfilme]] = float(nota) # vou colocar a nota parecido com avaliações
    return base
#dentro da base esta todas as avaliações dos usuarios
base = carregaMovieLens()

print('Testando')
print(getSimilares(base,'212'))
print(getRecomendacoesUsuario(base,'212'))