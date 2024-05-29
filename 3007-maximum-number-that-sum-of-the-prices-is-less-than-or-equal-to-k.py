def priceCal(bin: str, x: int):
    price = 0
    i = 1
    pos = i*x-1
    while pos < len(bin):

        if bin[pos] == '1':
            price += 1
        i += 1
        pos = i*x-1

    print(f"Bin={bin}, x = {x}, price = {price}")
    return price


class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        accPrice = 0
        i = 1
        while accPrice < k:
            bin = format(i, "050b")
            accPrice += priceCal(bin, x)
            i += 1
        return i - 1


if __name__ == "__main__":
    sol = Solution()
    k = 9
    x = 1
    print(sol.findMaximumNumber(k, x))
    print("==================")
    k = 7
    x = 2
    print(sol.findMaximumNumber(k, x))
