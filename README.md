# plneb-2526

# Exercícios de Python

## 1. Inverter uma String

Para inverter uma string, utiliza-se a funcionalidade de slicing. A função percorre a string do último índice até ao primeiro, criando uma cópia invertida desta.

---

## 2. Contar caracteres 'a' e 'A'

A função começa por definir um contador a zero. De seguida, percorre a string caractere a caractere utilizando um ciclo for. Em cada iteração, verifica se o caractere atual é igual a 'a' ou 'A'. Se a condição for verdadeira, o contador é incrementado em mais 1. No final, o valor total é retornado.

---

## 3. Contar Vogais

Define-se uma string de referência com todas as vogais (maiúsculas e minúsculas: "aeiouAEIOU") e cria-se um contador. A função percorre a string alvo usando um ciclo for e, para cada letra, verifica se esta existe dentro da string de referência. Se existir, considera-se uma vogal e incrementa-se o contador.

---

## 4. Converter para Minúsculas

Utiliza-se o método `.lower()`. Este método percorre a string e substitui qualquer caractere maiúsculo pelo seu equivalente minúsculo, mantendo os restantes caracteres inalterados.

---

## 5. Converter para Maiúsculas

Semelhante ao exercício anterior, utilizamos o método `.upper()`. Este converte todas as letras minúsculas em maiúsculas.

---

## 6. Verificar Capicua 

O algoritmo cria uma versão invertida da string original (usando a lógica do exercício 1). De seguida, compara a string original com a invertida. Se forem exatamente iguais, a função retorna `True` (Verdadeiro); caso contrário, retorna `False`.

---

## 7. Strings Balanceadas

Assume-se inicialmente que as strings estão balanceadas. Percorre-se cada letra da string `s1` e verifica-se se esse caractere existe em `s2`. Se for encontrada um único caractere que não esteja presente em `s2`, sabe-se imediatamente que não estão balanceadas. Nesse momento, o estado muda para `False` e o ciclo é interrompido.

---

## 8. Contar Ocorrências de uma Substring

O programa percorre a string `s2` índice por índice. Em cada posição, recorta um pedaço da string com o mesmo tamanho de `s1`. Se esse pedaço for igual a `s1`, o contador de ocorrências aumenta. O ciclo termina quando já não houver caracteres suficientes em `s2` para formar a palavra `s1`.

---

## 9. Verificar Anagrama

Um anagrama consiste em duas palavras que usam exatamente as mesmas letras, mas em ordem diferente. Para sabermos se duas strings são anagramas criamos duas listas com os caracteres de cada uma das strings. De seguida, ordenam-se ambas as listas com o método sorted. Por fim, comparam-se as listas ordenadas. Se forem iguais, as palavras são anagramas.

---