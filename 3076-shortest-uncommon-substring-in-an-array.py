from typing import List


def validateSubStr(substr: str, arr: List[str], originStr: str):
    count = 0
    for s in arr:
        # print(f"Validating substr {substr} with string {s}")
        if substr in s:
            count += 1
    if count > 1:
        return False
    return True


def generateAllSubStrs(s: str):
    subStrs = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            subStrs.append(s[i:j+1])
    # print(f"All Substring of \"{s}\" are: {subStrs}")
    return subStrs


def solve(arr: List[str]):
    ans = []
    for s in arr:
        allSubStrs = generateAllSubStrs(s)
        tempValidSubStrs = []
        for subStr in allSubStrs:
            if validateSubStr(subStr, arr, s):
                tempValidSubStrs.append(subStr)
        if len(tempValidSubStrs) == 0:
            ans.append("")
        else:
            tempValidSubStrs.sort()
            tempValidSubStrs.sort(key=len, reverse=False)
            ans.append(tempValidSubStrs[0])
    return ans


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        res = solve(arr)
        return res


if __name__ == "__main__":
    sol = Solution()
    arr = ["cab", "ad", "bad", "c"]
    res = sol.shortestSubstrings(arr)
    print(res)

    arr = ["abc", "bcd", "abcd"]
    res = sol.shortestSubstrings(arr)
    print(res)

    arr = ["gfnt", "xn", "mdz", "yfmr", "fi", "wwncn", "hkdy"]
    res = sol.shortestSubstrings(arr)
    print(res)

    arr = ["fhi", "ct", "s", "o", "o"]
    res = sol.shortestSubstrings(arr)
    print(res)
