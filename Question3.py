Jordan_belfort = {'calls': 178, 'meetings':17,  'sales':6}

def calculate_points(employee_dic):
    calls_pts, meetings_pts, sale_pts  = employee_dic['calls']*10, employee_dic['meetings']*30, employee_dic['sales']*100
    bonus = 100*sum([(employee_dic['calls']>150),(employee_dic['meetings']>20),(employee_dic['sales']>5)])
    employee_dic['score'] = calls_pts + meetings_pts + sale_pts + bonus
    return employee_dic


calculate_points(Jordan_belfort)
print(Jordan_belfort)
