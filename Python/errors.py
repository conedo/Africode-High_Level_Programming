# try:
#     result=3/0
# except ZeroDivisionError:
#     print(divion by zero wrong)
# try:
#     x =int(input("enter a number"))
#     y=1/x
# except (ValueError,ZeroDivisionError):
#     print("invalid input")
# try:
#     risky_operation()
# except Exception as e:
#     print(f'An error occured: {e}')
def validate_age(age):
    if age <18:
        raise ValueError("age must be 18 or older")
    else:
        return True
    
try:
    validate_age(20)
except ValueError as e:
    print(e)
else:
    print("meets the minimum age")
finally:
    print("i always run no matter what")