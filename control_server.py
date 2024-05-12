import socket
import keyboard  # Import the keyboard library for keyboard actions
import pyinputplus as pyip  # Import pyinputplus for mouse actions

# Set up socket
HOST = '192.168.1.6'  # Listen on all available network interfaces
PORT = 12345      # Choose a port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print(f"Server is listening on {HOST}:{PORT}")

while True:
    # Accept incoming connection
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive data from client
    data = client_socket.recv(1024).decode()

    # Print received data
    print(f"Received data: {data}")

    # Process the received data
    if data.startswith('keyboard:'):
        # Extract keyboard command
        command = data.split(':')[1]

        # Perform corresponding action based on command using the keyboard library
        keyboard.press_and_release(command)

        # Send response back to client
        response = "Keyboard command executed!"
        client_socket.sendall(response.encode())

    elif data.startswith('mouse:'):
        # Extract mouse command
        mouse_command = data.split(':')[1]

        # Perform corresponding action based on command using pyinputplus
        if mouse_command.lower() == 'left_click':
            pyip.moveTo(100, 100)  # Move mouse to a position
            pyip.click()  # Perform a left click
        elif mouse_command.lower() == 'right_click':
            pyip.moveTo(100, 100)  # Move mouse to a position
            pyip.rightClick()  # Perform a right click
        elif mouse_command.lower() == 'scroll_up':
            pyip.scroll(10)  # Scroll up by 10 steps
        elif mouse_command.lower() == 'scroll_down':
            pyip.scroll(-10)  # Scroll down by 10 steps

        # Send response back to client
        response = "Mouse command executed!"
        client_socket.sendall(response.encode())

    else:
        # Handle other types of commands here
        response = "Command received!"
        client_socket.sendall(response.encode())

    # Close the connection
    client_socket.close()
