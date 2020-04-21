from multiprocessing import Lock
from Packet import Packet
import queue

class PacketManager:

    def __init__(self):
        self.__queue_packets = queue.Queue()

        pass

    def Clear(self):
        mutex = Lock()
        mutex.acquire()
        length = self.__queue_packets.qsize()
        for i in range(length):
            self.__queue_packets.get()
        mutex.release()
        


    def HasPendingPackets(self):

        return self.__queue_packets.qsize() > 0

    def Append(self, p):

        lockMutex = Lock()
        lockMutex.acquire()
        self.__queue_packets.put(p)
        lockMutex.release()
        pass

    def Retrieve(self):
        mutex = Lock()
        mutex.acquire()
        p = self.__queue_packets.get()
        return p