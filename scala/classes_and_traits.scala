class Animal

// Criate a class with private attr power
class Weapon(var power: Double) { // var is mutable
    // void method
    def increase: Unit = {
        power = power + 1
    }
}

val w1 = new Weapon(88)
println(w1)
val w2 = new Weapon(90)

// cant access it (by default is private)
// w1.power > w2.power



// case keywork will turn the parameters public
// case class are immutable and can be compared using ==
case class Person(val name: String) // val is immutable

val p1 = new Person("Odair")
val p2 = Person("Jose")
println(p1.name + " " + p2.name)


abstract class Move {

}

// like interfaces but can extends abstract class
trait Fighter extends Move {
    def punch(): Unit
}

class Warrior(_person: Person, _weapon: Weapon) extends Fighter {
    def person = {
        _person
    }

    def weapon = {
        _weapon
    }

    override def punch = {
        println("Punch!")
    }

    override def toString = {
        "{ person: " + person + ", weapon: " + weapon + "}"
    }
}

val wr1 = new Warrior(p1, w1);
println(wr1.toString)
val wr2 = new Warrior(p2, w2);
println(wr2 toString)
