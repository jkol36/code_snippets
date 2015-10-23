


#recursively searches the keys of a dictionary and checks to see if the key matches an items in the items list
#accepts Tuples, or lists for items, and a dictionary object to search through
def search_dictionary_for_certain_keys(key, dictionary):
	val = None
	for k, value in dictionary.iteritems():
		if k == key or k.__contains__(key) or key.__contains__(k):
			return value

		else:
			if isinstance(value, dict):
				item = search_dictionary_for_certain_keys(key, value)
				if item is not None:
					return item

