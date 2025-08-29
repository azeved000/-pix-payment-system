# Sistema de Pagamento PIX com Flask 💳

Um sistema completo de pagamentos PIX desenvolvido com Flask, SQLAlchemy e WebSocket para notificações em tempo real.

## 📋 Funcionalidades

- ✅ **Criação de Pagamentos PIX**: Gere pagamentos com QR codes únicos
- ✅ **QR Code Dinâmico**: Códigos QR gerados automaticamente para cada pagamento
- ✅ **Confirmação de Pagamento**: Sistema de confirmação manual para testes
- ✅ **Notificações em Tempo Real**: WebSocket para atualizações instantâneas
- ✅ **Interface Responsiva**: Templates HTML modernos e responsivos
- ✅ **API RESTful**: Endpoints completos para integração

## 🚀 Tecnologias Utilizadas

- **Backend**: Flask 2.3.0
- **Banco de Dados**: SQLite com SQLAlchemy ORM
- **WebSocket**: Flask-SocketIO para comunicação em tempo real
- **QR Code**: Biblioteca qrcode com PIL
- **Frontend**: HTML5, CSS3, JavaScript Vanilla

## 📦 Instalação e Configuração

### Pré-requisitos
- Python 3.11+
- pip (gerenciador de pacotes do Python)

### 1. Clone o repositório
```bash
git clone https://github.com/azeved000/-pix-payment-system.git
cd -pix-payment-system
```

### 2. Crie um ambiente virtual
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação
```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

## 📚 Documentação da API

### Endpoints Disponíveis

#### 1. Criar Pagamento PIX
```http
POST /payments/pix
Content-Type: application/json

{
    "value": 150.75
}
```

**Resposta:**
```json
{
    "message": "The payment has been created",
    "payment_id": "123",
    "bank_payment_id": "uuid-generated",
    "qr_code_path": "static/img/qr_code_payment_uuid.png"
}
```

#### 2. Visualizar Pagamento
```http
GET /payments/pix/{payment_id}
```

Retorna a página HTML com o QR code e detalhes do pagamento.

#### 3. Confirmar Pagamento
```http
POST /payments/pix/confirmation
Content-Type: application/json

{
    "bank_payment_id": "uuid-do-pagamento"
}
```

## 🎯 Como Usar

### 1. **Criação de Pagamento**
- Faça uma requisição POST para `/payments/pix` com o valor desejado
- Receberá um ID de pagamento e o caminho do QR code

### 2. **Visualização**
- Acesse `/payments/pix/{payment_id}` no navegador
- O QR code será exibido junto com os detalhes do pagamento
- A página se atualizará automaticamente quando o pagamento for confirmado

### 3. **Confirmação**
- Use uma ferramenta como Postman ou curl para simular a confirmação
- Faça POST para `/payments/pix/confirmation` com o `bank_payment_id`
- A página será atualizada em tempo real via WebSocket

## 🧪 Testando com Postman

### Collection de Exemplo

1. **Criar Pagamento**
   - **Method**: POST
   - **URL**: `http://localhost:5000/payments/pix`
   - **Body**: `{"value": 150.75}`

2. **Confirmar Pagamento**
   - **Method**: POST  
   - **URL**: `http://localhost:5000/payments/pix/confirmation`
   - **Body**: `{"bank_payment_id": "cole-o-uuid-aqui"}`

## 📁 Estrutura do Projeto

```
pix-payment-system/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências do projeto
├── .gitignore            # Arquivos ignorados pelo Git
├── db_models/
│   └── payment.py        # Modelo de dados para pagamentos
├── payments/
│   └── pix.py           # Lógica de negócio do PIX
├── repository/
│   └── database.py       # Configuração do banco de dados
├── static/
│   ├── css/
│   │   └── styles.css    # Estilos CSS
│   ├── img/             # QR codes gerados
│   └── template_img/    # Imagens do template
├── templates/
│   ├── payment.html     # Página de pagamento
│   ├── confirmed_payment.html  # Página de confirmação
│   └── 404.html         # Página de erro 404
└── instance/
    └── database.db      # Banco de dados SQLite
```

## 🛠️ Configurações de Desenvolvimento

### Modo Debug
O Flask está configurado para executar em modo debug por padrão:
```python
if __name__ == "__main__":
    socketio.run(app, debug=True)
```

### Banco de Dados
- SQLite é usado por padrão para simplicidade
- O banco é criado automaticamente na pasta `instance/`
- Para produção, considere usar PostgreSQL ou MySQL

## 🚀 Deploy em Produção

### Considerações para Produção:
1. **Variáveis de Ambiente**: Configure `FLASK_ENV=production`
2. **Banco de Dados**: Migre para PostgreSQL/MySQL
3. **WebServer**: Use Gunicorn + Nginx
4. **HTTPS**: Configure SSL/TLS
5. **Monitoramento**: Adicione logs e métricas

### Exemplo com Gunicorn:
```bash
pip install gunicorn
gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:5000 app:app
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma feature branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🔧 Solução de Problemas

### Problemas Comuns:

**1. Erro de importação do Flask:**
```bash
pip install --upgrade flask
```

**2. WebSocket não conecta:**
- Verifique se o Flask-SocketIO está instalado
- Confirme se o JavaScript está carregando corretamente

**3. QR codes não aparecem:**
- Verifique se a pasta `static/img/` existe
- Confirme as permissões de escrita na pasta

## 📊 Status do Projeto

- ✅ **MVP Completo**: Funcionalidades básicas implementadas
- ✅ **WebSocket**: Notificações em tempo real funcionando
- ✅ **API REST**: Endpoints principais criados
- 🔄 **Em desenvolvimento**: Melhorias na interface
- 📋 **Próximos passos**: 
  - Autenticação de usuários
  - Histórico de pagamentos
  - Dashboard administrativo

---

**Desenvolvido com ❤️ para o curso Rocketseat Python Nível 3**
