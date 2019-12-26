// First order function
def apply(f: Int => Unit, v: Int) = f(v)

apply(println, 5)

// nested function
def filter(xs: List[Int], threshold: Int) = {
    def process(ys: List[Int]): List[Int] =
        if (ys.isEmpty) ys
        else if (ys.head < threshold) ys.head :: process(ys.tail)
        else process(ys.tail)
    process(xs)
}
println(filter(List(1, 9, 2, 8, 3, 7, 4), 5))


// currying
def filterIf(xs: List[Int], p: Int => Boolean): List[Int] =
    if (xs.isEmpty) xs
    else if (p(xs.head)) xs.head :: filterIf(xs.tail, p)
    else filterIf(xs.tail, p)

// when we call modN(x) will return a function Int => Boolean
def modN(n: Int)(x: Int) = ((x % n) == 0)

val nums = List(1, 2, 3, 4, 5, 6, 7, 8)
println(filterIf(nums, modN(2)))
println(filterIf(nums, modN(3)))