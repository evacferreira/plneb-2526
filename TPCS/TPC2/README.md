# Ficha de Expressões Regulares 



### Exercício 1


* **1.1 (`re.match`):** Utilizou-se `re.match(r'hello', line)` para verificar se a palavra se encontra logo no início da string.
* **1.2 (`re.search`):** Utilizou-se `re.search(r'hello', line)` para procurar a palavra em qualquer posição da string.
* **1.3 (`re.findall`):** Utilizou-se `re.findall(r'hello', line, flags=re.IGNORECASE)` para extrair todas as ocorrências da string 'hello'. Também foi usada a flag `IGNORECASE`garantindo que as ocorrências onde houverem letras maiúsculas e minúsculas sejam admitidas.
* **1.4 (`re.sub`):** Utilizou-se `re.sub('hello', '*YEP*', line, flags=re.IGNORECASE)` para substituir todas as variações de "hello" por "*YEP*".
* **1.5 (`re.split`):** Utilizou-se `re.split(r',', line)` para dividir a string sempre que aparece uma vírgula, criando uma lista de substrings.

### Exercício 2
Utilizou-se `re.search(r'por favor[.?!]$', frase, flags=re.IGNORECASE)`. 
* `[.?!]` garante que a frase termina com ponto final, ponto de interrogação ou exclamação.
* `$` pesquisa obrigatoriamente até ao final da string.
* A flag `IGNORECASE` permite que o utilizador escreva "Por favor" ou "POR FAVOR". A função `bool()` converte o resultado final em `True` ou `False`.

### Exercício 3: Narcisismo
Utilizou-se `len(re.findall(r'\beu\b', linha, flags=re.IGNORECASE))`.
* As fronteiras de palavra `\b` garantem que apanhamos apenas a palavra "eu" isolada (evitando contar o "eu" dentro de outras palavras). 
* O `len()` conta o tamanho da lista devolvida pelo findall, indicando o número de ocorrências.

### Exercício 4: Troca de Curso
Usou-se `re.sub('LEI', novo_curso, linha)`. A palavra "LEI" é procurada na linha e substituída pela string contida na variável `novo_curso`.

### Exercício 5: Soma String
Utilizou-se `re.split(',', linha)` para criar uma lista com os números (em formato de texto). Depois, iterou-se sobre essa lista com um ciclo `for`, convertendo cada elemento para inteiro (`int(n)`) e somando-o a um somador `s`.

### Exercício 6: Pronomes
Utilizou-se `re.findall(r'\b(eu|tu|ele|ela|nós|vós|eles|elas)\b', texto, flags=re.IGNORECASE)`.
* O grupo com o operador `|` permite procurar por qualquer um dos pronomes.
* O `\b` nas extremidades garante que extraímos apenas as palavras completas.

### Exercício 7: Variável Válida
Utilizou-se `re.match(r'^[A-Za-z]\w*$', nome)`.
* `^` e `$` obrigam a que a validação cubra a string do início ao fim.
* `[A-Za-z]` garante que o primeiro caractere é obrigatoriamente uma letra.
* `\w*` garante que os restantes caracteres (zero ou mais) são caracteres de palavra válidos (letras, números ou underscores).

### Exercício 8: Inteiros
Utilizou-se `re.findall(r'-?\d+', text)`.
* O `-?` torna o sinal de menos opcional (apanhando os números negativos).
* `\d+` procura por uma sequência de um ou mais números.

### Exercício 9: Underscores
Utilizou-se `re.sub('\s+', '_', texto)`. 
* O quantificador `+` aplicado ao `\s` (espaço em branco) garante que um ou mais espaços consecutivos sejam tratados como um único bloco e substituídos por apenas um `_`.

### Exercício 10: Códigos Postais
Iterou-se a lista original e aplicou-se `re.findall(r'(\d+)-(\d+)', cp)[0]`. 
* Os dois pares de parênteses `()` criam dois grupos de captura (antes e depois do hífen). 
* Como tem múltiplos grupos de captura, o `findall` devolve uma lista de tuplos `[('4700', '000')]`. 
* O índice `[0]` foi usado para extrair o tuplo diretamente dessa lista e adicioná-lo à lista de resultados final `r`.
