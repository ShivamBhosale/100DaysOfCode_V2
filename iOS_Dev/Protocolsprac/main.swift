protocol CanFly {
    func fly()
}

class Bird {
    
    var isFemale = true
    
    func layEgg() {
        if isFemale {
            print("This bird will lay egg.")
        }
    }
    
}

class Eagle: Bird, CanFly {
    func fly() {
        print("Eagle flaps  its wings anf lifts off into th sky")
    }
    
    
    func soar()
    {
        print("Able to glide using the air currents.")
    }
    
}
struct FlyingMuseum {
    func flyingDemo(flyingObject: CanFly)
    {
        flyingObject.fly()
    }
}

class Penguin: Bird {
    func swim()
    {
        print("Able to swim.")
    }
}

struct Airplane: CanFly {
    func fly() {
        print("Uses jet engines to fly.")
    }
}

let myEagle = Eagle()
let myPenguin = Penguin()
let museum = FlyingMuseum()
let myPlane = Airplane()
museum.flyingDemo(flyingObject: myPlane)
museum.flyingDemo(flyingObject: myEagle)
myEagle.fly()
myPlane.fly()
