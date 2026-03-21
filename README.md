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

1. Criação de múltiplas threads  
2. Estabelecimento de conexões TCP com um host  
3. Envio de requisições HTTP simples  
4. Recebimento (ou não) de respostas do servidor  
5. Monitoramento básico via saída no terminal  

---

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/robsujunior/DDos-Attack-2.0.git
cd DDos-Attack-2.0
```
### 2. Execute o script
```bash
python nome_do_arquivo.py
```
