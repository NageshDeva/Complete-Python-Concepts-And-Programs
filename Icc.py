class ICC:
    @staticmethod
    def india():
        finals = ['Dhoni', 'india', ' finishes off', ' lifts the world cup', 
                  ' in his style',' after 28 Years']
        s=''
        s1=''
        for i in range(len(finals)):
            if i % 2 == 0:
                s += finals[i]
            else:
                s1 += finals[i]
        print(s)
        print(s1)

ICC.india()