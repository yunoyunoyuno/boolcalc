import boolcalc

inp = "T ^ T <--> ( T --> F v ( T ^ T ) )".split(" ")
print(boolcalc.calculate(inp))

inp = "( ( ( T --> F --> T v F ) <--> T ) ^ T )".split(" ")
print(boolcalc.calculate(inp))

inp = "( ( ( T --> F --> T v F ) <--> T ) ^ T ) ".split(" ")
print(boolcalc.calculate(inp))
