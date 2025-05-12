# C:\Users\ianes\Desktop\AS-Cloud\Dockerfile

FROM python:3.13-slim

# 1) Build-args com defaults para dev local
ARG FLASK_ENV=development
ARG SECRET_KEY=dev-secret-key
ARG SQLALCHEMY_DATABASE_URI=mysql://mysql:minecraft2013%21@db:3306/galeria?ssl_mode=DISABLED

# 2) Transforma build-args em ENV para o processo em tempo de execução
ENV FLASK_ENV=${FLASK_ENV} \
    SECRET_KEY=${SECRET_KEY} \
    SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI}
    
# instalando dependências para mysqlclient
RUN apt-get update && \
    apt-get install -y \
      gcc \
      python3-dev \
      default-libmysqlclient-dev \
      pkg-config \
      build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# Copia arquivos essenciais
COPY requirements.txt main.py config.py ./
COPY app/ app/

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Usa Gunicorn para produção local com db dockerizado
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]