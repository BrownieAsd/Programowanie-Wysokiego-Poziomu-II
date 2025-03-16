import modelai
import matrix
import person
import employee
import manager

if __name__ == '__main__':
    #zadanie 1
    model1=modelai.ModelAI("model1", 2.0)
    model2=modelai.ModelAI.z_pliku("model.json")
    print(model2.nazwa_modelu)
    print(model1.nazwa_modelu)
    print(model1.ile_modeli())
    model3 = modelai.ModelAI("model13", 223.0)
    print(model1.ile_modeli())
    #zadanie 2
    matrix1=matrix.Matrix(1,2,3,4)
    matrix2=matrix.Matrix(5,6,7,8)
    matrix3=matrix1+matrix2
    print(matrix3)
    matrix4=matrix1*matrix2
    print(repr(matrix4))
    #zadanie 3
    p1=person.Person("John","Smith",22)
    p2=person.Person("Sam","Smith",23)
    p3=person.Person("Nicholas","Jackson",24)

    e1=employee.Employee("Sales",10000,p2)
    e2=employee.Employee("Sales",10000,p1)
    e3=employee.Employee("Manager",10000,p3)

    m1=manager.Manager("FCB",p3,p3)
    matrix1