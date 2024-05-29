from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int):
        def sol(candidates: List[int], target: int, temp: List[int], out: List[List[int]], i: int):
            print(target, temp, out, i)
            if target == 0:
                out.append(temp)
                print(f"out: {out}\n")
                return out
            
            for i in range(len(candidates)):
                if target - candidates[i] < 0:
                    return out
                temp.append(candidates[i])
                target = target-candidates[i]
                sol(candidates, target, temp, out, i)
                temp.pop()
                target = target + candidates[i]

            return out
        
        res = []
        chosen_candidates = []
        sorted_candidates = sorted(candidates)
        # for i in sorted_candidates:
        #     if i < target:
        #         chosen_candidates.append(i)
        #     if i == target:
        #         res.append([i])
        #         break
        return sol(sorted_candidates, target, [], [], 0)
        
        
        
        

if __name__ == "__main__":
    candidates = [1, 4, 3, 2, 7]
    target = 7
    sol = Solution()
    print(sol.combinationSum(candidates=candidates, target=target))

