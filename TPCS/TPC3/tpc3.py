import re

# 1. LER O FICHEIRO TXT
f = open('dicionario_medico.txt', 'r', encoding='utf8')
texto = f.read()
f.close() 

# Coloca um marcador '@' sempre que encontrar dois parágrafos. 
# marca onde potencialmente começam os conceitos.
texto = re.sub(r'\n\n', '\n\n@', texto)

# Troca o FF por um parágrafo novo.
texto = re.sub(r'\f', '\n', texto)


# Se houver um marcador '@' seguido de uma letra maiúscula, o código tenta unir as linhas, 
# presumindo que a quebra separou o conceito da sua definição.
# O \1 volta a colocar a letra maiúscula que foi capturada pelos parênteses.
texto = re.sub(r'\n\n@\n([A-ZÀ-Ú])', r'\n\1', texto) 


# Se o texto for interrompido entre duas letras minúsculas removemos a quebra e o '@', juntando a frase com um espaço ('\1 \2').
texto = re.sub(r'([a-zà-ú])\s*\n\n@\n\s*([a-zà-ú])', r'\1 \2', texto)

# Tira os '@' que sobraram.
texto = re.sub(r'@', '', texto)


conceitos = re.split(r"\n\n", texto)
print(len(conceitos))

def limpa_descricao(descricao):
    descricao = re.sub(r"\n", " ", descricao)
    descricao = descricao.strip() 
    return descricao

conceitos_dict ={}

for c in conceitos[1:]:
    elems = re.split(r"\n", c, maxsplit=1)
    
    if len(elems) > 1:
        designacao = elems[0].strip() 
        descricao = elems[1]          
        conceitos_dict[designacao] = limpa_descricao(descricao)
    else:
        continue

print(len(conceitos_dict))


def gera_html(filename, conceitos_dict):
    html = """
    <html>
        <head>
        <title> Dicionário Médico </title>
        <meta charset="UTF-8">
        </head>
        <body>
        <h1>Dicionário Médico</h1>
        <hr>
    """

 
    for c in conceitos_dict:
        html = html + f"""
        <div>
            <p> <b> {c} </b> </p>
            <p> {conceitos_dict[c]} </p>
        </div>
        <hr>
        """
    
    html = html + """</body>
    </html>
    """   

    f_out = open(filename, "w", encoding="utf8")
    f_out.write(html)
    f_out.close()

gera_html("dicionario_medico_TPC.html", conceitos_dict)