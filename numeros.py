# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: bernardo.dalessandro@aluno.faculdadeimpacta.com.br


def eh_primo(n):
    num_div = 0
    num = 1
    for i in range(1, n+1):
        if n % i == 0 :
            num_div+=1
    if num_div == 2:
        return True
    else :
        return False

def lista_primos(n):
    primos_encontrados = []
    for i in range(2, n):
        if eh_primo(i):
            primos_encontrados.append(i)
    return primos_encontrados

def conta_primos(s):
    r = {}
    for i in range(len(s)):
        if eh_primo(s[i]) == True:
            r[i] = s[i]
    return r
    pass

def eh_armstrong(n):
    p = len(str(n))
    s = 0
    k = n
    while k>0:
        d = k%10
        s = s + (d**p)
        k = k//10
    if n == s:
        return True
    else :
        return False



def eh_quase_armstrong(n):
    if eh_armstrong(n) == True:
        return False
    p = len(str(n))
    s = 0
    k = n
    while k>0:
        d = k%10
        s = s + (d**p)
        k = k//10
    if n == s + 1 or n == s - 1:
        return True
    else :
        return False
    


def lista_armstrong(n):
    lis=[]
    for i in range(n):
        if eh_armstrong(i) == True:
            lis.append(i)
    return lis


def eh_perfeito(n):
    soma = 0
    cont=0
    while cont < n-1:
        cont += 1
        if n%cont == 0:
            soma += cont
    if soma == n:
        return True
    else:
        return False

def lista_perfeitos(n):
    perfeitos = []
    for i in range(n-2):
        if eh_perfeito(i+2) == True:
            perfeitos.append(i+2)
    return perfeitos
