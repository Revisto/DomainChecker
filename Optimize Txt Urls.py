file1 = open('URL2.txt', 'r') 
Lines = file1.readlines() 
  
l=[]
# Strips the newline character 
for line in Lines: 
    l.append(line.replace("\n",""))
    
with open("URLS2.py","w") as f:
    f.write(str(l))