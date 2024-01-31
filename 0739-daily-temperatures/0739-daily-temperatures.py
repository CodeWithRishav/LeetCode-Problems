class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        save = {}
        answer = []
        for day in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[day]
            save[temp] = day
            larger = []
            for i in range(temp + 1, 102):
                if i in save:
                    larger.append(save[i] - day)
            if larger:
                answer.append(min(larger))
            else:
                answer.append(0)
        return answer[::-1]