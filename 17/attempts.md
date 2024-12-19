
always true
B is last 3 bits of A
B is xor with 110
C is A/2^B
B is B xor C
B is B xor 111
---
first output is last 3 bits of B

So, goal is 2, so last 3 bits of B at that point is 010

reverse engineer
B is last 3 bits of A
B is xor with 110
C is A with B less bits on right (A/2^B)
101 is B xor C
010 is 101 xor 111
---

thats hard, lets just guess!

engineer
A = 1110010010
B is last 3 bits of A. B == 010
B is xor with 110. B == 100
C is A/2^B. C == 111001
B is B xor C. B == 101
B is B xor 111
---
first output is last 3 bits of B (want 010)
---

ok so thats hard ig lol. Tried a lot of combos of last 6 digits but maybe i missed something with xors done in my head