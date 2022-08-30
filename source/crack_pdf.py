import pikepdf 
from tqdm import tqdm  
from datetime import datetime 
from time import sleep 
from rich.console import Console 
from logo import logo
console = Console()


def escreval(txt): 
    tam = len(txt) + 7
    print("="*tam)
    print(f"   {txt}")
    print("="*tam) 

def Pdf_decrypt(): 
    logo.logoo()
    word_list = console.input("[green][+] Informe o nome de sua Wordlist.txt:[/]  ") 
    if word_list == "": 
            console.print("[red][ERRO] Você não digitou nada![/]")
            exit()
    

    file_pdf = console.input("[green][+] Informe o nome de sua Arquivo.pdf:[/] ") 

    if file_pdf == "": 
         console.print("[red][ERRO] Você não digitou nada![/]")
         exit()
        
    try:

        passwords = [line.strip() for line in open(word_list,"r",encoding='cp437')] 
        n_words = len(passwords)
        time = datetime.now()
        print("Testando combinações...")

       
    except FileNotFoundError:  
        console.print("[red][ERRO] Arquivo não Encontrado!![/]")
        exit(0)
        

    for password in passwords: 
      try:
          with pikepdf.open(file_pdf,password=password) as pdf: 

                 print(" ")
                 escreval("Password Quebrado")
                 console.print(f"[+] Password Encontrado: [green]{password}[/]",style="#9400D3") 
                 console.print(f"[+] Total de tentativas: [green]{n_words}[/]",style="#9400D3") 
                 console.print(f"[+] Começou ás: {time} ",style="#9400D3")
                 console.print("[+] Terminou ás: ",datetime.now(),style="#9400D3")
                 console.print("[+] Tipo de Arquivo: [red]PDF[/]",style="#9400D3")
                 print('='*30)
                 print(" ")                   
                 exit(0) 
      except pikepdf._qpdf.PasswordError as e:        
               continue 
        
      


