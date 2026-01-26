import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
    """
    Função principal que demonstra o uso da API da OpenAI.
    """
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # Obtém a chave da API
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("Erro: OPENAI_API_KEY não encontrada no arquivo .env")
        return
    
    try:
        # Inicializa o cliente OpenAI com a chave da API
        client = OpenAI(api_key=api_key)
        
        # Cria uma conversa com o modelo
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente prestativo."},
                {"role": "user", "content": "O Palmeiras tem mundial?"}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        # Exibe a resposta
        print("Resposta da OpenAI:")
        print("-" * 50)
        print(response.choices[0].message.content)
        print("-" * 50)
        print(f"\nTokens utilizados: {response.usage.total_tokens}")
        
    except Exception as e:
        print(f"Erro ao chamar a API da OpenAI: {str(e)}")

if __name__ == "__main__":
    main()