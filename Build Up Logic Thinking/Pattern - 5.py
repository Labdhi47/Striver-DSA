#   * * * * *
#   * * * * 
#   * * * 
#   * *  
#   * 

class Solution:
    def printTriangle(self, N):
        for row in range(N):
            for col in range(N-row):
                print("*",end=" ")
            print()    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
