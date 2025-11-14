# 11-1 and 11-2 are included in this code
from cityfunctopt import city_country

def testcity():
    canada = city_country("montreal", "canada")
    assert canada == "montreal, canada"

def testpop():
    canada = city_country("montreal", "canada", population=2_000_000)
    assert canada == "montreal, canada population 2000000"

