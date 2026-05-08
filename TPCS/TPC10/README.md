# TPC 10

Segue a explicação do código presente nas 4 fases pela qual o programa em questão passa:

## 1. Configuração de Labels
Esta fase prepara a interface entre as previsões numéricas do modelo e a interpretação humana.
* **Extração da Lista de Tags**: Criou-se a variável `label_list` a partir das propriedades do dataset para identificar as 11 categorias disponíveis (ex: 'B-Pessoa', 'I-Local', 'O').
* **Mapeamento de IDs**: Definiram-se os dicionários `id2label` (converte o ID da classe para o nome textual) e `label2id` (converte o nome para o ID numérico).

## 2. Evaluate 
Implementação da lógica para medir a precisão do modelo durante o processo de aprendizagem.
* **Métrica Seqeval**: Foi carregada a métrica seqeval, que é o padrão para tarefas de NER, pois avalia se a entidade foi capturada por inteiro (início e fim) e não apenas palavra por palavra.
* **Função `compute_metrics`**: Esta função realiza o pós-processamento necessário:
    * **Seleção de Classe**: Usa `np.argmax` para extrair a previsão mais provável.
    * **Filtragem de Ruído**: Remove os tokens com valor `-100` (padding ou sub-tokens), garantindo que a pontuação não seja inflada artificialmente.
    * **Cálculo Estatístico**: Gera métricas de Precisão, Recall, F1-Score e Acurácia.

## 3. Train 
Fase de ajuste dos pesos do modelo BERT para a tarefa específica de extração de entidades.
* **Inicialização**: Carregou-se o modelo `neuralmind/bert-base-portuguese-cased` com uma cabeça de classificação adaptada para 11 etiquetas.
* **Data Collator**: Utilizou-se o `DataCollatorForTokenClassification` para gerir o preenchimento (padding) dinâmico dos lotes de treino.
* **Hiperparâmetros**: Configurou-se o treino para 2 épocas, com uma taxa de aprendizagem de $2e^{-5}$ e uma estratégia de salvamento baseada no melhor desempenho de validação.
* **Desempenho Final**: O modelo atingiu um F1-Score de **95,54%** e uma Acurácia de **98,41%** no conjunto de teste.

## 4. Inference 
Aplicação prática do modelo treinado em dados do mundo real.
* **Pipeline de NER**: Criou-se um pipeline que integra o modelo e o tokenizador, utilizando a estratégia de agregação `first` para unir sub-tokens numa única palavra/entidade.
* **Teste Prático**: Aplicou-se o modelo a uma notícia sobre o "Conselho Médico dos Açores" datada de 2026.
* **Resultados de Extração**: O modelo identificou corretamente entidades como:
    * **Pessoas**: "Carlos Ponte", "Mónica Seidi", "Paulo Simões".
    * **Datas**: "24 de abril de 2026", "2024", "2025".
    * **Locais**: "Açores", "Lisboa".
    * **Profissões**: "Presidente", "Secretária Regional da Saúde".
