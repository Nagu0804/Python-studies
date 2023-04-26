#assessment5 23-2-2023
f=open('NEWS_content.txt','w')
fw=f.write('1.chennai is capital of tamilnadu\n')
fw=f.write('2.It is aslo one of the most famous place in india\n')
fw=f.write('3.It has the 2nd largest beach in the world\n')
f.close()
#read the new file
f1=open('NEWS_content.txt','r')
fr=f1.read()
print(fr)


print('Process over')
