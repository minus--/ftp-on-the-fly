__author__ = 'Amine Kerkeni'

from ftp_utils import *
from time import time
import config
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--src", help="set the source file")
parser.add_argument("-d", "--dst", help="set the destination file")

args = parser.parse_args()

if args.src and args.dst:
    from_file_name = args.src
    to_file_name = args.dst
    try:
        path = '/'
        from_ftp = ftplib.FTP(config.from_server_ip, config.from_server_user, config.from_server_password)
        to_ftp = ftplib.FTP(config.to_server_ip, config.to_server_user, config.to_server_password)
        from_ftp.cwd(path)
        to_ftp.cwd(path)
        print(from_file_name, " -> ", to_file_name)
        start = time()
        copy_file(from_ftp, to_ftp, from_file_name, to_file_name)
        elapsed = time() - start
        print('%d seconds' % elapsed)
    except Exception as ex:
        print( 'Error transferring file {file_name}to destination server : {error}'.format(
            file_name=from_file_name, error=ex))
    finally:
        from_ftp.quit()
        to_ftp.quit()