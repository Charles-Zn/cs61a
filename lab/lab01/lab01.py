def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
#    "*** YOUR CODE HERE ***"
    result=1
    if n<k:
        print("DEBUG:",k)
    elif k==0:
        return result
    while k>0:
        result,n,k=result*n,n-1,k-1
    return result



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
#    "*** YOUR CODE HERE ***"
    sum =0
    front=y
    if front==0:
        return 0
    while front>0:
        front,back=front//10,front%10
        sum+=back
    return sum



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
#    "*** YOUR CODE HERE ***"
    front,count,judge = n,0,0
    while front>0:
        front,back=front//10,front%10
        c=front%10
        if back==c and c==8:
            judge=1
            return True
        count+=1
    if count<2 or judge == 0:
        return False

