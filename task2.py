import turtle
import math

def draw_tree(branch_length, level):
    if level == 0:
        return
    
    # Намалювати стовбур
    turtle.forward(branch_length)
    
    # Лівий кут
    turtle.left(45)
    draw_tree(branch_length * math.sqrt(2) / 2, level - 1)
    
    # Повернення до вузла
    turtle.right(90)
    draw_tree(branch_length * math.sqrt(2) / 2, level - 1)
    
    # Повернення до початкової позиції
    turtle.left(45)
    turtle.backward(branch_length)

def main():
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.backward(100)
    turtle.down()
    
    level = int(input("Введіть рівень рекурсії: "))
    draw_tree(100, level)
    
    turtle.done()

if __name__ == "__main__":
    main()
