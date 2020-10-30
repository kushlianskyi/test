#!/usr/bin/env python

import paramiko
import sys, os, string, threading

#user-selected command
cmd = "w"

def command(host):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username='ubuntu', password='PASSWORD')

    stdin, stdout, stderr = client.exec_command(cmd)

    for line in stdout:
        print line.strip('\n')
    client.close()

def main():
    hosts = sys.argv[1].split(",")
    threads = []
    for h in hosts:
        t = threading.Thread(target=command, args=(h,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

main()
