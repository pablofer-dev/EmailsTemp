import requests
import time
from rich.console import Console


class OneSecMail:
    def __init__(self, customDomain = False, domain = None):
        self.console = Console()
        self.email = None
        self.login = None
        self.domain = domain
        self.id = None
        self.message = None
        self.customDomain = customDomain
        self.customDomainEmail = None
        self.subject = None
        self.date = None
        self.textBody = None
        
    def generate_email(self):
        url = f"https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.email = data[0]
            self.__separate_email()
            self.check_email()
            
        else:
            return None
    
    def __separate_email(self):
        if self.email:
            if self.customDomain:
                self.login = self.email.split('@')[0]
                self.domain = 'laafd.com'
                self.customDomainEmail = f"{self.login}@{self.domain}"
            else:
                self.login, self.domain = self.email.split('@')
                
            return self.login, self.domain
        else:
            return None, None
    
    def check_email(self):
        url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={self.login}&domain={self.domain}"
        while True:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data:
                    self.id = data[0]['id']
                    self.get_email()
                    return self.id 
                else:
                    if self.customDomain:
                        self.console.print(f"Waiting for email: [white]{self.customDomainEmail}[/white]", end="\r", style="yellow")
                    else:
                        self.console.print(f"Waiting for email: [white]{self.email}[/white]", end="\r", style="yellow")
            time.sleep(3)  # Espera 5 segundos antes de revisar nuevamente
        
    def get_email(self):
        url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={self.login}&domain={self.domain}&id={self.id}"
        response = requests.get(url)
        if response.status_code == 200:
            self.message = response.json()
            self.subject = self.message['subject']
            self.date = self.message['date']
            self.textBody = self.message['textBody'].rstrip('\n')
            
            return self.message
        else:
            return None