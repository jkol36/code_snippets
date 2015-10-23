def check_string_and_join_two_strings_by_dash(string): #joins string 1 and string 2 together seperated by a - if string 1 contains a space
	tmpString = string.split() #split our string at the empty space
	if len(tmpString) > 1: #if our temporary string (now a list)'s length is greater than one
		string = '-'.join(x for x in tmpString) #join both strings together seperated by a -

	else:
		string = tmpString[0]
	return string