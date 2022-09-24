# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
from cmath import sqrt


f_coordinates = [int(i) for i in input(
    "Введите координаты первой точки через запятую  ").split(",")]
s_coordinates = [int(j) for j in input(
    "Введите координаты второй точки через запятую  ").split(",")]
res = (((f_coordinates[0]-s_coordinates[0])
        ** 2)+((f_coordinates[1]-s_coordinates[1])**2))**(0.5)
print(f"{res:.2f}")
