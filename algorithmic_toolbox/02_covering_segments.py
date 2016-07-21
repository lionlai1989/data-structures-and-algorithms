# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    tmpS = []
    #print(type(segments), segments)
    tmpS.append(min(segments, key=lambda x: x.end))
    segments.remove(min(segments, key=lambda x: x.end))
    #print(segments)
    while True:
        tmp = min(segments, key=lambda y: y.end)
        if tmp.start <= tmpS[-1].end:
            pass
        else:
            tmpS.append(tmp)
        segments.remove(min(segments, key=lambda x: x.end))
        if len(segments) == 0 :
            break
    #print(segments)
    #print(tmpS)
    for s in tmpS:
        #points.append(s.start)
        points.append(s.end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    #n = 5
    #data = [4, 7, 1, 3, 2, 5, 5, 6, 4, 5]
    #n = 4
    #data = [4, 7, 1, 3, 2, 5, 5, 6]
    #n = 3
    #data = [1, 3, 2, 5, 3, 6]
    
    #print(n ,data)
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    #print(points)
    print(len(points))
    for p in points:
        print(p, end=' ')
