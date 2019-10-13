from glob import glob
from random import choice
print(choice(glob ('images/*cat*.jpg')))

print(glob ('images/*cat.jpg'))
print(glob ('images/cat*.jpg'))
print(glob ('images/*cat*.jpg'))
