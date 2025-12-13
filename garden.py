def max_flowers(plot):
    if not plot or len(plot) == 0:
        return 0
    
    rows = len(plot)
    cols = len(plot[0])
    
    count = 0
    
    # Check each position in the grid
    for i in range(rows):
        for j in range(cols):
            # If current position is empty (0)
            if plot[i][j] == 0:
                # Check if we can plant a cactus here
                can_plant = True
                
                # Check above
                if i > 0 and plot[i-1][j] == 1:
                    can_plant = False
                
                # Check below
                if i < rows - 1 and plot[i+1][j] == 1:
                    can_plant = False
                
                # Check left
                if j > 0 and plot[i][j-1] == 1:
                    can_plant = False
                
                # Check right
                if j < cols - 1 and plot[i][j+1] == 1:
                    can_plant = False
                
                # If we can plant here, increment count and mark it as planted
                if can_plant:
                    plot[i][j] = 1
                    count += 1
    
    return count