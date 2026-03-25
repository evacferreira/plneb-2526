# TPC: Harry Friends 

Este projeto foi desenvolvido para a unidade curricular de **Processamento de Linguagem Natural (PLN)**. O objetivo é extrair uma rede de relações entre personagens a partir do livro *Harry Potter e A Pedra Filosofal* utilizando a biblioteca **spaCy**.

## Objetivo
O objetivo deste exercício é recorrer ao spaCy para identificar todas as personagens da história e mapear as suas interações, assumindo que existe uma relação de amizade sempre que dois nomes são mencionados na mesma frase.

---

O código funciona da seguinte forma:

### 1. Carregamento do Modelo NER
Ao usar o spacy.load("pt_core_news_lg"), ativamos um modelo de linguagem robusto que identifica entidades com base no contexto. Isto permite ao sistema ir além da simples leitura de texto e classificar corretamente "Harry" como uma pessoa (PER), diferenciando-o de cenários como "Hogwarts" (LOC).

### 2. Pipeline de Processamento

Quando executamos o comando `doc = nlp(texto)`, o spaCy processa o texto bruto através de uma "linha de montagem" (pipeline) que realiza três operações automáticas num único passo. Primeiro, ocorre a **tokenização**, onde o modelo divide o texto contínuo em unidades básicas chamadas "tokens" (palavras individuais, sinais de pontuação e símbolos). A partir desses tokens, realiza-se a **sentencização**, fase em que o spaCy reconhece a estrutura gramatical e divide o livro inteiro em frases lógicas, percebendo onde começa e acaba cada ideia. Por fim, ocorre a **extração de entidades (NER)**, onde o modelo analisa o contexto de cada palavra para detetar e classificar informações importantes, identificando automaticamente os nomes próprios no texto e atribuindo-lhes uma etiqueta (como a marcação `PER` para personagens).

### 3. Filtragem e Unicidade por Frase
O código percorre cada frase (`doc.sents`). Para cada uma:
* Procura entidades com a etiqueta `PER`.
* Guarda o nome numa lista temporária, mas apenas se ele ainda não estiver lá (`not in personagens_na_frase`). 

### 4. Lógica de Coocorrência e Contagem
Se a frase contiver pelo menos duas personagens diferentes:
* O código realiza um duplo ciclo `for` (p1 e p2) para cruzar todos os nomes encontrados.
* Se o par for novo, cria uma entrada no dicionário `amigos`.
* Se o par já existir, incrementa o valor em `+1`.
* **Resultado:** O valor final representa o número de frases distintas onde as duas personagens apareceram juntas.

---

## Formato de Saída
O dicionário final segue esta estrutura:

```json
{
  "Harry": {
    "Ron": 152,
    "Hermione": 148,
    "Hagrid": 63
  },
  "Ron": {
    "Harry": 152,
    "Hermione": 95
  }
}
```
