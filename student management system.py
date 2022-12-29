class Main:
    '''Main class to maintain all records'''
    student = {}


class Student(Main):
    '''Student class is the child class of Main class'''
    def input(self):                                                # To take input from users
        self.roll_no = int(input("Enter Roll Number:"))
        self.name = input("Enter Student Name:")
        self.gender = str(input('Enter Gender(M/F/O):'))
        self.perc = eval(input("Enter percentage:"))

        Main.student[self.roll_no] = [self.name, self.gender.upper(), self.perc]         # To add details to the student Dictionary

    def show(self):                                                # To display all records
        print('Roll no \t Name \t Gender \t Percentage')
        for i in Main.student.keys():
            print('{0} \t\t {1} \t\t {2} \t\t {3}'.format(str(i), str(Main.student.get(i)[0]), str(Main.student.get(i)[1]), str(Main.student.get(i)[2])))

    def update(self):                                             # To update students records
        ch = int(input("Enter roll number of the student whose record you want to update:"))
        name = input('Enter name again:')
        perc = eval(input('Enter percentage:'))
        gender = str(input(('Enter gender(M/F/O):')))
        Student.student[ch] = [name, gender.upper(), perc]
        self.show()

    def delete(self):                                            # To delete a record
        ch = int(input("Enter roll number of the student whose record you want to delete:"))
        del Student.student[ch]
        self.show()

    def details(self):
        countM = 0
        countF = 0
        count0 = 0
        for i in Main.student.keys():
            if str(Main.student.get(i)[1]) == 'M':
                countM += 1
            elif str(Main.student.get(i)[1]) == 'F':
                countF += 1
            else:
                count0 += 1

        avgperc = 0
        for i in Main.student.keys():
            avgperc += Main.student.get(i)[2]

        print('Total students:', len(Main.student))
        print('Male Student:', countM)
        print('Female students:', countF)
        print('Other gender students:', count0)
        print('Average percentage:', avgperc/len(Main.student))

def main():
    print("**Welcome to Student Management System**".center(75))
    print("1. Enter details")
    print("2. View Details")
    print("3. Update Details")
    print('4. Delete Record')
    print('5. Show Details')
    print('6. Exit System')

    obj = Student()                                             # This is the object of Student Class
    while True:
        while True:
            try:
                ch = int(input('Enter your choice:'))
                break
            except:
                print('Wrong input!!!')

        if ch == 1:
            ch1 = int(input('Enter number of details you want to add:'))
            for i in range(ch1):
                obj.input()
        elif ch == 2:
            obj.show()
        elif ch == 3:
            obj.update()
        elif ch == 4:
            obj.delete()
        elif ch == 5:
            obj.details()
        elif ch == 6:
            break
        else:
            pass
main()