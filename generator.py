def unp_generator(list_to_unp):
    if type(list_to_unp) != list:
        yield list_to_unp
    else:  
        for _i in list_to_unp:
            for _k in unp_generator(_i):
                yield _k


if __name__ == '__main__':
    nested_list = [
  	    ['a', 'b', 'c'],
  	    ['d', 'e', ['f', ['h']], False],
  	    [1, 2, None],
     ]
  
  
    for item in unp_generator(nested_list):
        print(item)