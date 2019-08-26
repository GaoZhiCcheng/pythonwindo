def zz(myclass):
    class InterClass:
        def __init__(self,z=0):
            self.z = 0
            self.wrapper = myclass()


        def position(self):
            self.wrapper.position()
            print('z轴坐标：',self.z)
    return InterClass
@zz
class coordination:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def position(self):
        print('x轴的坐标是：',self.x)
        print('y轴的坐标是：',self.y)

if __name__ ==  '__main__':

    coor = coordination()
    coor.y=20
    coor.position()