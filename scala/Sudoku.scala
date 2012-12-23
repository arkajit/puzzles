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
    assert(units("C2") == List(
      List("A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2"),
      List("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"),
      List("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")
    ))
    assert(peers("C2") == Set("A2", "B2", "D2", "E2", "F2", "G2", "H2", "I2",
                              "C1", "C3", "C4", "C5", "C6", "C7", "C8", "C9",
                              "A1", "A3", "B1", "B3"))
    println("All tests pass")
  }

  test
}
