import pysftp

host = '127.0.0.2'
userName = 'dilbert'
passWord = 'dogbert'
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
localPATH = ''
remotePATH = ''

with pysftp.Connection(host,username=userName,password=passWord,cnopts=cnopts) as sftp:
	sftp.put_r(localPATH, remotePATH, preserve_mtime=True)
