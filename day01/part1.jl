using Test

#=
print(@test [1, 2] + [2, 1] == [3, 3])
print(@test true)
=#
INPUT_S = "
3
3
4

0

2"
EXPECTED = 10

f = open("input.txt");
lines = readlines(f)
maxcol=0

for l in lines
    newval=Int(l)
    if newval> maxcol 
        maxcol=newcol
    end
end
print(maxcol)
