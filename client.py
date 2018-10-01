import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("127.0.0.1", 12345))

clients_input = input("Some input from the client: ")
soc.send(clients_input.encode("utf-8"))
result_bytes = soc.recv(4096)
result_string = result_bytes.decode("utf-8")

print("result from server is {}".format(result_string))
