# Word2Vec — Harry Potter

Treino de modelos Word2Vec sobre os dois primeiros livros da saga Harry Potter em português, para explorar relações semânticas no corpus.

## Corpus

- `Harry Potter e A Pedra Filosofal.txt`
- `Harry_Potter_Camara_Secreta-br.txt`

## Pré-processamento

Tokenização com spaCy (`pt_core_news_sm`), remoção de pontuação, espaços e stop words, conversão para minúsculas.

## Modelos

| Notebook | `sg` | `vector_size` | `epochs` |
|---|---|---|---|
| `harry.ipynb` | 0 (CBOW) | 100 | 40 |
| `harry2.ipynb` | 1 (Skip-gram) | 100 | 40 |
| `harry3.ipynb` | 0 (CBOW) | 100 | 20 |
| `harry4.ipynb` | 0 (CBOW) | 50 | 100 |

Todos com `window=5` e `min_count=2`.

## Experiências

```python
# Palavras mais próximas
model.wv.most_similar('casa')

# Similaridade entre personagens
model.wv.similarity("harry", "hermione")
model.wv.similarity("harry", "malfoy")

# Identificação do intruso
model.wv.doesnt_match(["harry", "rony", "hermione", "malfoy"])
model.wv.doesnt_match(["gryffindor", "slytherin", "hufflepuff", "snape"])
model.wv.doesnt_match(["taça", "vassoura", "quadribol", "hermione"])

# Aritmética de vetores
model.wv.most_similar(positive=['harry', 'sonserina'], negative=['draco'])
model.wv.most_similar(positive=['mulher', 'bruxo'], negative=['homem'])
```

## Visualização

Os vetores são exportados e convertidos para o [TensorFlow Projector](http://projector.tensorflow.org/):

```bash
python -m gensim.scripts.word2vec2tensor -i model_harry.txt -o model_harry
```
