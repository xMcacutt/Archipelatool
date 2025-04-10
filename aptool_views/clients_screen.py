import flet as ft
from functools import partial

from app_colors import AppColors


# Sample client data structure
class Client:
    def __init__(self, name, description=None, icon_path: str = "./assets/icon.ico"):
        self.name = name
        self.description = description
        self.icon = icon_path
        self.is_favorite = False


def clients_screen(page: ft.Page, client_list=None):
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=AppColors.red,
            primary_container=AppColors.red,
            secondary=AppColors.red,
            background=AppColors.mainBack,
            surface=AppColors.altBack,
            on_primary=AppColors.mainBack,
            on_background=AppColors.mainText,
            surface_bright=AppColors.specialBack,
        ),
        font_family="Roboto",
        use_material3=True,
    )

    if client_list is None:
        client_list = [
            Client("Text Client", ""),
            Client("Universal Tracker", ""),
            Client("Autopelago", ""),
            Client("AHIT Client", "Text client for A Hat in Time"),
            Client("Bizhawk Client", ""),
            Client("Manual Client", ""),
            Client("ChecksFinder Client", ""),
        ]

    search_field = ft.TextField(
        label="Search clients...",
        border_color=AppColors.specialBack,
        bgcolor=AppColors.altBack,
        color=AppColors.mainText,
        cursor_color=AppColors.red,
        selection_color=AppColors.red,
        label_style=ft.TextStyle(color=AppColors.red),
        on_change=lambda e: update_client_list(),
        expand=False,
    )

    client_column = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    def spawn_process(client):
        # Replace with actual process logic
        print(f"Spawning process for: {client.name}")

    def toggle_favorite(client):
        client.is_favorite = not client.is_favorite
        update_client_list()

    def update_client_list():
        search_text = search_field.value.lower()
        filtered_clients = [
            client for client in client_list
            if search_text in client.name.lower()
        ]
        sorted_clients = sorted(
            filtered_clients,
            key=lambda c: (not c.is_favorite, c.name.lower())
        )
        client_column.controls.clear()
        for client in sorted_clients:
            client_column.controls.append(
                ft.ListTile(
                    leading=ft.Image(client.icon, height=32),
                    title=ft.Text(client.name),
                    subtitle=ft.Text(client.description) if client.description else None,
                    trailing=ft.IconButton(
                        icon=ft.Icons.STAR if client.is_favorite else ft.Icons.STAR_BORDER,
                        on_click=partial(lambda c, e: toggle_favorite(c), client)
                    ),
                    on_click=partial(lambda c, e: spawn_process(c), client),
                )
            )
        page.update()

    update_client_list()

    return ft.View(
        route="/clients",
        controls=[
            ft.AppBar(
                title=ft.Row(
                    controls=[
                        ft.Icon(name=ft.Icons.GROUP_ROUNDED, color=AppColors.mainBack),
                        ft.Text("Clients", color=AppColors.mainBack, size=20),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=AppColors.red,
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    icon_color=AppColors.mainBack,
                    on_click=lambda e: page.go("/")
                )
            ),
            search_field,
            ft.Container(
                content=client_column,
                expand=True,
                padding=ft.padding.only(top=10),
            ),
        ],
        bgcolor=AppColors.mainBack
    )