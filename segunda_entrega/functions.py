import crcmod
import struct

def converterToTxt(username, texto, isServer = False):

    def calcularChecksum(data:bytes):
     return checksum


def criarPacote(msg:bytes, seq:int, ack:int):

    # Payload da mensagem a ser enviada
    payload = msg

    # Header sem o Checksum 
    pseudoHeader = struct.pack('!BB', seq, ack)

    # Calculando o checksum com as informações do cabeçalho e o payload
    checksum = calcularChecksum(pseudoHeader+payload)

    # Header de 4 Bytes (Seq - 1 Byte, Ack - 1 Byte, Checksum - 2 Bytes)
    header = struct.pack('!BBH', seq, ack, checksum)
    
    # Criando o pacote (Cabeçalho + Dados)
    pacote = header+payload

    return pacote  # Retornando o pacote já pronto para envio


def isCorrupt(header:bytes, payload:bytes):

    seq, ack, checksum = struct.unpack('!BBH', header)

    checksumChecked = calcularChecksum(struct.pack('!BB', seq, ack)+payload)

    return checksumChecked != checksum

def makeAck(seq, ack):
    # Cria um pacote sem mensagem (S/payload) com o ACK do pacote confirmado
    return criarPacote(''.encode("ISO-8859-1"), seq, ack)