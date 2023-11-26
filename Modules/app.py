import converters
from converters import kg_to_lbs
import utils
# import from package
from ecommerce import shipping

shipping.calc_shipping()

print(kg_to_lbs(70))

print(converters.lbs_to_kg(140))

numbers = [1, 12, 4, 8, 30, 6]
print(utils.find_max(numbers))