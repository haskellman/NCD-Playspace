import flet as ft

ft.Page.bgcolor = "#070f2b"

def example(page):
    page.bgcolor = "#070f2b"

    img = ft.Image(
        src="assets/cid.png",
        width=200,
        height=200,
    )
    def submit_form(e):
        e.control.page.update()
        print(f"logado com sucesso!")
        page.go("register.py")

    submit = ft.FilledButton("Submit", on_click=submit_form)

    email = ft.TextField(label="Email", keyboard_type=ft.KeyboardType.EMAIL, width=300, height=50,)
    password = ft.TextField(label="Senha", keyboard_type=ft.KeyboardType.NUMBER, password=True, can_reveal_password=True, width=300, height=50,)

    return ft.SafeArea(
        ft.Column(
            scroll=ft.ScrollMode.AUTO,
            # alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    controls=[email], 
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                ft.Row(
                    controls=[password], 
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                ft.Divider(thickness=1),
                ft.Row(controls=[submit], alignment=ft.MainAxisAlignment.CENTER),
                # ft.Column(img, alignment=ft.MainAxisAlignment.CENTER),
            ],
        ),
        expand=True,
    )
