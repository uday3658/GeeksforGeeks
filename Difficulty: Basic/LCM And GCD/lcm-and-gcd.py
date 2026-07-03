class Solution:
    def lcmAndGcd(self, n1, n2):
        list1 = []
        list2 = []

        # Factors of n1
        for i in range(1, n1 + 1):
            if n1 % i == 0:
                list1.append(i)

        # Factors of n2
        for i in range(1, n2 + 1):
            if n2 % i == 0:
                list2.append(i)

        # Common factors
        common = list(set(list1) & set(list2))
        gcd = max(common)

        lcm = (n1 * n2) // gcd

        return [lcm, gcd]