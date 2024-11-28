# Clon de ChatGPT en Línea de Comandos

Un clon simple de ChatGPT basado en Python que se ejecuta en tu terminal.

## Requisitos Previos

- Python 3.7 o superior
- Una cuenta en OpenAI y una API key
- Terminal o línea de comandos

## Configuración

1. Crea un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   .\venv\Scripts\activate   # En Windows
   ```

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Configura tu API key de OpenAI:
   - Crea una copia del archivo `.env.example` y renómbralo a `.env`
   - Abre el archivo `.env` y reemplaza `your-api-key-here` con tu API key de OpenAI:
     ```
     OPENAI_API_KEY=tu-api-key-aquí
     ```

## Uso

1. Ejecuta el programa:
   ```bash
   python chat.py
   ```
2. Interactúa con el chatbot escribiendo tus mensajes y presionando Enter.
3. Para salir, escribe 'exit', 'quit' o presiona Ctrl+C.

## Características

- Interfaz de línea de comandos simple e intuitiva
- Historial de conversación persistente
- Soporte para múltiples modelos de OpenAI
- Personalización de parámetros de generación

## Contribuir

1. Haz un fork del repositorio
2. Crea una rama para tu función (`git checkout -b feature/AmazingFeature`)
3. Realiza tus cambios y haz commit (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
