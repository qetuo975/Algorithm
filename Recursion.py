# Recursion

# Bir Yapının Yinelenmesidir.
# Recursive Metotlar Yinelemeli Metotlar Olarak Adlandırılır.
# For Loop yada While loop Çözüm Olmadığında Recursion Kullanılır.


def Factorial(n):
    print(n)

    # base case
    if n == 0:
        return 1
    else:
        return n * Factorial(n - 1)


# Factorial(5)


def Summation(n):
    print(n)

    # base case
    if n == 0:
        return 0
    else:
        return n + Summation(n - 1)


# Summation(5)


# Recursion ile String'in Tersini Bulmak

# Reverse("Deep") = peed

# (Reverse("eep") + d = pee

# Reverse("ep") + e = pe

# Reverse("p") + e  = p

def Reverse(String):
    print(String)

    # base case
    if len(String) == 1:
        return String

    else:
        return ReverseString(String[1:]) + String[0]


# Reverse("Deep")


# MultiPly(2,3) = 6

#          2  + MultiPly(2,2) = 4

#                        2 + MultiPly(2,1) = 2

#                                     2 + MultiPly(2,0) = 0
def MultiPly(x, y):
    # base case
    if y == 0:
        return 0

    # recursion
    return (x + MultiPly(x, y - 1))


# MultiPly(5,5)


# Power(2,3) = 8

#          MultiPly(2, Power(2,2)) = 4

#                        MultiPly(2, Power(2,1)) = 2

#                                     MultiPly(2, Power(2,0)) = 1


def MultiPly(x, y):
    # base case
    if y == 0:
        return 0

    # recursion
    return (x + MultiPly(x, y - 1))


def Power(a, b):
    # base case
    if b == 0:
        return 1

    # recursion
    return MultiPly(a, Power(a, b - 1))


Power(2, 3)

