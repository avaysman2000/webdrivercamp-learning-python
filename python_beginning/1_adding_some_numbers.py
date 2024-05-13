#Modify the print to use this variable to get: Learning Python is fun"' - 100 %
#
var1 = 100
#
#print("""Learning Python is fun"'"""," - ", var1,"%")
#
#Formatted String
#
formatted_string = f"""Learning Python is fun"' - {var1}%"""
print(formatted_string)
#
#.format()
#
formatted_string = """Learning Python is fun"' - {0}%""" .format(var1)
print(formatted_string)
#
#% formatting
#
formatted_string = """Learning Python is fun"' - %d%%""" % var1
print(formatted_string) 
