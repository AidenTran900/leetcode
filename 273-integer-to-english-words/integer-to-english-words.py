unique = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thsnds = ["", "Thousand", "Million", "Billion"]


def helper(num, res):  
   if num<20:
       if num == 0: return
       res.append(unique[num])
       
   elif num<100:
       res.append(tens[num//10])
       helper(num%10, res)
       
   elif num<1000:
       helper(num//100, res)
       res.append('Hundred')
       helper(num%100, res)

   else:  
       for i in (3, 2, 1):
           x = 1000**i
           if num>=x:
               helper(num//x, res)
               res.append(thsnds[i])
               helper(num%x, res)
               break


class Solution:
   def numberToWords(self, num: int) -> str:
       if num == 0: return 'Zero'
       result = []

       helper(num, result)
       return ' '.join(result)