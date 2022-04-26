In this assignment, you will create a chat room on a single computer where you and your (imaginary) friends can chat with each other. The following steps will be required to achieve this:

1)Create a server program that runs on a specific port passed via the command line.
2)Create a client program that can join this server.
3)The client needs a display name and a passcode to enter the chat room. (Assume all clients use the same passcode but different display name). The passcode will be restricted to a maximum of 5 alpha-numeric characters only. Anything over 5 letters can be treated as invalid. You do not have to handle input over 10 characters long. The display name is a maximum of 8 characters long.
4)The job of the server is to accept connections from clients, get their display name and passcode (in plaintext), verify that the passcode is correct and then allow clients into the chat room.
5)When any client sends a message, the display name is shown before the message, followed by a colon (:), and the message is delivered to all other current clients. 
6)Clients can type any text message, or can type one of the following shortcut codes to display specific text to everyone:
    1- Type :) to display [feeling happy]
    2- Type :( to display [feeling sad]
    3- Type :mytime to display the current time
    4- Type :+1hr to display the current time + 1 hour
    5- Type :Exit to close your connection and terminate the client
    6- [Fun part - not graded] '\' overrides the next word until a space or newline. For example,       
        \:mytime   will print :mytime instead of the actual time.