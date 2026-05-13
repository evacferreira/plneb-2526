# TPC 11

Este TPC consiste no desenvolvimento de um sistema de recuperação de informação simplificado, focado na aplicação prática dos conceitos de Term Frequency (TF), Inverse Document Frequency (IDF) e Similaridade de Cosseno. O objetivo central é processar uma coleção de documentos e, perante uma consulta específica, determinar qual o documento que apresenta a maior relevância semântica através de métodos estatísticos.

## Processamento de Linguagem Natural
O fluxo de trabalho inicia-se com a função de pré-processamento, que utiliza a biblioteca spaCy para transformar texto bruto em dados estruturados. Em vez de analisar frases completas, o sistema isola tokens individuais, converte-os para minúsculas e remove elementos que não contribuem para o significado, como pontuação e stop words (palavras gramaticais como "is" ou "the"). Este passo é fundamental para garantir que o cálculo matemático se foque apenas nas palavras que carregam conteúdo real, como "sun", "sky" ou "bright".

## A Lógica do TF-IDF
A atribuição de pesos às palavras é feita através de duas funções complementares. A função `tf` calcula a importância local, dividindo o número de ocorrências de um termo pelo total de palavras do documento. Já a função `idf` avalia a importância global, calculando o logaritmo da razão entre o número total de documentos e a frequência com que cada termo aparece no corpus. Esta combinação permite que palavras raras e distintivas tenham um peso superior a palavras comuns que aparecem em quase todos os documentos. No final, a função `tf_idf` consolida estes valores numa matriz vetorial que representa matematicamente a coleção.


## Vetorização da Query e Ranking de Similaridade
Para responder à consulta "The bright sun", o sistema não faz uma procura literal. Em vez disso, transforma a query num vetor numérico utilizando o mesmo vocabulário e os valores de IDF derivados do corpus original. Este alinhamento é crucial para que a comparação seja válida. A fase final do processo utiliza a função `cosine_similarity`, que calcula o cosseno do ângulo entre o vetor da query e cada um dos vetores dos documentos. 

O resultado deste cálculo permite estabelecer um ranking de relevância. O documento que apresentar o valor de cosseno mais elevado (mais próximo de 1) é identificado como o mais relevante. No caso específico deste exercício, o sistema analisa como a presença de termos como "bright" e "sun" se distribui pelo corpus para eleger automaticamente o documento que melhor satisfaz a intenção do utilizador.
