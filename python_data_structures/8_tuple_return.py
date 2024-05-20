def tuple_return(my_list):
	first_el = my_list[0]
	list_ln = len(my_list)
	if my_list != 0:
		return list_ln, first_el
	else:
		return list_ln, None
