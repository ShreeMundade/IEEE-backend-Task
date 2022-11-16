
class CharPattern :
    @staticmethod
    def main( args) :
        rows = 5
        alphabet = 65
        i = 0
        while (i <= rows) :
            j = 0
            while (j <= rows - i) :
                print(chr((alphabet + j)), end ="")
                j += 1
            k = 1
            while (k <= i * 2 - 1) :
                print(" ", end ="")
                k += 1
            l = rows - i
            while (l >= 0) :
                if (l != rows) :
                    print(chr((alphabet + l)), end ="")
                l -= 1
            print()
            i += 1
        i = rows - 1
        while (i >= 0) :
            j = 0
            while (j <= rows - i) :
                print(chr((alphabet + j)), end ="")
                j += 1
            k = 1
            while (k <= i * 2 - 1) :
                print(" ", end ="")
                k += 1
            l = rows - i
            while (l >= 0) :
                if (l != rows) :
                    print(chr((alphabet + l)), end ="")
                l -= 1
            print()
            i -= 1
    

if __name__=="__main__":
    CharPattern.main([])

# def CharBridge(n):
#     for i in range(n):
#         for j in range(n-1):
#             print(char(j), end='')
#         for k in range(i*2-1):
#             print(end=" ")
#         for l in range(n-i):
#             if(l!=n):
#                 print(char(l), end=''"")
#         print("\n", end='')
# # Driver Code
# n = 6
# CharBridge(n)


# For a given value N, reflect the number of characters taking part in the pattern, starting from A. For N = 5, Participating character would be A B C D E.
# By using a nested for loop we would compute the logic. Where the outer loop of ‘i’ would range from 0 to N and the inner loop of ‘j’ would range from 65(Start) to 64 + 2*N.
# Under which we would check the required condition for the pattern design. For all the values of j which are less than ((64+n)+ i) it would print the (char)((64 + n)-( j % (64+n))) 
# and for all the values of j <= ((64+n) -i) it would print (char)j.

# # Function to print pattern
# def ReverseCharBridge(n):
#     for i in range(n):
#         for j in range(ord('A'), ord('A') +
#                        (2 * n) - 1):
#             if j >= (ord('A') + n - 1) + i:
#                 print(chr((ord('A') + n - 1) - (j % (ord('A') + n - 1))), end='')
#             elif j <= (ord('A') + n - 1) - i:
#                 print(chr(j), end='')
#             else:
#                 print(end=" ")
                
#         print("\n", end='')
#     for i in range(n):
#         for j in range(ord('A'), ord('A') +
#                        (2 * n) - 1):
#             if j >= (ord('A') + n - 1) + i:
#                 print(chr((ord('A') + n - 1) - (j % (ord('A') + n - 1))), end='')
#             elif j <= (ord('A') + n - 1) - i:
#                 print(chr(j), end='')
#             else:
#                 print(end=" ")
                
#         print("\n", end='')
    
    
    
    


# # Driver Code
# n = 6
# ReverseCharBridge(n)

# def CharBridge( n ):
#     for i in range( n ):
#         for j in range( ord('A'), ord('A') +
#                               (2 * n) - 1):
#             if j >= (ord( 'A' ) + n - 1) + i:
#                 print(chr((ord('A') + n - 1) -
#                   (j % (ord('A') + n - 1))), end = '')
#             elif j <= (ord('A') + n - 1) - i:
#                 print(chr(j), end = '')
#             else:
#                 print(end = " ")
#         print("\n", end = '')
# # Driver Code
# n = 6
# CharBridge(n)

def Zpattern(n):
    str=""
    for Row in range(0,n):
        for Col in range(0,n):
            if (((Row == 0 or Row == n-1) and Col >= 0 and Col <= n-1) or Row+Col==n-1):
                str=str+"*"
            else:
                str=str+" "
        str=str+"\n"
    print(str)
n=7
Zpattern(n)
