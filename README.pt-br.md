# 🌙✨ Intérprete de Sonhos Morfeu

[Read in English](README.md) | [Leer en Español](README.es.md) | [Ler em Português](README.pt-br.md)

> *"Os sonhos são a estrada real para o inconsciente." - Sigmund Freud*

Morfeu é um oráculo digital que mergulha no subconsciente e interpreta sonhos através do simbolismo antigo, impulsionado pela IA moderna. Nomeado em homenagem a Morfeu, o deus grego dos sonhos, este intérprete faz a ponte entre seus mundos adormecido e desperto, oferecendo insights sobre a misteriosa linguagem de sua mente inconsciente.

## 🔮 Visão Geral

Morfeu emprega uma sinfonia de quatro agentes de IA especializados trabalhando em harmonia para desvendar os mistérios ocultos em seus sonhos:

1. **Agente de Busca de Símbolos** 🔍: Identifica símbolos potenciais nos sonhos e busca seus significados em interpretações antigas e modernas
2. **Analisador de Símbolos** 🧩: Analisa os símbolos no contexto do sonho e nossa base de dados arquetípica curada
3. **Intérprete de Sonhos** 📜: Cria uma interpretação poética e perspicaz conectando todos os elementos em uma narrativa significativa
4. **Verificador de Qualidade e Idioma** 🌐: Verifica a qualidade da interpretação e garante a correspondência de idiomas com traduções quando necessário

## 🌊 Como Funciona

Morfeu segue um fluxo cuidadosamente orquestrado para transformar seu sonho em um insight significativo:

1. **Entrada**: Você compartilha seu sonho através da API ou interface de linha de comando
2. **Descoberta de Símbolos**: O primeiro agente identifica símbolos significativos em seu sonho e pesquisa seus significados
3. **Análise Contextual**: O segundo agente analisa esses símbolos contra nossa base de dados e dentro do contexto único de seu sonho
4. **Interpretação Poética**: O terceiro agente tece todos os elementos em uma interpretação coesa com insights psicológicos
5. **Verificação e Tradução**: O quarto agente garante a qualidade e traduz se seu sonho estava em um idioma diferente do português
6. **Entrega**: Você recebe uma interpretação abrangente com orientação prática para sua vida desperta

Todo o processo leva apenas segundos, mas se baseia em milênios de simbolismo onírico e compreensão psicológica moderna.

## 🛠️ Instalação

1. Clone este repositório
   ```bash
   git clone https://github.com/yourusername/morfeu.git
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

4. Crie um arquivo `.env` na raiz do projeto com sua chave API do Google:
   ```
   GOOGLE_API_KEY=sua_chave_api_aqui
   ```

## 🚀 Uso

### Interface de Linha de Comando

Execute o intérprete de sonhos da linha de comando:

```bash
python test_dream_client.py --interactive
```

Ou forneça um sonho diretamente:

```bash
python test_dream_client.py --dream "Eu estava voando sobre um oceano azul claro, me sentindo livre e em paz."
```

### Servidor API

Inicie o servidor API:

```bash
python run_server.py
```

A API estará disponível em `http://localhost:8000` com os seguintes endpoints:
- `POST /interpret` - Interpreta um sonho
- `GET /health` - Endpoint de verificação de saúde
- `GET /docs` - Documentação da API (fornecida pelo FastAPI)

#### Exemplo de Requisição API

```bash
curl -X POST "http://localhost:8000/interpret" \
     -H "Content-Type: application/json" \
     -d '{"dream": "Eu estava voando sobre um oceano azul claro, me sentindo livre e em paz."}'
```

## 📁 Estrutura do Projeto

```
morfeu/
├── __init__.py
├── base_agent.py     # Funções auxiliares para agentes
├── dream_agent.py    # Agentes de interpretação de sonhos
├── main.py           # Aplicação FastAPI
└── symbols.json      # Base de dados de símbolos oníricos
tests/
└── test_dream_interpreter.py  # Testes unitários
```

## 💎 Base de Dados de Símbolos Oníricos

O sistema inclui uma base de dados curada de símbolos oníricos comuns com seus significados arquetípicos e interpretações contextuais. Os agentes usam esta base de dados junto com buscas online para fornecer análises completas dos sonhos.

## 🤝 Contribuindo

Bem-vindas contribuições de sonhadores, desenvolvedores, psicólogos e entusiastas da mitologia! Aqui está como você pode ajudar a tornar o Morfeu ainda mais perspicaz:

1. **Expandir a base de dados de símbolos**: Adicionar novos símbolos ou aprimorar os existentes
2. **Melhorar o suporte a idiomas**: Ajudar a refinar as traduções para sonhos em outros idiomas
3. **Aprimorar os prompts de IA**: Tornar as interpretações ainda mais poéticas e perspicazes
4. **Adicionar novos recursos**: Explorar diário de sonhos, padrões ao longo do tempo, etc.

Para contribuir:
1. Faça um fork deste repositório
2. Crie uma nova branch (`git checkout -b feature/amazing-feature`)
3. Faça suas alterações
4. Faça commit (`git commit -m 'Adiciona algum recurso incrível'`)
5. Faça push para a branch (`git push origin feature/amazing-feature`)
6. Abra um Pull Request

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.