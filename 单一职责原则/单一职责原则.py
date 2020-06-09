# 交通工具类


class Vehicle():
    def run(self, vehicle):
        print(vehicle + "在公路飙车")


class RoadVehicle():
    def run(self, vehicle):
        print(vehicle + "在公路飆車")


class AirVehicle():
    def run(self, vehicle):
        print(vehicle + "在天空飆車")


class WaterVehicle():
    def run(self, vehicle):
        print(vehicle + "在水里飆車")


class Vehicle3():
    def run(self, vehicle):
        print(vehicle + "在公路飆車")

    def runAir(self, vehicle):
        print(vehicle + "在天空飆車")

    def runWater(self, vehicle):
        print(vehicle + "在水中飆車")


if __name__ == '__main__':
    # 寻常写法
    # 方案1
    # 1.在方式1的run方法中,违反了单一职责原则
    # 2.解决的方案非常简单,根据交通工具运行方法不同,分解成不同类即可
    # Vehicle.run(Vehicle, "提莫")
    # Vehicle.run(Vehicle, "盲僧")
    # Vehicle.run(Vehicle, "剑圣")

    # 方案2的分析
    # 遵守单一职责原则
    # 但是这样改动很大,即将类分解,同事修改客户端
    # 改进:直接修改vehicle类
    # roadVehicle = RoadVehicle()
    # airVehicle = AirVehicle()
    # waterVehicle = WaterVehicle()
    # roadVehicle.run("汽车")
    # airVehicle.run("飞机")
    # waterVehicle.run("🐟")

    # 方案3分析
    # 这种修改方法没有对原来的类做大的修改,只是新增方法
    # 这里虽然没有在类这个级别上遵守单一职责原则,但是在方法级别上,任然是遵守单一职责
    vehicle = Vehicle3()
    vehicle.run("汽车")
    vehicle.runAir("飞机")
    vehicle.runWater("🐟")

# 1.降低类的复杂度,一个类只负责一项职责
# 2.提高类的可读性,可维护性
# 3.降低变更引起的风险

