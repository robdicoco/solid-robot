# 🌙✨ Morfeu Dream Interpreter

> *"Dreams are the royal road to the unconscious." - Sigmund Freud*

Morfeu is a digital oracle that dives into the subconscious and interprets dreams through ancient symbolism, powered by modern AI. Named after Morpheus, the Greek god of dreams, this interpreter bridges the gap between your sleeping and waking worlds, offering insight into the mysterious language of your unconscious mind.

## 🔮 Overview

Morfeu employs a symphony of four specialized AI agents working in harmony to unravel the mysteries hidden in your dreams:

1. **Symbol Search Agent** 🔍: Identifies potential dream symbols and searches for their meanings across ancient and modern interpretations
2. **Symbol Analyzer** 🧩: Analyzes symbols in the context of the dream and our curated archetypal database
3. **Dream Interpreter** 📜: Creates a poetic, insightful interpretation connecting all elements into a meaningful narrative
4. **Quality & Language Verifier** 🌐: Verifies interpretation quality and ensures language matching with translations if needed

## 🌊 How It Works

Morfeu follows a carefully orchestrated flow to transform your dream into meaningful insight:

1. **Input**: You share your dream through the API or command-line interface
2. **Symbol Discovery**: The first agent identifies significant symbols in your dream and researches their meanings
3. **Contextual Analysis**: The second agent analyzes these symbols against our database and within your dream's unique context
4. **Poetic Interpretation**: The third agent weaves all elements into a cohesive interpretation with psychological insights
5. **Verification & Translation**: The fourth agent ensures quality and translates if your dream was in a non-English language
6. **Delivery**: You receive a comprehensive interpretation with practical guidance for your waking life

The entire process takes only seconds, but draws upon millennia of dream symbolism and modern psychological understanding.

## ✨ Sample Results

### English Dream Sample

```
✨ Dream Interpretation ✨
============================================================
💭 Your Dream: I was flying over a clear blue ocean, feeling free and peaceful.
============================================================

🌐 Language: English (Dream) → English (Interpretation)

💯 Quality Assessment: The interpretation is poetic, insightful, and positive. It successfully connects the symbols of flying and water to create a meaningful narrative about freedom and emotional clarity.

📜 Interpretation:
Your dream weaves a tapestry of liberation and tranquility. As you soared above the vast blue ocean, you experienced the ultimate freedom—a release from earthly constraints and a connection to your highest self. The clear waters below symbolize emotional clarity and purification, a transparent window into your subconscious mind.

🧠 Psychological Insight:
This dream reflects a harmonious state of mind where you feel unburdened by life's constraints. The freedom of flight suggests you've overcome limitations, whether self-imposed or external. The peaceful emotions indicate you've achieved a form of emotional equilibrium, while the clear blue ocean reveals a clean and undisturbed relationship with your deeper emotions.

🌱 Life Application:
This dream arrives as an affirmation of your current path toward personal freedom and emotional clarity. It encourages you to maintain your elevated perspective on life's challenges and to continue nurturing the sense of peace you've cultivated. Consider areas where you might still feel constrained and explore ways to bring this same sense of liberation to those aspects of your life.

🔆 Guidance:
Trust your capacity for rising above difficulties. Like the dreamer who flies over vast waters, you possess the ability to transcend challenges while staying connected to your emotional depths. Embrace this period of clarity and freedom, and remember this feeling of peaceful flight when you encounter turbulent waters ahead.
```

### Spanish Dream Sample (with Translation)

```
✨ Dream Interpretation ✨
============================================================
💭 Your Dream: Soñé que volaba sobre un océano azul y claro, sintiéndome libre y en paz.
============================================================

🌐 Language: Spanish (Dream) → Spanish (Interpretation)

⚠️ Note: The interpretation has been translated to match your dream's language.

💯 Quality Assessment: La interpretación es poética, perspicaz y positiva. Conecta bien los símbolos del vuelo y el agua para crear una narrativa significativa sobre libertad y claridad emocional.

📜 Interpretation:
Tu sueño teje un tapiz de liberación y tranquilidad. Mientras te elevabas sobre el vasto océano azul, experimentaste la máxima libertad—una liberación de las restricciones terrenales y una conexión con tu ser superior. Las aguas claras debajo simbolizan claridad emocional y purificación, una ventana transparente a tu mente subconsciente.

🧠 Psychological Insight:
Este sueño refleja un estado de mente armonioso donde te sientes libre de las limitaciones de la vida. La libertad del vuelo sugiere que has superado limitaciones, ya sean autoimpuestas o externas. Las emociones pacíficas indican que has logrado una forma de equilibrio emocional, mientras que el océano azul claro revela una relación limpia y sin perturbaciones con tus emociones más profundas.

🌱 Life Application:
Este sueño llega como una afirmación de tu camino actual hacia la libertad personal y la claridad emocional. Te anima a mantener tu perspectiva elevada sobre los desafíos de la vida y a continuar nutriendo la sensación de paz que has cultivado. Considera áreas donde aún puedas sentirte limitado y explora maneras de llevar esta misma sensación de liberación a esos aspectos de tu vida.

🔆 Guidance:
Confía en tu capacidad para elevarte por encima de las dificultades. Como el soñador que vuela sobre vastas aguas, posees la habilidad de trascender los desafíos mientras permaneces conectado con tus profundidades emocionales. Abraza este período de claridad y libertad, y recuerda esta sensación de vuelo pacífico cuando encuentres aguas turbulentas en el futuro.
```

### Complex Dream with Multiple Symbols

```
✨ Dream Interpretation ✨
============================================================
💭 Your Dream: I entered an old house with many rooms. In one room, I found a snake coiled around a mirror. When...
============================================================

🌐 Language: English (Dream) → English (Interpretation)

💯 Quality Assessment: Excellent interpretation that addresses all the major symbols (house, snake, mirror) and weaves them into a cohesive, insightful narrative with positive guidance.

📜 Interpretation:
Your journey through the old house with many rooms represents an exploration of different aspects of your psyche, with each room reflecting a facet of your self-knowledge. The encounter with the snake coiled around a mirror is particularly significant—the snake, a symbol of transformation and wisdom, wrapped around the mirror of self-reflection, suggests a profound moment of facing your true self.

🧠 Psychological Insight:
This dream points to a deep process of self-discovery and transformation currently underway in your life. The old house suggests you're revisiting established patterns or beliefs, perhaps parts of yourself that have been long neglected. The snake around the mirror indicates both the challenge and wisdom that comes with honest self-examination. This combination suggests you're shedding old perspectives and embracing new self-awareness.

🌱 Life Application:
You're at a meaningful juncture where self-reflection can lead to powerful change. The dream encourages you to continue exploring different aspects of yourself (the rooms) without fear, knowing that even encounters with your shadow self (symbolized by the snake) will ultimately lead to greater wisdom. Consider areas of your life where you've been avoiding honest reflection and how embracing that truth might lead to positive transformation.

🔆 Guidance:
Don't fear the rooms you haven't yet explored within yourself. Each discovery, even those that initially seem threatening, offers a gift of wisdom when approached with courage and openness. Like the snake that sheds its skin, you too are in a process of renewal. Trust this natural cycle of growth, and allow your honest reflection to guide you toward your most authentic self.
```

## 🛠️ Installation

1. Clone this repository
   ```bash
   git clone https://github.com/yourusername/morfeu.git
   cd morfeu
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

4. Create a `.env` file in the project root with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## 🚀 Usage

### Command Line Interface

Run the dream interpreter from the command line:

```bash
python test_dream_client.py --interactive
```

Or provide a dream directly:

```bash
python test_dream_client.py --dream "I was flying over a clear blue ocean, feeling free and peaceful."
```

### API Server

Start the API server:

```bash
python run_server.py
```

The API will be available at `http://localhost:8000` with the following endpoints:
- `POST /interpret` - Interpret a dream
- `GET /health` - Health check endpoint
- `GET /docs` - API documentation (provided by FastAPI)

#### Example API Request

```bash
curl -X POST "http://localhost:8000/interpret" \
     -H "Content-Type: application/json" \
     -d '{"dream": "I was flying over a clear blue ocean, feeling free and peaceful."}'
```

## 📁 Project Structure

```
morfeu/
├── __init__.py
├── base_agent.py     # Helper functions for agents
├── dream_agent.py    # Dream interpretation agents
├── main.py           # FastAPI application
└── symbols.json      # Dream symbols database
tests/
└── test_dream_interpreter.py  # Unit tests
```

## 💎 Dream Symbol Database

The system includes a curated database of common dream symbols with their archetypal meanings and contextual interpretations. The agents use this database along with online searches to provide comprehensive dream analyses.

## 🤝 Contributing

We welcome contributions from dreamers, developers, psychologists, and mythology enthusiasts alike! Here's how you can help make Morfeu even more insightful:

1. **Expand the symbols database**: Add new symbols or enhance existing ones
2. **Improve language support**: Help refine translations for non-English dreams
3. **Enhance the AI prompts**: Make the interpretations even more poetic and insightful
4. **Add new features**: Explore dream journaling, patterns over time, etc.

To contribute:
1. Fork this repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

# 🌙✨ Morfeu - Interpretador de Sonhos

> *"Os sonhos são a estrada real para o inconsciente." - Sigmund Freud*

Morfeu é um oráculo digital que mergulha no subconsciente e interpreta sonhos através de símbolos antigos, potencializado pela IA moderna. Nomeado após Morfeu, o deus grego dos sonhos, este interpretador estabelece uma ponte entre seus mundos adormecido e desperto, oferecendo insights sobre a linguagem misteriosa da sua mente inconsciente.

## 🔮 Visão Geral

Morfeu emprega uma sinfonia de quatro agentes de IA especializados trabalhando em harmonia para desvendar os mistérios escondidos em seus sonhos:

1. **Agente de Busca de Símbolos** 🔍: Identifica potenciais símbolos de sonhos e pesquisa seus significados em interpretações antigas e modernas
2. **Analisador de Símbolos** 🧩: Analisa símbolos no contexto do sonho e em nosso banco de dados arquetípico
3. **Interpretador de Sonhos** 📜: Cria uma interpretação poética e perspicaz conectando todos os elementos em uma narrativa significativa
4. **Verificador de Qualidade e Idioma** 🌐: Verifica a qualidade da interpretação e garante correspondência de idioma com traduções quando necessário

## 🌊 Como Funciona

Morfeu segue um fluxo cuidadosamente orquestrado para transformar seu sonho em insights significativos:

1. **Entrada**: Você compartilha seu sonho através da API ou interface de linha de comando
2. **Descoberta de Símbolos**: O primeiro agente identifica símbolos significativos em seu sonho e pesquisa seus significados
3. **Análise Contextual**: O segundo agente analisa estes símbolos contra nosso banco de dados e dentro do contexto único do seu sonho
4. **Interpretação Poética**: O terceiro agente tece todos os elementos em uma interpretação coesa com insights psicológicos
5. **Verificação e Tradução**: O quarto agente garante qualidade e traduz se seu sonho estava em um idioma não-inglês
6. **Entrega**: Você recebe uma interpretação abrangente com orientação prática para sua vida desperta

O processo inteiro leva apenas segundos, mas se baseia em milênios de simbolismo de sonhos e entendimento psicológico moderno.

## ✨ Exemplos de Resultados

[Os mesmos exemplos já presentes no README, traduzidos para português]

## 🛠️ Instalação

1. Clone este repositório
   ```bash
   git clone https://github.com/seuusuario/morfeu.git
   cd morfeu
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -e .
   ```

4. Crie um arquivo `.env` na raiz do projeto com sua chave de API do Google:
   ```
   GOOGLE_API_KEY=sua_chave_api_aqui
   ```

## 🚀 Uso

### Interface de Linha de Comando

Execute o interpretador de sonhos pela linha de comando:

```bash
python test_dream_client.py --interactive
```

Ou forneça um sonho diretamente:

```bash
python test_dream_client.py --dream "Eu estava voando sobre um oceano azul claro, sentindo-me livre e em paz."
```

### Servidor API

Inicie o servidor API:

```bash
python run_server.py
```

A API estará disponível em `http://localhost:8000` com os seguintes endpoints:
- `POST /interpret` - Interpretar um sonho
- `GET /health` - Verificação de saúde do serviço
- `GET /docs` - Documentação da API (fornecida pelo FastAPI)

#### Exemplo de Requisição API

```bash
curl -X POST "http://localhost:8000/interpret" \
     -H "Content-Type: application/json" \
     -d '{"dream": "Eu estava voando sobre um oceano azul claro, sentindo-me livre e em paz."}'
```

## 📁 Estrutura do Projeto

```
morfeu/
├── __init__.py
├── base_agent.py     # Funções auxiliares para agentes
├── dream_agent.py    # Agentes de interpretação de sonhos
├── main.py           # Aplicativo FastAPI
└── symbols.json      # Banco de dados de símbolos de sonhos
tests/
└── test_dream_interpreter.py  # Testes unitários
```

## 💎 Banco de Dados de Símbolos de Sonhos

O sistema inclui um banco de dados curado de símbolos comuns de sonhos com seus significados arquetípicos e interpretações contextuais. Os agentes usam este banco de dados junto com pesquisas online para fornecer análises abrangentes de sonhos.

## 🤝 Contribuindo

Recebemos contribuições de sonhadores, desenvolvedores, psicólogos e entusiastas da mitologia! Aqui está como você pode ajudar a tornar Morfeu ainda mais perspicaz:

1. **Expandir o banco de dados de símbolos**: Adicionar novos símbolos ou aprimorar os existentes
2. **Melhorar o suporte de idiomas**: Ajudar a refinar traduções para sonhos não-ingleses
3. **Aprimorar os prompts de IA**: Tornar as interpretações ainda mais poéticas e perspicazes
4. **Adicionar novos recursos**: Explorar diários de sonhos, padrões ao longo do tempo, etc.

Para contribuir:
1. Faça um fork deste repositório
2. Crie um novo branch (`git checkout -b feature/recurso-incrivel`)
3. Faça suas alterações
4. Faça commit (`git commit -m 'Adicionar algum recurso incrível'`)
5. Faça push para o branch (`git push origin feature/recurso-incrivel`)
6. Abra um Pull Request

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.