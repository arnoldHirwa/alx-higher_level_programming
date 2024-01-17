#!/usr/bin/python3

import sys

# Set a higher recursion limit if needed
sys.setrecursionlimit(100000)

class Queen():
    queen_id = 0

    def __init__(self, x, y):
        Queen.queen_id += 1
        self.x = x 
        self.y = y
        self.options = []

    def same_oblique_line(self, queen):
        y1 = queen.x - self.x + self.y
        y2 = -queen.x + self.x + self.y
        
        if queen.y == y1 or queen.y == y2:
            return True
        else:
            return False
    
    def same_horizontal_line(self, queen):
        if self.y == queen.y :
            return True
        else:
            return False

    def attack(self, array):
        if len(array) == 0:
            return True

        for quen in array:
            if self.same_horizontal_line(quen) or self.same_oblique_line(quen):
                    return False

        return True
    

allQ = []
solutions = []

def find_options(q, allQ, N):
    for i in range(N):
        q.y = i
        if q.attack(allQ):
            q.options.append(i)
        
    return q

def back_track(previous_failed=False, cursor=0, N=4):
    if previous_failed:
        allQ.pop()
        if len(allQ) == 0:
            return
    else:
        q = Queen(cursor, 0)
        q = find_options(q, allQ, N)
        allQ.append(q)
    
    q = allQ[-1]
    if len(q.options) == 0:
        return back_track(previous_failed=True, cursor=cursor-1, N=N)
    
    q.y = q.options.pop(0)
    
    if cursor == N - 1:
        solutions.append([[qn.x, qn.y] for qn in allQ])
        return back_track(previous_failed=True, cursor=cursor-1, N=N)
    
    return back_track(previous_failed=False, cursor=cursor+1, N=N)



if __name__ == "__main__":
    arguments = sys.argv[1:]
    argc = len(arguments)
    
    if argc != 1:
        print("Usage: nqueens N")
        sys.exit(1)
    N = int(arguments[0])
    if type(N) is not int:
        print("N must be a number")
        sys.exit(1)
    elif N < 4:
        print("N must be atleast 4")
        sys.exit(1)
    back_track(previous_failed=False, cursor=0, N=N)
    for solution in solutions:
        print(solution)
