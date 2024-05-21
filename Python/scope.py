# def my_function():
#     local_var="I am local!"
#     print(local_var)
# my_function()
# print(local_var)
global_var= "I am global!"
def show_global ():
    global global_var
    global_var="i am over riding"
    print(global_var,"inside a function")
show_global()
print(global_var)