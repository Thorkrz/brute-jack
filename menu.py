from rich.console import Console 
from source import crack_pdf,crack_zip,decrypt_md5
import os
from time import sleep


def escreval(txt): 
    tam = len(txt) + 6 
    print("="*tam)
    print(f"   {txt}")
    print("="*tam) 


console = Console() 
def menu():
#Logo
    console.print('''\n 

▄▄▄██▀▀▀▄▄▄       ▄████▄   ██ ▄█▀   ▓█████   ██████ ▄▄▄█████▓ ██▀███   ██▓ ██▓███   ▄▄▄      ▓█████▄  ▒█████   ██▀███  
   ▒██  ▒████▄    ▒██▀ ▀█   ██▄█▒    ▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▓██▒▓██░  ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒
   ░██  ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░    ▒███   ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▒██  ▀█▄  ░██   █▌▒██░  ██▒▓██ ░▄█ ▒
▓██▄██▓ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄    ▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██░▒██▄█▓▒ ▒░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░▒██▀▀█▄  
 ▓███▒   ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄   ░▒████▒▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░██░▒██▒ ░  ░ ▓█   ▓██▒░▒████▓ ░ ████▓▒░░██▓ ▒██▒
 ▒▓▒▒░   ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒   ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ▒ ░▒░    ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░    ░ ░  ░░ ░▒  ░ ░    ░      ░▒ ░ ▒░ ▒ ░░▒ ░       ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░
 ░ ░ ░    ░   ▒   ░        ░ ░░ ░       ░   ░  ░  ░    ░        ░░   ░  ▒ ░░░         ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░░   ░ 
 ░   ░        ░  ░░ ░      ░  ░         ░  ░      ░              ░      ░                 ░  ░   ░        ░ ░     ░     
                  ░                                                                            ░                                         
 Code By: [white]Thor_Kryp[/] ''',style="#682cac bold") 



    console.print('______________________________________')
    console.print('|[[red]1[/]] [white]Quebrar Password de arquivo.zip[/] | ')
    console.print('|[[red]2[/]] [white]Quebrar Password de arquivo.pdf[/] |') 
    console.print('|[[red]3[/]] [white]Decrypt Hash MD5[/]                |') 
    console.print('|[[red]4[/]] [white]Wordlists Disponíveis[/]           |')
    console.print('|____________________________________|') 
    console.print('|[[red]0[/]] [white]Sair do Programa[/]                |')
    console.print('|____________________________________|')
            
    try:
       opcao = int(input("==> "))  
    except ValueError  as erro: 
        console.print("[red][ERRO] Digite um número, não letra![/]")
        print("Deseja retornar ao menu? [Y/N]") 
        opca = str(input("==> ")).upper()

        if opca == "": 
              console.print("[red][ERRO] Você não digitou nada!![/]")

        if opca == "Y":
               os.system("cls || clear")  
               return menu() 

        elif opca == "N": 
                print("Você saiu do programa...")
                exit(0)
  


    if opcao == 1: 
        
        os.system("cls || clear")
        os.system("cls || clear")
        crack_zip.Zip_crack()
 
        

    elif opcao == 2: 
        os.system("cls || clear")
        os.system("cls || clear")
        
        crack_pdf.Pdf_decrypt()

    elif opcao == 3: 
            os.system("cls || clear")
            os.system("cls || clear")
            decrypt_md5.Decrypt_hash()
                

    
    elif opcao == 4: 
    
        escreval("Wordlists Ativas")

        console.print('[red]1[/] - [pink]rocky.txt[/]\n[red]2[/] - [pink]aizen.txt[/]',style="#FF00FF")

        console.print("Deseja retornar ao menu? [[red]Y[/]/[red]N[/]]",style="#B0E0E6") 
        try:
          opca = str(input("==> ")).upper()
        except ValueError: 
            console.print("[red][ERRO] Digite um número, não letra![/]")
            console.print("Deseja retornar ao menu? [[red]Y[/]/[red]N[/]]",style="#7B68EE") 
            opca = str(input("==> ")).upper()


        if opca == "": 
            console.print("[red][ERRO] Você não digitou nada!![/]")

        if opca == "Y":
            os.system("cls || clear")  
            return menu() 
        elif opca == "N": 
            print("Você saiu do programa...")
            exit(0)

        
    
    elif opcao == 0: 
        print("Saindo do Programa....") 
        sleep(1.6)
        exit()

    else:
        console.print('[red]Opção inválida[/]')
        exit()
     

menu()
