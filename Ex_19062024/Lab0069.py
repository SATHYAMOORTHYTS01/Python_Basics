
# function with in the function
def outer_funtion():
    var11 = 30
    var12 = 40

    def inner_funtion():
        print(var11)
    inner_funtion()
    def inner_funtion2():
        print(var12)
    inner_funtion2()
    def inner_funtion3():
        print(var12)
    inner_funtion3()

outer_funtion()