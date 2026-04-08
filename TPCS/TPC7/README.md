#  MedDict - Dicionário de Conceitos Médicos

O **MedDict** é uma plataforma web moderna e minimalista desenvolvida para a consulta de terminologia clínica. Este projeto utiliza o micro-framework **Flask** para o backend e uma interface baseada em **Bootstrap 5** para garantir uma experiência de utilizador premium.

---

## Funcionamento do Sistema

A aplicação funciona através de um ciclo de pedido e resposta (Request-Response) entre o servidor Python e o navegador do utilizador.

### 1. Backend (Lógica do Servidor)
* **Servidor Flask**: O ficheiro `aula7_2.py` atua como o motor principal, gerindo as rotas e a lógica de negócio.
* **Gestão de Dados**: No arranque, o servidor lê o ficheiro `dicionario_medico.json` e armazena os conceitos na memória para garantir respostas rápidas.
* **Rotas Dinâmicas**: O sistema utiliza parâmetros na URL (ex: `/conceitos/<designacao>`) para servir definições específicas de forma automática, sem precisar de criar uma página individual para cada termo.
* **API REST**: Existe um endpoint dedicado (`/api/conceitos`) que fornece os dados em formato JSON puro para consumo externo.

### 2. Frontend (Interface e Estética)
* **Arquitetura de Templates**: Utiliza **Jinja2** com um ficheiro base (`layout.html`), permitindo que todas as páginas herdem a mesma identidade visual, fontes e navegação.
* **Pesquisa Inteligente**: O ficheiro `conceitos.html` contém um script em **JavaScript** que filtra os resultados localmente no browser. Ao detetar a escrita no input, o script esconde ou mostra os cartões de conceitos comparando o texto com a classe `.concept-title`.

---

### Estrutura Global (`layout.html`)
* **Templates**: Define a estrutura mestre (HTML, Head, Body) para que as outras páginas herdem o estilo sem duplicação de código. 
* **Design**: Integra a fonte **Plus Jakarta Sans** e o **Bootstrap 5**, focando-se em sombras suaves, cantos arredondados (`border-radius: 50px`) e uma paleta de cores verde-escuro médico.

### Motor de Pesquisa Local (`conceitos.html`)
* **Filtragem Instantânea**: Utiliza **JavaScript** para monitorizar o evento de entrada (`input`) na barra de pesquisa. 
* **Lógica**: O script percorre todos os elementos com a classe `.concept-item` e compara o texto da classe `.concept-title` com o que o utilizador escreveu, escondendo os que não coincidem através de manipulação de CSS (`display: none/block`).

---

## 3. Fluxo de uma Requisição

1. **Pedido**: O utilizador clica num conceito (ex: "Anemia") na lista.
2. **Processamento**: O Flask recebe o pedido na rota dinâmica, valida a existência do termo no objeto `db` e recupera a descrição técnica.
3. **Renderização**: O servidor combina o template `conceito.html` com os dados encontrados e gera o HTML final.
4. **Resposta**: O browser recebe a página já processada e exibe-a com o estilo definido no `layout.html`.

---

## Estrutura de Ficheiros

- `aula7_2.py`: O ficheiro principal que corre a aplicação Flask.
- `dicionario_medico.json`: A base de dados que contém os conceitos e definições.
- `templates/`:
    - `layout.html`: Estrutura mestre (Head, Navbar, Fontes).
    - `home.html`: Página inicial com o ícone flutuante e boas-vindas.
    - `conceitos.html`: Lista de conceitos com a barra de pesquisa.
    - `conceito.html`: Página de visualização detalhada da definição.