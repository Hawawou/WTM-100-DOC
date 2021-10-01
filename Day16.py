import world
print(world)

world.africa
#does not import spain
from world import europe
#imports spain omly
import world.europe.spain 
from world.africa import cameroon


# structuring imports