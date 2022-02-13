# remove duplicates from a list 
# it is possible to use the set() but it messes up the original order of your dup_list so i used the dict.fromkeys() 

# list with duplicates 
dup_list = [2, 3, 4, 5, 6, 3, 6, 2]

# removes duplicates and makes it a dic 
remove_dup = dict.fromkeys(dup_list)

# now converr dic to final list 
no_dup_list = list(remove_dup)
print(no_dup_list) 

# to do this in one line 
print(list(dict.fromkeys(dup_list)))