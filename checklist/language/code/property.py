# @property将方法伪装为属性,外部可通过属性方式访问内部变量

class MyClass:
    def __init__(self,value):
        self.value=value
        
    @property
    def value(self):
        return self._value #为了避免循环调用问题
    
    @value.setter
    def value(self,new_value):
        self._value =new_value
        
    @value.deleter
    def value(self):
        del self._value #_开头表示内部使用,为了区分函数value()
    