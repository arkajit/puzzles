/**
 * Assume you're given a list of stock prices for the next N days. Each day you can buy one unit or
 * sell any number of units you already own. What is the maximum profit you can earn?
 *
 * Input format:
 *   T   (Number of testcases: 1 - 10)
 *   N   (Number of prices in this test case: 1 - 50,000)
 *   p1 p2 p3 ... pN   (N prices in this test case, separated by spaces)
 *   ...
 * Output: T lines, one answer (max profit) per line.
 */
object StockMax {
  def maxProfit(prices: List[Int]) = {
    val maxes = prices.scanRight(0) { case (price, prevMax) =>
      math.max(price, prevMax)
    }.dropRight(1)

    // Make profits Longs since max sum could be as high as 5B which won't fit in a 32-bit Integer.
    prices.zip(maxes).map { case (buy, sell) => (sell - buy).toLong }.sum
  }

  def main(args: Array[String]) {
    val it = io.Source.fromFile("input.txt").getLines
    val T = it.next().toInt
    for (t <- 1 to T) {
      val N = it.next().toInt
      val prices = it.next().split(" ").map { _.toInt }.toList
      println(maxProfit(prices))
    }
  }
}
