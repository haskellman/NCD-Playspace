import register
import flet as ft
class AppTile(ft.ListTile):
    def __init__(self, name, view, icon_name, file_name):
        super().__init__()
        self.view = view
        self.bgcolor = ft.colors.BLACK
        self.title = ft.Text(name)
        self.leading = ft.Icon(icon_name)
        self.on_click = self.app_button_clicked
        self.name = name
        self.file_name = file_name

    def app_button_clicked(self, e):
        e.control.page.views.append(
            ft.View(
                controls=[
                    ft.AppBar(
                        title=ft.Text(f"{e.control.name}"),
                    ),
                    e.control.view,
                ],
            )
        )
        e.control.page.update()


def main(page: ft.Page):
    page.title = "NCD App"
    page.window_full_screen = True
    page.window_resizable = True
    page.window_movable = True
    page.window_minimizable = True
    page.window_title_bar_buttons_hidden = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    menu = ft.GridView(
    width=800,
    height=1200,
    runs_count=2,
    run_spacing=10,
    auto_scroll=False,
    adaptive=True,
    controls=[
        AppTile(
            name="Register",
            file_name="register.py",
            view=register.example(page),
            icon_name=ft.icons.LOGIN,
        ),
    ],
    )
    page.add(menu)

    def view_pop(view):
        page.views.pop()
        top_view = page.views[0]
        page.go(top_view.route)

    page.on_view_pop = view_pop
    page.window_width = 390
    page.window_height = 844
    page.update()


ft.app(target=main, assets_dir="assets",port=8550, view=WEB)
