import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar el cliente de OpenAI
cliente = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def chatear_con_gpt():
    print("¡Bienvenido al ChatGPT de Línea de Comandos!")
    print("Escribe 'salir' para terminar el chat")
    print("-" * 50)

    # Mantener el historial de la conversación
    conversacion = []

    while True:
        # Obtener entrada del usuario
        entrada_usuario = input("\nTú: ")

        # Verificar si el usuario quiere salir
        if entrada_usuario.lower() == 'salir':
            print("\n¡Hasta luego!")
            break

        # Agregar mensaje del usuario a la conversación
        conversacion.append({"role": "user", "content": entrada_usuario})

        try:
            # Obtener respuesta de OpenAI
            respuesta = cliente.chat.completions.create(
                model="gpt-4o",
                messages=conversacion,
                max_tokens=1000
            )

            # Extraer e imprimir la respuesta del asistente
            respuesta_asistente = respuesta.choices[0].message.content
            print("\nAsistente:", respuesta_asistente)

            # Agregar respuesta del asistente al historial
            conversacion.append({"role": "assistant", "content": respuesta_asistente})

        except Exception as e:
            print(f"\nError: {str(e)}")

if __name__ == "__main__":
    chatear_con_gpt() 