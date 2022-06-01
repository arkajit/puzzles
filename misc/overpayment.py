SAME_NOTE = "Same as in-store"
PERCENTAGE_SIGN = "%"
HIGHER = "higher"
LOWER = "lower"

# Returns percentage difference (in units of 0.0 - 1.0) embedded in the note
def get_percentage_diff(note):
  if note == SAME_NOTE:
    return 0
  tokens = note.split(" ")
  percentage = float(tokens[0].strip(PERCENTAGE_SIGN))
  if tokens[1] == HIGHER:
    return percentage/100
  elif tokens[1] == LOWER:
    return (-1 * percentage)/100
  else:
    raise ValueError("Unexpected note")
    
def in_store_price(price, perc_diff):
  if perc_diff == 0:
    return price
  else:
    # Diff is higher than 100% if price is higher
    return round(price / (1 + perc_diff), 6)
    

def solution(prices, notes, x):
  overpayments = [(p - in_store_price(p, get_percentage_diff(n))) for (p, n) in zip(prices, notes)]
  print(overpayments)
  total_over = sum(overpayments) 
  return total_over <= 
