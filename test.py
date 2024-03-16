import pandas as pd

class Question:
    def __init__(self, lan):
        self.lan = lan
        self.df = pd.read_csv('data.csv', na_filter=['all', 'empty'])

    def question(self):
        arr = self.df.sample().values[0].tolist()
        if(self.lan == 'e'):
            arr.reverse()
        return arr
        
    def gen_question(self):
        q, a = self.question()
        ans = input(f'What is the meaning of the following word : {q} \n')
        if(ans == a):
            print('Correct Answer! \n')
        else:
            print(f'Wrong Answer!, Correct answer is {a} \n')
        
        self.gen_question()

def main():
    lan = input('Which language you need the question? e/g : ')
    q_obj = Question(lan)
    try:
        q_obj.gen_question()
    except KeyboardInterrupt:
        print("KeyboardInterrupt received. Exiting...")

if __name__ == '__main__':
    main()
