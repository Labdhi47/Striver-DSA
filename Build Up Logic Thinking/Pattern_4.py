#   1
#   2 2 
#   3 3 3 
#   4 4 4 4 
#   5 5 5 5 5

class Solution:
    def printTriangle(self, N):
        for row in range(N):
            for col in range(row+1):
                print(row+1,end=" ")
            print()    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
