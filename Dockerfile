# 1. Imagem base
# Começamos com uma imagem oficial do Python. A versão 'slim' é menor e ideal para produção.
FROM python:3.9-slim

# 2. Definir o diretório de trabalho dentro do contêiner
# Todos os comandos a seguir serão executados a partir desta pasta.
WORKDIR /app

# 3. Copiar o arquivo de dependências e instalá-las
# Copiamos primeiro para aproveitar o cache do Docker. Se este arquivo não mudar,
# o Docker não precisará reinstalar as dependências toda vez que construir a imagem.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar o resto do código da sua aplicação para o contêiner
COPY . .

# 5. Expor a porta que a aplicação usa
# Informa ao Docker que o contêiner escutará na porta 3001.
EXPOSE 3001

# 6. Comando para executar a aplicação quando o contêiner iniciar
# Executa o servidor Flask.
CMD ["gunicorn", "--bind", "0.0.0.0:3001", "api:app"]