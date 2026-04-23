message = "kamal Nanduru is one of the best software engineers in the world"

print("1.", message.capitalize())  # First character uppercase
print("2.", message.casefold())  # Converts to lowercase (stronger than lower)
print("3.", message.center(50))  # Centers string with padding
print("4.", message.count("a"))  # Counts occurrences of 'a'
print("5.", message.encode())  # Converts to bytes
print("6.", message.endswith("world"))  # Checks if string ends with 'world'
print("7.", message.expandtabs())  # Expands tabs (no effect here)
print("8.", message.find("best"))  # Returns index of 'best' or -1 if not found
print("9.", message.format())  # Formats string (no placeholders here)
print("10.", message.format_map({}))  # Formats using dictionary (empty here)
print("11.", message.index("best"))  # Returns index of 'best' (error if not found)
print("12.", message.isalnum())  # Checks if all characters are alphanumeric
print("13.", message.isalpha())  # Checks if all are alphabets
print("14.", message.isdecimal())  # Checks if all are decimal numbers
print("15.", message.isdigit())  # Checks if all are digits
print("16.", message.isidentifier())  # Checks if valid Python identifier
print("17.", message.islower())  # Checks if all characters are lowercase
print("18.", message.isnumeric())  # Checks if all are numeric
print("19.", message.isprintable())  # Checks if all are printable
print("20.", message.isspace())  # Checks if all are spaces
print("21.", message.istitle())  # Checks if string is in title case
print("22.", message.isupper())  # Checks if all characters are uppercase
print("23.", message.join("Hello"))  # Joins each char of "Hello" with message
print("24.", message.ljust(50))  # Left-aligns string
print("25.", message.lower())  # Converts to lowercase
print("26.", message.lstrip())  # Removes leading spaces
print("27.", message.maketrans("a", "e"))  # Creates translation table (a→e)
print("28.", message.partition("best"))  # Splits into 3 parts at 'best'
print("29.", message.replace("best", "great"))  # Replaces 'best' with 'great'
print("30.", message.rfind("best"))  # Last occurrence index or -1
print("31.", message.rindex("best"))  # Last occurrence index (error if not found)
print("32.", message.rjust(50))  # Right-aligns string
print("33.", message.rpartition("best"))  # Splits into 3 parts from right
print("34.", message.rsplit())  # Splits into list (from right)
print("35.", message.rstrip())  # Removes trailing spaces
print("36.", message.split())  # Splits string into words
print("37.", message.splitlines())  # Splits by line breaks
print("38.", message.startswith("kamal"))  # Checks if starts with 'kamal'
print("39.", message.strip())  # Removes leading & trailing spaces
print("40.", message.swapcase())  # Swaps lowercase ↔ uppercase
print("41.", message.title())  # Capitalizes first letter of each word
print("42.", message.translate(message.maketrans("a", "e")))  # Replaces 'a' with 'e'
print("43.", message.upper())  # Converts to uppercase
print("44.", message.zfill(50))  # Pads with zeros on left