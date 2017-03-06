import room_find
import data_gather

# subpages = room_find.find_subpages("https://classes.cornell.edu/browse/roster/SP17")
# print(subpages)

# room_pairs = room_find.find_room_time("https://classes.cornell.edu/browse/roster/SP17/subject/AAS")
# print(room_pairs)

# codes = room_find.get_building_codes("https://registrar.cornell.edu/spaces/building-codes")
# print(codes)

all_timings = data_gather.get_all_room_time()
print(all_timings)