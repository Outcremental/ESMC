import os
with open(str("ram.esmc")) as f:
      ram = f.read()
with open(str("argument.esmc")) as f:
      gui = f.read()
argument = int(ram) * 2
os.system("java -Xmx"+ str(argument) +"G -Xms"+ ram +"G -XX:MaxHeapSize=1G -jar server.jar " + gui)