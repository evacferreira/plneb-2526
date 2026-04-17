# TPC8 Template Pesquisar
# Arquitetura e Design

O componente de pesquisa do **MedDict** foi concebido para transformar a consulta de dados técnicos numa experiência visualmente rica e tecnicamente precisa, equilibrando a robustez do processamento de linguagem natural com uma interface minimalista. 

No núcleo da interface, o **Search Header** estabelece a identidade visual através de uma tipografia *extra-bold* e um sistema de `letter-spacing` negativo, enquanto o formulário principal reside numa `search-container` elevada por sombras suaves, isolando a zona de interação do utilizador.

O campo de entrada de texto utiliza uma `input-group-custom` que reage ao foco com transições cromáticas para o tom `#e6f2f0`, proporcionando um feedback tátil-visual imediato.

### Lógica de Interação e Filtros
A funcionalidade de busca permite ao utilizador refinar a extração de dados através de dois interruptores lógicos  que comunicam diretamente com o backend via parâmetros `GET`:
* **Controlo de Sensibilidade**: A opção **Case Sensitive** determina se a comparação de strings deve diferenciar maiúsculas de minúsculas durante o processamento no servidor.
* **Delimitação de Termos**: O filtro **Palavra Exata (Word Boundary)** garante que apenas termos isolados sejam validados, eliminando ruído e resultados parciais indesejados em consultas curtas.

### Resultados e Destaque Visual
Ao processar os resultados, o template abandona a estrutura tabular convencional passando a uma **Grelha de Cards Dinâmicos** (`row g-4`):
* **Micro-interações**: Cada `result-card` utiliza propriedades de transformação CSS para se elevar (`translateY`) ao passar o rato, conferindo interatividade e profundidade à navegação.
* **Highlighter Inteligente**: A aplicação utiliza o filtro `| safe` do Jinja2 para injetar as marcações de negrito (`<b>`) geradas no Python, permitindo que as correspondências da pesquisa surjam destacadas com um fundo verde translúcido.
* **Consistência de Layout**: O uso da classe `line-clamp-3` assegura que descrições longas sejam truncadas visualmente.
