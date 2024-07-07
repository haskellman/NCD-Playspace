# from  User import User
import flet as ft
import flet_router as fr
from .Base_url import router
from flet import (Radio, 
                  RadioGroup, 
                  Row, 
                  Container, 
                  Dropdown, 
                  TextField, 
                  FilledButton, 
                  AlertDialog, 
                  TextButton, 
                  Text, 
                  MainAxisAlignment, 
                  Column, 
                  SafeArea, 
                  KeyboardType, 
                  dropdown, 
                  Divider,
                  ScrollMode,
                  Image,
                  ElevatedButton)


USERS = []

@router.route(name="register",
              path="/register/{variable}/value"
              )

async def register(
    router: fr.Router,
    variable: str,
    query:str = "you not send"
    ):    
    def go_back(e):
        router.back()

    gender = RadioGroup(
        content=Row(
            [
                Radio(value="female", label="Feminimo"),
                Radio(value="male", label="Masculino"),
                Radio(value="not_specified", label="Não especificado"),
            ]
        )
    )
    

    birthdate = Container(
        Row(
            controls=[
            Dropdown(
                label="Dia",
                options=[dropdown.Option(str(i)) for i in range(1, 32)],
                width=100,
            ),
            Dropdown(
                label="Mes",
                options=[dropdown.Option("Janeiro"),
                        dropdown.Option("Fevereiro"),
                        dropdown.Option("Março"),
                        dropdown.Option("Abril"),
                        dropdown.Option("Maio"),
                        dropdown.Option("Junho"), 
                        dropdown.Option("Julho"), 
                        dropdown.Option("Agosto"),
                        dropdown.Option("Setembro"),
                        dropdown.Option("Outubro"),
                        dropdown.Option("Novembro"), 
                        dropdown.Option("Dezembro")],
                width=150,
            ),
            Dropdown(
                label="Ano",
                options=[dropdown.Option(str(i)) for i in reversed(range(1900, 2024))],
                width=100,
            ),
        ],)
    )
    
    # def create_user(name, email, password):
    #     USERS.append(User(name, email, password))

    def submit_form(e):
        e.control.page.dialog = success_dlg
        go_back(e)
        success_dlg.open = True
        e.control.page.update()

        # if (password.value == password_confirm.value):
        #     create_user(fullname.value, email.value, password.value)
        #     print(f"obrigado por se registrar! {User.__str__(USERS[-1])}")


    def close_dlg(e):
        success_dlg.open = False
        e.control.page.update()

    def validate_required_text_field(e):
        if e.control.value == "":
            e.control.error_text = "Por favor, preencha este campo"
            e.control.update()
        elif password.value != password_confirm.value:
            e.control.error_text = "As senhas não coincidem"
            e.control.update()

    success_dlg = AlertDialog(
        modal=True,
        title=Text("Registrado com sucesso!"),
        content=Text(f"agora você faz parte dos NCD Gamers!!"),
        actions=[
            TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=MainAxisAlignment.CENTER,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    submit = FilledButton("Submit", on_click=submit_form)
    fullname = TextField(label="Nome Completo",keyboard_type=KeyboardType.NAME,on_blur=validate_required_text_field)
    email = TextField(label="Email", keyboard_type=KeyboardType.EMAIL, on_blur=validate_required_text_field)
    password = TextField(label="Senha",keyboard_type=KeyboardType.NUMBER,password=True,can_reveal_password=True)
    password_confirm = TextField(label="Repetir Senha",keyboard_type=KeyboardType.NUMBER,on_blur=validate_required_text_field,password=True,can_reveal_password=True)
    divider = Divider(thickness=1)
    submit_buttom = Row(controls=[submit], alignment=MainAxisAlignment.CENTER)
    cid_register = Row(controls=[Image(src="assets/cid_register.png", width=400, height=400)], alignment=MainAxisAlignment.CENTER)
    playspace = Row(controls=[Image(src="assets/playspace.png", width=100, height=100)], alignment=MainAxisAlignment.CENTER)
    back = ElevatedButton("Voltar", on_click=go_back)
    return SafeArea(
        Column(
            scroll=ScrollMode.ALWAYS,
            # alignment=MainAxisAlignment.CENTER,
            controls=[back,playspace,fullname,email,password,password_confirm,birthdate, Text("Gênero:"), gender, divider, submit_buttom,cid_register
            ],
        ),
        expand=True,
    )
