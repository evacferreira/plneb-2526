def reverse(s):
    return s[::-1]



def count_a(s):
    r=0
    for c in s:
        if c=='a' or c=='A':
            r=r+1
    return r



def vogais(s):
    vogais='aeiouAEIOU'
    r=0
    for c in s:
        if c in vogais:
            r=r+1
    return r



def lowercase(s):
    return s.lower()




def uppercase(s):
    return s.upper()




def iscapicua(s):
    cond=False
    inverso=s[::-1]
    if s==inverso:
        cond=True
    return cond




def balanceadas(s1, s2):
    cond=True
    for c in s1:
        if c not in s2:
            cond=False
    return cond



def ocorrencias(s1, s2):
    r=0
    for i in range( len(s2)-len(s1)+1):
        if s2[i : i + len(s1)] == s1:
            r += 1
    return r



def anagrama(s1, s2):
    lista1=[]
    lista2=[]
    cond=False
    for c in s1:
        lista1.append(c)
    for c in s2:
        lista2.append(c)
    if sorted(lista1) == sorted(lista2):
        cond=True
    return cond

