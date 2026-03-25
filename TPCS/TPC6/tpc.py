import spacy

nlp = spacy.load("pt_core_news_lg")

f = open(r"C:\Users\Utilizador\Desktop\Mestrado Informática Médica\pln\Harry Potter e A Pedra Filosofal.txt", "r", encoding="utf-8")
texto = f.read()
f.close()

doc = nlp(texto)

amigos = {}

for sent in doc.sents:
    # Cria uma lista de nomes únicos nesta frase (PER)
    personagens_na_frase = []
    for ent in sent.ents:
        if ent.label_ == "PER" and ent.text not in personagens_na_frase:
            personagens_na_frase.append(ent.text)

    # Se houver mais de um personagem regista
    if len(personagens_na_frase) > 1:
        for p1 in personagens_na_frase:
            for p2 in personagens_na_frase:
                if p1 != p2:
                    # Garante que o dicionário para p1 existe
                    if p1 not in amigos:
                        amigos[p1] = {}
                    
                    # Aumenta a contagem de p2 na lista do p1
                    if p2 not in amigos[p1]:
                        amigos[p1][p2] = 1
                    else:
                        amigos[p1][p2] += 1

print(amigos)