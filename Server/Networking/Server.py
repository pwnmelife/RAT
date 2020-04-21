from FileTransferData import FileTransferData
from PacketManager import PacketManager
from multiprocessing import Lock
from PacketStructs import Message
from PacketType import PacketType
import threading
import socket


class Connection:
    def __init__(self, socket_):
        
        self.ActiveConnection = True
        self.socket_ = socket_
        self.file = FileTransferData()
        self.pm = PacketManager()


class Server:

    # public property

    # private property
    

    # public function
    def __init__(self, port, BroadcastPublically):
        
        # public proerty

        # private property
        
        self.__UnusedConnection = 0 # int
        self.__connections = list()
        self.__connectionMgr_mutex = Lock()
        # connection
        # connectionMgr_mutex
        # addr
        # addrlen
        # sListen
        # currentSessionID
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if BroadcastPublically:
            s.bind((socket.INADDR_ANY, port))
        else:
            s.bind(("127.0.0.1",port))
        s.listen(5)
        self.__server = s
        # # to do
        # pass
    
    # public function
    def ListenForNewConnection(self):
        lt = threading.Thread(self.__ListenerThread, args=())
        lt.start()
        pass

    def HandleInput(self):


        pass

    # private function
    @staticmethod
    def __ClientHandleThread(ID):
        

        pass

    @staticmethod
    def __PacketSenderThread():


        pass

    @staticmethod
    def __ListenerThread(self):
        while True:
            
            conn, address = self.__server.accept()

            # acquire mutex lock, when to release it
            # 
            self.__connectionMgr_mutex.acquire()
            # connectionMgr_mutex is automatically unlocked when lock goes out of scope
            NewConnectionID = len(self.__connections)

            if self.__UnusedConnection > 0:
                
                for i in range(len(self.__connections)):
                    if self.__connections[i].ActiveConnection == False:
                        self.__connections[i].socket_ = conn
                        self.__connections[i].ActiveConnection = True
                        NewConnectionID = i
                        self.__UnusedConnection -= 1
                        break
            else:
                connection = Connection(conn)
                self.__connections.append(connection)

            
            print("Client Connected! ID: {0} | IP: {1} ".format(NewConnectionID, address[0]))
            threading.Thread(Server.__ClientHandleThread, args=(NewConnectionID)).start()
            self.__connectionMgr_mutex.release()

    def __handleScript(self, script):
        

        pass

    # send content
    def __sendall(self, ID, data, totalbytes):
        try:
            result = self.__connections[ID].socket_.sendall(data)
        except socket.error:
            return False
        
        return True
        

    def __recvall(self, ID, totalbytes):
        
        bytesReceived = 0
        while bytesReceived < totalbytes:
            try:
                data = self.__connections[ID].socket__.recv(totalbytes)
            except socket.error:
                return (False, "")
            bytesReceived += len(data)
        
        return (True, data)
        

    # int32
    def __Sendint32_t(self, ID, _int32_t):
        
        net_int32 = socket.htonl(_int32_t)
        s_int32 = str(net_int32)
        result = self.__sendall(ID, s_int32, 4)
        if result:
            return True
        else:
            return False
        
    
    def __Getint32_t(self, ID):

        result, _int32_t = self.__recvall(ID, 4)
        if result == False:
            return (False, "")
        tmp = socket.ntohl(int(_int32_t))
        return (True, tmp)
        

   
    def __SendPacketType(self, ID, _packettype):
        
        result = self.__Sendint32_t(ID, _packettype)
        if result:
            return True
        else:
            return False

    def __GetPacketType(self, ID):
        
        result, _packettype = self.__Getint32_t(ID)
        if result == False:
            return (False, "")
        else :
            return (True, _packettype)

    # string
    #
    # 4/21/2020 9:36 rewrite __SendString
    #
    def __SendString(self, ID, _string, _packettype):
        
        message = Message(_string)

        if ID == -2:
            size = len(self.__connections)
            for i in range(size):
                self.__connections[i].pm.Append(message.toPacket(_packettype))
        else:
            self.__connections[ID].pm.Append(message.toPacket(_packettype))

        pass

    #
    # 4/21/2020 9:36 rewrite _GetString
    #
    def __GetString(self, ID):
        
        bufferLength = self.__Getint32_t(ID)
        buffer = self.__recvall(ID, bufferLength)
        return buffer
        
        pass

    def __ProcessPacket(self, ID, _packettype):

        if _packettype == PacketType.Instruction:

            pass
        elif _packettype == PacketType.CMDCommand:
            
            pass
        elif _packettype == PacketType.Warning:


            pass
        elif _packettype == PacketType.FileTransferRequestFile:
            
            pass
        elif _packettype == PacketType.FileTransferRequestNextBuffer:
            
            pass
        else:
            
            pass
        pass

    def __HandleSendFile(self, ID):
        pass
  
    def __DisconnectClient(self, ID):
        pass

    # private function


