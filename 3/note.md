## Why is there no entry for day 3?

It was pretty easy and so I just did it with some regex stuff.

### Part 1

1. Remove everything that doesn't fit `mul\(\d*,\d*\)`
2. Multiply through the list

### Part 2

1. Remove everything that doesn't fit `mul\(\d*,\d*\)`
2. Remove the non-important multiply things lazily `don't\(\)(\n|.)+?do\(\)\n`
3. Remove the redundant `do\(\)\n`
4. Multiply through the list