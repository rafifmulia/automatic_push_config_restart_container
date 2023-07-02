import sys
import os
import json
import paramiko
import re
import traceback
import datetime
from watchfiles import run_process

hostname = sys.argv[1]
port = int(sys.argv[2])
username = sys.argv[3]
path_pkey = sys.argv[4]
watchdir = sys.argv[5]

def stdout(output):
  filelog = open("./logs/app.log", "a")
  now = datetime.datetime.now()
  filelog.write(f"{now}|{output}\n")
  filelog.close()

def stderr(output):
  filelog = open("./logs/err.log", "a")
  now = datetime.datetime.now()
  filelog.write(f"START - {now}\n")
  filelog.write(f"{output}\n")
  filelog.write(f"END - {now}\n")
  filelog.close()

def config_changed():
  try:
    # changes will be an empty list "[]" the first time the function is called
    changes = json.loads(os.getenv('WATCHFILES_CHANGES'))
    print('config_changed called due to changes:', changes)
    for change in changes:
      if (change[0] == 'modified' and re.search("config/url_hub/.*",change[1]) != None):
        push_config(hostname, port, username, localpath=change[1], remotepath='/var/www/url_hub/.env')
        restart_container(hostname, port, username, container="url_hub-dev01")
  except Exception as e:
    err = traceback.format_exc()
    stderr(err)

def push_config(hostname, port, username, localpath, remotepath):
  try:
    stdout("changes detected on "+localpath)
    transport = paramiko.Transport((hostname, port))
    pk = paramiko.Ed25519Key.from_private_key(open(path_pkey))
    stdout("try to connect transport layer for push configuration using sftp")
    transport.connect(username=username, hostkey=None, pkey=pk)

    sftp_client = paramiko.SFTPClient.from_transport(transport)
    sftp_client.put(localpath=localpath, remotepath=remotepath)
    stdout("success push configuration")
    sftp_client.close()

    transport.close()
  except Exception as e:
    err = traceback.format_exc()
    stderr(err)

def restart_container(hostname, port, username, container):
  try:
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.WarningPolicy())
    
    stdout("try to connect transport layer for restart container using ssh")
    ssh_client.connect(hostname=hostname, port=port, username=username)
    ssh_client.exec_command(f"docker container restart {container}")
    stdout("success restart container")
  except Exception as e:
    err = traceback.format_exc()
    stderr(err)

if __name__ == '__main__':
  try:
    run_process(watchdir, target=config_changed)
  except Exception as e:
    err = traceback.format_exc()
    stderr(err)