from Stack import Stack

def network_path_exists(network, start_x, start_y):
    s = Stack()
    s.push((start_x,start_y))
    step = 1
    network[start_x][start_y] = step

    directions = [(-1,0),(0,-1),(1,0),(0,1)]

    while not s.isEmpty():
        x,y = s.peek()

        moved = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if network[nx][ny] == 'G':
                return True
            elif network[nx][ny] == ' ':
                step += 1
                network[nx][ny] = step
                s.push((nx, ny))
                moved = True
                break
        if not moved:
            s.pop()
    return False

