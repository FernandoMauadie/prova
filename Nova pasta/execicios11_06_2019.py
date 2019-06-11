Y = 0
A = 0
B = 0
Ç = 0
    
a =  []
a2 = []
a3 = []
a4 = []


K = 0
K2 = 0
K3 = 0
K4 = 0
K5 = 0


b = []
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []

mediaParcial = 0
mediaParcial2 = 0
mediaParcial3 = 0
mediaParcial4 = 0
mediaParcial5 = 0
mediaParcialA = 0
mediaParcialB = 0
mediaParcialC = 0
mediaParcialD = 0





#EXE 1 ##############################################
def media(nota1, nota2):
    media = float(nota1+nota2)/2
    return media
#####################################################

# EXE 2##############################################
print("series")
arq =  open('series.csv','r',encoding='utf-8')
for k in arq.readlines():
    arqs = k.split(',')
#####################################################

#EXE 3###############################################

    ç = arqs[0]
    
    if ç == 'The Big Bang Theory':
        Z ='temporada: {} episódios: {} '.format(arqs[1],arqs[2])
        a.insert(Y,Z)
        Y += 1
        #EXE4#################################
        mediaTotalA = media(i,h) + mediaParcialA/2
        mediaParcial = media(i,h)
        ######################################
    if ç == 'Friends':
        L ='temporada: {} episódios: {} '.format(arqs[1],arqs[2])
        a2.insert(A,L)
        A += 1
        #EXE4#################################
        mediaTotalB = media(i,h) + mediaParcialB/2
        mediaParcial = media(i,h)
        ######################################
    if ç == 'Breaking Bad':
        O ='temporada: {} episódios: {} '.format(arqs[1],arqs[2])
        a3.insert(B,O)
        B += 1
        #EXE4#################################
        mediaTotalC = media(i,h) + mediaParcialC/2
        mediaParcial = media(i,h)
        ######################################
    if ç == 'Black Mirror':
        P ='temporada: {} episódios: {} '.format(arqs[1],arqs[2])
        a4.insert(Ç,P)
        Ç += 1
        #EXE4#################################
        mediaTotalD = media(i,h) + mediaParcialD/2
        mediaParcial = media(i,h)
        ######################################
print('The Big Bang Theory')
print(a)
print('')
print('Friends')
print(a2)
print('')
print('Breaking Bad')
print(a3)
print('')
print('Black Mirror')
print(a4)
print('')
######################################################

#EXE 2 ###############################################
print("series novas")
arq2 =  open('series_novas.csv','r',encoding='utf-8')
for k in arq2.readlines():
    arqs2 = k.split(',')
######################################################
    
#EXE3#################################################
    J = arqs2[0]
    
    if J == 'Fuller House':
        Z ='temporada: {} episódios: {} '.format(arqs2[1],arqs2[2])
        b.insert(K,Z)
        K += 1
        i = int(arqs[5])
        h = int(arqs[6])
        #EXE4#################################
        mediaTotal1 = media(i,h) + mediaParcial/2
        mediaParcial = media(i,h)
        ######################################
    if J == 'Designated Survivor':
        L ='temporada: {} episódios: {} '.format(arqs2[1],arqs2[2])
        b2.insert(K2,L)
        K2 += 1
        i = int(arqs[5])
        h = int(arqs[6])
        #EXE4##################################
        mediaTotal2 = media(i,h) + mediaParcial2/2
        mediaParcial2 = media(i,h)
        #######################################
    if J == 'Suits':
        O ='temporada: {} episódios: {} '.format(arqs2[1],arqs2[2])
        b3.insert(K3,O)
        K3 += 1
        #EXE4#####################################
        mediaTotal3 = media(i,h) + mediaParcial3/2
        mediaParcial3 = media(i,h)
        ##########################################
    if J == 'Lucifer':
        P ='temporada: {} episódios: {} '.format(arqs2[1],arqs2[2])
        b4.insert(K4,P)
        K4 += 1
        #EXE4#####################################
        mediaTotal4 = media(i,h) + mediaParcial4/2
        mediaParcial4 = media(i,h)
        ###########################################
    if J == 'Narcos':
        P2 ='temporada: {} episódios: {} '.format(arqs2[1],arqs2[2])
        b5.insert(K5,P2)
        K5 += 1
        #EXE4#####################################
        mediaTotal5 = media(i,h) + mediaParcial5/2
        mediaParcial5 = media(i,h)
        ##########################################

print('Fuller House')
print(b)
print('')
print('Designated Survivor')
print(b2)
print('')
print('Suits')
print(b3)
print('')
print('Lucifer')
print(b4)
print('')
print('Narcos')
print(b5)
#######################################################

dicionario_novas = {'Narcos':mediaTotal5 , 'Lucifer':mediaTotal4}

'''
melhor = open('melhores.csv','r+',encoding = 'utf-8')

i = int(arqs[5])
h = int(arqs[6])
if media(i,h)>7.5:
    m = 'nome: {}'.format(arqs[0]
        melhor.write
'''
