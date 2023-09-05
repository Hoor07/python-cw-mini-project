def padel_court_cost (court_type):
 if court_type == "indoor":
     return 30
 
 elif court_type ("outdoor"):
     return 20
 
 
 def rackets_cost(racket_brand):
  if rackets_cost ("bullpadel"): 
    return 100
  elif rackets_cost ("nox"): 
    return 140
  elif rackets_cost ("siux"): 
    return 200


 def ball_cost(ball_box):
     if ball_box == 1:
         return 2 
     elif ball_box == 2:
         return 3.5
     elif ball_box == 3:
         return 5
     else:
         return 
     
     
     
def padel_balls_cost():
    court_type = input("do you want indoor or outdoor")
    racket_brand = input ("what brand do you want")
    ball_box = int (input("how maney balls do you want"))
    return padel_court_cost (court_type) + Rackets_cost(racket_brand) + ball_cost(ball_box)
print(padel_balls_cost())