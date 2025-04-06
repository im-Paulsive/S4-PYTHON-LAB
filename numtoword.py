def number_to_words(num):
    if num == 0:
        return "Zero"

    below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                "Seventeen", "Eighteen", "Nineteen"]

    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    thousands = ["", "Thousand", "Million", "Billion"]

    def helper(n):
        if n == 0:
            return ""
        elif n < 20:
            return below_20[n] + " "
        elif n < 100:
            return tens[n // 10] + " " + helper(n % 10)
        else:
            return below_20[n // 100] + " Hundred " + helper(n % 100)

    result = ""
    i = 0
    while num > 0:
        if num % 1000 != 0:
            result = helper(num % 1000) + thousands[i] + " " + result
        num //= 1000
        i += 1

    return result.strip()
