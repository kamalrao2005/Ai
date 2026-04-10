import math
values = list(map(int, input("Enter leaf node values separated by space: ").split()))
minmax = 0
alp = 0
def minimax(start, end, maxplayer):
    global minmax
    minmax += 1
    if start == end:
        return values[start]
    mid = (start + end) // 2

    if maxplayer:
        left = minimax(start, mid, False)
        right = minimax(mid + 1, end, False)
        return max(left, right)
    else:
        left = minimax(start, mid, True)
        right = minimax(mid + 1, end, True)
        return min(left, right)
def alpb(start, end, maxplayer, alpha, beta):
    global alp
    alp += 1
    if start == end:
        return values[start]
    mid = (start + end) // 2
    if maxplayer:
        best = -math.inf
        val = alpb(start, mid, False, alpha, beta)
        best = max(best, val)
        alpha = max(alpha, best)
        if beta <= alpha:
            print("Pruned branch from", mid+1, "to", end)
            return best
        val = alpb(mid + 1, end, False, alpha, beta)
        best = max(best, val)
        alpha = max(alpha, best)
        return best
    else:
        best = math.inf
        val = alpb(start, mid, True, alpha, beta)
        best = min(best, val)
        beta = min(beta, best)

        if beta <= alpha:
            print("Pruned branch from", mid+1, "to", end)
            return best
        val = alpb(mid + 1, end, True, alpha, beta)
        best = min(best, val)
        beta = min(beta, best)
        return best
opt1 = minimax(0, len(values)-1, True)
opt2 = alpb(0, len(values)-1, True, -math.inf, math.inf)
print("Optimal value using Minimax:", opt1)
print("Nodes visited in Minimax:", minmax)
print("Optimal value using Alpha-Beta:", opt2)
print("Nodes visited in Alpha-Beta:", alp)
