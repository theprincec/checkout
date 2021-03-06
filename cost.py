# cost = price x units
def calc_base_cost(category, price, units):
   if category == 'per-unit':
       cost = price * round(units)
   elif category == 'by weight':
       cost = price * units
   elif category == 'markdown':
       discount = .3
       price = (price * (1 - discount))
       cost = price * units
   else:
        cost = 1
   return cost