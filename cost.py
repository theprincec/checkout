# cost = price x units
def calc_base_cost(category, price, units):
   if category == 'per-unit':
       cost = price * units
   else:
        cost = 1
   return cost