
import zipfile 
from time import sleep  
from datetime import datetime 
from tqdm import tqdm 
from rich.console import Console 
from logo import logo
console = Console()

def escreval(txt): 
    tam = len(txt) + 6 
    print("="*tam)
    print(f"   {txt}")
    print("="*tam) 


def Zip_crack(): 
    logo.logoo()
    word_list = console.input("[green][+] Informe o nome de sua Wordlist.txt:[/] ") 
    if word_list == "": 
        console.print("[red][ERRO] Você não digitou nada!![/]")
        exit()
    
    file_zip = console.input("[green][+] Informe o nome do seu arquivo.zip:[/] ")

    if file_zip == "": 
        console.print("[red][ERRO] Você não digitou nada!![/]")
        exit() 
    try:
        file_zip = zipfile.ZipFile(file_zip)
        n_words = len(list(open(word_list,"r",encoding='cp437'))) 
        time = datetime.now()
        print("Testando combinações...")
        
        
        
        
    except FileNotFoundError as e: 
        console.print("[red][ERRO] Arquivo não Encontrado!![/]")
        exit()


    with open(word_list,"r",encoding='cp437') as wordlist: 
        for word in wordlist: 
          try:
              file_zip.extractall(pwd=word.strip())
             
              

        
          except: 
               continue 
        
          else: 
                 print(" ")
                 escreval("Password Quebrado")
                 console.print(f"[+] Password Encontrado: [green]{word.strip()}[/]",style="#9400D3") 
                 console.print("[+] Começou ás: ",time,style="#9400D3") 
                 console.print("[+] Terminou ás: ", datetime.now(),style="#9400D3")
                 console.print("[+] Tipo de Arquivo: [green]Zip[/]",style="#9400D3")
                 console.print(f"[+] Total de Tentativas: [green]{n_words}[/]",style="#9400D3")
                 print('='*30)
                 print(" ")
                 exit(0) 
        console.print("[red][-] Password não Encontrado!![/]") 