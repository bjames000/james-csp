#asks for class number and checks if it can be converted to a float
def enter():
  global x
  print "How many classes do you take?"
  classes=raw_input()
  try:
    x = float(classes)
    conv()
  except:
    enter()



#asks, converts and adds grades
def conv():
  global t
  t=0.0  
  global y
  y=0
  while y<x:
    print "Enter grade for class:"
    Answer=raw_input()
    Answer= Answer.lower().replace("/", "")

    if Answer=='a':
     t+=4.0
    elif Answer=='ab':
     t+=3.5
    elif Answer=='b':
     t+=3.0 
    elif Answer=='bc':
     t+=2.5
    elif Answer=='c':
     t+=2.0
    elif Answer=='cd':
     t+=1.5
    elif Answer=='d':
     t+=1.0  
    elif Answer=='ie' or Answer=='f':
     t+=0.0
    else:
        try:
            num=float(Answer)
            t+=num
        except:
            pass                                            
    y+=1
  final()
 
#finds median of all grades added 
def final():
  total=t
  classes=x
  gpa=total/classes
  print "Your GPA is: "+str(gpa)