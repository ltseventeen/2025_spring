class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer=[]
        for i in range(1,numRows+1):
            answer.append([1]*i)

        if numRows<=2:
            return answer

        for i in range(2,numRows):
            for j in range(1,i):
                answer[i][j]=answer[i-1][j-1]+answer[i-1][j]
        return answer