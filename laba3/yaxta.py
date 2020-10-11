"""здесь комментарии будут использоваться после написанной команды
(не до нее), и знак решетки "#" не будет использоваться для комментариев,
так как это может повлечь сбои в работе программы """
import pygame
from pygame import draw

import math as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 402))
''' устанавливаем размер изображения'''

back_color = (255, 255, 0)
screen.fill(back_color)
''' рисуем песок '''


def draw_clouds(main_cloud_x, main_cloud_y, cloud_radius, density_of_clouds):
    """

    Функция рисует скопление облаков белого цвета.
    main_cloud_x - координата x "главного" облака. Это облако
    относительно которого будут рисолваться остальные семь облаков скопления
    main_cloud_y - координата y "главного" облака.
    cloud_radius - радиус каждого облака density_of_clouds - коэфициент,
    определяющий насколько близко облака расположены друг к другу

    """
    draw.circle(screen, (0, 0, 0), (main_cloud_x, main_cloud_y),
                cloud_radius + 1)
    ''' Облако 1 (1-я строчка для окантовки, а следующая для заливки белым '''
    draw.circle(screen, (255, 255, 255), (main_cloud_x, main_cloud_y),
                cloud_radius)
    draw.circle(screen, (0, 0, 0), (main_cloud_x -
                                    density_of_clouds * 2,
                                    main_cloud_y +
                                    density_of_clouds * 3),
                cloud_radius + 1)
    ''' Облако 2 (1-я строчка для окантовки, а следующая для заливки белым '''
    draw.circle(screen, (255, 255, 255), (main_cloud_x -
                                          density_of_clouds * 2,
                                          main_cloud_y +
                                          density_of_clouds * 3),
                cloud_radius)
    draw.circle(screen, (0, 0, 0), (main_cloud_x +
                                    density_of_clouds * 3,
                                    main_cloud_y), cloud_radius + 1)
    ''' Облако 3 (1-я строчка для окантовки, а следующая для заливки белым '''
    draw.circle(screen, (255, 255, 255), (main_cloud_x +
                                          density_of_clouds * 3,
                                          main_cloud_y), cloud_radius)
    draw.circle(screen, (0, 0, 0), (main_cloud_x +
                                    density_of_clouds * 2,
                                    main_cloud_y +
                                    density_of_clouds * 3),
                cloud_radius + 1)
    ''' Облако 4 (1-я строчка для окантовки, а следующая для заливки белым '''
    draw.circle(screen, (255, 255, 255), (main_cloud_x +
                                          density_of_clouds * 2,
                                          main_cloud_y +
                                          density_of_clouds * 3),
                cloud_radius)
    draw.circle(screen, (0, 0, 0), (main_cloud_x + density_of_clouds * 6,
                                    main_cloud_y + density_of_clouds * 3),
                cloud_radius + 1)
    ''' Облако 5 (1-я строчка для окантовки, а следующая для заливки белым '''
    draw.circle(screen, (255, 255, 255), (main_cloud_x +
                                          density_of_clouds * 6,
                                          main_cloud_y +
                                          density_of_clouds * 3),
                cloud_radius)
    draw.circle(screen, (0, 0, 0), (main_cloud_x + density_of_clouds * 8,
                                    main_cloud_y), cloud_radius + 1)
    ''' Облако 6 (1-я строчка для окантовки, а следующая для заливки белым '''
    draw.circle(screen, (255, 255, 255), (main_cloud_x +
                                          density_of_clouds * 8,
                                          main_cloud_y), cloud_radius)
    draw.circle(screen, (0, 0, 0), (main_cloud_x + density_of_clouds * 10,
                                    main_cloud_y + density_of_clouds * 3),
                cloud_radius + 1)
    ''' Облако 7 (1-я строчка для окантовки, а следующая для заливки белым '''
    draw.circle(screen, (255, 255, 255), (main_cloud_x +
                                          density_of_clouds * 10, main_cloud_y
                                          + density_of_clouds * 3),
                cloud_radius)


def draw_umbrella(left_upper_x, left_upper_y, width_umb, height_umb,
                  umb_radius, umb_length, dist_betw_spokes):
    """

    left_upper_x - координата x левого верхнего угла стержня зонтика
    left_upper_y - координата y левого верхнего угла стержня зонтика
    width_umb - ширина стержня зонтика
    height_umb - высота стержня зонтика
    umb_radius - радиус "шапочки" зонтика
    umb_length - длина "шапочки" зонтика
    dist_betw_spokes - ширина между спицами зонтика

    """

    draw.rect(screen, (210, 110, 34), (left_upper_x, left_upper_y, width_umb,
                                       height_umb))
    draw.polygon(screen, (249, 96, 75), [(left_upper_x + width_umb,
                                          left_upper_y), (
                                             left_upper_x + width_umb,
                                             left_upper_y + umb_length), (
                                             left_upper_x + width_umb +
                                             umb_radius, left_upper_y +
                                             umb_length)])
    draw.polygon(screen, (249, 96, 75), [(left_upper_x, left_upper_y), (
        left_upper_x, left_upper_y + umb_length),
                                         (left_upper_x - umb_radius,
                                          left_upper_y +
                                          umb_length)])
    draw.rect(screen, (249, 96, 75), (left_upper_x, left_upper_y, width_umb,
                                      umb_length))
    draw.aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (
        left_upper_x - umb_radius + 1 * dist_betw_spokes, left_upper_y +
        umb_length))
    draw.aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y),
                (left_upper_x - umb_radius + 2 * dist_betw_spokes,
                 left_upper_y + umb_length))
    draw.aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y),
                (left_upper_x - umb_radius + 3 * dist_betw_spokes,
                 left_upper_y + umb_length))
    draw.aaline(screen, (0, 0, 0), (left_upper_x + width_umb, left_upper_y),
                (left_upper_x + width_umb + umb_radius - 3 * dist_betw_spokes,
                 left_upper_y + umb_length))
    draw.aaline(screen, (0, 0, 0), (left_upper_x + width_umb, left_upper_y),
                (left_upper_x + width_umb + umb_radius - 2 * dist_betw_spokes,
                 left_upper_y + umb_length))
    draw.aaline(screen, (0, 0, 0), (left_upper_x + width_umb, left_upper_y),
                (left_upper_x + width_umb + umb_radius - 1 * dist_betw_spokes,
                 left_upper_y + umb_length))
    draw.aaline(screen, (0, 0, 0), (left_upper_x + width_umb, left_upper_y),
                (left_upper_x + width_umb, left_upper_y + umb_length))
    draw.aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (
        left_upper_x, left_upper_y + umb_length))


def draw_boat(boat_x, boat_y, p):
    """

    boat_x - координата x центра иллюминатора
    boat_y - координата y центра иллюминатора
    p - коэффициент пропорциональности размеров лодки


    """
    draw.circle(screen, (139, 80, 20), (boat_x, boat_y), p * 7)
    draw.rect(screen, (0, 0, 255), (boat_x - p * 7, boat_y - p * 7, p * 7 * 2,
                                    p * 7))
    draw.rect(screen, (0, 0, 255), (boat_x, boat_y, p * 7, p * 7))
    draw.rect(screen, (0, 0, 0), (boat_x, boat_y, p * 28 + 2, p * 7))
    draw.rect(screen, (139, 80, 20), (boat_x + 1, boat_y, p * 28, p * 7))
    draw.polygon(screen, (0, 0, 0),
                 [(boat_x + p * 28 + 2, boat_y), (
                     boat_x + p * 28 + 2, boat_y + p * 7 - 1), (
                     boat_x + p * 43, boat_y)])
    draw.polygon(screen, (139, 80, 20),
                 [(boat_x + p * 28 + 2, boat_y), (boat_x + p * 28 + 2,
                                                  boat_y + p * 7 - 1), (
                     boat_x + p * 43, boat_y)])
    draw.circle(screen, (0, 0, 0), (boat_x + p * 33, boat_y + p * 3 - 2),
                p * 2)
    draw.circle(screen, (255, 255, 255), (boat_x + p * 33,
                                          boat_y + p * 3 - 2), p * 2 - 3)


def draw_parus(parus_x, parus_y, p):
    """

    parus_x - координата x левого верхнего угла стержня паруса
    parus_y - координата y левого верхнего угла стержня паруса
    p - коэффициент пропорциональности размеров паруса

    """
    draw.rect(screen, (0, 0, 0), (parus_x, parus_y, p * 2 - 2, 2 * 10 * p))
    draw.polygon(screen, (218, 173, 128),
                 [(parus_x + p * 2 - 2, parus_y), (parus_x + p * 6,
                                                   parus_y + p * 10),
                  (parus_x + p * 14, parus_y + p * 10)])
    draw.polygon(screen, (218, 173, 128),
                 [(parus_x + p * 2 - 2, parus_y + p * 10 * 2), (
                     parus_x + p * 6, parus_y + p * 10),
                  (parus_x + p * 14, parus_y + p * 10)])
    draw.aaline(screen, (0, 0, 0), (parus_x + p * 6, parus_y + p * 10), (
        parus_x + p * 14, parus_y + p * 10))
    draw.aaline(screen, (0, 0, 0), (parus_x + p * 6, parus_y + p * 10), (
        parus_x + p * 2 - 2, parus_y))
    draw.aaline(screen, (0, 0, 0), (parus_x + p * 14, parus_y + p * 10), (
        parus_x + p * 2 - 2, parus_y))
    draw.aaline(screen, (0, 0, 0), (parus_x + p * 6, parus_y + p * 10), (
        parus_x + p * 2 - 2, parus_y + 2 * 10 * p))
    draw.aaline(screen, (0, 0, 0), (parus_x + p * 14, parus_y + p * 10), (
        parus_x + p * 2 - 2, parus_y + 2 * 10 * p))


def draw_waves(x_start, x_stop, w_color, y_wave, h_wave):
    """

    Функция рисует функцию синуса, путем метода апроксимации 
    синусоиды трапециями

    x_start - координата x начала гребня
    x_stop - координата x конца гребня
    w_color - цвет волны
    y_wave - y координата начала волны
    h_wave - высота гребня

    """

    d_wave = (x_stop - x_start) / 90
    for step in range(89):
        draw.polygon(screen, w_color, [(x_start + d_wave * step, y_wave), (
            x_start + d_wave * (step + 1), y_wave), (
            x_start + d_wave * step, y_wave -
            np.sin(np.pi * step / 90) * h_wave), (
            x_start + d_wave * (step + 1),
            y_wave - np.sin(np.pi * (step + 1) / 90) * h_wave)])


def draw_sand(x_start, x_stop, w_color, y_wave, h_wave):
    """

    Функция рисует функцию косинуса, путем метода апроксимации 
    косинусоиды трапециями

    x_start - координата x начала гребня
    x_stop - координата x конца гребня
    w_color - цвет волны
    y_wave - y координата начала волны
    h_wave - высота гребня

    """

    d_wave = (x_stop - x_start) / 90
    for step in range(89):
        draw.polygon(screen, w_color, [(x_start + d_wave * step, y_wave), (
            x_start + d_wave * (step + 1), y_wave), (
            x_start + d_wave * step,
            y_wave + np.sin(np.pi * step / 90) * h_wave), (
            x_start + d_wave * (step + 1),
            y_wave + np.sin(np.pi * (step + 1) / 90) * h_wave)])


def draw_sun(sun_radius, beam_length, number_of_beams):
    """

    sun_radius - радиус солнца
    beam_length - длина лучей солнца
    number_of_beams - число солнечных лучей

    """

    draw.circle(screen, (255, 255, 0), (540, 60), sun_radius)
    for step in range(60):
        draw.polygon(screen, (255, 255, 0), [(
            540 + sun_radius * np.sin(2 * step * np.pi / number_of_beams),
            60 - sun_radius * np.cos(2 * step * np.pi / number_of_beams)), (
            540 + sun_radius * np.sin((2 * step + 1) * 
                                      np.pi / number_of_beams),
            60 - sun_radius * np.cos((2 * step + 1) *
                                     np.pi / number_of_beams)), (
            (540 + (sun_radius + beam_length) * np.sin(
                (2 * step + 0.5) * np.pi / number_of_beams
            ), 60 - (sun_radius + beam_length) * np.cos(
                (2 * step + 0.5) * np.pi / number_of_beams)))])


draw.rect(screen, (0, 0, 255), (0, 0, 600, 260))
''' рисуем воду '''

for i in range(7):
    draw_waves(43 * i * 2, 43 * (i * 2 + 1), (255, 255, 0), 260, 10)
    draw_sand(43 * (i * 2 + 1), 43 * (i * 2 + 2), (0, 0, 255), 260, 10)
''' рисуем волны'''

draw_boat(360, 190, 5)
draw_boat(185, 170, 3)
''' рисуем большую и маленькую лодку'''

draw.rect(screen, (129, 218, 247), (0, 0, 600, 160))
''' рисуем небо '''

draw_parus(415, 90, 5)
draw_parus(225, 110, 3)
''' рисуем парусы для большой и маленькой лодки'''

draw_clouds(170, 40, 15, 5)
''' рисуем скопление облаков маленького размера'''
draw_clouds(306, 30, 25, 8)
''' рисуем скопление облаков среднего размера'''
draw_clouds(116, 98, 19, 7)
''' рисуем скопление облаков большого размера'''

draw_sun(40, 8, 60)
''' рисуем солнце'''

draw_umbrella(110, 220, 8, 140, 54, 25, 15)
'''рисуем большой зонтик'''
draw_umbrella(240, 245, 4, 96, 28, 28, 7)
'''рисуем маленький зонтик'''

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

