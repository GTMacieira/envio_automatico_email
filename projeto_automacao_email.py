#importar bibliotecas
import os
import logging
import smtplib # Envio de e-mail via SMTP
from dotenv import load_dotenv
from email.mime.text import MIMEText # Para criar o corpo do e-mail
from email.mime.multipart import MIMEMultipart # Para criar e-mail com multiplas partes (assunto, corpo, ...)

# Carrega as cariáveis de ambiente so arquivo .env
load_dotenv()

# Configurar o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Obtém as credenciais das variáveis de ambiente
remetente = os.getenv('EMAIL_REMETENTE') #E-mail remetente
senha = os.getenv('EMAIL_SENHA') # Senha do e-mail
destinatario = os.getenv('EMAIL_DESTINATARIO') # E-mail destinatário

# Valida se as credenciais foram carregadas corrtamente
if not remetente or not senha or not destinatario:
    raise ValueError ('Credenciais não encontradas no arquivo .env')

#Configurações do e-mail
assunto = 'Assunto do e-mail' # Assunto do e-mail
corpo = 'Corpo do e-mail em HTML' # Corpo do e-mail

# Criando a estrutura do e-mail
msg = MIMEMultipart() # Cria um objeto MIMEMultipart para o e-mail
msg['From'] = remetente # Define o remetente
msg['To'] = destinatario # Define o destinatário
msg['Subject'] = assunto # Define o assunto

# Adicionando o corpo do e-mail
msg.attach(MIMEText(corpo, 'plain')) # Anexa o corpo ao e-mail

# Enviando o e-mail
try:
    # Código para enviar e-mail
    logging.info('Enviando email...')
    server = smtplib.SMTP('smtp.gmail.com', 587) # Usando o servidor SMTP do Gmail na porta 587
    server.starttls() #Inicia a conexão segura (TLS)
    server.login(remetente, senha) # Faz login no servidor SMTP
    server.sendmail(remetente, destinatario, msg.as_string()) # Envia o e-mail
    server.quit() # Encerra a conexão com o servidor
    logging.info('Email enviado com sucesso!') # Mensagem de sucesso
except smtplib.SMTPAuthenticationError:
    logging.info('Verifique suas credenciais')
except smtplib.SMTPException as e:
    logging.info(f'Erro ao enviar e-mail: {e}')
except Exception as e:
    logging.info(f'Erro inesperado: {e}') 