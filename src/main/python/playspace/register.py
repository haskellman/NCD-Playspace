import flet as ft

fullname = ft.TextField

def example(page):
    gender = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="female", label="Female"),
                ft.Radio(value="male", label="Male"),
                ft.Radio(value="not_specified", label="Not specified"),
            ]
        )
    )

    birthdate = ft.Container(
        ft.Row(
            controls=[
            ft.Dropdown(
                label="Dia",
                options=[ft.dropdown.Option(str(i)) for i in range(1, 32)],
                width=100,
            ),
            ft.Dropdown(
                label="Mes",
                options=[ft.dropdown.Option("Janeiro"),
                        ft.dropdown.Option("Fevereiro"),
                        ft.dropdown.Option("Março"),
                        ft.dropdown.Option("Abril"),
                        ft.dropdown.Option("Maio"),
                        ft.dropdown.Option("Junho"), 
                        ft.dropdown.Option("Julho"), 
                        ft.dropdown.Option("Agosto"),
                        ft.dropdown.Option("Setembro"),
                        ft.dropdown.Option("Outubro"),
                        ft.dropdown.Option("Novembro"), 
                        ft.dropdown.Option("Dezembro")],
                width=150,
            ),
            ft.Dropdown(
                label="Ano",
                options=[ft.dropdown.Option(str(i)) for i in reversed(range(1900, 2024))],
                width=100,
            ),
        ],)
    )

    def submit_form(e):
        fullname = e.control.value
        if (e.control.value is not None or fullname.value != ""):
            e.control.page.dialog = success_dlg
            success_dlg.open = True
            e.control.page.update()
            print(f"obrigado por se registrar! {fullname.value}")
        else:
            pass

    def close_dlg(e):
        success_dlg.open = False
        e.control.page.update()

    def validate_required_text_field(e):
        if e.control.value == "":
            e.control.error_text = "The field is required"
            e.control.update()

    success_dlg = ft.AlertDialog(
        # modal=True,
        # title=ft.Text("Form submitted"),
        content=ft.Text(f"Obrigado por se registrar!! {fullname.value}"),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    submit = ft.FilledButton("Submit", on_click=submit_form)

    return ft.SafeArea(
        ft.Column(
            scroll=ft.ScrollMode.AUTO,
            # alignment=ft.MainAxisAlignment.CENTER,
            controls=[
               fullname(
                    label="Nome Completo",
                    keyboard_type=ft.KeyboardType.NAME,
                    on_blur=validate_required_text_field,
                ),
                ft.TextField(
                    label="Email",
                    keyboard_type=ft.KeyboardType.EMAIL,
                    on_blur=validate_required_text_field,
                ),
                ft.TextField(
                    label="Senha",
                    keyboard_type=ft.KeyboardType.NUMBER,
                    on_blur=validate_required_text_field,
                    password=True,
                    can_reveal_password=True,
                ),
                ft.TextField(
                    label="Repetir Senha",
                    keyboard_type=ft.KeyboardType.NUMBER,
                    on_blur=validate_required_text_field,
                    password=True,
                    can_reveal_password=True,
                ),
                birthdate,

                ft.Text("Gender:"),
                gender,
                ft.Divider(thickness=1),
                ft.Row(controls=[submit], alignment=ft.MainAxisAlignment.CENTER),
            ],
        ),
        expand=True,
    )


def main(page: ft.Page):
    page.title = "Flet entry form example"
    page.window_width = 390
    page.window_height = 844
    page.add(example(main))


if __name__ == "__main__":
    ft.app(target=main)
