import turtle
t=turtle.Pen()

A=int(input ("Ingrese los lados de la estrella: "))

for x in range(A):
    t.forward(108)
    t.left(((A-2)*180)/A)
    t.left(((A-2)*180)/A)

    t.forward(100)
    t.left(360/A)

turtle.getscreen()._root.mainloop()
