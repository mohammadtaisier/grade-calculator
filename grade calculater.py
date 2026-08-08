def computegrade (score):
    if score > 1 or score<0:
        print ("bad score")
        return(score)
    elif score >= 0.9 :
        print("A")
        return(score)
    elif score >= 0.8:
        print("B")
        return(score)
    elif score >= 0.7:
        print("C")   
        return(score)  
    elif score >= 0.6:
        print("D")       
        return(score)
    elif score < 0.6:
        print("F") 
        return(score)
        
try:           
    score =input ("enter score")
    score=float(score)   
except:
    print("Bad score")
    quit()
computegrade (score)