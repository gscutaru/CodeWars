"""
Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or
camelCase in Java) for strings.
All words must have their first letter capitalized without spaces.
For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
"""

def camel_case(string):
    new_string = string.split(" ")
    alt_string = []
    for i in range(len(new_string)):
        alt_string += new_string[i].title()
    return "".join(alt_string)

print(camel_case("camel base word jocker"))
