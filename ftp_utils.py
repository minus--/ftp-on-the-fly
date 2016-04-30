__author__ = 'Amine Kerkeni'
import ftplib


def copy_file(from_ftp, to_ftp, source, destination):
    """
    Low level routine that copy files between ftp servers
    """
    from_Sock = from_ftp.transfercmd('RETR %s' % source)
    to_Sock = to_ftp.transfercmd('STOR %s' % destination)
    state = 0
    while 1:
        block = from_Sock.recv(1024)
        if len(block) == 0:
            break
        state += len(block)
        while len(block) > 0:
            sentlen = to_Sock.send(block)
            block = block[sentlen:]
    print(state, "bytes transfered")
    from_Sock.close()
    to_Sock.close()


