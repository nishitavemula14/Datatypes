A={10,20,30}
B={30,50,70,80}
print(A.union(B))
print(A.intersection(B))
print(A|B)
print(A&B)
print(A.difference(B))
print(A-B)
print(A.symmetric_difference(B))
print(A^B)
print(A.issubset(B))
print(A.issuperset(B))
print(A>=B)
print(A<=B)
print(A.isdisjoint(B))
print(len(A))
print(len(B))
print(max(A))
print(min(A))
print(max(B))
print(min(B))
print(sum(A))



C={10,52,93}
C.add(25)
print(C)

C.remove(10)
print(C)

C.discard(52)
print(C)

D=set([200,60,85])
print(sorted(D))