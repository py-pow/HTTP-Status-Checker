import requests,argparse
from rich import print
from rich.table import Table
from rich.console import Console
from rich_argparse import *
console = Console()
banner = """ 
██╗  ██╗████████╗████████╗██████╗     ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██║  ██║╚══██╔══╝╚══██╔══╝██╔══██╗    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████║   ██║      ██║   ██████╔╝    ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██╔══██║   ██║      ██║   ██╔═══╝     ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║   ██║      ██║   ██║         ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝         ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

def parse_args():
    
    parser = argparse.ArgumentParser(formatter_class=RichHelpFormatter, add_help=False,prog="HTTP STATUS CHECHKER")
    parser._optionals.title = f"[py_pow]{banner}  >• Coded by py_pow https://github.com/py-pow"
    parser.add_argument('--help','-h', action='help', default=argparse.SUPPRESS, help="Shows the help page.")
    parser.add_argument('--url','-u', metavar="URL", help="Used to enter URL.")
    parser.add_argument('--list','-l', metavar="List", help="Used to specify a list of URLs.")
    #parser.add_argument('--status','-s', metavar="Status", help="Specifies the Status Code and saves the specified status code as output only.")
    parser.add_argument('--output','-o', default='output.txt', metavar="Output", help="output is used to display default:output.txt")
    args = parser.parse_args()
    return args, parser
args, parser = parse_args()

def oneUrl(url):
 try:
    oneurl = requests.get(args.url,headers=headers)
    
    if oneurl.status_code == 200:
        print(f"[bold green4]Connection Success![/] Status Code: {oneurl.status_code}")
    elif oneurl.status_code == 204:
        print(f"[bold green4]Connection Success! [/] [cornflower_blue] 204 No Content[/]")
    elif oneurl.status_code == 301:
        print(f"[bold green4]Connection Success! [/] [cornflower_blue] 301 Moved Permanently[/]")
    elif oneurl.status_code == 400:
        print(f"[bold red]Connection Error![/] [cornflower_blue] Bad Request [/]Status Code: {oneurl.status_code}")
    elif oneurl.status_code == 401: 
        print(f"[bold red]Connection Error![/] [cornflower_blue] Unauthorized [/]Status Code: {oneurl.status_code}")
    elif oneurl.status_code == 402: 
        print(f"[bold red]Connection Error![/] [cornflower_blue] Payment Required [/]Status Code: {oneurl.status_code}")
    elif oneurl.status_code == 403: 
        print(f"[bold red]Connection Error![/] [cornflower_blue] Forbidden [/]Status Code: {oneurl.status_code}")
    elif oneurl.status_code == 404: 
        print(f"[bold red]Connection Error![/] [cornflower_blue] Not Found [/]Status Code: {oneurl.status_code}")
    elif oneurl.status_code == 405: 
        print(f"[bold red]Connection Error![/] [cornflower_blue] Method Not Allowed [/]Status Code: {oneurl.status_code}")
    elif oneurl.status_code == 406: 
        print(f"[bold red]Connection Error![/] [cornflower_blue] Not Acceptable [/]Status Code: {oneurl.status_code}")
    elif oneurl.status_code == 408: 
        print(f"[bold red]Connection Error![/] [cornflower_blue] Request Timeout [/]Status Code: {oneurl.status_code}")
    elif oneurl.status_code == 414: 
        print(f"[bold red]Connection Error![/] [cornflower_blue] URI Too Long [/]Status Code: {oneurl.status_code}")
    elif oneurl.status_code == 429: 
        print(f"[bold red]Connection Error![/] [cornflower_blue] Too Many Requests [/]Status Code: {oneurl.status_code}")
    elif oneurl.status_code == 500: 
        print(f"[bold red]Connection Error![/] [cornflower_blue] Internal Server Error [/]Status Code: {oneurl.status_code}")
    elif oneurl.status_code == 502: 
        print(f"[bold red]Connection Error![/] [cornflower_blue] Bad Gateway [/]Status Code: {oneurl.status_code}")
    elif oneurl.status_code == 503: 
        print(f"[bold red]Connection Error![/] [cornflower_blue]Service Unavailable [/]Status Code: {oneurl.status_code}")
    elif oneurl.status_code == 504: 
        print(f"[bold red]Connection Error![/] [cornflower_blue] Gateway Timeout [/]Status Code: {oneurl.status_code}")
    else:
        print(f"[bold red]Connection Error![/] [cornflower_blue] Undefined [/]Status Code: {oneurl.status_code}")
        
               
        
 except requests.exceptions.ConnectionError as ConnectionError:
     print(f"[bold red]Connection Error![/] Check the URL Spelling.: ",args.url)
 except requests.exceptions.Timeout:
    print("[bold red]Connection Error![/] Connection Timed Out")
 except requests.exceptions.MissingSchema:
     print("[bold red]Connection Error![/] Invalid URL 'None': No scheme supplied.")  
 except KeyboardInterrupt:
        print("[bold red]Pressed CTRL+C button.[/]")  
        exit()  
     
     
def listUrls(list,output):
    try:
        with open(args.list,'r',encoding='UTF-8') as list:
         # table = Table(expand=True,show_lines=True)

         # table.add_column("URL", style="cyan", no_wrap=True)
          #table.add_column("Status", style="magenta")

          for qaz in list:
              get = requests.get(qaz,headers=headers)
            #  table.add_row(f"{qaz}", f'[blue] Status Code: {get.status_code}[/]')
              if get.status_code == 200:
                 print(f"[bold green4]Connection Success![/] Status Code: {get.status_code}")
              elif get.status_code == 204:
               print(f"[bold green4]Connection Success! [/] [cornflower_blue] 204 No Content[/]")
              elif get.status_code == 301:
               print(f"[bold green4]Connection Success! [/] [cornflower_blue] 301 Moved Permanently[/]")
              elif get.status_code == 400:
                 print(f"[bold red]Connection Error![/] [cornflower_blue] Bad Request [/]Status Code: {get.status_code}")
              elif get.status_code == 401: 
                  print(f"[bold red]Connection Error![/] [cornflower_blue] Unauthorized [/]Status Code: {get.status_code}")
              elif get.status_code == 402: 
                 print(f"[bold red]Connection Error![/] [cornflower_blue] Payment Required [/]Status Code: {get.status_code}")
              elif get.status_code == 403: 
                  print(f"[bold red]Connection Error![/] [cornflower_blue] Forbidden [/]Status Code: {get.status_code}")
              elif get.status_code == 404: 
                 print(f"[bold red]Connection Error![/] [cornflower_blue] Not Found [/]Status Code: {get.status_code}")
              elif get.status_code == 405: 
                 print(f"[bold red]Connection Error![/] [cornflower_blue] Method Not Allowed [/]Status Code: {get.status_code}")
              elif get.status_code == 406: 
                 print(f"[bold red]Connection Error![/] [cornflower_blue] Not Acceptable [/]Status Code: {get.status_code}")
              elif get.status_code == 408: 
                 print(f"[bold red]Connection Error![/] [cornflower_blue] Request Timeout [/]Status Code: {get.status_code}")
              elif get.status_code == 414: 
                 print(f"[bold red]Connection Error![/] [cornflower_blue] URI Too Long [/]Status Code: {get.status_code}")
              elif get.status_code == 429: 
                 print(f"[bold red]Connection Error![/] [cornflower_blue] Too Many Requests [/]Status Code: {get.status_code}")
              elif get.status_code == 500: 
                 print(f"[bold red]Connection Error![/] [cornflower_blue] Internal Server Error [/]Status Code: {get.status_code}")
              elif get.status_code == 502: 
                 print(f"[bold red]Connection Error![/] [cornflower_blue] Bad Gateway [/]Status Code: {get.status_code}")
              elif get.status_code == 503: 
                 print(f"[bold red]Connection Error![/] [cornflower_blue]Service Unavailable [/]Status Code: {get.status_code}")
              elif get.status_code == 504: 
                 print(f"[bold red]Connection Error![/] [cornflower_blue] Gateway Timeout [/]Status Code: {get.status_code}")
              else:
                  print(f"[bold red]Connection Error![/] [cornflower_blue] Undefined [/]Status Code: {get.status_code}")
              with open(args.output,'a',encoding='UTF-8') as saveOutput:                    
                    saveOutput.write(qaz.replace('\n','')  +" : "+str(get.status_code))
                    saveOutput.write('\n')
                    saveOutput.close()
          
         # console.print(table)
           
    except FileNotFoundError:
      print(f"[bold red]File Not Found[/]")
    except requests.exceptions.ConnectionError as ConnectionError:
      print(f"[bold red]Connection Error![/] Check the URL Spelling.: ",qaz)
    except requests.exceptions.Timeout:
     print("[bold red]Connection Error![/] Connection Timed Out")
    except requests.exceptions.MissingSchema:
     print("[bold red]Connection Error![/] Invalid URL : Please edit!")  
    except KeyboardInterrupt:
        print("[bold red]Pressed CTRL+C button.[/]")  
        exit()       
              
              
              
              
             
             

   

def main():
    if  args.url != None and args.list != None:
         print("[bold red]Error! Both URL and LIST parameters cannot be selected. Choose One![/]")   
         exit()
    elif args.url != None and args.list == None:
         oneUrl(args.url)
    
    elif args.list != None and args.url == None:
        
        listUrls(args.list,args.output)
         
    

   
main()
    