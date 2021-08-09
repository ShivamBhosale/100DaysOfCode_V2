def overlap(r1, r2):
    
    r1_x, r1_y = r1['x'], r1['y']
    r2_x, r2_y = r2['x'], r2['y']
    
    
    r1_x_range, r1_y_range = r1['h'], r1['w']
    r2_x_range, r2_y_range = r2['h'], r2['w']
    
    
    if r2_x in range(r1_x + r1_x_range) and \
    r2_y in range(r1_y + r1_y_range):
        
        return True
    
    else:
        
        return False

r1 = {'x': 2 , 'y': 4,'w':5,'h':12}
r2 = {'x': 1 , 'y': 5,'w':7,'h':14}
print(overlap(r1,r2))