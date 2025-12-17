import paramiko

session=paramiko.SSHClient() #default method here
session.set_missing_host_key_policy(paramiko.autoaddpolicy)  #auto add policy

#or in case of private keys
key_file=paramiko.RSAKey.from_private_key_file("filepath")
session.connect(hostname=host,user_name="",password="",port=22,Pkey=key_file)

session.connect(hostname=host,user_name="",password="",port=22)
stdin,stdout,stderr= session.exec_command("ls -l")

output=stdout.read().decode()
input=stdin.read.decode()
error=stdout.read().decode()

if error:
  with open("error_log.txt","w") as f:
    f.write(error)

-----------------------------------------------------------------------------
