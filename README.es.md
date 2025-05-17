# 🌙✨ Intérprete de Sueños Morfeu

[Read in English](README.md) | [Leer en Español](README.es.md) | [Ler em Português](README.pt-br.md)

> *"Los sueños son el camino real hacia el inconsciente." - Sigmund Freud*

Morfeu es un oráculo digital que se sumerge en el subconsciente e interpreta los sueños a través del simbolismo antiguo, impulsado por la IA moderna. Nombrado en honor a Morfeo, el dios griego de los sueños, este intérprete une el puente entre tus mundos dormido y despierto, ofreciendo una visión del misterioso lenguaje de tu mente inconsciente.

## 🔮 Descripción General

Morfeu emplea una sinfonía de cuatro agentes de IA especializados trabajando en armonía para desentrañar los misterios ocultos en tus sueños:

1. **Agente de Búsqueda de Símbolos** 🔍: Identifica símbolos potenciales en los sueños y busca sus significados en interpretaciones antiguas y modernas
2. **Analizador de Símbolos** 🧩: Analiza los símbolos en el contexto del sueño y nuestra base de datos arquetípica curada
3. **Intérprete de Sueños** 📜: Crea una interpretación poética e intuitiva conectando todos los elementos en una narrativa significativa
4. **Verificador de Calidad y Lenguaje** 🌐: Verifica la calidad de la interpretación y asegura la coincidencia de idiomas con traducciones si es necesario

## 🌊 Cómo Funciona

Morfeu sigue un flujo cuidadosamente orquestado para transformar tu sueño en una visión significativa:

1. **Entrada**: Compartes tu sueño a través de la API o la interfaz de línea de comandos
2. **Descubrimiento de Símbolos**: El primer agente identifica símbolos significativos en tu sueño e investiga sus significados
3. **Análisis Contextual**: El segundo agente analiza estos símbolos contra nuestra base de datos y dentro del contexto único de tu sueño
4. **Interpretación Poética**: El tercer agente teje todos los elementos en una interpretación cohesiva con perspectivas psicológicas
5. **Verificación y Traducción**: El cuarto agente asegura la calidad y traduce si tu sueño estaba en un idioma diferente al español
6. **Entrega**: Recibes una interpretación completa con orientación práctica para tu vida despierta

Todo el proceso toma solo segundos, pero se basa en milenios de simbolismo onírico y comprensión psicológica moderna.

## 🛠️ Instalación

1. Clona este repositorio
   ```bash
   git clone https://github.com/yourusername/morfeu.git
   cd morfeu
   ```

2. Crea un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -e .
   ```

4. Crea un archivo `.env` en la raíz del proyecto con tu clave API de Google:
   ```
   GOOGLE_API_KEY=tu_clave_api_aqui
   ```

## 🚀 Uso

### Interfaz de Línea de Comandos

Ejecuta el intérprete de sueños desde la línea de comandos:

```bash
python test_dream_client.py --interactive
```

O proporciona un sueño directamente:

```bash
python test_dream_client.py --dream "Estaba volando sobre un océano azul claro, sintiéndome libre y en paz."
```

### Servidor API

Inicia el servidor API:

```bash
python run_server.py
```

La API estará disponible en `http://localhost:8000` con los siguientes endpoints:
- `POST /interpret` - Interpreta un sueño
- `GET /health` - Endpoint de verificación de estado
- `GET /docs` - Documentación de la API (proporcionada por FastAPI)

#### Ejemplo de Solicitud API

```bash
curl -X POST "http://localhost:8000/interpret" \
     -H "Content-Type: application/json" \
     -d '{"dream": "Estaba volando sobre un océano azul claro, sintiéndome libre y en paz."}'
```

## 📁 Estructura del Proyecto

```
morfeu/
├── __init__.py
├── base_agent.py     # Funciones auxiliares para agentes
├── dream_agent.py    # Agentes de interpretación de sueños
├── main.py           # Aplicación FastAPI
└── symbols.json      # Base de datos de símbolos oníricos
tests/
└── test_dream_interpreter.py  # Pruebas unitarias
```

## 💎 Base de Datos de Símbolos Oníricos

El sistema incluye una base de datos curada de símbolos oníricos comunes con sus significados arquetípicos e interpretaciones contextuales. Los agentes utilizan esta base de datos junto con búsquedas en línea para proporcionar análisis completos de los sueños.

## 🤝 Contribuir

¡Bienvenimos contribuciones de soñadores, desarrolladores, psicólogos y entusiastas de la mitología! Así es como puedes ayudar a hacer que Morfeu sea aún más perspicaz:

1. **Expandir la base de datos de símbolos**: Añadir nuevos símbolos o mejorar los existentes
2. **Mejorar el soporte de idiomas**: Ayudar a refinar las traducciones para sueños en otros idiomas
3. **Mejorar los prompts de IA**: Hacer las interpretaciones aún más poéticas e intuitivas
4. **Añadir nuevas características**: Explorar el diario de sueños, patrones a lo largo del tiempo, etc.

Para contribuir:
1. Haz un fork de este repositorio
2. Crea una nueva rama (`git checkout -b feature/amazing-feature`)
3. Realiza tus cambios
4. Haz commit (`git commit -m 'Añade alguna característica increíble'`)
5. Haz push a la rama (`git push origin feature/amazing-feature`)
6. Abre un Pull Request

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

--- 