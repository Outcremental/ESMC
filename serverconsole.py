import os
with open(str("ram.esmc")) as f:
      ram = f.read()
os.system("java -Xmx"+ ram +"G -Xms"+ ram +"G -jar server.jar nogui")