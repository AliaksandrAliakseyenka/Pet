import socket

server = socket.create_server(("127.0.0.1", 8442))
# Освободить порт после выхода из приложения
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Размер очереди сетевых запросов
server.listen(10)
try:
	while True:
		# Tup
		client_socket, address = server.accept()
		received_data = client_socket.recv(1024).decode('utf-8')

		print(f"Received data on a socket", received_data)

		path = received_data.split(" ")[1]
		response = f"HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n" \
				   f"Hi!<br />Path: {path}"

		client_socket.send(response.encode("utf-8"))
		client_socket.shutdown(socket.SHUT_RDWR)

except KeyboardInterrupt:
	server.close()
