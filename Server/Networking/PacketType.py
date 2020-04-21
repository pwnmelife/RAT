from enum import Enum


class PacketType(Enum):
    Instruction = 0
    CMDCommand = 1
    Warning = 2
    ChatMessage = 3
    FileTransferRequestFile = 4
    FileTransfer_EndOfFile = 5
    FileTransferByteBuffer = 6
    FileTransferRequestNextBuffer = 7