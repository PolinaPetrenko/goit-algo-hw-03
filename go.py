import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    # Введення рівня рекурсії
    order = int(input("Enter the recursion level: "))
    # Створення вікна та об'єкта черепахи
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    t = turtle.Turtle()
    t.color("blue")
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    # Виклик функції для створення сніжинки Коха
    for i in range(3):
        koch_snowflake(t, order, 300)
        t.right(120)
    
    # Закриття вікна при кліку
    wn.exitonclick()

if __name__ == "__main__":
    main()
