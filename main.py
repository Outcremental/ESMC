print("Loading...")
import sys
import os
from time import sleep
os.system('cls')
settings = "settings.esmc"
ngrokset = "ngrokset.esmc"
regionfile = "region.esmc"
with open(str(settings)) as f:
    isngrokset = f.read()
if isngrokset == "false":
  print("Looks like you don't have ngrok auth token set. Go to https://dashboard.ngrok.com/get-started/setup to get one")
  print("When you get the token copy it and put it here V")
  ngroktoken = input("Token: ")
  f = open(str(settings),"w")
  f.write("true")
  f.close()
  with open(str(ngrokset)) as f:
    variablefortrash = f.read()
  f = open(str(ngrokset),"w")
  f.write(ngroktoken)
  f.close()
  os.system('cls')
  print("Type the region you are in")
  with open("regions") as f:
    licensetext = f.read()
  print(licensetext)
  regionvariabletosave = input("region: ")
  with open(str(regionfile)) as f:
    variablefortrash = f.read()
  f = open(str(regionfile),"w")
  f.write(regionvariabletosave)
  f.close()
  print("Token saved for next time")
  print("Restarting...")
  sleep(2)
  os.system("ESMC.exe")
  sys.exit()
if isngrokset == "true":
  print("ngrok token found continuing...")
  sleep(1)
  os.system('cls')
  print("Do you want to have a GUI?")
  choosegui = input("[y/n]:")
  if choosegui == "y":
    f = open("argument.esmc","w")
    f.write("")
    f.close()
  elif choosegui == "n":
    f = open("argument.esmc","w")
    f.write("nogui")
    f.close()
  os.system('cls')
  print("OK now I need to know how much ram do you want to give the server")
  print("WARNING")
  print("Do NOT overstimate the power of your pc recommended is 1GB to 2GB of ram")
  print("type ONLY the NUMBER")
  ram = input("how much? ")
  os.system('cls')
  print("OK starting server")
  sleep(2)
  os.system('cls')
  with open(str(ngrokset)) as f:
    ngroktokens = f.read()
  with open(str(regionfile)) as f:
    regioncode = f.read()
  with open(str("ram.esmc")) as f:
    trashram = f.read()
  f = open(str("ram.esmc"),"w")
  f.write(ram)
  f.close()
  os.startfile("sw.exe")
  os.system("ngrok authtoken " + ngroktokens)
  os.system("ngrok tcp -region="+ regioncode +" 25565")