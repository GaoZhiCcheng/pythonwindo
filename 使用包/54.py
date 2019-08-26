def zz(myclass):
    class InnerClass:
        def __init__(self, z=0):
            self.z = 0
            self.wrapper = myclass()

        def position(self):
            self.wrapper.position()
            print('z轴坐标：', self.z)

    return InnerClass


@zz
class coordination:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def position(self):
        print('x轴坐标：', self.x)
        print('y轴坐标：', self.y)
if __name__ == '__main__':
    coor = coordination()
    coor.position()
