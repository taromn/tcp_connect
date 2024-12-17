import socket, sys
 
def tcp_connect(host_name, tcp_port, timeout=5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host_name, tcp_port))
        print(f"{host_name}:{tcp_port} is open")
        s.close()
        return True
    except Exception as error:
        print(error)
        print(f"failed to connect to {host_name}:{tcp_port}")
        return False


t_port = int(sys.argv[1])
tcp_connect("localhost", t_port)
