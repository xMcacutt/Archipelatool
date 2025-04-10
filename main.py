import flet as ft

from app_colors import AppColors
from aptool_views.clients_screen import clients_screen
from aptool_views.yamls_screen import yamls_screen
from aptool_views.home_screen import home_screen


def main(page: ft.Page):
    page.title = "Archipelatool"
    page.bgcolor = AppColors.mainBack
    page.window.width = 1000
    page.window.min_width = 500
    page.window.height = 700
    page.window.min_height = 400

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(home_screen(page))
        elif page.route == "/clients":
            page.views.append(clients_screen(page))
        elif page.route == "/yamls":
            page.views.append(yamls_screen(page))
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Tell Flet what to do on navigation
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Navigate to the current route
    page.go(page.route)


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
