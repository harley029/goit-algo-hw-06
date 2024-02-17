class Pet:
    __PI=3.1427
    def __init__(self,name:str,age:int,color:str):
        self.name=name
        self.age=age
        self.color=color
        self.__count=0

    def setCount(self,count:int):
        self.__count=count
    
    def voice(self,phrase:str):
        print(phrase)
        
    def walk(self) -> str:
        return 'step '*self.__count
