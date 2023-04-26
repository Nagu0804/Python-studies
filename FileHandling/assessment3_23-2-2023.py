#assessment3 23-2-2023
f=open('sample_content.txt','r')
f1=f.read()
u_count=0
d_count=0
for i in f1:
    if i.isupper():
        u_count+=1
    elif i.isdigit():
        d_count+=1

print('The count of uppercase is:',u_count)
print('The count of digits is:',d_count)

        
        
    
