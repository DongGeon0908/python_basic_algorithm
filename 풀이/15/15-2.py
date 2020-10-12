def print_all_friends(g, start):
    qu = []
    done = set()

    qu.append((start, 0))
    done.add(start)

    while qu:
        (p, d) = qu.pop(0)
        print(p, d)
        for x in g[p]:
            if x not in done:
                qu.append((x, d + 1))
                done.add(x)

fr_info = {
    'summer': ['john','justin','mike'],
    'john': ['summer', 'justin'],
    'justin': ['john','summer','mike','may'],
    'mike': ['summer', 'justin'],
    'may': ['justin', 'kim'],
    'kim': ['may'],
    'tom': ['jerry'],
    'jerry': ['tom']
}

print_all_friends(fr_info, 'summer')
