import flet as ft

def example(page):
    page.title = "Row example"

    return ft.SafeArea(
        ft.Column(
            scroll=ft.ScrollMode.AUTO,
            # alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Divider(thickness=1),
                # ft.Column(img, alignment=ft.MainAxisAlignment.CENTER),
            ],
        ),
        expand=True,
    )
