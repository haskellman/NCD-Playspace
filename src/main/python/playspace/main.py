import register
import flet as ft
import login
import games
import time
class AppTile(ft.ListTile):
    def __init__(self, name, view, icon_name, file_name, color):
        super().__init__()
        self.view = view
        self.bgcolor = color
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
    page.bgcolor = "#070f2b"
    page.window_full_screen = True
    page.window_resizable = True
    page.window_movable = True
    page.window_minimizable = True
    page.window_title_bar_buttons_hidden = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.splash = ft.ProgressBar(visible=False)
    page.theme_mode = "dark"


    def change_theme(e):
        page.splash.visible = True
        page.update()
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.splash.visible = False
        theme_icon_button.selected = not theme_icon_button.selected
        time.sleep(1.2)
        page.update()

    theme_icon_button = ft.IconButton(
        ft.icons.DARK_MODE,
        selected_icon=ft.icons.LIGHT_MODE,
        icon_color=ft.colors.BLACK,
        icon_size=35,
        tooltip="change theme",
        on_click=change_theme,
        style=ft.ButtonStyle(
            color={"": ft.colors.BLACK, "selected": ft.colors.WHITE},
        ),
    )

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

# APPBAR
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.ACCESSIBILITY),
        leading_width=40,
        title=ft.Text("NCD PlaySpace"),
        center_title=False,
        bgcolor=ft.colors.GREY,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.SUPERVISED_USER_CIRCLE_SHARP),
            theme_icon_button,
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )

# GRIDVIEW
    menu = ft.GridView(
    width=800,
    height=1200,
    runs_count=2,
    run_spacing=10,
    auto_scroll=False,
    adaptive=True,
    controls=[
        AppTile(
            name="Registrar",
            file_name="register.py",
            view=register.example(page),
            icon_name=ft.icons.LOGIN,
            color="#c73d52",
        ),
        AppTile(
            name="Login",
            file_name="login.py",
            view=login.example(page),
            icon_name=ft.icons.LOGIN,
            color="#f4ad42",
        ),
        AppTile(
            name="Jogos",
            file_name="games.py",
            view=games.example(page),
            icon_name=ft.icons.GAMES,
            color="#bcd246"
        ),
        AppTile(
            name="Scores",
            file_name="games.py",
            view=login.example(page),
            icon_name=ft.icons.GAMES,
            color="#4289bc"
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


ft.app(target=main, assets_dir="assets",port=8550,)
