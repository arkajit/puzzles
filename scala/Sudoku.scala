object Sudoku extends App {
  def cross(A: String, B: String) = for (a <- A; b <- B)
    yield (a.toString + b.toString)

  val digits = "123456789"
  val rows = "ABCDEFGHI"
  val cols = digits
  val squares = cross(rows, cols)
  val unitlist =
    cols.map { (c: Char) => cross(rows, c.toString) } ++
    rows.map { (r: Char) => cross(r.toString, cols) } ++
    (for {
      rs <- List("ABC", "DEF", "GHI")
      cs <- List("123", "456", "789")
    } yield cross(rs, cs))
  val units = squares.map { s =>
    (s, unitlist.filter { _.contains(s) })
  }.toMap
  val peers = squares.map { s =>
    (s, units(s).flatten.toSet - s)
  }.toMap

  def test = {
    assert(squares.size == 81)
    assert(unitlist.size == 27)
    assert(squares.forall { units(_).size == 3 })
    assert(squares.forall { peers(_).size == 20 })
    println("All tests pass")
  }

  test
}
