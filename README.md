Projeto de Automação de Envio de E-mails em Python
Este projeto consiste em um script Python que automatiza o envio de e-mails usando o protocolo SMTP. Ele foi desenvolvido para ser seguro, fácil de usar e personalizável.

Funcionalidades
Envio de e-mails automatizados via Gmail.

Uso de variáveis de ambiente para armazenar credenciais sensíveis.

Tratamento de exceções para garantir robustez.

Logging para monitoramento e depuração.

Pré-requisitos
Antes de começar, certifique-se de ter o seguinte instalado:

Python 3.8 ou superior.

pip para gerenciar dependências.

Uma conta do Gmail com verificação em duas etapas ativada e uma Senha de App gerada.

Configuração
Clone o repositório:

bash
Copy
git clone https:https://github.com/GTMacieira/envio_automatico_email
cd projeto-automacao-email
Crie e ative um ambiente virtual:

bash
Copy
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

bash
Copy
pip install python-dotenv
Crie o arquivo .env:
Crie um arquivo chamado .env na raiz do projeto e adicione as seguintes variáveis:

Copy
EMAIL_REMETENTE=seu_email@gmail.com
EMAIL_SENHA=sua_senha_de_app
EMAIL_DESTINATARIO=destinatario@example.com
Observação: Substitua os valores pelas suas credenciais reais. Nunca compartilhe o arquivo .env publicamente.

Gere uma Senha de App:

Acesse sua conta Google.

Ative a verificação em duas etapas.

Gere uma Senha de App e use-a no campo EMAIL_SENHA.

Como Usar
Execute o script:

bash
Copy
python enviar_email.py
Verifique o resultado:

Se o e-mail for enviado com sucesso, você verá a mensagem: E-mail enviado com sucesso!.

Em caso de erro, o script exibirá uma mensagem de erro detalhada.

Estrutura do Projeto
Copy
projeto-automacao-email/
├── .env                    # Arquivo de variáveis de ambiente (não versionado)
├── .gitignore             # Ignora o arquivo .env e o ambiente virtual
├── README.md              # Este arquivo
├── enviar_email.py        # Script principal
└── requirements.txt       # Lista de dependências
Personalização
Adicionar anexos: Use a biblioteca email.mime.base e email.mime.application para anexar arquivos.

Enviar para múltiplos destinatários: Modifique o campo destinatario para uma lista de e-mails.

Agendar envios: Use bibliotecas como schedule ou cron para enviar e-mails em horários específicos.

Segurança
Nunca compartilhe o arquivo .env: Ele contém credenciais sensíveis.

Revogue a Senha de App se necessário: Caso suspeite que ela foi comprometida, gere uma nova.

Use HTTPS: Se o script se comunicar com APIs externas, certifique-se de que a conexão seja segura.

Contribuição
Contribuições são bem-vindas! Siga os passos abaixo:

Faça um fork do projeto.

Crie uma branch para sua feature (git checkout -b feature/nova-feature).

Commit suas mudanças (git commit -m 'Adiciona nova feature').

Push para a branch (git push origin feature/nova-feature).

Abra um Pull Request.

Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Contato
Se tiver dúvidas ou sugestões, entre em contato:

Nome: Guilherme Talpo Macieira

E-mail: macieira.talpo@gmail.com

GitHub: GTMacieira

Esse README.md cobre todos os aspectos essenciais do projeto e pode ser adaptado conforme necessário. Se precisar de mais alguma coisa, estou à disposição! 😊

