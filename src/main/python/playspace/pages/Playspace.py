import os
from entities.Game import Game
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
    Checkbox,
    ) 

@router.route(name="playspace",
              path="/playspace"
              )

async def playspace(router: fr.Router,page: Page): 
    page.splash = ProgressBar(visible=False)
    page.theme_mode = "dark"

    # function to go to the previous page
    def go_back(e):
        router.back()

    # function to change the theme
    def change_theme(e):
        page.splash.visible = True
        page.update()
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.splash.visible = False
        switch_theme.label = "Dark Theme" if page.theme_mode == "dark" else "Light Theme"
        time.sleep(0.4)
        page.update()

    # switch control to change the theme
    switch_theme = Switch(
        value=True,
        on_change=change_theme,
        label="Dark Theme",
        label_position=LabelPosition.LEFT,
    )

    def cancel_dialog(e):
        page.dialog.open = False
        page.update()


    wordle_img = Container(margin=10,padding=10, alignment=alignment.center, image_src="../assets/wordle_example.png", width=300, height=300, border_radius=10, ink=True, on_click= lambda e: print("Wordle Clicked"))
    forca_img = Container(margin=10,padding=10, alignment=alignment.center, image_src="../assets/forca_example.png", width=300, height=300, border_radius=10, ink=True, on_click= lambda e: print("Forca Clicked"))
    back_buttom = ElevatedButton("Voltar", on_click=go_back)
    game_list = []
    game1 = Game('Forca', 3, ['seila', 'palavras'])
    game2 = Game('Wordle', 5, ['puzzle', 'palavras'])

    game_list.append(game1)
    game_list.append(game2)

    # print(len(game_list))
    # for elem in game_list:
    #     print(elem.name)
    #     print(elem.record)


    # games data table
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
            DataColumn(Text("Gêneros")),
        ],
            # content
            rows=[
                DataRow(
                    [DataCell(Text("Forca")), DataCell(Text("⭐⭐⭐⭐⭐"), DataCell(Text("Seila, Aventura")))],
                    selected=False,
                    on_select_changed=lambda e: open_forca_dialog(e)
                ),
                DataRow(
                    [DataCell(Text(value=game1.name)), DataCell(Text("⭐⭐⭐⭐⭐"), DataCell(Text("Puzzle, Palavras")))],
                    selected=True,
                    on_select_changed=lambda e: open_wordle_dialog(e)
                )
            ],
        )

    # --------------------------------- Wordle ---------------------------------
    def play_wordle(e):
        wordle_dialog.open = False
        page.update()
        os.system("python wordle/ncd_gamestation.py")


    def open_wordle_dialog(e):
        page.dialog = wordle_dialog
        page.dialog.open = True
        page.update()

    wordle_dialog = AlertDialog(
        modal=True,
        title=Text("Wordle"),
        content=Text("Um jogo de adivinhação de palavras de cinco letras. "),
        actions=[
            wordle_img,
            Row(controls=[
                OutlinedButton("Jogar", on_click=play_wordle),
                ElevatedButton("Cancelar", on_click=cancel_dialog),
                ],
                alignment=MainAxisAlignment.SPACE_AROUND,
            ),
        ],
        actions_alignment="end",
    )

    # def dropdown_changed(e):
    #     t.value = f"Dropdown changed to {dd.value}"
    #     games_dt.rows.remove(game1.name)
    #     page.update()

    # t = ft.Text()
    
    # dd = ft.Dropdown(
    #     on_change=dropdown_changed,
    #     options=[
    #         ft.dropdown.Option("puzzle"),
    #         ft.dropdown.Option("palavras"),
    #         ft.dropdown.Option("seila"),
    #     ],
    #     width=200,
    # )
    def showhidename(e):
        value = e.control.value
        keyword = str(e.control.label).lower()
        if value == False:
            for i, game in enumerate(score_dt.rows):
                if any(keyword in li for li in(str(game.cells[2].content)).split(",")):
                    score_dt.rows[i].visible = False
                    page.update()
        else:
            for i, game in enumerate(score_dt.rows):
                if any(keyword in li for li in(str(game.cells[2].content)).split(",")):
                    score_dt.rows[i].visible = True        
                    page.update()
                    
    fill_puzzle = Checkbox(label="Puzzle", value=True, on_change=showhidename)
    fill_aventura = Checkbox(label="Aventura", value=True, on_change=showhidename)
    fill_palavras = Checkbox(label="Palavras", value=True, on_change=showhidename)
    fill_games = Row(controls=[fill_puzzle, fill_aventura, fill_palavras], alignment=MainAxisAlignment.CENTER)

# --------------------------------- Pontuacao ---------------------------------
    score_dt = DataTable(
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
            DataColumn(Text("Score")),
            DataColumn(Text("Gêneros")),
        ],
            # content
            rows=[
            ],
        )   
    	# PUSH DATA TO DATATABLE
         
    def open_game_dialog(e:ft.ControlEvent):
        
        print(e.control.cells[0].content.value)

    for game in game_list:
        score_dt.rows.append(
        DataRow(
            cells=[
                DataCell(Text(game.name)),
                DataCell(Text(game.record)),
                DataCell(Text(game.tags)),
            ],
            on_select_changed=lambda e: open_game_dialog(e)
        )
    )


# --------------------------------- Forca ---------------------------------
    def play_forca(e):
        forca_dialog.open = False
        page.update()
        os.system("python forca/forca.py")

    def open_forca_dialog(e):
        page.dialog = forca_dialog
        page.dialog.open = True
        page.update()

    forca_dialog = AlertDialog(
        modal=True,
        title=Text("Forca"),
        content=Text("Descubra a palavra-chave antes que o Cid perca a cabeça! "),
        actions=[
            forca_img,
            Row(controls=[
                OutlinedButton("Jogar", on_click=play_forca),
                ElevatedButton("Cancelar", on_click=cancel_dialog),
                ],
                alignment=MainAxisAlignment.SPACE_AROUND,
            ),
        ],
        actions_alignment="end",
    )
    
    tabs = Tabs(
        selected_index=0,
        animation_duration=300,
        indicator_tab_size=True,
        divider_color = colors.WHITE,

        tabs=[
            Tab(
                text="Jogos",
                icon=icons.GAMES,
                content=Container(
                    Column(
                        [fill_games,games_dt,back_buttom]
                    ),
                ),
            ),
            Tab(
                text="Pontuações",
                icon=icons.STAR,
                content=Container(
                    Column(
                        [fill_games,score_dt,back_buttom]
                    ),
                ),
            ),
            Tab(
                text="Configurações",
                icon=icons.SETTINGS,
                content=Container(
                    Column(
                        [switch_theme,back_buttom]
                    ),
                ),
            ),
        ],
        expand=1,
        )
    return SafeArea(tabs,back_buttom
    )






    