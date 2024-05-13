#Modify the prints to get the float number printed with only 2 digits followed
#
var1 = 3.141592653589793238
#
#print("""Learning Python is fun"'"""," - ", var1,"%")
#
#Formatted String
#
formatted_string = f"""Learning Python is fun"' - {var1:.2f}%"""
print(formatted_string)
#
#.format()
#
formatted_string = """Learning Python is fun"' - {:.2f}%""" .format(var1)
print(formatted_string)
#
#% formatting
#
formatted_string = """Learning Python is fun"' - %.2f%%""" % var1
print(formatted_string)
