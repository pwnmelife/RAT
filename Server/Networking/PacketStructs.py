from Packet import Packet
from socket import htonl

class Message:

    def __init__(self, s):

        self.__message = s
    
    def toPacket(self, _packettype):

        packetSize = 4 + len(self.__message)
        buffer = htonl(_packettype)
        buffer += htonl(len(self.__message))
        buffer += self.__message

        p = Packet(buffer, packetSize)
        return p