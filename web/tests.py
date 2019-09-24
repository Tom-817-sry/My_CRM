from django.test import TestCase

# Create your tests here.

d = {'a':'aa','b':'bb','c':'cc','d':'dd'}

for i in d.items():
    print(type(i))
    print(i)