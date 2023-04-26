#assessment4 23-2-2023
f=open('sample_content.txt','r')
f1=f.read()
li=['A','a','E','e','I','i','O','o','U','u']
count=0
for i in f1:
    if i in li:
        count+=1
        
print(f1)
print('The count of vowels is:',count)
