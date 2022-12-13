'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if from_member in social_graph[to_member]["following"] and to_member in social_graph[from_member]["following"]:
        return "friends"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    else:
        return "no relationship"
    
def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    
    for column in board:
        temp = ""
        for row in range(len(board)):
            if x == "":
                x = board[row][column]
            elif temp == board[row][column]:
                if row + 1 == len(board):
                    return x
                continue
            else:
                break
    
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    elif len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    #    if first_stop == "upd" and second_stop == "admu":
    #    return int(legs[("upd","admu")]["travel_time_mins"])
    #if first_stop == "admu" and second_stop == "dlsu":
    #    return int(legs[("admu","dlsu")]["travel_time_mins"])
    #if first_stop == "dlsu" and second_stop == "upd":
    #    return int(legs[("dlsu","upd")]["travel_time_mins"])
    #if first_stop == "upd" and second_stop == "dlsu":
    #    return int(legs[("upd","admu")]["travel_time_mins"]) + int(legs[("admu","dlsu")]["travel_time_mins"])
    #if first_stop == "admu" and second_stop == "up":
    #    return int(legs[("admu","dlsu")]["travel_time_mins"]) + int(legs[("dlsu","up")]["travel_time_mins"])
    #if first_stop == "dlsu" and second_stop == "admu":
    #    return int(legs[("dlsu","up")]["travel_time_mins"]) + int(legs[("up","admu")]["travel_time_mins"])
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    key=list(route_map.keys())
    firstkey=[item[0] for item in key]
    secondkey=[item[1] for item in key]
    time=list(route_map.values())
    answer=[]
    final=[]
    
    position1=firstkey.index(first_stop)
    position2=secondkey.index(second_stop)
    
    for x in range(len(time)):
        answer=answer+list(time[x].values())
        
    if first_stop==second_stop:
        return sum(answer)
    elif position1==position2:
        return answer[position1]
    elif position1 < position2:
        final = answer[position1:position2 + 1]
        return sum(final)
    elif position1 > position2:
        final = answer[position1:] + answer[:position2 + 1]
        return sum(final)
