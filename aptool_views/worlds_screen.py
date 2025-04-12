import flet as ft
from functools import partial

from app_colors import AppColors


def worlds_screen(page: ft.Page):

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=AppColors.green,
            primary_container=AppColors.green,
            secondary=AppColors.green,
            background=AppColors.mainBack,
            surface=AppColors.altBack,
            on_primary=AppColors.mainBack,
            on_background=AppColors.mainText,
            surface_bright=AppColors.specialBack,
        ),
        font_family="Roboto",
        use_material3=True,
    )

    search_field = ft.TextField(
        label="Search clients...",
        border_color=AppColors.specialBack,
        bgcolor=AppColors.altBack,
        color=AppColors.mainText,
        cursor_color=AppColors.green,
        selection_color=AppColors.green,
        label_style=ft.TextStyle(color=AppColors.green),
        expand=False,
    )

    return ft.View(
        route="/worlds",
        controls=[
            ft.AppBar(
                title=ft.Row(
                    controls=[
                        ft.Icon(name=ft.Icons.TRAVEL_EXPLORE_ROUNDED, color=AppColors.mainBack),
                        ft.Text("Worlds", color=AppColors.mainBack, size=20),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=AppColors.green,
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    icon_color=AppColors.mainBack,
                    on_click=lambda e: page.go("/")
                )
            ),
            search_field,
        ],
        bgcolor=AppColors.mainBack
    )