# plneb-2526

# Exercício TPC 3
 
## Código

### 1. Preparação e Leitura
O código começa por abrir o ficheiro `dicionario_medico.txt` usando a codificação `utf-8` (para não desformatar os acentos) e guarda todo o texto numa única variável para ser processado.

### 2. Limpeza de  Expressões Regulares 

Como o texto vem de um PDF, tem quebras de página e frases cortadas a meio. Usa-se a função `re.sub()` para limpar o texto passo a passo:
* **Marcador `@`:** Coloca-se um `@` sempre que há dois parágrafos seguidos (`\n\n`), para marcar onde potencialmente começa um conceito novo.
* **Eliminar Quebras de Página:** Substituem-se os Form Feeds (`\f`) por parágrafos novos.
* **Juntar Frases Cortadas (Maiúsculas):** Se o `@` separou erradamente uma frase que continuava com letra maiúscula na página seguinte, o código apaga o `@` e volta a juntar o texto.
* **Juntar Frases Cortadas (Minúsculas):** Se uma quebra de página separou duas letras minúsculas, o código percebe que a frase foi cortada a meio, apaga o `@` e cola a frase novamente com um espaço.
* **Limpeza Final:** Apagam-se todos os `@` que sobraram, deixando o texto limpo e pronto a extrair.

### 3. Dicionário
Depois de limpar o texto, extrai-se a informação:
* **Dividir em Blocos:** Usa-se `re.split(r"\n\n", texto)` para cortar o texto gigante em vários "blocos" independentes.
* **Separar Nome da Descrição:** Em cada bloco, usa-se `maxsplit=1` para cortar o texto apenas no *primeiro* "Enter" (`\n`). A primeira linha fica a ser o nome da doença/conceito, e o resto do texto fica a ser a definição.
* **Guardar:** Limpam-se as quebras de linha a meio da definição e guarda-se tudo num Dicionário de Python estruturado: `{ "Conceito": "Descrição" }`.

### 4. Exportação para HTML
No fim, o código percorre o Dicionário de Python e coloca cada termo e descrição dentro de tags HTML . O resultado é guardado num novo ficheiro `dicionario_medico_TPC.html` pronto a abrir no navegador.