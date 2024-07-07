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
    SafeArea,
    DataTable,
    DataColumn,
    Text,
    DataCell,
    DataRow,
    AlertDialog,
    OutlinedButton,
    Switch,
    LabelPosition,
    alignment,
    ProgressBar,
    Row,
    MainAxisAlignment,
    ) 

@router.route(name="playspace",
              path="/playspace"
              )

async def playspace(router: fr.Router,page: Page): 
    page.splash = ProgressBar(visible=False)
    page.theme_mode = "dark"

    def go_back(e):
        router.back()

    def change_theme(e):
        page.splash.visible = True
        page.update()
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.splash.visible = False
        switch.label = "Dark Theme" if page.theme_mode == "dark" else "Light Theme"
        time.sleep(0.4)
        page.update()

    def go_to_wordle(e):
        os.system("python wordle/ncd_gamestation.py")
        
    switch = Switch(
        value=True,
        on_change=change_theme,
        label="Dark Theme                                                                  ",
        label_position=LabelPosition.LEFT,
    )
    wordle = Container(margin=10,padding=10, alignment=alignment.center, image_src="../assets/wordle_example.png", width=300, height=300, border_radius=10, ink=True, on_click=go_to_wordle)
    back = ElevatedButton("Voltar", on_click=go_back)
    games_dt = DataTable(
            width=2000,
            border_radius=10,
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=50,
            data_row_color={"hovered": "0xFFFFFF"},
            divider_thickness=0,
            column_spacing=100,
        columns= [
            DataColumn(Text("Nome")),
            DataColumn(Text("Avaliação")),
        ],
            rows=[
                DataRow(
                    [DataCell(Text("Wordle")), DataCell(Text("⭐⭐⭐⭐⭐"))],
                    selected=True,
                    on_select_changed=lambda e: go_to_wordle(e)
                ),
                DataRow(
                    [DataCell(Text("Forca")), DataCell(Text("⭐⭐⭐⭐⭐"))],
                    selected=False,
                    on_select_changed=lambda e: print(e)
                )
            ],
        )
    
    def yes_click(e):
        wordle_dialog.open = False
        page.update()
        go_to_wordle(e)

    def no_click(e):
        wordle_dialog.open = False
        page.update()



    wordle_dialog = AlertDialog(
        modal=True,
        title=Text("Wordle"),
        content=Text("Um jogo de adivinhação de palavras de cinco letras. "),
        actions=[
            wordle,
            Row(controls=[
                OutlinedButton("Jogar", on_click=yes_click),
                ElevatedButton("Cancelar", on_click=no_click),
                ],
                alignment=MainAxisAlignment.SPACE_AROUND,
            ),
        ],
        actions_alignment="end",
    )

    forca_dialog = AlertDialog(
        modal=True,
        title=Text("Forca"),
        content=Text("Descubra a palavra antes que o cid perca a cabeça. "),
        actions=[
            wordle,
            Row(controls=[
                OutlinedButton("Jogar", on_click=yes_click),
                ElevatedButton("Cancelar", on_click=no_click),
                ],
                alignment=MainAxisAlignment.SPACE_AROUND,
            ),
        ],
        actions_alignment="end",
    )
    
    tabs = Tabs(
        selected_index=1,
        animation_duration=300,
        indicator_tab_size=True,
        divider_color = colors.WHITE,

        tabs=[
            Tab(
                text="Jogos",
                icon=icons.GAMES,
                content=Container(
                    Column(
                        [games_dt,back]
                    ),
                ),
            ),
            Tab(
                text="Pontuações",
                icon=icons.STAR,
                content=Container(
                    Column(
                        [back]
                    ),
                ),
            ),
            Tab(
                text="Configurações",
                icon=icons.SETTINGS,
                content=Container(
                    Column(
                        [back,switch]
                    ),
                ),
            ),
        ],
        expand=1,
        )
    return SafeArea(tabs,back
    )






    