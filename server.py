from socket import *


def main():
    #set the server port to 80
    serverPort=80
    serverSocket = socket(AF_INET, SOCK_STREAM)
    #Prepare a sever socket
    serverSocket.bind((gethostname(),serverPort))
    serverSocket.listen(1)
    #print the server state is running or not 
    print('the web server is on prot:',serverPort)
    #run the server in progress
    while True:
        print('Ready to serve...')
        (connectionSocket,address) = serverSocket.accept()

        try:
            #record the respons message
            message = (connectionSocket.recv(1024))
            #print the response message
            print (message,'::',message.split()[0],':',message.split()[1])
            #fromat the message and find the file that requested
            filename = message.split()[1]
            #print the file name 
            print (filename,'||',filename[1:])
            #open the target file 
            f = open(filename[1:])
            #read the target file 
            outputdata = f.read() 
            #Send one HTTP header line into socket
            httpok = '\nHTTP/1.1 200 OK\n\n'
            #encode the response and send
            connectionSocket.send(httpok.encode())
             
            #send the file feed back biy "connectionSocket.send(outputdata.encode())"
            #this line will cause show helloworld twice, delete

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            
        except IOError:
#Send response message for file not found
            print( "404 Page Not Found")
            #save the error on information client
            errorsent = '\nHTTP/1.1 404 Not Found\n\n'
            #encode the error information and send to the host
            connectionSocket.send(errorsent.encode())
        #shut down the socket
        connectionSocket.close()

#run the fuction at the end start the server
if __name__ == '__main__':
    main()