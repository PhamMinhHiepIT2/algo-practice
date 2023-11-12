import copy

class Solution:
    def __init__(self):
        self.mapper = {
            "0": 0,
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0
        }
    
    def countAndSay(self, n: int) -> str:
        if n == 0:
            return ""
        if n == 1:
            return "1"
        else:
            return self.say(self.countAndSay(n-1))

    def say(self, s: str):
        tmp_mapper = copy.deepcopy(self.mapper)
        res = ""

        n = len(s)
        for i in range(n):
            
            if i == 0:
                tmp_mapper[s[i]] += 1
            else:
                if s[i] != s[i-1]:
                    tmp_mapper[s[i]] += 1
                    res += str(tmp_mapper[s[i-1]]) + s[i-1]
                    tmp_mapper[s[i-1]] = 0
                else:
                    tmp_mapper[s[i]] += 1
        
        for k,v in tmp_mapper.items():
            if v != 0:
                res += str(v) + k
        return res


        

            


if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(4))
    print(sol.say("12222"))

