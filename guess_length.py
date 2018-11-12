import re
from tabulate import tabulate
import itertools
import collections
cipher=""#上边那一坨
cipher="".join(re.findall(r"[a-z]",cipher))
#计算距离的2到20内的因数
def get_fact(n):
	result=[]
	for i in range(2,21):
		if(int(n/i)==n/i):
			result.append(i)
	return result

#计算重复序列的各种组合的距离
def calc_space(str,sub_str):
	n=[]
	for i in range(0,len(cipher)-(len(cipher)+2)%3):
		if sub_str==str[i:i+3]:
			n.append(i)
	n=(itertools.combinations(n,2))
	n=[abs(i[0]-i[1]) for i in n]
	n=set(n)
	return (n if n!=set([]) else 0)

l=[]
seqs=[cipher[i:i+3] for i in range(0,len(cipher)-(len(cipher)+2)%3)]
for seq in seqs:
	n=calc_space(cipher,seq)
	if n!=0:
		for i in n:
			m=get_fact(i)
			l+=m
			#print(seq,i,m)

a=collections.Counter(l).most_common()
print(tabulate(a))