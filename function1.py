def num_points(word):
    total_points = 0

    for char in word:
        if char in "a,e,i,o,u,l,n,s,t,r":
            total_points += 1
        elif char in "d,g":
            total_points += 2
        elif char in "b,c,m,p":
            total_points += 3
        elif char in "f,h,v,w,y":
            total_points += 4
        elif char == "k":
            total_points += 5
        elif char in "j,x":
            total_points += 8
        elif char in "q,z":
            total_points += 10

    return total_points

def best_word(word_list):
    best_word = None
    max_points = 0

    for word in word_list:
        points = num_points(word)
        if points > max_points:
            max_points = points
            best_word = word

    return best_word