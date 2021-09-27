# author: LM (AMDG) 9/20/2021

# free throws, baskets inside 3 point line, and baskets outside 3 point line are subject to change 
freethrow = input("What is the total number of free throws? ")

basket_inside_3point_line = input( "What is the total number of baskets inside the three point line? ")
     
basket_beyond = input("What is the toal number of baskets outside the three point line? ")

total = int(freethrow)  + int(basket_inside_3point_line) * 2  + int(basket_beyond) * 3


print( "The player scored " + str(total) + " points")