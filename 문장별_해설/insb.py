import sys
f,k,add=sys.argv[1],int(sys.argv[2]),sys.argv[3]
L=[l for l in open(f,encoding='utf-8').read().split('\n') if l.strip()]
A=[l for l in open(add,encoding='utf-8').read().split('\n') if l.strip() and l.strip()!='EOF']
for l in A: assert len(l.split(' ¦ '))==7,(l[:60],len(l.split(' ¦ ')))
pos=len(L)-k
L[pos:pos]=A
open(f,'w',encoding='utf-8').write('\n'.join(L)+'\n')
print(len(A),'inserted; total',sum(1 for l in L if '¦' in l))
