class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0
        st = []
        for c in s:
            st.append(c)

        count = 0
        while len(st) > 1:
            print(f'st={st}, count={count}')
            if st[-1] == '1':
                mark = False
                for i in range(len(st)-2, -1, -1):
                    if st[i] == '0':
                        st[i] = '1'
                        mark = True
                        break
                    else:
                        st[i] = '0'
                if mark == False:
                    st.insert(0, '1')
                    mark = True
                st[-1] = '0'
            else:
                st.pop()
            count += 1
        return count


if __name__ == "__main__":
    # s = "1111011110000011100000110001011011110010111001010111110001"
    sol = Solution()
    # res = sol.numSteps(s)
    # print(res)
    s = "1101"
    res = sol.numSteps(s)
    print(res)
    s = "10"
    res = sol.numSteps(s)
    print(res)
