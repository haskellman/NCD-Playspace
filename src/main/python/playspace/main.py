from flet import *
import flet_router as fr
from pages.Base_url import router

# Pages
from pages.Home import home
from pages.Register import register
from pages.Playspace import playspace


def main(page:Page):
    def window_event(e):
        if e.data == "close":
            page.dialog = confirm_dialog
            confirm_dialog.open = True
            page.update()

    page.window_prevent_close = True
    page.on_window_event = window_event

    def yes_click(e):
        page.window_destroy()

    def no_click(e):
        confirm_dialog.open = False
        page.update()

    confirm_dialog = AlertDialog(
        modal=True,
        title=Text("Tem Certeza?"),
        content=Text("voce tem certeza que deseja sair? "),
        actions=[
            ElevatedButton("Yes", on_click=yes_click),
            OutlinedButton("No", on_click=no_click),
        ],
        actions_alignment="end",
    )
    page.title = "NCD Playspace"

    page.window_width = 440
    page.window_height = 844
    page.scroll = ScrollMode.AUTO
    
    app_router = fr.Router.mount(
        page,
        routes=router.routes  
    )
    app_router.go_root("/")

app(main,view=AppView.WEB_BROWSER,port=5050)