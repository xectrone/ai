from random import choice

class ExpertSystem:
    def __init__(self, symptoms, deseases):
        self.symptoms = symptoms
        self.deseases = deseases
        self.current_symptom = None
        self.current_desease = None
    
    def start(self):
        self.current_symptom = choice(self.symptoms)
        n = int(input(f"What is severity of {self.current_symptom} (0-10) : "))
        self.current_desease = self.deseases[self.current_symptom]
        if n>5:
            print(f"You may have {self.current_desease}")
        else:
            print(f"You dont have {self.current_desease}")
            
        self.askNextQuestion()
    
    def askNextQuestion(self):
        if self.current_desease is not None:
            n = input("Do you have any other symptoms (yes/no) : ")
            if n.lower() == "yes":
                self.start()
            else:
                print("Thank you for using our Expert System !")
        else:
            print("Sorry, I cant Help you with desease dignosis.")
            
if __name__=='__main__':
    symptoms = ["fever", "cough", "sore throat", "running nose", "headache"]
    desease = {
        "fever":"flu",
        "cough":"cold",
        "sore throat": "strep throat",
        "running nose": "allergies",
        "headache": "migraine"
    }
            
    es = ExpertSystem(symptoms, desease)
    es.start()
        
        
            