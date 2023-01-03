import joblib
opposites={'cat':'go','sat':'stand'} #global variable

def main():
    while True: # infinite way loop
        word=input("enter a word\n").strip().lower() #case sensitive
    #if word in opposites:  # in operaters is loop hachutade 
    #print(opposites[word])
        opposite=getOpposite(word) #we using get we get output faster than using of if word in oppo
        if opposite is None:
            addWord(word);print("word added")

        else:
            print(f"opposites of {word} is {opposite}")

        inp=input("do you want to quit\n")
        if inp=='Y':
            joblib.dump(opposites,"data.pkl") #before exit dump the word and then exit
            break


def addWord(word):
    opp=input(f"enter opposites of {word}").strip().lower() # case insensitive
    opposites[word]=opp

def getOpposite(word):
    opp=opposites.get(word)
    if opp is None: #when we want none use is operator
        for k,v in opposites.items():
            if v==word:
                return k 
    return opp
def loadOpposites():
     global opposites # update of global varible
     try: # error barutta or elva anta check madutte 
         opposites=joblib.load("data.pkl") #eror bandri 
     except Exception as e: # yavude Exception bandru handle madutade
        print("no file found,using default")

loadOpposites()

main()