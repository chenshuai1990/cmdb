#coding:utf-8

import paramiko

class sshServer:
	def __init__(self,hostname,username,password):
		self.ssh  = paramiko.SSHClient()


		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		self.ssh.connect  (
			hostname = hostname,
			username = username,
			password = password
			)
	def connect(self):
		channel = self.ssh.invoke_shell() #生成在当前堡垒机上执行的代码的交互式
		channel.settimeout(1) #定义每条命令执行等待的时间 单位是秒
		while True:
			try:
				recvdata = channel.recv(99999)
				if recvdata:
					printData = recvdata.splitlines()[:-1]
					if isinstance(printData,str):
						print printData
					elif isinstance(printData,list):
						print "\n".join(printData)
					else:
						continue
				else:
					continue
			except:
				control = raw_input(recvdata.splitlines()[-1])
				if control == "exit":
					break
				else:
					channel.send(control+"\n")
		self.ssh.close()


if __name__ == "__main__":
	p = sshServer("192.168.0.104","root","123456")
	p.connect()