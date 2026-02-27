from collections import deque
init_st = ('door', 'on_floor', 'window', False)
def is_goal(st):
    return st[3] == True
def succ(st):
    res = []
    m_pos, m_h, b_pos, has_b = st
    if m_h == 'on_floor':
        for p in ['door', 'middle', 'window']:
            if p != m_pos:
                res.append(((p, m_h, b_pos, has_b),
                            f"Monkey walks to {p}"))
    if m_h == 'on_floor' and m_pos == b_pos:
        for p in ['door', 'middle', 'window']:
            if p != b_pos:
                res.append(((p, m_h, p, has_b),
                            f"Monkey pushes box to {p}"))
        res.append(((m_pos, 'on_box', b_pos, has_b),
                    "Monkey climbs onto the box"))
    if m_h == 'on_box' and m_pos == 'middle':
        res.append(((m_pos, m_h, b_pos, True),
                    "Monkey grabs the banana"))
    return res
def bfs(init_st):
    q = deque([(init_st, [])])
    vis = set()
    while q:
        st, path = q.popleft()
        if is_goal(st):
            return path
        if st in vis:
            continue
        vis.add(st)
        for nxt, act in succ(st):
            q.append((nxt, path + [act]))
    return None
sol = bfs(init_st)
print("Solution Steps:\n")
for i, step in enumerate(sol, 1):
    print(f"{i}. {step}")
