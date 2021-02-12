import os
from os import environ
from dhooks import Webhook
import datetime
import time
#link webhooka
hook = Webhook(environ['kluczyk'])
x=1

#tablica lekcji
lekcja = ["Aplikacje internetowe",
"Bazy danych",
"Historia i społeczeństwo",
"Język angielski",
"Język niemiecki",
"Język polski",
"Matematyka",
"Pracownia aplikacji internetowych",
"Pracownia baz danych",
"Pracownia projektów internetowych",
"Pracownia sieci komputerowych i sieciowych systemów operacyjnych",
"Praktyka zawodowa w szkole",
"Programowanie",
"Projekty internetowe",
"Sieci komputerowe i sieciowe systemy operacyjne",
"Wychowanie fizyczne",
"Zajęcia z wychowawcą"
]
#wysylanie odpowiednej zmiennej webhookiem
def wyslanie(x):
    x
   
    hook.send(f'{d.hour+1}godzina,{d.minute} minuta ,{lekcja[x]} <@&803931420664922152>')
    

def wyslanie2(x):
    x
    
    hook.send(f'{d.hour+1}godzina,{d.minute} minuta ,{lekcja[x]} <@&803931239617789962>')
    time.sleep(60)






#wotek i dzialania sprwdznie godziny

def poniedzialek():
    if d.hour == 7 and d.minute == 0:
        wyslanie(4)
        wyslanie2(7)
    elif d.hour == 7 and d.minute == 55:
        wyslanie(7)
        wyslanie2(4)
    elif d.hour == 8 and d.minute == 45:
        wyslanie(11)
        wyslanie2(3)

    elif d.hour == 9 and d.minute ==50:
        wyslanie(9)
        wyslanie2(12)

    elif d.hour == 10 and d.minute ==45:
        wyslanie(0)
        wyslanie2(0)

    elif d.hour == 11 and d.minute ==35:
        wyslanie(3)
        wyslanie2(7)

    elif d.hour == 12 and d.minute ==25:
        wyslanie(9)
        wyslanie2(3)
    elif d.hour == 13 and d.minute ==15:
        wyslanie(5)
        wyslanie2(5)
    
        



def wtorek():
    if d.hour == 7 and d.minute == 0:
        wyslanie(1)
        wyslanie2(1)
    elif d.hour == 7 and d.minute == 55:
        wyslanie(1)
        wyslanie2(1)
    elif d.hour == 8 and d.minute == 45:
        wyslanie(6)
        wyslanie2(6)

    elif d.hour == 9 and d.minute ==50:
        wyslanie(8)
        wyslanie2(9)

    elif d.hour == 10 and d.minute ==45:
        wyslanie(8)
        wyslanie2(9)
    elif d.hour == 11 and d.minute ==35:
        wyslanie(7)
        wyslanie2(11)
    elif d.hour == 12 and d.minute ==25:
        wyslanie(3)
        wyslanie2(11)
    elif d.hour == 13 and d.minute ==15:
        wyslanie(5)
        wyslanie2(5)


def sroda():
    if d.hour == 7 and d.minute == 0:
        wyslanie(11)
        time.sleep(60)
    elif d.hour == 7 and d.minute == 55:
        wyslanie(6)
        wyslanie2(6)

    elif d.hour == 9 and d.minute ==50:
        wyslanie(6)
        wyslanie2(6)

    elif d.hour == 10 and d.minute ==45:
        wyslanie(14)
        wyslanie2(14)

    elif d.hour == 11 and d.minute ==35:
        wyslanie(5)
        wyslanie2(5)

    elif d.hour == 12 and d.minute ==25:
        wyslanie(3)
        wyslanie2(8)
    elif d.hour == 13 and d.minute ==15:
        wyslanie(3)
        time.sleep(60)

def czwartek():
    if d.hour == 7 and d.minute == 0:
        wyslanie(10)
        wyslanie2(10)
    elif d.hour == 7 and d.minute == 55:
        wyslanie(12)
        wyslanie2(10)
    elif d.hour == 8 and d.minute == 45:
        wyslanie(14)
        wyslanie2(14)

def piatek():
    if d.hour == 7 and d.minute == 55:
        wyslanie2(8)
    elif d.hour == 8 and d.minute == 45:
        wyslanie(6)
        wyslanie2(6)

    elif d.hour == 9 and d.minute ==50:
        wyslanie(2)
        wyslanie2(2)

    elif d.hour == 10 and d.minute ==45:
        wyslanie(16)
        wyslanie2(16)

    elif d.hour == 11 and d.minute ==35:
        wyslanie(10)
        wyslanie2(3)

    elif d.hour == 12 and d.minute ==25:
        wyslanie(6)
        wyslanie2(6)
    elif d.hour == 13 and d.minute ==15:
        wyslanie2(3)
 


#pętla sprawdza godzine
while True:
    d = datetime.datetime.today()
    
    time.sleep(3)
    if datetime.datetime.now().weekday() == 0:
        poniedzialek()
    elif datetime.datetime.now().weekday() == 1:
        wtorek()
    elif datetime.datetime.now().weekday() == 2:
        sroda()
    elif datetime.datetime.now().weekday() == 3:
        czwartek()
    elif datetime.datetime.now().weekday() == 4:
        piatek()



