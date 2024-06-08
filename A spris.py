'''
Meklit has a
 mango, b
 avocado and c
 banana. She decided to cook a spris. According to the recipe the fruits should be in the ratio 1:2:4
. It means that for each mango in the spris should be exactly 2
 avocado and exactly 4
 banana. You can't crumble up, break up or cut these fruits into pieces. These fruits — mango, avocado and banana — should be put in the spris as whole fruits.

Your task is to determine the maximum total number of mango, avocado and banana from which Meklit can cook the spris. It is possible that Meklit can't use any fruits, in this case print 0
.

Input
The first line contains the positive integer a
 (1≤a≤1000
) — the number of mango Meklit has.

The second line contains the positive integer b
 (1≤b≤1000
) — the number of avocado Meklit has.

The third line contains the positive integer c
 (1≤c≤1000
) — the number of banana Meklit has.

Output
Print the maximum total number of mango, avocado and banana from which Meklit can cook the spris.
'''


# solution

m=int(input())
av=int(input())//2
ban=int(input())//4
s=min(m,av,ban)
print(s*1+s*2+s*4)
