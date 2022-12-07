tst=',2,2,3'
tst.split(',')
int(tst.split(','))
[int(c) for c in tst.split(',')]
[c for c in tst.split(',')]
r1=[c for c in tst.split(',')]
tst=',1,5,6'
r2=[c for c in tst.split(',')]
lst = [r1,r2]
zip(*lst)
list(zip(*lst))
tmp = list(zip(*lst))
%history
tmp = tmp[0]
tmp
tmp = [c for c in tmp[0] if '' not in tmp[0]]
tmp = [c for c in tmp[0] if '' not in tmp[0]]
tmp = [c for c in tmp[0] if '' not in tmp[0]]
tmps = [c for c in tmp[0] if '' not in tmp[1]]
