# from django.test import TestCase

# Create your tests here.

a = True
b = True
c = []

result1 = all([a, b, c])
result2 = any([a, b, c])

print(result1, result2, sep='\n')