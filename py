def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}
    
    
    
OR


def pick_peaks(arr):
    res = {'pos': [], 'peaks': []}
    prev, cur = 0, 0
    for next in xrange(1, len(arr)):
        if arr[next] > arr[cur]:
            prev = cur
            cur = next
        elif arr[next] < arr[cur]:
            if arr[cur] > arr[prev]:
                res['pos'].append(cur)
                res['peaks'].append(arr[cur])
            prev = cur
            cur = next
    return res
    
    
    
OR


from itertools import izip


def pick_peaks(a):
    deltas = [(i, x2 - x1) for i, (x1, x2) in enumerate(izip(a, a[1:]), 1) if x1 != x2]
    indexes = [i for (i, dx1), (_, dx2) in izip(deltas, deltas[1:]) if dx1 > 0 > dx2]
    return dict(pos=indexes, peaks=[a[i] for i in indexes])
