class Aclass():
    def __init__(self, id, name, grades=[]):
        self.id = id
        self.name = name
        self.grades = grades
        print(f"{self.id}. Adı: {self.name}\tOrtalaması: {self.calc()}")

    def calc(self):
        result = 0
        gradeCounter = 0
        for grade in self.grades:
            gradeCounter += 1
            if gradeCounter > 3:
                print(f"\n[HATA] Yalnızca 3 sınav notu girebilirsiniz. Yanlış veri girdiğiniz yer: {self.id}:{self.name}:{self.grades}:{grade}")
                exit()
            if grade < 0 or grade > 100:
                print(f"\n[HATA] Sınav notu 0 ile 100 arasında olmalıdır. Yanlış veri girdiğiniz yer: {self.id}:{self.name}:{self.grades}: {grade}")
                exit()
            result += grade
            self.average = result / 3
        
        if self.average < 50 and self.average > 0:
            return f"{'%.2f' % self.average} {'Kaldı'.rjust(10)}"
        else:
            return f"{'%.2f' % self.average} {'Geçti'.rjust(10)}"


student1 = Aclass(1, "Cyber", [13, 50, 70])
student2 = Aclass(2, "Worm", [140, 50, 70])
student3 = Aclass(3, "x", [50, 0, 10])
student4 = Aclass(4, "y", [10, 100, 100])
