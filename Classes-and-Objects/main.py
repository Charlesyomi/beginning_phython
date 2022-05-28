class Student:
    
    def __init__(self, name="unknown", age=0,  tracks=["BE","FE","W3"], score=0):
        self.name=name
        self.age=int(age)
        self.tracks=tracks
        self.score=float(score)
        #pass


    def change_name(self,new_name):
        self.name=new_name

    def change_age(self,new_age):
        self.age=int(new_age)
##        try:
##            self.age=int(new_age)
##        except (ValueError, NameError) :
##            print("argument for age must be convertible to integer")

    def add_track(self,new_track):
        self.tracks.append(new_track)

    def rem_track(self,track_name):
        self.tracks.remove(track_name)

    def get_score(self):
        return(self.score)
        
        

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
