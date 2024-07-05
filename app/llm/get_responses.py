from openai import OpenAI


client = OpenAI()
def responses(prompt: str, question: str):
  
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {'role': 'system',
             'content': 'Eres un agente que se especializa en dictaminar actas constitutivas. Se te dará un texto de una acta constitutiva, una constancia de situación fiscal, o una identificación, el texto de cualquiera de estos tres documentos estará envuelto en tres pares de comillas, algo como: """[texto]""", y tendrás que responder de manera concisa a las preguntas que se te hagan al respecto. Únicamente deberás responder con el dato que se te está solicitando, NI UN CARACTER MÁS, y EN UNA SOLA LINEA. En caso de que no encuentres en el texto provisto una respuesta concreta a la información solicitada, debes responder "N/A".'
             },
            {'role': 'user', 
             'content': f'''En base al siguiente texto: """${prompt}""". Responde la siguiente pregunta: ${question}'''
             }
        ]
    )

    return response.choices[0].message.content