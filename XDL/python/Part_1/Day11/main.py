from XDL.hsq.Day11.bullet import Bullet
from XDL.hsq.Day11.gun import Gun
from XDL.hsq.Day11.person import Person

if __name__ == "__main__":
    bullet = Bullet(100)
    gun = Gun(bullet)
    p = Person(gun)

    p.fire(99)
    p.fire(2)
    p.fill(3)
    p.fire()
