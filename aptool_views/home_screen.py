import flet as ft

from app_colors import AppColors


def home_screen(page: ft.Page):
    items = [
        {'title': 'Clients', 'icon': ft.Icons.GROUP_ROUNDED, 'route': 'clients'},
        {'title': 'Generate & Host', 'icon': ft.Icons.WIFI_PROTECTED_SETUP_ROUNDED, 'route': 'generate'},
        {'title': 'Worlds', 'icon': ft.Icons.TRAVEL_EXPLORE_ROUNDED, 'route': 'worlds'},
        {'title': 'Yamls', 'icon': ft.Icons.SETTINGS_ROUNDED, 'route': 'yamls'},
        {'title': 'Games', 'icon': ft.Icons.VIDEOGAME_ASSET_ROUNDED, 'route': 'games'},
        {'title': 'Links', 'icon': ft.Icons.LINK_ROUNDED, 'route': 'links'},
    ]

    colors = [
        AppColors.yellow,
        AppColors.red,
        AppColors.green,
        AppColors.blue,
        AppColors.orange,
        AppColors.pink,
    ]

    grid_items = []
    for i, item in enumerate(items):
        grid_items.append(
            ft.Container(
                bgcolor=colors[i],
                border_radius=50,
                expand=True,
                padding=20,
                content=ft.GestureDetector(
                    on_tap=lambda e, route=item['route']: page.go(f"/{route}"),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                        controls=[
                            ft.Icon(item["icon"], size=50, color=AppColors.mainBack),
                            ft.Text(item["title"], size=18, color=AppColors.mainBack)
                        ]
                    )
                )
            )
        )

    return ft.View(
        route="/",
        controls=[
            ft.Column(
                controls=[
                    ft.GridView(
                        expand=True,
                        runs_count=3,
                        spacing=30,
                        padding=20,
                        run_spacing=30,
                        controls=grid_items
                    )
                ],
                spacing=30,
                expand=True,
                scroll=ft.ScrollMode.AUTO
            )
        ],
        bgcolor=AppColors.mainBack
    )
