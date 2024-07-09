import flet as ft
import flet_router as fr
from .Base_url import router
import webbrowser
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
                  ElevatedButton,
                  OutlinedButton,
                  Text,
                  icons,
                  )

@router.route(name="home")

async def home(router: fr.Router, page: Page):

    def go_register(e):
        router.go_push(
            fr.Location(
                name="register",
                params={"variable":"seila"},
                query={"query_variable":"world"}
            )
        )

    def go_playspace(e):
        e.control.page.update()
        router.go_push(
            fr.Location(
                name="playspace"
                # params={"page":page},
            )
        )

    register_buttom = Row(controls=[ElevatedButton("Registre-se", on_click=go_register)], alignment=MainAxisAlignment.CENTER)
    submit_buttom = Row(controls=[FilledButton("Entrar", on_click=go_playspace), FilledButton(text="Entrar como Convidado", on_click=go_playspace)], alignment=MainAxisAlignment.CENTER)
    playspace = Row(controls=[Image(src="assets/playspace.png", width=400, height=400)], alignment=MainAxisAlignment.CENTER)
    email = TextField(label="Email", keyboard_type=KeyboardType.EMAIL)
    password = TextField(label="Senha",keyboard_type=KeyboardType.NUMBER,password=True,can_reveal_password=True)
    divider = Divider(thickness=1)
    follow_box = Row(controls=[Text("Siga-nos nas redes sociais:")], alignment=MainAxisAlignment.CENTER)
    instagram_buttom = Row(controls=[OutlinedButton(text="Instagram",icon=icons.CAMERA_ALT_OUTLINED, on_click=lambda e: webbrowser.open('https://www.instagram.com/ncd_ufes/'))], alignment=MainAxisAlignment.CENTER)
    blank = Row(controls=[Text("")])

    return ft.SafeArea(
        Column(
            scroll=ScrollMode.ADAPTIVE,
            # alignment=MainAxisAlignment.CENTER,
            controls=[playspace,email,password, divider, submit_buttom, register_buttom, blank, blank, follow_box, instagram_buttom
            ],
        ),
        expand=True,
    )
