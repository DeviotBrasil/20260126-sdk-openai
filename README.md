# SDK OpenAI - Python

Projeto de demonstração para utilização da API da OpenAI com Python.

## 📋 Descrição

Este projeto demonstra como integrar a API da OpenAI em aplicações Python, utilizando o SDK oficial. Inclui exemplos práticos de uso do modelo GPT para criar conversas e processar texto.

## 🚀 Funcionalidades

- Integração com a API da OpenAI
- Uso do modelo GPT-3.5-turbo para chat
- Gerenciamento seguro de chaves de API
- Tratamento de erros
- Controle de tokens utilizados

## 📦 Pré-requisitos

- Python 3.8 ou superior
- Chave de API da OpenAI ([obtenha aqui](https://platform.openai.com/api-keys))

## ⚙️ Configuração Inicial

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd 20260126-sdk-openai
```

### 2. Criar ambiente virtual

#### Windows (CMD)

```cmd
python -m venv .venv
.venv\Scripts\activate
```

#### Linux/macOS (Bash)

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Configurar a chave da API

Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione sua chave da API:

```env
OPENAI_API_KEY=sua-chave-api-aqui
```

⚠️ **Importante**: Nunca compartilhe ou commite seu arquivo `.env` com a chave da API!

## 🎯 Como Usar

Execute o script principal:

```bash
python main.py
```

O script irá:
1. Carregar a chave da API do arquivo `.env`
2. Inicializar o cliente OpenAI
3. Enviar uma mensagem para o modelo GPT
4. Exibir a resposta e o número de tokens utilizados

## 📚 Estrutura do Projeto

```
20260126-sdk-openai/
├── main.py              # Script principal
├── requirements.txt     # Dependências do projeto
├── .env.example        # Exemplo de configuração
├── .env                # Suas configurações (não versionar!)
└── README.md           # Esta documentação
```

## 🔧 Comandos Úteis

### Atualizar dependências

```bash
python -m pip install -r requirements.txt --upgrade
```

### Listar dependências instaladas

```bash
pip freeze
```

### Gerar novo requirements.txt

```bash
pip freeze > requirements.txt
```

## 📖 Exemplos de Uso

### Modificar a mensagem

Edite o arquivo [main.py](main.py) e altere o conteúdo da mensagem:

```python
messages=[
    {"role": "system", "content": "Você é um assistente prestativo."},
    {"role": "user", "content": "Sua pergunta aqui"}
]
```

### Alterar o modelo

Você pode usar diferentes modelos da OpenAI:

```python
model="gpt-4"  # Mais capaz, mais caro
model="gpt-3.5-turbo"  # Rápido e econômico
```

### Ajustar parâmetros

- `temperature` (0.0 - 2.0): Controla a criatividade das respostas
- `max_tokens`: Limita o tamanho da resposta

## 🔗 Recursos

- [Documentação Oficial da OpenAI](https://platform.openai.com/docs)
- [SDK Python da OpenAI](https://github.com/openai/openai-python)
- [Preços da API](https://openai.com/pricing)

## 📄 Licença

Este projeto é livre para uso educacional e de demonstração.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

Atualiza as dependências já instaladas
```bash
python -m pip install -r requirements.txt --upgrade
```

Lista todas as dependências instaladas (para gerar requirements.txt)
```bash
python -m pip freeze > requirements.txt
```
