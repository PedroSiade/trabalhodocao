from Simula import  cria_cenario, posiciona_blocos, mostra_img, encerra
from Simula import  sec_barra, tam_bloco, tam_mola
from decimal import Decimal
from math import cos, sin, e

#x1 = decimal(-1.398047538899)*cos(decimal((1.725554106593*periodos)))*e**(decimal(-0.665869315209*periodos))-decimal(0.543347494885)*e**(decimal(-0.665869315209*periodos))*sin(decimal(1.725554106593*periodos))+decimal(0.012045439804)*e**(decimal((-0.000797351457*periodos)))*sin(decimal(0.936459671869*periodos))+decimal(2.898047538899)*cos(decimal((0.936459671869*periodos)))*e**(decimal(-0.000797351457*periodos))
def gera_periodos(tf, tp):
    periodos = []
    p = 0
    while p < tf:
        periodos.append(p)
        p += tp
    return periodos

def acelera(x1, x2, k1, k2, k3, b, m1, m2, v):
    
    #print("%.5f, %.5f, %.5f, %.5f, %.5f, %.4f, %.4f, %.4f, %.4f " % \
         # (x1, x2, mv1, mv2, mv3, tm, tb, sb))
    # Calcula real deformação da primeira, segunda e terceira mola
    mv1 = Decimal(x1 - tm)
    mv2 = Decimal(x2 - x1 - (tm + tb))
    mv3 = Decimal(x2 + tb + tm - sb)
    
    # Calcula a atuação das forças nos blocos
    f1 = Decimal(mv1 * k1)
    f2 = Decimal(mv2 * k2)
    f3 = Decimal(-mv3 * k3)
    fb = Decimal(v*b)
    #print(v, '<---->')
    

    
    a1  = Decimal(-f1 + f2 + fb) / m1
    a2  = Decimal(-f2 + f3 - fb) / m2
    #print("%.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f " % \
    #      (t, mv1, mv2, mv3, f1, f2, f3, fb, v, a1, a2))
    
    return a1, a2, f1, f2, f3, fb

def nova_posição(x1, x2, a1, a2, v1, v2):
    xa1 = Decimal(x1)
    xa2 = Decimal(x2)
    
    x1 = Decimal(x1 + v1*tp + Decimal(0.5) * (a1*tp**2))
    x2 = Decimal(x2 + v2*tp + Decimal(0.5) * (a2*tp**2))
    
    return x1, x2, xa1, xa2

#
# Programa principal gera o movimento dos blocos, molas e amortecedores
#
tm = Decimal(tam_mola/100)
tb = Decimal(tam_bloco/100)
sb = Decimal(sec_barra/100)

x1 = Decimal('1.50')     # posição inicial
x2 = Decimal('3.0')     # posição final
tf = Decimal('60.0')      # tempo final da simulação
tp = Decimal('0.1')     # passo de mudança do tempo

# Velocidades iniciais 
v1  = Decimal('0')
va1 = Decimal('0')
v2  = Decimal('0')
va2 = Decimal('0')

# Caracteísticas do sistema
k1 = Decimal('10')
k2 = Decimal('15')
k3 = Decimal('12')
b  = Decimal('8')
m1 = Decimal('10')
m2 = Decimal('15')

image = cria_cenario()

periodos = gera_periodos(tf, tp)

x1 = Decimal('-1.398047538899')*cos(Decimal(('1.725554106593*periodos')))*e**(Decimal('-0.665869315209*periodos'))-Decimal('0.543347494885')*e**(Decimal('-0.665869315209*periodos'))*sin(Decimal('1.725554106593*periodos')) + \
    Decimal('0.012045439804')*e**(Decimal(('-0.000797351457*periodos')))*sin(Decimal('0.936459671869*periodos')) + \
    Decimal('2.898047538899')*cos(Decimal(('0.936459671869*periodos'))) * \
    e**(Decimal('-0.000797351457*periodos'))


for t in periodos:
    img = image.copy()
    
    # A partir da posição calcula as acelerações do bloco
    v = Decimal(v1-va1) + Decimal(v2-va2)
    a1, a2, f1, f2, f3, fb = acelera(x1, x2, k1, k2, k3, b, m1, m2, v)
    
    # Calcula nova posição dos blocos
    x1, x2, xa1, xa2 = nova_posição(x1, x2, a1, a2, v1, v2)
    v1 = (x1 - xa1) / tp
    v2 = (x2 - xa2) / tp
    #print('v1 e v2', v1, v2)

    # Gera quadro da imagem com nova posição dos blocos
    print("%.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f " % \
          (x1, x2, k1, k2, k3, b, m1, m2, v, a1, a2, f1, f2, f3, fb))
    img = posiciona_blocos(img, int(x1*100), int(x2*100), str(t) + " em " + str(tf))
    
    # Mostra a imagem em movimento
    fim = mostra_img(img)

encerra()
    


