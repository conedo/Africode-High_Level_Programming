# import sys
# max_recursion=sys.getrecursionlimit()
# print(max_recursion)
# def hello():
#     print(hello)
#     hello()
# hello()
# def count_down(start):
#     '''count_down from a number'''
#     print(start)
#     if start<25:
#         count_down(start+1)
# count_down(0)
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# result = fact(10)
# print(result)
def factorial(n):
    '''calculate the factorial of a number'''
    if n==0:
      return 1
    else:
      return n*(n-1)
print(factorial(5))
