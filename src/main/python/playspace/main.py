from copy import deepcopy

import flet as ft
from flet.utils import slugify
import register
import login
import time
from flet import (
    AppBar, 
    Card, 
    Column, 
    Container, 
    ElevatedButton, 
    IconButton,
    NavigationRail,
    NavigationRailDestination,
    Page,
    Row,
    Stack,
    Switch,
    Text,
    VerticalDivider,
    colors,
    icons,) 

class ResponsiveMenuLayout(Row):
    def __init__(
        self,
        page,
        pages,
        *args,
        support_routes=True,
        menu_extended=True,
        minimize_to_icons=False,
        landscape_minimize_to_icons=False,
        portrait_minimize_to_icons=False,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        self.page = page
        self.pages = pages

        self._minimize_to_icons = minimize_to_icons
        self._landscape_minimize_to_icons = landscape_minimize_to_icons
        self._portrait_minimize_to_icons = portrait_minimize_to_icons
        self._support_routes = support_routes

        self.expand = True

        self.navigation_items = [navigation_item for navigation_item, _ in pages]
        self.routes = [
            f"/{item.pop('route', None) or slugify(item['label'])}"
            for item in self.navigation_items
        ]
        self.navigation_rail = self.build_navigation_rail()
        self.update_destinations()
        self._menu_extended = menu_extended
        self.navigation_rail.extended = menu_extended

        page_contents = [page_content for _, page_content in pages]

        self.menu_panel = Row(
            controls=[self.navigation_rail, VerticalDivider(width=1)],
            spacing=0,
            tight=True,
        )
        self.content_area = Column(page_contents, expand=True)

        self._was_portrait = self.is_portrait()
        self._panel_visible = self.is_landscape()

        self.set_navigation_content()

        if support_routes:
            self._route_change(page.route)
            self.page.on_route_change = self._on_route_change
        self._change_displayed_page()

        self.page.on_resize = self.handle_resize

    def select_page(self, page_number):
        self.navigation_rail.selected_index = page_number
        self._change_displayed_page()

    @property
    def minimize_to_icons(self) -> bool:
        return self._minimize_to_icons or (
            self._landscape_minimize_to_icons and self._portrait_minimize_to_icons
        )

    @minimize_to_icons.setter
    def minimize_to_icons(self, value: bool):
        self._minimize_to_icons = value
        self.set_navigation_content()

    @property
    def landscape_minimize_to_icons(self) -> bool:
        return self._landscape_minimize_to_icons or self._minimize_to_icons

    @landscape_minimize_to_icons.setter
    def landscape_minimize_to_icons(self, value: bool):
        self._landscape_minimize_to_icons = value
        self.set_navigation_content()

    @property
    def portrait_minimize_to_icons(self) -> bool:
        return self._portrait_minimize_to_icons or self._minimize_to_icons

    @portrait_minimize_to_icons.setter
    def portrait_minimize_to_icons(self, value: bool):
        self._portrait_minimize_to_icons = value
        self.set_navigation_content()

    @property
    def menu_extended(self) -> bool:
        return self._menu_extended

    @menu_extended.setter
    def menu_extended(self, value: bool):
        self._menu_extended = value

        dimension_minimized = (
            self.landscape_minimize_to_icons
            if self.is_landscape()
            else self.portrait_minimize_to_icons
        )
        if not dimension_minimized or self._panel_visible:
            self.navigation_rail.extended = value

    def _navigation_change(self, e):
        self._change_displayed_page()
        self.check_toggle_on_select()
        self.page.update()

    def _change_displayed_page(self):
        page_number = self.navigation_rail.selected_index
        if self._support_routes:
            self.page.route = self.routes[page_number]
        for i, content_page in enumerate(self.content_area.controls):
            content_page.visible = page_number == i

    def _route_change(self, route):
        try:
            page_number = self.routes.index(route)
        except ValueError:
            page_number = 0

        self.select_page(page_number)

    def _on_route_change(self, event):
        self._route_change(event.route)
        self.page.update()

    def build_navigation_rail(self):
        return NavigationRail(
            selected_index=0,
            label_type="none",
            on_change=self._navigation_change,
        )

    def update_destinations(self, icons_only=False):
        navigation_items = self.navigation_items
        if icons_only:
            navigation_items = deepcopy(navigation_items)
            for item in navigation_items:
                item.pop("label")

        self.navigation_rail.destinations = [
            NavigationRailDestination(**nav_specs) for nav_specs in navigation_items
        ]
        self.navigation_rail.label_type = "none" if icons_only else "all"

    def handle_resize(self, e):
        if self._was_portrait != self.is_portrait():
            self._was_portrait = self.is_portrait()
            self._panel_visible = self.is_landscape()
            self.set_navigation_content()
            self.page.update()

    def toggle_navigation(self, event=None):
        self._panel_visible = not self._panel_visible
        self.set_navigation_content()
        self.page.update()

    def check_toggle_on_select(self):
        if self.is_portrait() and self._panel_visible:
            self.toggle_navigation()

    def set_navigation_content(self):
        if self.is_landscape():
            self.add_landscape_content()
        else:
            self.add_portrait_content()

    def add_landscape_content(self):
        self.controls = [self.menu_panel, self.content_area]
        if self.landscape_minimize_to_icons:
            self.update_destinations(icons_only=not self._panel_visible)
            self.menu_panel.visible = True
            if not self._panel_visible:
                self.navigation_rail.extended = False
            else:
                self.navigation_rail.extended = self.menu_extended
        else:
            self.update_destinations()
            self.navigation_rail.extended = self._menu_extended
            self.menu_panel.visible = self._panel_visible

    def add_portrait_content(self):
        if self.portrait_minimize_to_icons and not self._panel_visible:
            self.controls = [self.menu_panel, self.content_area]
            self.update_destinations(icons_only=True)
            self.menu_panel.visible = True
            self.navigation_rail.extended = False
        else:
            if self._panel_visible:
                dismiss_shield = Container(
                    expand=True,
                    on_click=self.toggle_navigation,
                )
                self.controls = [
                    Stack(
                        controls=[self.content_area, dismiss_shield, self.menu_panel],
                        expand=True,
                    )
                ]
            else:
                self.controls = [
                    Stack(controls=[self.content_area, self.menu_panel], expand=True)
                ]
            self.update_destinations()
            self.navigation_rail.extended = self.menu_extended
            self.menu_panel.visible = self._panel_visible

    def is_portrait(self) -> bool:
        # Return true if window/display is narrow
        # return self.page.window_height >= self.page.window_width
        return self.page.height >= self.page.width

    def is_landscape(self) -> bool:
        # Return true if window/display is wide
        return self.page.width > self.page.height


if __name__ == "__main__":

    def main(page: Page, title="Basic Responsive Menu"):

        page.title = title
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

        menu_button = IconButton(icons.MENU)

        page.appbar = AppBar(
            leading=menu_button,
            leading_width=40,
            bgcolor=colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.ACCOUNT_CIRCLE, on_click=lambda e: printseila),
                theme_icon_button],
        )

        pages = [
            (
                dict(
                    icon=icons.LANDSCAPE_OUTLINED,
                    selected_icon=icons.LANDSCAPE,
                    label="Jogos",
                ),
                create_page(
                    "Jogos",
                    "Colocar jogos aqui",
                ),
            ),
            (
                dict(
                    icon=icons.PORTRAIT_OUTLINED,
                    selected_icon=icons.PORTRAIT,
                    label="Pontuações",
                ),
                create_page(
                    "Pontuações",
                    "Colocar pontuações aqui",
                ),
            ),
        ]

        menu_layout = ResponsiveMenuLayout(page, pages)

        page.add(menu_layout)

        # menu_button.on_click = lambda e: menu_layout.toggle_navigation()

    def create_page(title: str, body: str):
        return Row(
            controls=[
                Column(
                    horizontal_alignment="stretch",
                    controls=[
                        Card(content=Container(Text(title, weight="bold"), padding=8)),
                        Text(body),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )

    def toggle_icons_only(menu: ResponsiveMenuLayout):
        menu.minimize_to_icons = not menu.minimize_to_icons
        menu.page.update()

    def toggle_menu_width(menu: ResponsiveMenuLayout):
        menu.menu_extended = not menu.menu_extended
        menu.page.update()

    ft.app(target=main)
