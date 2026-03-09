# --- VERSÃO BOMBOÉMIA: DADOS OFICIAIS UMINHO + PROTEÇÃO DE ERROS WINDOWS ---

# O "r" antes das aspas (Raw String) impede o erro do 'unicodeescape' no Windows
html_header = r"""
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bomboémia | O Estoiro</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;500;800;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --laranja: #FF5A00;
            --preto-fundo: #0a0a0a;
            --preto-seccao: #141414;
            --branco: #ffffff;
            --cinza-texto: #aaaaaa;
        }

        body {
            background-color: var(--preto-fundo);
            color: var(--branco);
            font-family: 'Montserrat', sans-serif;
            margin: 0;
            scroll-behavior: smooth;
        }

        strong {
            color: var(--laranja);
            font-weight: 800;
        }

        /* Menu */
        nav {
            background: rgba(10, 10, 10, 0.85);
            backdrop-filter: blur(10px);
            padding: 20px 5%;
            display: flex;
            justify-content: center;
            gap: 40px;
            position: fixed;
            width: 90%;
            top: 0;
            z-index: 1000;
            border-bottom: 2px solid rgba(255, 90, 0, 0.3);
        }

        nav a {
            color: var(--branco);
            text-decoration: none;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-size: 0.85rem;
            transition: 0.3s;
        }

        nav a:hover { color: var(--laranja); text-shadow: 0 0 10px rgba(255, 90, 0, 0.5); }

        /* HERO - Capa Principal */
        .hero {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            text-align: center;
            /* Se quiseres uma foto tua, muda o link abaixo para url('fundo.jpg') */
            background: linear-gradient(rgba(10, 10, 10, 0.8), var(--preto-fundo) 95%), url('https://images.unsplash.com/photo-1514525253161-7a46d19cd819?q=80&w=1920');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            padding: 20px;
        }

        .logo-oficial {
            width: 220px;
            height: 220px;
            object-fit: cover;
            border-radius: 50%;
            border: 3px solid var(--laranja);
            box-shadow: 0 0 60px rgba(255, 90, 0, 0.5);
            margin-bottom: 30px;
            margin-top: 60px;
            transition: transform 0.4s ease, box-shadow 0.4s ease;
        }

        .logo-oficial:hover {
            transform: scale(1.05);
            box-shadow: 0 0 90px rgba(255, 90, 0, 0.8);
        }

        .hero h1 {
            font-size: clamp(3rem, 8vw, 6rem);
            font-weight: 900;
            margin: 0;
            color: var(--branco);
            letter-spacing: 2px;
            text-transform: uppercase;
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
        }

        .hero p {
            font-size: 1.2rem;
            color: var(--cinza-texto);
            max-width: 600px;
            margin-top: 15px;
            font-weight: 300;
            letter-spacing: 1px;
        }

        section { padding: 100px 10%; }
        .bg-escuro { background-color: var(--preto-seccao); }

        h2 {
            font-size: 2.5rem;
            font-weight: 900;
            color: var(--branco);
            text-transform: uppercase;
            margin-top: 0;
            margin-bottom: 50px;
            display: inline-block;
            border-bottom: 4px solid var(--laranja);
            padding-bottom: 10px;
        }

        /* SECÇÃO FESTIVAL */
        .festival-container {
            display: flex;
            flex-wrap: wrap;
            gap: 40px;
            align-items: center;
        }

        .festival-img {
            flex: 1;
            min-width: 300px;
            max-width: 600px;
            border-radius: 12px;
            border: 2px solid #222;
            box-shadow: 0 10px 40px rgba(255, 90, 0, 0.2);
            transition: transform 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease;
        }

        .festival-img:hover {
            transform: scale(1.02);
            border-color: var(--laranja);
            box-shadow: 0 15px 50px rgba(255, 90, 0, 0.4);
        }

        .festival-texto {
            flex: 1;
            min-width: 300px;
            font-size: 1.1rem;
            line-height: 1.8;
            color: #ccc;
        }

        /* GALERIA */
        .galeria-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        .foto-galeria {
            width: 100%;
            height: 250px;
            object-fit: cover;
            border-radius: 12px;
            border: 2px solid #222;
            filter: grayscale(40%) brightness(0.8);
            transition: transform 0.4s ease, filter 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease;
        }

        .foto-galeria:hover {
            transform: scale(1.03);
            filter: grayscale(0%) brightness(1.1);
            border-color: var(--laranja);
            box-shadow: 0 15px 40px rgba(255, 90, 0, 0.3);
            z-index: 2;
            position: relative;
        }

        /* AGENDA */
        .agenda-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .card-evento {
            background-color: var(--preto-fundo);
            border: 1px solid #222;
            border-bottom: 3px solid rgba(255, 90, 0, 0.2);
            border-radius: 16px;
            padding: 35px 30px;
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), 
                        box-shadow 0.4s ease, border-color 0.4s ease;
            position: relative;
            z-index: 1;
        }

        .card-evento:hover {
            transform: translateY(-10px) scale(1.03);
            border-color: var(--laranja);
            box-shadow: 0 15px 40px rgba(255, 90, 0, 0.25), inset 0 0 20px rgba(255, 90, 0, 0.05);
            z-index: 2;
        }

        .data-evento { 
            font-size: 2.2rem; 
            font-weight: 900; 
            color: var(--laranja); 
            display: inline-block; 
            margin-bottom: 8px; 
            transition: transform 0.3s ease, text-shadow 0.3s ease;
        }

        .card-evento:hover .data-evento {
            transform: scale(1.1) translateX(5px);
            text-shadow: 0 0 15px rgba(255, 90, 0, 0.5);
        }

        .nome-evento { 
            font-size: 1.3rem; 
            font-weight: 800; 
            color: var(--branco); 
            margin-bottom: 5px; 
        }

        /* CONTACTOS & REDES */
        .contactos {
            text-align: center;
            padding: 100px 10%;
            background: radial-gradient(circle at bottom, rgba(255, 90, 0, 0.1) 0%, var(--preto-seccao) 80%);
        }

        .info-bloco {
            background-color: var(--preto-fundo);
            border: 1px solid #222;
            border-radius: 12px;
            padding: 20px;
            margin-top: 30px;
            display: inline-block;
            text-align: left;
            max-width: 400px;
        }

        .redes-sociais {
            margin-top: 30px;
            display: flex;
            justify-content: center;
            gap: 20px;
        }

        .btn-rede {
            display: inline-block;
            background-color: transparent;
            color: var(--branco);
            border: 2px solid var(--laranja);
            padding: 10px 25px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            transition: 0.3s;
            text-transform: uppercase;
        }

        .btn-rede:hover {
            background-color: var(--laranja);
            color: var(--branco);
            box-shadow: 0 0 20px rgba(255, 90, 0, 0.4);
        }

        .btn-email {
            display: inline-block;
            background-color: var(--laranja);
            color: var(--branco);
            font-size: 1.2rem;
            font-weight: 800;
            padding: 18px 45px;
            border-radius: 50px;
            text-decoration: none;
            margin-top: 20px;
            transition: 0.3s;
            text-transform: uppercase;
            box-shadow: 0 8px 25px rgba(255, 90, 0, 0.4);
        }

        .btn-email:hover { 
            background-color: var(--branco); 
            color: var(--laranja); 
            box-shadow: 0 12px 35px rgba(255, 90, 0, 0.6); 
            transform: translateY(-3px);
        }

        footer {
            background-color: #050505;
            text-align: center;
            padding: 30px;
            color: #444;
            font-size: 0.8rem;
            letter-spacing: 1px;
            border-top: 1px solid rgba(255, 90, 0, 0.2);
        }
    </style>
</head>
"""

# O "r" aplica-se a todo o HTML
html_body = r"""
<body>
    <nav>
        <a href="#historia">História</a>
        <a href="#festival">Do Bira ao Samba</a>
        <a href="#galeria">Galeria</a>
        <a href="#agenda">Onde Atuamos</a>
        <a href="#contactos">Contactos</a>
    </nav>

    <div class="hero">
        <img src="https://graph.facebook.com/bomboemia/picture?width=800&height=800" alt="Logótipo Bomboémia" class="logo-oficial">
        <h1>BOMBOÉMIA</h1>
        <p>Grupo de Percussão da Universidade do Minho. Ritmos tradicionais e brasileiros desde 2004.</p>
    </div>

    <section id="historia" class="bg-escuro">
        <h2>A Nossa Essência</h2>
        <p style="font-size: 1.1rem; max-width: 800px; line-height: 1.8; color: #ccc;">
            A Bomboémia surgiu em <strong>2004</strong>, de uma reestruturação do Grupo de Cabeçudos, Gigantones e Zés Pereiras da Universidade do Minho. 
            O nosso projeto resulta numa enorme variedade de sons e estilos de percussão, partindo dos bons <strong>ritmos minhotos e populares portugueses</strong>, e viajando até ao samba e às batucadas do Brasil.
        </p>
    </section>

    <!-- SECÇÃO DO FESTIVAL COM A IMAGEM -->
    <section id="festival">
        <h2>Do Bira ao Samba</h2>
        <div class="festival-container">
            <!-- Apenas o nome do ficheiro aqui. Certifica-te que a imagem está na mesma pasta do tpc4.py -->
            <img src="festival.jpg" alt="Festival Do Bira ao Samba" class="festival-img">
            <div class="festival-texto">
                <p>O <strong>Do Bira ao Samba</strong> é o nosso grande palco aberto à cidade. Durante <strong>2 dias</strong> (entre o fim de julho e o início de agosto), a festa tem entrada livre e gratuita.</p>
                <p>É o momento onde a academia minhota e a comunidade se unem num estoiro de caixas, bombos e timbalões, mostrando porque a Bomboémia e os grupos convidados são o verdadeiro espírito da percussão.</p>
            </div>
        </div>
    </section>

    <!-- SECÇÃO DA GALERIA -->
    <section id="galeria" class="bg-escuro">
        <h2>A Nossa Galeria</h2>
        <div class="galeria-grid">
            <img src="https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?q=80&w=800" alt="Atuação Bomboémia" class="foto-galeria">
            <img src="https://images.unsplash.com/photo-1459749411175-04bf5292ceea?q=80&w=800" alt="Atuação Bomboémia" class="foto-galeria">
            <img src="https://images.unsplash.com/photo-1598387181032-a3103a2db5b3?q=80&w=800" alt="Atuação Bomboémia" class="foto-galeria">
            <img src="https://images.unsplash.com/photo-1464375117522-1314d6c4692c?q=80&w=800" alt="Atuação Bomboémia" class="foto-galeria">
        </div>
    </section>

    <section id="agenda">
        <h2>Presenças Habituais</h2>
        <div class="agenda-grid">
            <div class="card-evento">
                <span class="data-evento">OUT</span>
                <div class="nome-evento">Receção ao Caloiro</div>
                <div style="color: #888; font-weight: 500;">Abertura da Latada em Guimarães</div>
            </div>
            <div class="card-evento">
                <span class="data-evento">MAI</span>
                <div class="nome-evento">Enterro da Gata</div>
                <div style="color: #888; font-weight: 500;">Abertura do Cortejo e Recinto, Braga</div>
            </div>
            <div class="card-evento">
                <span class="data-evento">DEZ</span>
                <div class="nome-evento">Récita do 1º de Dezembro</div>
                <div style="color: #888; font-weight: 500;">Theatro Circo, Braga</div>
            </div>
        </div>
    </section>

    <div class="contactos bg-escuro" id="contactos">
        <h2>Fala Connosco</h2>
        
        <div class="info-bloco">
            <p><strong>Ensaios:</strong> Segundas e Quintas às 21:00</p>
            <p><strong>Local:</strong> ARCUM (por baixo do BA de Braga)</p>
            <p>Rua da Fundação Calouste Gulbenkian, Braga</p>
        </div>

        <br>
        <a href="mailto:bomboemia@arcum.pt" class="btn-email">bomboemia@arcum.pt</a>
        
        <div class="redes-sociais">
            <a href="https://www.facebook.com/bomboemia" target="_blank" class="btn-rede">Facebook</a>
            <a href="https://instagram.com/bomboemia" target="_blank" class="btn-rede">Instagram</a>
            <a href="http://www.arcum.pt" target="_blank" class="btn-rede">Site ARCUM</a>
        </div>
    </div>
"""

# O "r" aplica-se ao footer
html_footer = r"""
    <footer>
        &copy; 2026 Bomboémia - Grupo de Percussão da Universidade do Minho.
    </footer>
</body>
</html>
"""

# Gravar o Ficheiro
try:
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_header + html_body + html_footer)
    print("Sucesso! Código livre de erros. Podes abrir o index.html!")
except Exception as e:
    print(f"Ocorreu um erro ao gravar: {e}")