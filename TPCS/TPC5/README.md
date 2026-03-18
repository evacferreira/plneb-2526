# TPC 5
# Doenças de A a Z

Este programa em Python procede à recolha de informações médicas do portal **Atlas da Saúde**. O script percorre o índice alfabético e extrai descrições detalhadas de cada condição listada.

## Funcionalidades

* **Iteração Alfabética**: O script gera URLs para cada letra do abecedário (`a` a `z`).

* **Extração de Dois Níveis**:
    1.  **Nível de Listagem**: Captura o nome da doença e o resumo (descrição curta).
    2.  **Nível de Detalhe**: Segue o link de cada doença para extrair o texto completo da patologia.

* **Tratamento de Dados**: Limpeza dos espaços em branco com `.strip()` e suporte a caracteres especiais via `encoding="utf8"`.

## Tecnologias e Bibliotecas

| Tecnologia | Função | Justificação Técnica |
| :--- | :--- | :--- |
| **Requests** | Cliente HTTP | Gestão de sessões e headers para pedidos. |
| **BeautifulSoup4**| HTML Parser | Permite navegar no DOM de forma robusta, mesmo com HTML complexo. |
| **Python** | Linguagem | Uso de *Dictionary Union Operators*.|
| **JSON UTF-8** | Formato de Saída | Interoperabilidade e preservação de acentuação portuguesa. |


## Estrutura do JSON 

Os dados são guardados no ficheiro `doencasTPC.json` seguindo este esquema:

```json
{
    "Nome da Doença": {
        "descrição curta": "Breve resumo da doença...",
        "descrição completa": "Texto completo com causas, sintomas e tratamentos..."
    }
}