import interface

def get_content_search():
    """
    return: start_time,end_time,vehicle_type for search part
    parameters:
    start_time: str
    end_time: str
    vehicle_type: int
    """
    start_time=interface.list1.get()
    end_time=interface.list2.get()
    vehicle_type=int(interface.combobox1.get())
    return start_time,end_time,vehicle_type

def get_content_sort():
    """
    return: ascending and entry_number for sort part
    Parameters:
    ascending: bool
    n_row: int
    """
    ascending_type=interface.combobox2.get()
    if ascending_type=='Ascending order':
        ascending=True
    else:
        ascending=False
    entry_number=int(interface.e1.get())
    return entry_number,ascending




