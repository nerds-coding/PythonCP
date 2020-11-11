'''
“I am not in danger, Skyler. I am the danger. A guy opens his door and gets shot, and you think that of me? No! I am the one who knocks!”

Skyler fears Walter and ponders escaping to Colorado. Walter wants to clean his lab as soon as possible and then go back home to his wife.

In order clean his lab, he has to achieve cleaning level of lab as Y
. The current cleaning level of the lab is X

.

He must choose one positive odd integer a
and one positive even integer b. Note that, he cannot change a or b

once he starts cleaning.

He can perform any one of the following operations for one round of cleaning:

    Replace X

with X+a
.
Replace X
with X−b

    .

Find minimum number of rounds (possibly zero) to make lab clean.
'''


for _ in range(int(input())):
    x,y = list(map(int,input().split()))

    