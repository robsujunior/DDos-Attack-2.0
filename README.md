# 📌 Ataque DDos

Este projeto tem como objetivo demonstrar o funcionamento de um ataque DDos (Dos, caso seja executado em apenas uma máquina).

---

## 🧠 Conceitos abordados

- Conexão TCP (Socket)
- Handshake TCP
- Envio de requisições HTTP
- Concorrência com Threads
- Overhead no kernel
- Degradação de serviço sob carga

---

## ⚙️ Funcionamento

O código realiza:

- Criação de múltiplas threads  
- Estabelecimento de conexões TCP com um host  
- Envio de requisições HTTP simples  
- Recebimento (ou não) de respostas do servidor  
- Monitoramento básico via saída no terminal  

---

## 📋 Requisitos

Para executar este projeto, você precisará de:

- Python3
- Sistema operacional baseado em Linux (Ubuntu, Debian, etc.) ou macOS

---

## 🚀 Como executar

### 1. Clone o repositório e navegue até a pasta

```bash
git clone https://github.com/robsujunior/DDos-Attack-2.0.git
cd DDos-Attack-2.0
```

### 2. Dê permissão de execução 

```bash
chmod +x DDos Attack.py
```

### 2. Execute o script
```bash
python3 DDos Attack.py
```
