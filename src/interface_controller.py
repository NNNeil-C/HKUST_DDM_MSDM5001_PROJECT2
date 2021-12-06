def get_content_search(elements):
    """
    return: start_time,end_time,vehicle_type for search part
    parameters:
    start_time: str
    end_time: str
    vehicle_type: int
    """
    start_time = elements[0].get()
    end_time = elements[1].get()
    vehicle_type = int(elements[2].get())
    return start_time, end_time, vehicle_type


def get_content_sort(elements):
    """
    return: ascending and entry_number for sort part
    Parameters:
    ascending: bool
    n_row: int
    """
    #ascending_type = interface.combobox2.get()
    ascending_type = elements[0].get()
    if ascending_type == 'Ascending order':
        ascending = True
    else:
        ascending = False
    # 5 indicates 'TripLength'
    column_index = int(elements[1].get())-1 if len(elements) > 3 else 5
    number_of_entry_to_show = int(elements[2].get())
    return ascending, column_index, number_of_entry_to_show
