from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Configurações do e-mail
    smtp_server = 'smtp.gmail.com'  # Ex: smtp.gmail.com
    smtp_port = 587  # Porta padrão para TLS
    smtp_user = 'derikbrandon4@gmail.com'  # e-mail
    smtp_password = 'jfjxzaykkseperie'  # senha ou senha de app

    # Criar a mensagem
    msg = MIMEText(f'Mensagem de {name} ({email}):\n\n{message}')
    msg['Subject'] = f'Contato de {name}'
    msg['From'] = smtp_user
    msg['To'] = smtp_user

    try:
        # Enviando o e-mail
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Inicia a conexão segura
            server.login(smtp_user, smtp_password)
            server.send_message(msg)

        return f"Obrigado pela mensagem, {name}!"
    except Exception as e:
        return f"Ocorreu um erro ao enviar a mensagem: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
