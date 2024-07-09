import flet as ft
import flet_router as fr
from .Base_url import router
from flet import (
    TextField,
    KeyboardType,
    Divider,
    Row,
    FilledButton,
    MainAxisAlignment,
    SafeArea,
    Column,
    ScrollMode,
    Dropdown,
    Text,
    dropdown,
    icons,
    )

@router.route(name="assesment",
              path="/assesment/{variable}/value"
              )

async def assesment(
    router: fr.Router,
    variable: str,
    page: ft.Page,
    ):    
    def go_back(e):
        router.back()

    def submit_form(e):
        page.dialog = dlg_modal
        page.dialog.open = True
        page.update()

    back_buttom = FilledButton("Voltar",icon=icons.ARROW_BACK, on_click=go_back)
    title = Row(controls=[Text("Avalie o Jogo!")], alignment=MainAxisAlignment.CENTER)
    game_name = TextField(label="Jogo",value=variable,disabled=True)
    divider = Divider(thickness=1)
    submit_buttom = Row(controls=[FilledButton("Enviar", on_click=submit_form)], alignment=MainAxisAlignment.CENTER)

    def handle_close_modal(e):
        page.close(dlg_modal)

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Obrigado Pela Sua Avaliação!!!"),
        content=ft.Text("Sua opinião é muito importante para a gente! ^,^"),
        actions=[
            ft.TextButton("Ok", on_click=go_back),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(
            ft.Text("Modal dialog dismissed"),
        ),
    )

    assesment = ft.Dropdown(
        width=150,
        options=[
            ft.dropdown.Option("1"),
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("5"),
        ],
        label="Avaliação",
    )
    comentary_label = Row(controls=[Text("Comentário")], alignment=MainAxisAlignment.CENTER)
    comentary = TextField(max_length=300, multiline=True, keyboard_type=KeyboardType.NUMBER)

    return SafeArea(
        Column(
            scroll=ScrollMode.ADAPTIVE,
            # alignment=MainAxisAlignment.CENTER,
            controls=[back_buttom,title, game_name, assesment, comentary_label, comentary ,divider, submit_buttom
            ],
            alignment=MainAxisAlignment.CENTER,
        ),
        expand=True,
    )