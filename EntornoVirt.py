""" import requests

#r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
r = requests.get('https://jsonplaceholder.typicode.com/posts/3', auth=('user', 'pass'))
r.status_code
print(r.text)
print(r.json()) """


 #Ejercicio 1. Translate (pag71)
"""from translate import Translator
translator= Translator(to_lang="es")
translation= translator.translate("what are you doing? ")
print(translation)
 """
 
#Ejercicio2. Barra de progreso (pip install tqdm)
"""from tqdm import tqdm
import time
for _ in tqdm(range(10)):
    time.sleep(2)
 """

# Validar email
""" from email_validator import validate_email, EmailNotValidError

email = "my+address@example.org"
try:

  # Check that the email address is valid. Turn on check_deliverability
  # for first-time validations like on account creation pages (but not
  # login pages).
  emailinfo = validate_email(email, check_deliverability=False)

  # After this point, use only the normalized form of the email address,
  # especially before going to a database query.
  email = emailinfo.normalized
  if  EmailNotValidError:
    print("El email es correcto")

except EmailNotValidError as e:

  # The exception message is human-readable explanation of why it's
  # not a valid (or deliverable) email address.
  print(str(e))
 """
# tu dni es correcto?
""" from typing import List
from spanish_dni.dni import DNI
from spanish_dni.exceptions import NotValidDNIException
from spanish_dni.validator import validate_dni


my_dnis: List[str] = [
    "23414538D",
    "Y2853959H",
    "23418D",
    "U2853959H",
    "23414538T",
]


for dni in my_dnis:
    valid = True
    try:
        dni_parsed: DNI = validate_dni(dni)
        print(f"DNI {dni} is type {dni_parsed.dni_type}")
    except NotValidDNIException:
        valid = False
        print(f"DNI {dni} is not valid") """

#isbn(codigo de barras!)
""" from is_isbn.is_isbn import is_isbn
print(is_isbn('978-1449330729'))
 """
#Program to create a countdown timer(falta por terminar de copiar de la pagina 72)
import time

def countdown(time_sec):
    while time_sec:
        mins, secs= divmod(time_sec,60)
        timeformat= '{:02d}:{:02d}'.format(mins, secs)
 

#Ventana de mensaje, una con bucle y otra sin bucle
"""from plyer import notification
notification.notify(title='Hola', message='nos quedan 15 minutos', timeout=10)"""

#con bucle
""" from plyer import notification
import time
while True:
    notification.notify(title='Hola', message='nos quedan 15 minutos', timeout=10)

    time.sleep(20)
 """