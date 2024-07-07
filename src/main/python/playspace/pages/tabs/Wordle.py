# import os
# import flet as ft
# from flet import (Row, 
#                   Container, 
#                   CrossAxisAlignment, 
#                   FilledButton,
#                   SafeArea,
#                   Column,)



# def games():
#     def go_to_wordle(e):
#         os.system("python ../wordle/ncd_gamestation.py")

#     wordle = Container(margin=10,padding=10, alignment=ft.alignment.center, image_src="../assets/wordle_example.png", width=300, height=300, border_radius=10, ink=True, on_click=go_to_wordle)

#     return SafeArea(
#         Column(
#             [wordle]
#         ),
#         expand=True,
#     )