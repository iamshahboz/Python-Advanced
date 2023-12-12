# Here are top 10 built in class decorators that optimize the python code 


# 1. @classmethod

class GFGClass:
    class_var = 10 

    @classmethod
    def gfg_class_method(cls):
        print('This is class method')
        print(f' Value of the class variable {cls.class_var}')
    


GFGClass.gfg_class_method()
