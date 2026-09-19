def total_profits(n):
    prices = [1, n, 1, n]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

input("total_profits(n) sums every upswing in prices [1, n, 1, n]   Press Enter")
print("  total_profits(4)  = ", total_profits(4))
print("  total_profits(5)  = ", total_profits(5))
n = int(input("Enter n (try 6 or 7): "))
guess = input("WHat is total_profits(n) for n = " + str(n) + "? ")
input("add every positive step - teo peaks contibute n -1   Press Enter")
print("   total profits(" + str(n) + ")  = ", total_profits(n), "  your guess was ", guess)