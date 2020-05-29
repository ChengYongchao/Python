import base64
f=open(r'','rb') #二进制方式打开图文件
resfile=open(r'','wb');
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
resfile.write(ls_f);
#print(ls_f)
