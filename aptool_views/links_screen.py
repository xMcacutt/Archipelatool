import flet as ft
from functools import partial

from app_colors import AppColors


def link_tile(icon_name, text, url):
    return ft.Container(
        content=ft.ElevatedButton(
            icon=icon_name,
            text=text,
            icon_color=AppColors.pink,
            color=AppColors.pink,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=10,
                bgcolor=AppColors.altBack,
            ),
            on_click=lambda e: ft.UrlTarget(url),
        ),
        padding=5,
    )


def section_title(text):
    return ft.Text(text, size=18, weight=ft.FontWeight.BOLD, color=AppColors.mainText)


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

    return ft.View(
        route="/links",
        scroll=ft.ScrollMode.AUTO,
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
            ft.Container(
                padding=20,
                content=ft.Column(
                    spacing=25,
                    controls=[
                        section_title("Links"),
                        ft.ResponsiveRow(
                            spacing=10,
                            controls=[
                                link_tile(ft.Icons.PUBLIC, "Archipelago.gg", "https://archipelago.gg"),
                                link_tile(ft.Icons.CODE, "Archipelago Repository", "https://github.com/ArchipelagoMW/Archipelago"),
                                link_tile(ft.Icons.CODE, "Archipelatool Repository", "https://github.com/xMcacutt/Archipelatool"),
                                link_tile(ft.Icons.DISCORD_ROUNDED, "Archipelago Discord", "https://discord.gg/archipelago"),
                                link_tile(ft.Icons.NIGHTLIFE, "After Dark Discord (18+)", "https://discord.gg/afterdark"),
                            ]
                        ),
                        ft.Column(
                            spacing=10,
                            controls=[
                                section_title("About This Tool"),
                                ft.Text("This tool was designed to consolidate many common features and requests for the Archipelago project into a single, user-friendly application. "
                                        "It streamlines access to essential resources, tools, and community links, reducing friction for both new and experienced players."
                                        "\n\n It includes quick access to key websites, Discord communities, and the project's GitHub as well as mini apps for creating and modifying yamls, "
                                        "generating and hosting multiworlds, and installing and updating apworlds helping to bridge the gap between supported and unsupported worlds without undermining the integrity of the project.",
                                        color=AppColors.mainText,
                                ),
                                section_title("Authors"),
                                ft.Text(
                                    "xMcacutt, ..., ...",
                                    color=AppColors.mainText,
                                )
                            ]
                        ),
                    ]
                )
            )
        ],
        bgcolor=AppColors.mainBack
    )
