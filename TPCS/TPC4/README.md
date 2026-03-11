# Bomboémia


Este projeto consiste numa *Landing Page* (página única) responsiva e interativa, desenvolvida para apresentar a identidade, a história, a agenda e os contactos do grupo, bem como para atrair novos membros e promover o nosso festival "Do Bira ao Samba".

## Funcionalidades e Secções do Site

O site está estruturado numa única página com navegação fluida (*smooth scroll*) entre as seguintes secções:

* **Menu de Navegação Fixo:** Permite acesso rápido a qualquer parte do site.

* **Hero Section:** Cabeçalho de grande impacto visual com o logótipo e o título principal.

* **Sobre Nós:** Uma breve história sobre a fundação do grupo e a ligação à ARCUM.

* **Próximas Atuações (Agenda):** Uma grelha interativa de cartões com as datas e locais dos próximos espetáculos.

* **Do Bira ao Samba:** Destaque para o grande festival de percussão organizado pelo grupo.

* **20 Anos Bomboémia (Vlogs):** Secção dedicada aos bastidores com um reprodutor de vídeo incorporado (`iframe`) do YouTube.

* **A Nossa Galeria:** Um *slider* de imagens interativo construído com JavaScript, permitindo visualizar fotografias do grupo através de setas de navegação.

* **Junta-te a Nós:** Secção de recrutamento com informações detalhadas sobre os ensaios.

* **Contactos:** Botão de ação direta para o email oficial e links para as redes sociais.

## Tecnologias Utilizadas

* **HTML5:** Estrutura semântica do documento (os blocos e "tijolos" do site).

* **CSS3:** Utilização de variáveis CSS, Flexbox, CSS Grid e animações (`@keyframes`) (a pintura e a arrumação dos elementos).

* **JavaScript:** Utilizado para manipulação do DOM e interatividade do carrossel (o que dá ação e "eletricidade" ao site).

* **Google Fonts:** Tipografia `Montserrat`.

## Dicionário de Código (Variáveis, Classes e Funções)

Para facilitar a manutenção e leitura do código, o site foi construído de forma modular. Abaixo está o mapeamento detalhado de tudo o que foi programado:

### 1. Variáveis CSS Globais (`:root`)

O esquema de cores foi guardado em variáveis globais no início do CSS, funcionando como a paleta oficial do site. Se for necessário mudar uma cor no futuro, basta alterar aqui e aplica-se ao site inteiro.

💡 **Explicação Prática:** Em vez de escrever o código da cor laranja dezenas de vezes pelo site todo, usamos a variável `--laranja`. É como ter um "balde de tinta" com um rótulo. Se o grupo mudar a sua cor amanhã, basta mudar a cor dentro desse único balde no `:root` e o site atualiza-se por completo!

| Variável | Cor (Hexadecimal) | Onde é utilizada | 
| ----- | ----- | ----- | 
| `--laranja` | `#FF5A00` | Títulos `strong`, sublinhados, botões principais, realces (`:hover`). | 
| `--laranja-claro` | `#f7dcbf` | Fundos de secções alternadas e bordas suaves. | 
| `--branco` | `#ffffff` | Fundo de cartões, texto sobre fundos escuros. | 
| `--fundo-geral` | `#FAFAFA` | Cor de fundo principal do `body`. | 
| `--texto-escuro` | `#1e2430` | Títulos (`h1`, `h2`), rodapé e elementos de maior peso visual. | 
| `--cinza-texto` | `#4A5568` | Cor base para leitura longa (`p`). | 

### 2. Classes de Layout e Estrutura (CSS)

Para evitar a repetição de código, foram criadas classes utilitárias baseadas em Flexbox e Grid:

* `.bg-seccao`: Aplica o fundo `--laranja-claro` para criar alternância visual entre as secções brancas e coloridas.

* `.flex-container` e `.flex-coluna` (Flexbox): O bloco principal que organiza o conteúdo. Utiliza `display: flex; flex-wrap: wrap;` para colocar imagem e texto lado-a-lado no PC, e empilhá-los no telemóvel.

  * **Explicação:** O Flexbox funciona como um "elástico inteligente". Num ecrã de PC há espaço, então ele põe as coisas lado a lado. Quando vemos no telemóvel, o ecrã encolhe e o Flexbox reage, empilhando o texto em cima da imagem de forma automática para nada ficar esmagado.

* `.agenda-grid` (CSS Grid): Utiliza CSS Grid (`grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))`) para criar uma grelha inteligente de cartões de eventos que se adapta sozinha ao tamanho do ecrã.

  * **Explicação:** O CSS Grid fornece um poderoso sistema bidimensional. A função auto-fit aliada ao minmax faz com que o navegador calcule intrinsecamente quantas colunas de pelo menos 300px cabem no ecrã. Quando o espaço transversal é insuficiente, os elementos transitam de forma fluida para a linha inferior, maximizando a área de ecrã disponível.


### 3. Funções e Variáveis de JavaScript (O Motor da Galeria)

O slider fotográfico é suportado por uma lógica de controlo de estado desenvolvida em Vanilla JavaScript, alojada no final do documento para garantir o carregamento prévio do DOM.

* **Explicação:**  A variável global slideIndex atua como um controlador de estado (State Management). Ao interagir com as setas de navegação, disparamos eventos que forçam o script a atualizar a interface do utilizador: o algoritmo itera por todos os elementos da galeria alterando a propriedade CSS display para none (ocultação total) e, logo de seguida, injeta display: block estritamente na imagem correspondente ao índice ativo. Isto previne quebras de layout e assegura uma renderização exata.

**Variável Global:**

* `let slideIndex = 1;`: Variável que guarda o número do slide/foto que está atualmente ativo. Começa no 1 quando o site abre.

**Funções:**

* `plusSlides(n)`: Função ativada pelo HTML através do evento `onclick` nas setas (`<` e `>`).

  * *O que faz:* Recebe um parâmetro `n` (que será `-1` para voltar atrás, ou `1` para avançar) e soma esse valor ao `slideIndex` atual, chamando logo de seguida a função principal.

* `showSlides(n)`: É o "cérebro" da galeria.

  * **Passo 1 (Recolher imagens):** Utiliza `document.getElementsByClassName("mySlides")` para criar uma lista (`array`) com todas as fotografias HTML da galeria.

  * **Passo 2 (Loops de Limite):** Se o utilizador tentar avançar da última foto (ex: foto 5), a condição `if (n > slides.length)` reseta o `slideIndex` para `1` (cria um ciclo contínuo). Se tentar recuar estando na primeira foto, a condição `if (n < 1)` envia-o para a última foto.

  * **Passo 3 (Esconder tudo):** Utiliza um ciclo `for` para percorrer todas as imagens e aplicar `slides[i].style.display = "none"`, garantindo que o ecrã fica "limpo".

  * **Passo 4 (Mostrar a atual):** Seleciona apenas a imagem correspondente ao `slideIndex` atual (subtraindo `-1` porque em programação as listas começam a contar do 0) e aplica `style.display = "block"` para a revelar.

