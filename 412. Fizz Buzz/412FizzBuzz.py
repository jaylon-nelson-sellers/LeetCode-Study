class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        fizzBuss
        @sum coded version of the game fizzbuzz
        @n: int. Value to count up to 
        @return: List[str]. A list of strings counting to n. Does not include zero (starts at 1)
        """

        #Had to google how to initilize an empty array. Turns out you can use append instead to dynamically size it
        answer = [0] * n
        for i in range(n):
            temp = i+1
            #Important to do this first, as others should not override this check
            if temp % 3 == 0 and temp % 5 == 0:
                answer[i] = "FizzBuzz"
            elif temp % 3 == 0:
                answer[i] = "Fizz"
            elif temp % 5 == 0:
                answer[i] = "Buzz"
            else:
                answer[i] = str(temp)
        return answer
    
    def fizzBuzz(self, n: int):
        """
        Cool solution with terniary operator
        """
        ans = []
        for i in range(1, n + 1):
            ans.append(
                "FizzBuzz" if i % 15 == 0 else
                "Buzz" if i % 5 == 0 else
                "Fizz" if i % 3 == 0 else
                str(i)
            )
        return ans
