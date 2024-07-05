import os
import flet as ft
import time
import flet_router as fr
# from .tabs.Wordle import games
from .Base_url import router
from flet import (
    AppBar, 
    Column, 
    Container, 
    ElevatedButton, 
    IconButton,
    Page,
    colors,
    icons,
    Tab,
    Tabs,
    SafeArea) 

@router.route(name="playspace",
              path="/playspace"
              )

async def playspace(router: fr.Router,
    page: Page,
    ): 
    page.splash = ft.ProgressBar(visible=False)
    page.theme_mode = "dark"

    def go_back(e):
        router.back()

    def change_theme(e):
        page.splash.visible = True
        page.update()
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.splash.visible = False
        theme_icon_button.selected = not theme_icon_button.selected
        time.sleep(1.2)
        page.update()

    theme_icon_button = ft.IconButton(
        ft.icons.DARK_MODE,
        selected_icon=ft.icons.LIGHT_MODE,
        icon_color=ft.colors.BLACK,
        icon_size=35,
        tooltip="change theme",
        on_click=change_theme,
        style=ft.ButtonStyle(
            color={"": ft.colors.BLACK, "selected": ft.colors.WHITE},
        ),
    )

    menu_button = IconButton(icons.MENU)

    page.appbar = AppBar(
        leading=menu_button,
        leading_width=40,
        bgcolor=colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.ACCOUNT_CIRCLE, on_click=lambda e: None),
            theme_icon_button],
    )

    back = ElevatedButton("Voltar", on_click=go_back)

    def go_to_wordle(e):
        os.system("python ncd_gamestation.py")

    wordle = Container(margin=10,padding=10, alignment=ft.alignment.center, image_src="../assets/wordle_example.png", width=300, height=300, border_radius=10, ink=True, bgcolor=colors.AMBER, on_click=go_to_wordle)

    t = Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            Tab(
                text="Jogos",
                content=Container(
                    Column(
                        [wordle,back]
                    ),
                ),
            ),
        ],
        expand=1,
    )
    return SafeArea(t,back
    )






    