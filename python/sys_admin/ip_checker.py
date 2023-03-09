import socket

def get_ip_address():
    """
    Returns the IP address of the current machine.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

if __name__ == '__main__':
    print(get_ip_address())

