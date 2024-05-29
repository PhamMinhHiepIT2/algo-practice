class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        costs = []
        for i in range(n):
            costs.append(abs(ord(s[i]) - ord(t[i])))
        st = []
        res = 0
        cur_cost = 0
        for i in range(n):
            if cur_cost + costs[i] <= maxCost:
                st.append(costs[i])
                cur_cost += costs[i]

            else:
                while st and cur_cost + costs[i] > maxCost:
                    cur_cost -= st[0]
                    st.pop(0)

                if cur_cost + costs[i] <= maxCost:
                    st.append(costs[i])
                    cur_cost += costs[i]
            res = max(res, len(st))
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "abcd"
    t = "bcdf"
    maxCost = 3
    res = sol.equalSubstring(s, t, maxCost)
    print(res)

    s = "krrgw"
    t = "zjxss"
    maxCost = 19
    res = sol.equalSubstring(s, t, maxCost)
    print(res)

    s = "abcd"
    t = "cdef"
    maxCost = 3
    res = sol.equalSubstring(s, t, maxCost)
    print(res)

    s = "thjdoffka"
    t = "qhrnlntls"
    maxCost = 11
    res = sol.equalSubstring(s, t, maxCost)
    print(res)
