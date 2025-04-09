import flet as ft

from app_colors import AppColors


def clients_screen(page: ft.Page):
    return ft.View(
        route="/clients",
        controls=[
            ft.AppBar(
                title=ft.Text("Clients", color=AppColors.mainText),
                bgcolor=AppColors.specialBack,
                leading=ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    on_click=lambda e: page.go("/")  # Navigate back to the home screen
                )
            ),
            ft.Text("This is the Clients Screen", color=AppColors.mainText),
        ],
        bgcolor=AppColors.mainBack
    )