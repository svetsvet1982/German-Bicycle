import sys
f,line,add=sys.argv[1],int(sys.argv[2]),sys.argv[3]
L=open(f,encoding='utf-8').read().split('\n')
A=[l for l in open(add,encoding='utf-8').read().split('\n') if l.strip() and l.strip()!='EOF']
for l in A: assert len(l.split(' ¦ '))==7,(l[:60],len(l.split(' ¦ ')))
L[line:line]=A
open(f,'w',encoding='utf-8').write('\n'.join(L))
print(len(A),'inserted')
