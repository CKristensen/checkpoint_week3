Jordan_belfort = {'calls': 178, 'meetings':17,  'sales':6}

def calculate_points(employee_dic):
    """ each call 10pts
        each meeting 30pts
        each sale 100pts
        bonus 100pts if more than 150call/20meetings/5sales
    Args:
        employee_dic (dictionary): [description]
    """    
    calls_pts = employee_dic['calls']*10
    meetings_pts = employee_dic['meetings']*30
    sale_pts = employee_dic['sales']*100
    bonus = 100*sum([(employee_dic['calls']>150),(employee_dic['meetings']>20),(employee_dic['sales']>5)])

    employee_dic['score'] = calls_pts + meetings_pts + sale_pts + bonus


calculate_points(Jordan_belfort)
print(Jordan_belfort)
