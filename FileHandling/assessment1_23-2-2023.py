#23-2-2023 1st assessmennt
f=open('sample_content.txt','r')
f1=f.read()
count=0
for i in f1:
    if i=='a':
        count=count+1
print(f1)
print('The count of letter \'a\' is',count)
f.close()

    
