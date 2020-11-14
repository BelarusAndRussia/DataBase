import socket, time
host = socket.gethostbyname(socket.gethostname())
port = 9090

BUFFER = 1024
clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
quit = False
print("[ Server Started ]")

while True:
    try:
        data, addr = s.recvfrom(BUFFER)
        if addr not in clients:
            clients.append(addr)
        try:
            if data.decode("utf-8").endswith(" <= left chat "):
                clients.remove(addr)
        except UnicodeDecodeError:
            pass


        # itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        # print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime + "]/", end="")
        # print(data.decode("utf-8"))

        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except:
        clients.remove(addr)
        continue
s.close()
