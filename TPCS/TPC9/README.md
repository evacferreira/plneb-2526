# Word2Vec — Harry Potter

Treino de modelos Word2Vec sobre os dois primeiros livros da saga Harry Potter em português, para explorar relações semânticas.

## Análise de Livros

- `Harry Potter e A Pedra Filosofal.txt`
- `Harry_Potter_Camara_Secreta-br.txt`

## Pré-processamento

O texto é processado com spaCy (pt_core_news_sm): tokenização por frase, remoção de pontuação, espaços e stop words, e conversão para minúsculas. O resultado é uma lista de frases tokenizadas, que serve de input direto ao Word2Vec.

## Modelos


Foram treinadas 4 configurações para comparar o efeito do algoritmo, da dimensão dos vetores e do número de épocas:


| Notebook | `sg` | `vector_size` | `epochs` |
|---|---|---|---|
| `harry.ipynb` | 0 (CBOW) | 100 | 40 |
| `harry2.ipynb` | 1 (Skip-gram) | 100 | 40 |
| `harry3.ipynb` | 0 (CBOW) | 100 | 20 |
| `harry4.ipynb` | 0 (CBOW) | 50 | 100 |

Todos com `window=5` e `min_count=2`.

## Experiências

```python
# Palavras mais próximas de 'casa' no espaço vetorial
model.wv.most_similar('casa')
 
# Similaridade entre harry e outros personagens
model.wv.similarity("harry", "hermione")
model.wv.similarity("harry", "malfoy")
model.wv.similarity("harry", "rony")
model.wv.similarity("harry", "hagrid")
model.wv.similarity("harry", "gryffindor")
 
# Qual a palavra que menos encaixa no grupo?
model.wv.doesnt_match(["harry", "rony", "hermione", "malfoy"])
model.wv.doesnt_match(["gryffindor", "slytherin", "hufflepuff", "snape"])
model.wv.doesnt_match(["taça", "vassoura", "quadribol", "hermione"])
 
# Aritmética de vetores (analogias)
model.wv.most_similar(positive=['harry', 'sonserina'], negative=['draco'])
model.wv.most_similar(positive=['sonserina', 'harry'], negative=['grifinória'])
model.wv.most_similar(positive=['mulher', 'bruxo'], negative=['homem'])
```
 
 
### Similaridade entre personagens
 
Similaridade cosseno entre harry e outros personagens/locais, nos 4 modelos:
 
| Par | harry.ipynb | harry2.ipynb | harry3.ipynb | harry4.ipynb |
|---|---|---|---|---|
| harry / hermione | 0.354 | 0.161 | 0.662 | 0.258 |
| harry / malfoy | 0.209 | 0.197 | 0.358 | 0.379 |
| harry / rony | 0.504 | 0.304 | 0.576 | 0.621 |
| harry / hagrid | 0.398 | 0.096 | 0.625 | 0.292 |
| harry / gryffindor | -0.258 | -0.154 | -0.131 | 0.109 |
 
Os modelos CBOW com mais épocas (`harry3.ipynb`, `harry4.ipynb`) tendem a produzir similaridades mais altas entre personagens com relações próximas (harry/rony, harry/hermione). O Skip-gram (`harry2.ipynb`) gerou valores consistentemente mais baixos, o que pode refletir a maior esparsidade dos seus vetores com este tamanho de corpus. A similaridade negativa com `gryffindor` em alguns modelos é inesperada e sugere que o modelo associa o nome da casa a contextos distintos dos do personagem.
 
### Pares temáticos
 
| Par | harry.ipynb | harry3.ipynb | harry4.ipynb |
|---|---|---|---|
| harry / rony | 0.30 | 0.58 | 0.62 |
| harry / voldemort | -0.05 | 0.09 | 0.22 |
| vassoura / quadribol | 0.21 | 0.17 | 0.33 |
| varinha / bruxo | -0.02 | -0.08 | 0.15 |
 
A relação harry/voldemort é consistentemente fraca ou negativa nos modelos com menos épocas, o que faz sentido — os dois personagens surgem em contextos opostos. Com mais épocas (`harry4.ipynb`), o modelo começa a capturar a co-ocorrência frequente dos dois nomes. Os pares vassoura/quadribol e varinha/bruxo têm similaridades baixas, possivelmente porque os termos ocorrem em contextos temáticos distintos dentro das frases.
 
### Identificação do intruso (`doesnt_match`)
 
| Lista | harry.ipynb | harry2.ipynb | harry3.ipynb | harry4.ipynb |
|---|---|---|---|---|
| harry, rony, hermione, malfoy | hermione | hermione | malfoy | malfoy |
| gryffindor, slytherin, hufflepuff, snape | snape | snape | snape | snape |
| taça, vassoura, quadribol, hermione | hermione | hermione | hermione | hermione |
 
O intruso `snape` no grupo das casas de Hogwarts é identificado corretamente e de forma consistente por todos os modelos. Nos outros casos, os resultados variam ligeiramente entre modelos mas são semanticamente plausíveis — hermione é identificada como intrusa no primeiro grupo (quando deveria ser o malfoy), e é a única personagem num grupo de objetos/atividades.

## Visualização

Os vetores são exportados e convertidos para o [TensorFlow Projector](http://projector.tensorflow.org/):

```bash
python -m gensim.scripts.word2vec2tensor -i model_harry.txt -o model_harry
```
