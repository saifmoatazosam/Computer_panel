import socket
import pyautogui

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

        # Perform corresponding action based on command
        if command.lower() == 'enter':
            pyautogui.press('enter')
        elif command.lower() == 'tab':
            pyautogui.press('tab')
        elif command.lower() == 'space':
            pyautogui.press('space')
        elif command.lower() == 'left':
            pyautogui.press('left')
        elif command.lower() == 'right':
            pyautogui.press('right')
        elif command.lower() == 'up':
            pyautogui.press('up')
        elif command.lower() == 'down':
            pyautogui.press('down')
        elif command.lower() == 'esc':
            pyautogui.press('esc')
        elif command.lower() == 'delete':
            pyautogui.press('delete')
        elif command.lower() == 'home':
            pyautogui.press('home')
        elif command.lower() == 'end':
            pyautogui.press('end')
        else:
            # If the command is not recognized, type it as it is
            pyautogui.typewrite(command)

        # Send response back to client
        response = "Keyboard command executed!"
        client_socket.sendall(response.encode())

    elif data.startswith('mouse:'):
        # Extract mouse command
        mouse_command = data.split(':')[1]

        # Perform corresponding action based on command
        if mouse_command.lower() == 'left_click':
            pyautogui.click(button='left')
        elif mouse_command.lower() == 'right_click':
            pyautogui.click(button='right')
        elif mouse_command.lower() == 'scroll_up':
            pyautogui.scroll(3)  # Scroll up by 3 "clicks"
        elif mouse_command.lower() == 'scroll_down':
            pyautogui.scroll(-3)  # Scroll down by 3 "clicks"

        # Send response back to client
        response = "Mouse command executed!"
        client_socket.sendall(response.encode())

    else:
        # Handle other types of commands here
        response = "Command received!"
        client_socket.sendall(response.encode())

    # Close the connection
    client_socket.close()
