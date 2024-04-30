def f(x):
    units = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]

    if 0 <= x < 10:
        return len(units[x])
    elif 10 <= x < 20:
        return len(teens[x - 10])
    elif 20 <= x < 100:
        return len(tens[x // 10]) + len(units[x % 10])
    elif 100 <= x < 1000:
        if x % 100 == 0:
            return len(units[x // 100]) + len("HUNDRED")
        else:
            return len(units[x // 100]) + len("HUNDREDAND") + f(x % 100)

x = int(input())

result = x
for i in range(1000):
    result = f(result)

print(result)
