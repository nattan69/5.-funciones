def computepay(h, r) :
    if h > 40:
        xhrs = 40 * r + (h - 40) * r * 1.5
    else:
        xhrs = h * r
    return xhrs

hrs = float(input('Enter hours: '))
rate = float(input("enter rate:"))
xpay = computepay(hrs, rate)
print ("Pay", xpay)
