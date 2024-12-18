import socket 
import sys

# Usage : python3 bannerGrab.py {IP/DOMAIN} {PORT}

def banniereSSH(ip,port=int(sys.argv[2]),timeout=3):
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.settimeout(timeout)
			s.connect((ip, port))
			banner= s.recv(1024).decode('utf-8',errors="ignore")
			return f"[{ip}:{port}] - {banner.strip()}"
	except Exception as e:
		return f"[{ip}:{port}] - erreur: Le port est fermé/filtré"
		

if __name__ == "__main__":
	targets=[sys.argv[1]]
	for target in targets:
		result = banniereSSH(target)
		print(result)
