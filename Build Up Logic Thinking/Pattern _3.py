#   1
#   1 2 
#   1 2 3 
#   1 2 3 4 
#   1 2 3 4 5

class Solution:
    def printTriangle(self, N):
        for row in range(N):
            for col in range(row+1):
                print(col+1,end=" ")
            print()    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
