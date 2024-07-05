import flet as ft
import flet_router as fr
from .Base_url import router
from flet import (KeyboardType,
                  Row,
                  TextField,
                  ScrollMode,
                  Image,
                  MainAxisAlignment,
                  Column,
                  SafeArea,
                  Divider,
                  Page,
                  FilledButton,
                  ElevatedButton)

@router.route(name="home")

async def home(router: fr.Router, page: Page):
    def submit_form(e):
        e.control.page.update()
        print(f"logado com sucesso!")
        go_playspace(e)

    def go_register(e):
        router.go_push(
            fr.Location(
                name="register",
                params={"variable":"seila"},
                query={"query_variable":"world"}
            )
        )

    def go_playspace(e):
        router.go_push(
            fr.Location(
                name="playspace"
                # params={"page":page},
            )
        )

    page.scroll = ScrollMode.ALWAYS
    register = ElevatedButton("Registre-se", on_click=go_register)
    register_buttom = Row(controls=[register], alignment=MainAxisAlignment.CENTER)
    submit = FilledButton("Entrar", on_click=submit_form)
    submit_buttom = Row(controls=[submit], alignment=MainAxisAlignment.CENTER)
    playspace = Row(controls=[Image(src="assets/playspace.png", width=400, height=400)], alignment=MainAxisAlignment.CENTER)
    email = TextField(label="Email", keyboard_type=KeyboardType.EMAIL)
    password = TextField(label="Senha",keyboard_type=KeyboardType.NUMBER,password=True,can_reveal_password=True)
    divider = Divider(thickness=1)

    return SafeArea(
        Column(
            scroll=ScrollMode.ADAPTIVE,
            # alignment=MainAxisAlignment.CENTER,
            controls=[playspace,email,password, divider, submit_buttom, register_buttom
            ],
        ),
        expand=True,
    )
