inp = sorted([int(line.strip()) for line in open("../input/ten")])

jumps = {1:0, 3:1}
start_joltage = 0
joltage = start_joltage

for adapt in inp:
    joltage, jdiff = adapt, adapt - joltage
    jumps[jdiff] += 1
solution1 = jumps[1] * jumps[3]

def memoize(f):
    memo = {}
    def helper(value):
        if value not in memo:
            memo[value] = f(value)
        return memo[value]
    return helper

last = inp[-1]
@memoize
def pathsFrom(n):
    if n == last: # Last number has only one path.
        return 1
    res = 0
    for i in range(1,4):
        next_n = n + i
        # Needs memoization as three calls may ocurr
        if next_n <= last and next_n in inp:
            res += pathsFrom(next_n)
    return res
solution2 = pathsFrom(start_joltage)

print("First solution:", solution1)
print("Second solution:", solution2)
