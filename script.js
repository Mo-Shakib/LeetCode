const problems = [
  {
    "title": "Add Binary",
    "status": "Accepted",
    "runtime": "51 ms",
    "memory": "14.3 MB",
    "code": "// https://leetcode.com/problems/add-binary\n\nclass Solution:\n    def addBinary(self, a: str, b: str) -> str:\n        return bin(int(a, 2) + int(b, 2))[2:]\n    ",
    "url": "https://leetcode.com/problems/add-binary"
  },
  {
    "title": "Add Digits",
    "status": "Accepted",
    "runtime": "67 ms",
    "memory": "14.3 MB",
    "code": "// https://leetcode.com/problems/add-digits\n\nclass Solution:\n    def addDigits(self, num: int) -> int:\n        if num <= 9:\n            return num\n        if num % 9 == 0:\n            return 9\n        return num % 9\n    # Time complexity: O(1)\n    ",
    "url": "https://leetcode.com/problems/add-digits"
  },
  {
    "title": "Add Strings",
    "status": "Accepted",
    "runtime": "45 ms",
    "memory": "14.2 MB",
    "code": "// https://leetcode.com/problems/add-strings\n\nclass Solution:\n    def addStrings(self, num1: str, num2: str) -> str:    \n        ans = int(num1) + int(num2)\n        return str(ans)\n        ",
    "url": "https://leetcode.com/problems/add-strings"
  },
  {
    "title": "Arranging Coins",
    "status": "Accepted",
    "runtime": "1514 ms",
    "memory": "13.8 MB",
    "code": "// https://leetcode.com/problems/arranging-coins\n\nclass Solution:\n    def arrangeCoins(self, n: int) -> int:\n        staircase = 0\n        while (staircase <= n):\n            n -= staircase\n            staircase += 1\n        return staircase - 1",
    "url": "https://leetcode.com/problems/arranging-coins"
  },
  {
    "title": "Average Salary Excluding the Minimum and Maximum Salary",
    "status": "Accepted",
    "runtime": "0 ms",
    "memory": "16.7 MB",
    "code": "// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary\n\nclass Solution:\n    def average(self, salary: List[int]) -> float:\n        return ((sum(salary)- max(salary) - min(salary))/ (len(salary)-2) )\n        ",
    "url": "https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary"
  },
  {
    "title": "Burst Balloons",
    "status": "Accepted",
    "runtime": "11715 ms",
    "memory": "19.9 MB",
    "code": "// https://leetcode.com/problems/burst-balloons\n\nclass Solution(object):\n    def maxCoins(self, nums):\n        \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n        nums = [1] + nums + [1] # build the complete array \n        n = len(nums)\n        dp = [[0] * n for _ in range(n)]\n\n        for gap in range(2, n):\n            for i in range(n-gap):\n                j = i + gap\n                for k in range(i+1, j):\n                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])\n        return dp[0][n-1]",
    "url": "https://leetcode.com/problems/burst-balloons"
  },
  {
    "title": "Capitalize the Title",
    "status": "Accepted",
    "runtime": "50 ms",
    "memory": "14.1 MB",
    "code": "// https://leetcode.com/problems/capitalize-the-title\n\nclass Solution:\n    def capitalizeTitle(self, title: str) -> str:\n        title = title.split()\n        res = \"\"\n        for char in title:\n            if 1 <= len(char) <= 2:\n                res += char.lower()\n            else:\n                res += char[0].upper() + char[1:].lower()\n            res += \" \"\n        return res[:-1]",
    "url": "https://leetcode.com/problems/capitalize-the-title"
  },
  {
    "title": "Check if All A's Appears Before All B's",
    "status": "Accepted",
    "runtime": "46 ms",
    "memory": "14.2 MB",
    "code": "// https://leetcode.com/problems/check-if-all-as-appears-before-all-bs\n\nclass Solution:\n    def checkString(self, s: str) -> bool:\n        for i in range(len(s)):\n            if s[i] == 'b':\n                for j in range(i, len(s)):\n                    if s[j] == 'a':\n                        return False\n                return True\n            else:\n                x = True\n        return x\n            ",
    "url": "https://leetcode.com/problems/check-if-all-as-appears-before-all-bs"
  },
  {
    "title": "Check if Every Row and Column Contains All Numbers",
    "status": "Accepted",
    "runtime": "744 ms",
    "memory": "14.8 MB",
    "code": "// https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers\n\nclass Solution:\n    def checkValid(self, matrix: List[List[int]]) -> bool:\n        n = len(matrix)\n        for i in range(n):\n            if len(set(matrix[i])) != n:\n                return False\n        for j in range(n):\n            temp = []\n            for i in range(n):\n                temp.append(matrix[i][j])\n            if len(set(temp)) != n:\n                return False\n        return True",
    "url": "https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers"
  },
  {
    "title": "Climbing Stairs",
    "status": "Accepted",
    "runtime": "0 ms",
    "memory": "17.6 MB",
    "code": "// https://leetcode.com/problems/climbing-stairs\n\nclass Solution:\n    def climbStairs(self, n: int) -> int:\n        if n <= 1:\n            return n\n\n        # To store the curr Fibonacci number\n        curr = 0\n\n        # To store the previous Fibonacci numbers\n        prev1 = 1\n        prev2 = 1\n\n        # Loop to calculate Fibonacci numbers from 2 to n\n        for i in range(2, n + 1):\n        \n            # Calculate the curr Fibonacci number\n            curr = prev1 + prev2\n\n            # Update prev2 to the last Fibonacci number\n            prev2 = prev1\n\n            # Update prev1 to the curr Fibonacci number\n            prev1 = curr\n\n        return curr",
    "url": "https://leetcode.com/problems/climbing-stairs"
  },
  {
    "title": "Complement of Base 10 Integer",
    "status": "Accepted",
    "runtime": "0 ms",
    "memory": "16.5 MB",
    "code": "// https://leetcode.com/problems/complement-of-base-10-integer\n\nclass Solution(object):\n    def bitwiseComplement(self, n):\n\t    return ((2 << int(math.log(max(n, 1), 2))) - 1) - n\n        ",
    "url": "https://leetcode.com/problems/complement-of-base-10-integer"
  },
  {
    "title": "Construct the Rectangle",
    "status": "Accepted",
    "runtime": "3 ms",
    "memory": "17.7 MB",
    "code": "// https://leetcode.com/problems/construct-the-rectangle\n\nimport math\nclass Solution:\n    def constructRectangle(self, area: int) -> List[int]:\n        i = 1\n        l = 0\n        w = 0\n        while math.floor(i*i) <= area:\n            if area % i == 0:\n                w = i\n                l = area/w\n            i += 1\n        return [int(l), int(w)]\n\n        \n        ",
    "url": "https://leetcode.com/problems/construct-the-rectangle"
  },
  {
    "title": "Contains Duplicate",
    "status": "Accepted",
    "runtime": "112 ms",
    "memory": "20.1 MB",
    "code": "// https://leetcode.com/problems/contains-duplicate\n\nclass Solution:\n    def containsDuplicate(self, nums: List[int]) -> bool:\n        x = set(nums)\n        if len(nums) == len(x):\n            return False\n        return True",
    "url": "https://leetcode.com/problems/contains-duplicate"
  },
  {
    "title": "Contains Duplicate II",
    "status": "Accepted",
    "runtime": "6038 ms",
    "memory": "26.2 MB",
    "code": "// https://leetcode.com/problems/contains-duplicate-ii\n\nclass Solution:\n    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:\n        \n        window = []\n\n        for i in range(len(nums)):\n            if nums[i] in window:\n                return True\n\n            window.append(nums[i])\n\n            if len(window) > k:\n                window.pop(0)\n\n        return False\n\n\n\n        \n        \n\n            \n\n",
    "url": "https://leetcode.com/problems/contains-duplicate-ii"
  },
  {
    "title": "Excel Sheet Column Number",
    "status": "Accepted",
    "runtime": "59 ms",
    "memory": "14.1 MB",
    "code": "// https://leetcode.com/problems/excel-sheet-column-number\n\nclass Solution:\n    def titleToNumber(self, columnTitle: str) -> int:\n        res = 0\n        for x in range(len(columnTitle)):\n            res += 26**(len(columnTitle)-x-1) * (ord(columnTitle[x]) - ord('A') + 1)\n        return res\n        ",
    "url": "https://leetcode.com/problems/excel-sheet-column-number"
  },
  {
    "title": "Find Closest Number to Zero",
    "status": "Accepted",
    "runtime": "7 ms",
    "memory": "16.7 MB",
    "code": "// https://leetcode.com/problems/find-closest-number-to-zero\n\nclass Solution:\n    def findClosestNumber(self, nums: List[int]) -> int:\n        res = float('inf')\n        nums = set(nums)\n        for i in nums:\n            if abs(i) < abs(res):\n                res = i\n            elif i == abs(res):\n                if i > res:\n                    res = i\n        return res",
    "url": "https://leetcode.com/problems/find-closest-number-to-zero"
  },
  {
    "title": "Find the Town Judge",
    "status": "Accepted",
    "runtime": "1299 ms",
    "memory": "19 MB",
    "code": "// https://leetcode.com/problems/find-the-town-judge\n\nclass Solution:\n    def findJudge(self, n: int, trust: List[List[int]]) -> int:\n        trusted = {}\n        if len(trust) == 0 and n == 1:\n            return 1\n        if n > 1 and len(trust) == 0:\n            return -1\n        \n        for (a, b) in trust:\n            if a not in trusted:\n                trusted[a] = -1\n            else:\n                trusted[a] -= 1\n            \n            if b not in trusted:\n                trusted[b] = 1\n            else:\n                trusted[b] += 1\n        \n        for key, value in trusted.items():\n            if value == n -1:\n                return key\n        return -1\n        ",
    "url": "https://leetcode.com/problems/find-the-town-judge"
  },
  {
    "title": "Fizz Buzz",
    "status": "Accepted",
    "runtime": "38 ms",
    "memory": "17.7 MB",
    "code": "// https://leetcode.com/problems/fizz-buzz\n\nclass Solution:\n    def fizzBuzz(self, n: int) -> List[str]:\n        res = []\n        for num in range(1, n+1):\n            if (num % 3 == 0) and (num % 5 == 0):\n                res.append(\"FizzBuzz\")\n            elif (num % 3 == 0):\n                res.append(\"Fizz\")\n            elif (num % 5 == 0):\n                res.append(\"Buzz\")\n            else:\n                res.append(str(num))\n        return res\n        ",
    "url": "https://leetcode.com/problems/fizz-buzz"
  },
  {
    "title": "Hamming Distance",
    "status": "Accepted",
    "runtime": "65 ms",
    "memory": "14.2 MB",
    "code": "// https://leetcode.com/problems/hamming-distance\n\nclass Solution:\n    def hammingDistance(self, x: int, y: int) -> int:\n        res = bin(x ^ y)[2:]\n        return str(res).count('1')\n        ",
    "url": "https://leetcode.com/problems/hamming-distance"
  },
  {
    "title": "Happy Number",
    "status": "Accepted",
    "runtime": "3 ms",
    "memory": "16.5 MB",
    "code": "// https://leetcode.com/problems/happy-number\n\nclass Solution:\n    def isHappy(self, n):\n        mem = set()\n        while n != 1:\n            n = sum([int(i) ** 2 for i in str(n)])\n            if n in mem:\n                return False\n            else:\n                mem.add(n)\n        else:\n            return True\n        ",
    "url": "https://leetcode.com/problems/happy-number"
  },
  {
    "title": "Intersection of Two Arrays",
    "status": "Accepted",
    "runtime": "74 ms",
    "memory": "14.4 MB",
    "code": "// https://leetcode.com/problems/intersection-of-two-arrays\n\nclass Solution:\n    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:\n        nums1 = set(nums1)\n        nums2 = set(nums2)\n        \n        res = nums1 & nums2\n        \n        return list(res)",
    "url": "https://leetcode.com/problems/intersection-of-two-arrays"
  },
  {
    "title": "Intersection of Two Arrays II",
    "status": "Accepted",
    "runtime": "113 ms",
    "memory": "14.3 MB",
    "code": "// https://leetcode.com/problems/intersection-of-two-arrays-ii\n\nclass Solution:\n    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:\n        output = []\n        dic = {}\n        for ele in nums2:\n            if ele not in dic:\n                dic[ele] = 1\n            else:\n                dic[ele] += 1\n        \n        for i in nums1:\n            if i in nums2 and dic[i] > 0:\n                output.append(i)\n                dic[i] -= 1\n        return output\n        \n        ",
    "url": "https://leetcode.com/problems/intersection-of-two-arrays-ii"
  },
  {
    "title": "Is Subsequence",
    "status": "Accepted",
    "runtime": "0 ms",
    "memory": "16.5 MB",
    "code": "// https://leetcode.com/problems/is-subsequence\n\nclass Solution:\n    def isSubsequence(self, s: str, t: str) -> bool:\n\n        found = 0\n        x = 0\n        for i in s:\n            while x < len(t) and t[x] != i:\n                x += 1  \n            if x < len(t): \n                x += 1 \n                found += 1\n            else:\n                break  \n\n        return found == len(s)\n            \n\n        ",
    "url": "https://leetcode.com/problems/is-subsequence"
  },
  {
    "title": "Largest Perimeter Triangle",
    "status": "Accepted",
    "runtime": "9 ms",
    "memory": "17.7 MB",
    "code": "// https://leetcode.com/problems/largest-perimeter-triangle\n\nclass Solution:\n    def largestPerimeter(self, nums: List[int]) -> int:\n        nums.sort(reverse=True)\n        for i in range(len(nums)-2):\n            if nums[i] < nums[i+1]+nums[i+2]:\n                return nums[i] + nums[i+1] + nums[i+2]\n        return 0",
    "url": "https://leetcode.com/problems/largest-perimeter-triangle"
  },
  {
    "title": "Longest Common Prefix",
    "status": "Accepted",
    "runtime": "51 ms",
    "memory": "16.6 MB",
    "code": "// https://leetcode.com/problems/longest-common-prefix\n\nclass Solution:\n    def longestCommonPrefix(self, strs: List[str]) -> str:\n        # Find the smallest length element\n        smallest_length_element = min(strs, key=len)\n        # Get the length of the smallest element\n        smallest_length = len(smallest_length_element)\n        res = ''\n        for i in range(smallest_length):\n            x = len(strs)\n            y = 0\n            for element in strs:\n                if element[i] == smallest_length_element[i]:\n                    y += 1\n                    if y == x:\n                        res += element[i]\n                        y = 0\n                else:\n                    return res\n        return res\n\n        ",
    "url": "https://leetcode.com/problems/longest-common-prefix"
  },
  {
    "title": "Majority Element",
    "status": "Accepted",
    "runtime": "4 ms",
    "memory": "18.5 MB",
    "code": "// https://leetcode.com/problems/majority-element\n\nclass Solution:\n    def majorityElement(self, nums: List[int]) -> int:\n        nums = sorted(nums)\n        return nums[len(nums)//2]\n        ",
    "url": "https://leetcode.com/problems/majority-element"
  },
  {
    "title": "Maximum Average Subarray I",
    "status": "Accepted",
    "runtime": "99 ms",
    "memory": "26.5 MB",
    "code": "// https://leetcode.com/problems/maximum-average-subarray-i\n\nclass Solution:\n    def findMaxAverage(self, nums: List[int], k: int) -> float:\n        \n        currSum = maxSum = sum(nums[:k])\n\n        for i in range(k, len(nums)):\n            currSum += nums[i] - nums[i - k]\n            \n            maxSum = max(maxSum, currSum)\n\n        return maxSum / k\n",
    "url": "https://leetcode.com/problems/maximum-average-subarray-i"
  },
  {
    "title": "Maximum Number of Words Found in Sentences",
    "status": "Accepted",
    "runtime": "45 ms",
    "memory": "14.3 MB",
    "code": "// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences\n\nclass Solution:\n    def mostWordsFound(self, sentences: List[str]) -> int:\n        total = []\n        for i in sentences:\n            words = i.split()\n            total.append(len(words))\n        return max(total)",
    "url": "https://leetcode.com/problems/maximum-number-of-words-found-in-sentences"
  },
  {
    "title": "Maximum Subarray",
    "status": "Accepted",
    "runtime": "116 ms",
    "memory": "15.1 MB",
    "code": "// https://leetcode.com/problems/maximum-subarray\n\nclass Solution:\n    def maxSubArray(self, nums: List[int]) -> int:\n        currSum = nums[0]\n        maxSum = nums[0]\n        \n        for i in nums[1:]:\n            currSum = max(i, currSum+i)\n            maxSum = max(maxSum, currSum)\n        return maxSum\n    ",
    "url": "https://leetcode.com/problems/maximum-subarray"
  },
  {
    "title": "Median of Two Sorted Arrays",
    "status": "Accepted",
    "runtime": "120 ms",
    "memory": "14.6 MB",
    "code": "// https://leetcode.com/problems/median-of-two-sorted-arrays\n\nclass Solution:\n    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:\n        for element in nums2:\n            nums1.append(element)\n        \n        nums1.sort()\n        lenth = len(nums1)\n        \n        if lenth % 2 == 0:\n            n1 = lenth // 2\n            n2 = n1 - 1\n            return (nums1[n1] + nums1[n2])/2\n        else:\n            return nums1[lenth//2]\n            \n        ",
    "url": "https://leetcode.com/problems/median-of-two-sorted-arrays"
  },
  {
    "title": "Merge Sorted Array",
    "status": "Accepted",
    "runtime": "78 ms",
    "memory": "14.2 MB",
    "code": "// https://leetcode.com/problems/merge-sorted-array\n\nclass Solution:\n    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:\n        \"\"\"\n        Do not return anything, modify nums1 in-place instead.\n        \"\"\"\n        for i in range(m, len(nums1)):\n            nums1[i] = nums2[i-m]\n        nums1.sort()\n        ",
    "url": "https://leetcode.com/problems/merge-sorted-array"
  },
  {
    "title": "Merge Strings Alternately",
    "status": "Accepted",
    "runtime": "37 ms",
    "memory": "16.3 MB",
    "code": "// https://leetcode.com/problems/merge-strings-alternately\n\nclass Solution:\n    def mergeAlternately(self, word1: str, word2: str) -> str:\n    \n        m = min(len(word1), len(word2))\n        res = ''\n        for i in range(m):\n            res += word1[i] + word2[i]\n\n        if m == len(word1):\n            return res + word2[m:]\n        else:\n            return res + word1[m:]",
    "url": "https://leetcode.com/problems/merge-strings-alternately"
  },
  {
    "title": "Missing Number",
    "status": "Accepted",
    "runtime": "7 ms",
    "memory": "18.7 MB",
    "code": "// https://leetcode.com/problems/missing-number\n\nclass Solution:\n    def missingNumber(self, nums: List[int]) -> int:\n        n = len(nums)\n        a = 0\n        for i in range(0, n+1):\n            a ^= i\n        b = 0\n        for i in nums:\n            b ^= i\n        \n        return a ^ b\n\n        ",
    "url": "https://leetcode.com/problems/missing-number"
  },
  {
    "title": "Move Zeroes",
    "status": "Accepted",
    "runtime": "160 ms",
    "memory": "15.5 MB",
    "code": "// https://leetcode.com/problems/move-zeroes\n\nclass Solution:\n    def moveZeroes(self, nums: List[int]) -> None:\n        \"\"\"\n        Do not return anything, modify nums in-place instead.\n        \"\"\"\n        x = 0\n        for i in range(len(nums)):\n            if nums[i] != 0:\n                nums[i], nums[x] = nums[x], nums[i]\n                x += 1",
    "url": "https://leetcode.com/problems/move-zeroes"
  },
  {
    "title": "Number of 1 Bits",
    "status": "Accepted",
    "runtime": "0 ms",
    "memory": "17.6 MB",
    "code": "// https://leetcode.com/problems/number-of-1-bits\n\nclass Solution:\n    def hammingWeight(self, n: int) -> int:\n        count = 0\n        while n != 0:\n            n = n & (n-1)\n            count += 1\n        return count",
    "url": "https://leetcode.com/problems/number-of-1-bits"
  },
  {
    "title": "Number of Steps to Reduce a Number to Zero",
    "status": "Accepted",
    "runtime": "38 ms",
    "memory": "16.4 MB",
    "code": "// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero\n\nclass Solution:\n    def numberOfSteps(self, num: int) -> int:\n        count = 0\n        while num != 0:\n            if num % 2 == 0:\n                num = num/2\n                count += 1\n            else:\n                num -= 1\n                count += 1\n        \n        return count",
    "url": "https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero"
  },
  {
    "title": "Palindrome Number",
    "status": "Accepted",
    "runtime": "56 ms",
    "memory": "14.4 MB",
    "code": "// https://leetcode.com/problems/palindrome-number\n\nclass Solution:\n    def isPalindrome(self, x: int) -> bool:\n        x = str(x)\n        y = x[::-1]\n        if x == y:\n            return True\n        return False\n        ",
    "url": "https://leetcode.com/problems/palindrome-number"
  },
  {
    "title": "Pascal's Triangle",
    "status": "Accepted",
    "runtime": "38 ms",
    "memory": "14.3 MB",
    "code": "// https://leetcode.com/problems/pascals-triangle\n\n\n\nclass Solution:\n    def generate(self, numRows: int) -> List[List[int]]:\n        pascal = [[1]*(i+1) for i in range(numRows)]\n        for i in range(1, numRows):\n            for j in range(1, i):\n                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]\n        return pascal\n        ",
    "url": "https://leetcode.com/problems/pascals-triangle"
  },
  {
    "title": "Perfect Number",
    "status": "Accepted",
    "runtime": "76 ms",
    "memory": "14.3 MB",
    "code": "// https://leetcode.com/problems/perfect-number\n\nimport math\nclass Solution:\n    def checkPerfectNumber(self, num: int) -> bool:\n        divisors = [1]\n        if num == 1:\n            return False\n        for i in range(2,int(math.sqrt(num))+1):\n            if num%i == 0:\n                divisors.extend([i,num/i])\n                \n        if sum(set(divisors)) == num:\n            return True\n        return False\n    \n        ",
    "url": "https://leetcode.com/problems/perfect-number"
  },
  {
    "title": "Plus One",
    "status": "Accepted",
    "runtime": "31 ms",
    "memory": "14.2 MB",
    "code": "// https://leetcode.com/problems/plus-one\n\nclass Solution:\n    def plusOne(self, digits: List[int]) -> List[int]:\n        value = ''\n        res = []\n        \n        for i in digits:\n            value += str(i)\n        \n        value = int(value)\n        value += 1\n        \n        for i in str(value):\n            res.append(int(i))\n            \n        return res\n        ",
    "url": "https://leetcode.com/problems/plus-one"
  },
  {
    "title": "Power of Two",
    "status": "Accepted",
    "runtime": "0 ms",
    "memory": "16.6 MB",
    "code": "// https://leetcode.com/problems/power-of-two\n\nclass Solution:\n    def isPowerOfTwo(self, n: int) -> bool:\n        if (n==1):\n            return True\n        \n        n_bin = bin(n)\n        n_bin = n_bin[2:]\n        \n        if (n_bin[0]!= '1'):\n            return False\n        \n        elif (n_bin.count('1')>1):\n            return False\n        \n        return True\n                ",
    "url": "https://leetcode.com/problems/power-of-two"
  },
  {
    "title": "Remove Duplicates from Sorted Array",
    "status": "Accepted",
    "runtime": "148 ms",
    "memory": "15.6 MB",
    "code": "// https://leetcode.com/problems/remove-duplicates-from-sorted-array\n\nclass Solution:\n    def removeDuplicates(self, nums: List[int]) -> int:\n        index = 1\n        while index < len(nums):\n            if nums[index] == nums[index-1]:\n                nums.pop(index)\n            else:\n                index += 1\n        return len(nums)\n        ",
    "url": "https://leetcode.com/problems/remove-duplicates-from-sorted-array"
  },
  {
    "title": "Remove Element",
    "status": "Accepted",
    "runtime": "74 ms",
    "memory": "14.3 MB",
    "code": "// https://leetcode.com/problems/remove-element\n\nclass Solution:\n    def removeElement(self, nums: List[int], val: int) -> int:\n        idx = 0\n        for item in nums:\n            if item != val:\n                nums[idx] = item\n                idx += 1\n        return idx\n    ",
    "url": "https://leetcode.com/problems/remove-element"
  },
  {
    "title": "Reverse String",
    "status": "Accepted",
    "runtime": "213 ms",
    "memory": "18.6 MB",
    "code": "// https://leetcode.com/problems/reverse-string\n\nclass Solution:\n    def reverseString(self, s: List[str]) -> None:\n        \"\"\"\n        Do not return anything, modify s in-place instead.\n        s = s[:-1]\n        return s\n        \"\"\"\n        s[:] = s[::-1]\n        return s",
    "url": "https://leetcode.com/problems/reverse-string"
  },
  {
    "title": "Richest Customer Wealth",
    "status": "Accepted",
    "runtime": "51 ms",
    "memory": "16.5 MB",
    "code": "// https://leetcode.com/problems/richest-customer-wealth\n\nclass Solution:\n    def maximumWealth(self, accounts: List[List[int]]) -> int:\n        max_w = []\n        for w in accounts:\n            max_w.append(sum(w))\n        return max(max_w)\n        ",
    "url": "https://leetcode.com/problems/richest-customer-wealth"
  },
  {
    "title": "Roman to Integer",
    "status": "Accepted",
    "runtime": "48 ms",
    "memory": "14.3 MB",
    "code": "// https://leetcode.com/problems/roman-to-integer\n\nclass Solution:\n    def romanToInt(self, s: str) -> int:\n        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500,'M':1000}\n        orders = {'I':1, 'V':2, 'X':3, 'L':4, 'C':5,'D':6,'M':7}\n        total = 0\n        for i in range(len(s)-1):\n            roman = s[i]\n            \n            if orders[s[i]] >= orders[s[i+1]]:\n                total += values[s[i]]\n            else:\n                total -= values[s[i]]\n\n        return total+values[s[-1]]\n        ",
    "url": "https://leetcode.com/problems/roman-to-integer"
  },
  {
    "title": "Rotate Image",
    "status": "Accepted",
    "runtime": "0 ms",
    "memory": "16.4 MB",
    "code": "// https://leetcode.com/problems/rotate-image\n\nclass Solution:\n    def rotate(self, matrix: List[List[int]]) -> None:\n        \"\"\"\n        Do not return anything, modify matrix in-place instead.\n        \"\"\"\n        # reverse\n        l = 0\n        r = len(matrix) -1\n        while l < r:\n            matrix[l], matrix[r] = matrix[r], matrix[l]\n            l += 1\n            r -= 1\n        # transpose \n        for i in range(len(matrix)):\n            for j in range(i):\n                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]\n                ",
    "url": "https://leetcode.com/problems/rotate-image"
  },
  {
    "title": "Running Sum of 1d Array",
    "status": "Accepted",
    "runtime": "39 ms",
    "memory": "16.8 MB",
    "code": "// https://leetcode.com/problems/running-sum-of-1d-array\n\nclass Solution:\n    def runningSum(self, nums: List[int]) -> List[int]:\n        res = nums[:1]\n        for i in range(1, len(nums)):\n            res.append((res[-1] + nums[i]))\n        return res",
    "url": "https://leetcode.com/problems/running-sum-of-1d-array"
  },
  {
    "title": "Single Number",
    "status": "Accepted",
    "runtime": "9204 ms",
    "memory": "16.5 MB",
    "code": "// https://leetcode.com/problems/single-number\n\nclass Solution:\n    def singleNumber(self, nums: List[int]) -> int:\n        dic = {}\n        for x in range(len(nums)):\n            count = nums.count(nums[x])\n            if count == 1:\n                return nums[x]\n            if nums[x] not in dic:\n                dic[count] = nums[x]\n                \n        return dic[1]\n    \n        \n        ",
    "url": "https://leetcode.com/problems/single-number"
  },
  {
    "title": "Smallest Range I",
    "status": "Accepted",
    "runtime": "3 ms",
    "memory": "17.6 MB",
    "code": "// https://leetcode.com/problems/smallest-range-i\n\nclass Solution:\n    def smallestRangeI(self, nums: List[int], k: int) -> int:\n        M, m = max(nums), min(nums)\n        diff, extension = M - m, 2*k\n        \n        if diff <= extension:\n            return 0\n        \n        else:\n            return diff - extension",
    "url": "https://leetcode.com/problems/smallest-range-i"
  },
  {
    "title": "Sqrt(x)",
    "status": "Accepted",
    "runtime": "51 ms",
    "memory": "13.8 MB",
    "code": "// https://leetcode.com/problems/sqrtx\n\nimport math\n\nclass Solution:\n    def mySqrt(self, x: int) -> int:\n        return int(math.sqrt(x))",
    "url": "https://leetcode.com/problems/sqrtx"
  },
  {
    "title": "Sum of Square Numbers",
    "status": "Accepted",
    "runtime": "164 ms",
    "memory": "14 MB",
    "code": "// https://leetcode.com/problems/sum-of-square-numbers\n\nfrom math import sqrt\n\nclass Solution:\n    def judgeSquareSum(self, c: int) -> bool:\n        a = 0\n        b = int(sqrt(c))\n        \n        if c <= 2:\n            return True\n        \n        while (a<=b):\n            result = (a*a) + (b*b)\n            if result == c:\n                return True\n            if result < c:\n                a += 1\n            else:\n                b -= 1\n        return False",
    "url": "https://leetcode.com/problems/sum-of-square-numbers"
  },
  {
    "title": "Three Divisors",
    "status": "Accepted",
    "runtime": "49 ms",
    "memory": "14 MB",
    "code": "// https://leetcode.com/problems/three-divisors\n\nclass Solution:\n    def isThree(self, n: int) -> bool:\n        count = 0\n        for i in range(1, n+1):\n            if n % i == 0:\n                count += 1\n        if count == 3:\n            return True\n        else:\n            return False",
    "url": "https://leetcode.com/problems/three-divisors"
  },
  {
    "title": "To Lower Case",
    "status": "Accepted",
    "runtime": "31 ms",
    "memory": "14.3 MB",
    "code": "// https://leetcode.com/problems/to-lower-case\n\nclass Solution:\n    def toLowerCase(self, s: str) -> str:\n        return s.lower()\n        ",
    "url": "https://leetcode.com/problems/to-lower-case"
  },
  {
    "title": "Top K Frequent Elements",
    "status": "Accepted",
    "runtime": "7 ms",
    "memory": "20.1 MB",
    "code": "// https://leetcode.com/problems/top-k-frequent-elements\n\nclass Solution:\n    def topKFrequent(self, nums: List[int], k: int) -> List[int]:\n        my_dict = {}\n\n        for i in nums:\n            if i not in my_dict:\n                my_dict[i] = 1\n            else:\n                my_dict[i] += 1\n        # Sort the dictionary based on values and create a list of keys\n        sorted_keys = sorted(my_dict, key=lambda x: my_dict[x], reverse=True)\n\n        return sorted_keys[:k]\n        ",
    "url": "https://leetcode.com/problems/top-k-frequent-elements"
  },
  {
    "title": "Two Sum",
    "status": "Accepted",
    "runtime": "86 ms",
    "memory": "15.7 MB",
    "code": "// https://leetcode.com/problems/two-sum\n\nclass Solution:\n    def twoSum(self, nums, target):\n        \"\"\"\n        :type nums: List[int]\n        :type target: int\n        :rtype: List[int]\n        \"\"\"\n        # create a dictionary to store the number and index\n        dic = {}\n        for i in range(len(nums)):\n            if nums[i] in dic:\n                return [dic[nums[i]], i]\n            else:\n                dic[target - nums[i]] = i",
    "url": "https://leetcode.com/problems/two-sum"
  },
  {
    "title": "Valid Anagram",
    "status": "Accepted",
    "runtime": "19 ms",
    "memory": "17.5 MB",
    "code": "// https://leetcode.com/problems/valid-anagram\n\nclass Solution:\n    def isAnagram(self, s: str, t: str) -> bool:\n        if len(s) != len(t):\n            return False \n        \n        s = sorted(s)\n        t = sorted(t)\n        \n        for i, j in zip(s,t):\n            if i == j:\n                continue\n            elif i != j:\n                return False\n        return True\n\n        ",
    "url": "https://leetcode.com/problems/valid-anagram"
  },
  {
    "title": "Valid Palindrome",
    "status": "Accepted",
    "runtime": "49 ms",
    "memory": "18.1 MB",
    "code": "// https://leetcode.com/problems/valid-palindrome\n\nimport re\n\nclass Solution:\n    def isPalindrome(self, s: str) -> bool:\n        s = re.sub(r'[^a-zA-Z0-9]', '', s)\n        \n        if s.lower() == s[::-1].lower():\n            return True\n        else:\n            return False\n",
    "url": "https://leetcode.com/problems/valid-palindrome"
  },
  {
    "title": "Valid Parentheses",
    "status": "Accepted",
    "runtime": "0 ms",
    "memory": "16.6 MB",
    "code": "// https://leetcode.com/problems/valid-parentheses\n\nclass Solution:\n    def isValid(self, s: str) -> bool:\n        if len(s) < 2:\n            return False\n        \n        open = ['(','{','[']\n        stack = []\n        for braket in s:\n            if braket in open:\n                stack.append(braket)\n            else:\n                if len(stack) == 0:\n                    return False\n                popped = stack.pop()\n                if (braket == ')' and popped != '(') or (braket == '}' and popped != '{') or (braket == ']' and popped != '['):\n                    return False\n        return (len(stack) == 0)\n              ",
    "url": "https://leetcode.com/problems/valid-parentheses"
  },
  {
    "title": "Valid Perfect Square",
    "status": "Accepted",
    "runtime": "43 ms",
    "memory": "13.8 MB",
    "code": "// https://leetcode.com/problems/valid-perfect-square\n\nclass Solution:\n    def isPerfectSquare(self, num: int) -> bool:\n        x = int(num ** 0.5)\n        if x ** 2 == num:\n            return True\n        return False",
    "url": "https://leetcode.com/problems/valid-perfect-square"
  },
  {
    "title": "XOR Operation in an Array",
    "status": "Accepted",
    "runtime": "34 ms",
    "memory": "14.4 MB",
    "code": "// https://leetcode.com/problems/xor-operation-in-an-array\n\nclass Solution:\n    def xorOperation(self, n: int, start: int) -> int:\n        nums = [start + 2 * i for i in range(n)]\n        res = nums[0]\n        for i in range(1, n):\n            res ^= nums[i]\n        return res\n        ",
    "url": "https://leetcode.com/problems/xor-operation-in-an-array"
  }
];
const container = document.getElementById("solutions-container");
const searchInput = document.getElementById("search-input");
const darkModeToggle = document.getElementById("dark-mode-toggle");

// Function to render the problems
function renderProblems(filter = "") {
  container.innerHTML = ""; // Clear the container
  const filteredProblems = problems.filter(problem =>
  problem.title.toLowerCase().includes(filter.toLowerCase())
  );

  filteredProblems.forEach(problem => {
  const card = document.createElement("div");
  card.className = "solution-card";

  card.innerHTML = `
    <h2>${problem.title}</h2>
    <p><strong>Status:</strong> ${problem.status}</p>
    <p><strong>Runtime:</strong> ${problem.runtime}</p>
    <p><strong>Memory:</strong> ${problem.memory}</p>
    <a href="${problem.url}" target="_blank">View Problem</a>
    <h3>Solution:</h3>
    <pre>${problem.code}</pre>
  `;

  container.appendChild(card);
  });
}

// Event listener for the search input
searchInput.addEventListener("input", () => {
  renderProblems(searchInput.value);
});

// Dark mode toggle
let isDarkMode = false;

darkModeToggle.addEventListener("click", () => {
  isDarkMode = !isDarkMode;
  document.body.classList.toggle("dark-mode", isDarkMode);
  document.querySelectorAll(".solution-card").forEach(card => {
  card.classList.toggle("dark-mode", isDarkMode);
  });
  document.querySelector("footer").classList.toggle("dark-mode", isDarkMode);
});

// Initial render
renderProblems();
