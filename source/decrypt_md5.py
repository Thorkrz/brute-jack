import hashlib 
from datetime import datetime 
from time import sleep 
from tqdm import tqdm
from rich.console import Console 
from logo import logo
console = Console()

def escreval(txt): 
    tam = len(txt) + 6 
    print("="*tam)
    print(f"   {txt}")
    print("="*tam) 


def Decrypt_hash(): 
    logo.logoo()
    hash = console.input("[green][+] Digite a Hash MD5 para ser Decryptada:[/] ") 
    if hash == "": 
        print("[ERRO] Você não digitou nada!")
        exit()

    word_list = console.input("[green][+] Informe o nome de sua Wordlist.txt:[/] ")
    if word_list == "":
        print("[ERRO] Você não digitou nada!")
        exit() 
    
    try:

        pass_file = open(word_list,"r",encoding='cp437')
        n_words = len(list(open(word_list,"r",encoding='cp437'))) 

        
        console.print("[white]Testando combinações...[/]")
       
        time = datetime.now()
        
        
       
    except FileNotFoundError as erro: 
        console.print("[red][ERRO] Arquivo não Encontrado!![/]")
        exit() 

    
    for word in pass_file: 
        
        codificador = hashlib.md5(word.encode("UTF-8").strip()).hexdigest() 

        if hash == codificador: 
             print(" ")
             escreval("Hash Decrypt")
             console.print(f"[+] Hash MD5 Decrypt: [green]{word}[/]",style="#9400D3") 
             console.print("[+] Começou ás:", time,style="#9400D3")
             console.print("[+] Terminou ás:", datetime.now(),style="#9400D3") 
             console.print("[+] Tipo de Hash: [red]MD5[/]",style="#9400D3")
             console.print(f"[+] Total de Combinações testadas foram: [green]{n_words}[/]",style="#9400D3")
             print("="*30) 
                     
             print(" ")
             exit(0) 
        else:
                console.print(f"[red][-]Não é essa: {word}[/] \n[green](Caso o programa pare é devido a hash não está na wordlist)[/]")
                    


