// mixin classes
abstract class Iterator {
    type T
    def hasNext: Boolean
    def next: T
}

trait RichIterator extends Iterator {
    def foreach(f: T => Unit) {
        while (hasNext) f(next)
    }
}

class StringIterator(s: String) extends Iterator {
  type T = Char
  private var i = 0
  def hasNext = i < s.length()
  def next() = { val ch = s charAt i; i += 1; ch }
}

object StringIteratorTest {
  def main(args: Array[String]) {
    // will inherit only the new methods from rich (RichIterator must be a trait)
    class Iter extends StringIterator("Scala") with RichIterator
    val iter = new Iter
    iter foreach println
  }
}