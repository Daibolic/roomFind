import room_find

subpages = room_find.find_subpages("https://classes.cornell.edu/browse/roster/SP17")
print(subpages)

room_pairs = room_find.find_room_time("https://classes.cornell.edu/browse/roster/SP17/subject/AAS")
print(room_pairs)