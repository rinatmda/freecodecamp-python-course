import numpy as np

def calculate(list):
    if len(list) == 9:
        x = np.array(list).reshape(3,3)
        method = {'mean': x.mean,
                'variance': x.var,
                'standard deviation': x.std,
                'max': x.max,
                'min': x.min,
                'sum': x.sum}
        axes = [0, 1, None]
        calculations = {} 
        for m in method:
            results_for_method = []
            for a in axes:
                result = method[m](axis = a).tolist()  #calculation for given statistical method m and given axis a
                results_for_method.append(result)   
            calculations[m] = results_for_method    
    else:
        raise ValueError('List must contain nine numbers.')

    return calculations