// # Types
let v1: Bool = false
let v2: String = "Text"
let v3: Int = 42
let v4: Float = 42
let v5: Double = 42

// Functions are first-class type, it can be passed and returned. It is a special case of closure
// creating a closure
let myClosure = ({ (x: Int) -> Int in
    return x * x
})
// create a const to receive the closure
let myFunction: ((Int) -> Int) = myClosure

// no need to import IO
print("Hello World!")

// # Declaring Vars and Constants
// const
let f: Float = 3
// var
var x = "Eita pleula " + String(f)

var y = "\(x) Eita meniano \(3 + 4)"
var multiline = """
So nice to have \(x)
"""

// # Array and Maps
var myFruits = [String]()
myFruits.append("apple")

myFruits = [] // infer

var myMap = [String: String]()
myMap["key-1"] = "value-1"
myMap = [:] // also infer


// # Control FLow
var n = 2
while n < 100 {
    n *= 2
}
print(n)

var m = 2
repeat {
    m *= 2
} while m < 100
print(m)


let individualScores = [75, 43, 103, 87, 12]
var teamScore = 0
// () are optional
for score in individualScores {
    if (score > 50) {
        teamScore += 3
    } else {
        teamScore += 1
    }
}
print(teamScore)


let interestingNumbers = [
    "Prime": [2, 3, 5, 7, 11, 13],
    "Fibonacci": [1, 1, 2, 3, 5, 8],
    "Square": [1, 4, 9, 16, 25],
]
var largest = 0
for (kind, numbers) in interestingNumbers {
    for number in numbers {
        if number > largest {
            largest = number
        }
    }
}
print("Largest: \(largest)")

// ## For in range
print("From 0 to 3, exclusive")
for i in 0..<3 {
    print("i = \(i)")
}

print("From 0 to 3, inclusive")
for i in 0...3 {
    print("i = \(i)")
}



// ## Switch
let vegetable = "red pepper"
switch vegetable {
    case "celery":
        print("Add some raisins and make ants on a log.")
    case "cucumber", "watercress":
        print("That would make a good tea sandwich.")
    case let x where x.hasSuffix("pepper"):
        print("Is it a spicy \(x)?")
    default: // some types requires default case
        print("Everything tastes good in soup.")
}


// # Optional
var inputedName: String? = "Odair"

print("Is null ? \(inputedName == nil)")

// we can use let on if to se if has value
if let name = inputedName {
    print("His name is \(name)")
} else {
    print("He is anonymous")
}

var nickname: String? = nil
var defaultValue = "Random"
print("His nickname is \(nickname ?? defaultValue)")



// # Functions and Closures
// the parameter name is the argument's default name, we can define a name
// to it or use "_" to use no name
func greet(_ person: String, on day: String, lunch: String, hours: Int = 12) -> String {
    return "Hello \(person), today is \(day) and we will have \(lunch) at \(hours) o'clock."
}
greet("John", on: "Wednesday", lunch: "pizza")

// return tuple
func createPair(first: String, second: String) -> (first: String, second: String) {
    return (first, second)
}
let myPair = createPair(first: "Odair", second: "Jose")
print("Pair: \(myPair.first) and \(myPair.1)")

// ## Nested Functions
func outerFunc() -> Int {
    func innerFunc() -> Int {
        return 42
    }
    return innerFunc()
}
print("Anwser: \(outerFunc())")

// ## Returning Functions
func getOperation() -> ((Int) -> Int) {
    func square(x: Int) -> Int {
        return x * x
    }
    return square
}
print("Operation result passing 2: \(getOperation()(2))")

// ## Ways to writing closures
let numbers = [1, 1, 2, 3, 5, 8, 11]
var squares = numbers.map({ (n: Int) -> Int in return n * n})
squares = numbers.map({ n in n * n }) // infer and only one statement to just return
squares = numbers.map { n in n * n } // when the function expect only a function
squares = numbers.map() { n in n * n } // when the function received a function in the last paramenter we can write it after the ()
squares = numbers.map { $0 * $0 } // we can refer the parameters using its indexes
print(squares)



// # Object and Class
class Person {
    let minAge = 0
    var name = ""
    
    init(_ name: String) {
        self.name = name
    }
    
    func greets() -> String {
        return "Hi, my name is \(self.name)"
    }
}
var p = Person("Odair Jose")
print(p.greets())

// ## Inherits, Getter, Setter and property observer
class Player: Person {
    private var myOwnGame: String
    
    init(name: String, game: String, level: Int = 1) {
        self.myOwnGame = game
        self.level = level
        super.init(name)
    }
    
    // getter and setter
    var game: String {
        get {
            return self.myOwnGame
        }
        set { // we can also set the var name using: set(myNewGame)
            self.myOwnGame = newValue
        }
    }
    
    // observer of property
    var level: Int {
        willSet {
            print("Will change level from \(self.level) to \(newValue)")
            if newValue < 0 || newValue > 5 {
                print("Invalid level")
            }
        }
        didSet {
            print("Changed level from \(oldValue) to \(self.level)")
        }
    }
    
    override func greets() -> String {
        return "\(super.greets()), I play \(self.game) on level \(level)"
    }
}
var player = Player(name: "Odair Jose", game: "CS GO")
print(player.greets())
player.game = "F1 2018"
player.level = 4
print(player.greets())

// ## Optional operator
var optionalPlayer: Player? = Player(name: "Anonymous", game: "Mario Bros")
// if optionalPlayer is nil then the whole expression is resolved to nil, greets() is ignored
// if optionalPlayer is non nil then the expression is resolved and returned wrapped in Optional
print(optionalPlayer?.greets())



// # Enumerations and Structures
// we can extend a type or just make it as a new one
enum League {
    case National, Worldwide
}
print(League.Worldwide)

// when extending a type it will have a property rawValue
enum Rank: Int {
    case gold = 1 // by default starts from 0
    case silver, iron, wood
    
    func description() -> String {
        switch self {
        case .gold: // .gold is a shortcut for Rank.gold
            return "Gold"
        case .silver:
            return "Silver"
        default:
            return "Too Low"
        }
    }
}

print("Enum Rank.\(Rank.gold) has value \(Rank.gold.rawValue)")
print("Enum Rank.\(Rank.iron) has value \(Rank.iron.rawValue)")
// Create enum from raw value, can return nil
print("Enum with value 3: \(Rank(rawValue: 3))")
