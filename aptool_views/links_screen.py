import flet as ft
from functools import partial

from app_colors import AppColors


def links_screen(page: ft.Page):

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=AppColors.pink,
            primary_container=AppColors.pink,
            secondary=AppColors.pink,
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
        cursor_color=AppColors.pink,
        selection_color=AppColors.pink,
        label_style=ft.TextStyle(color=AppColors.pink),
        expand=False,
    )

    return ft.View(
        route="/links",
        controls=[
            ft.AppBar(
                title=ft.Row(
                    controls=[
                        ft.Icon(name=ft.Icons.LINK_ROUNDED, color=AppColors.mainBack),
                        ft.Text("Links", color=AppColors.mainBack, size=20),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=AppColors.pink,
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