import flet as ft
import json

from app_colors import AppColors


def games_screen(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=AppColors.orange,
            primary_container=AppColors.orange,
            secondary=AppColors.orange,
            background=AppColors.mainBack,
            surface=AppColors.altBack,
            on_primary=AppColors.mainBack,
            on_background=AppColors.mainText,
            surface_bright=AppColors.specialBack,
        ),
        elevated_button_theme=ft.ElevatedButtonTheme(
            bgcolor=AppColors.orange,
            foreground_color=AppColors.mainBack,
        ),
        radio_theme=ft.RadioTheme(fill_color=AppColors.orange),
        divider_color=AppColors.specialBack,
        font_family="Roboto",
        use_material3=True,
    )
    page.controls.clear()

    game_data = {}
    try:
        with open("assets/games_index.json", "r", encoding="utf-8-sig") as f:
            game_data = json.load(f)
    except Exception as e:
        print(f"Failed to load game data: {e}")

    selected_platforms = set()
    selected_phases = set()

    platforms = sorted({info["Platform"] for info in game_data.values()})
    phases = sorted({info["DevelopmentPhase"] for info in game_data.values()})

    list_view = ft.ListView(expand=True, spacing=10, padding=10, auto_scroll=False)

    def create_game_card(name, details):
        return ft.Card(
            shadow_color=AppColors.invertedText,
            elevation=10,
            content=ft.Container(
                border_radius=10,
                bgcolor=AppColors.altBack,
                content=ft.ListTile(
                    title=ft.Text(name, size=20, color=AppColors.orange),
                    subtitle=ft.Column(controls=[
                        ft.Text(details.get('Description', 'No description provided'), color=AppColors.mainText),
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Text(f"Platform: {details.get('Platform', 'Unknown')}", color=AppColors.mainText, size=12),
                                    ft.Text(f"Phase: {details.get('DevelopmentPhase', 'Unknown')}", color=AppColors.mainText, size=12),
                                    ft.Text(f"Author: {details.get('Author', 'Unknown')}", color=AppColors.mainText, size=12),
                                ],
                            ),
                        )],
                        expand=True
                    ),
                    trailing=ft.Container(
                        ft.Row(controls=[
                            ft.IconButton(icon=ft.Icons.MENU_BOOK_ROUNDED),
                            ft.IconButton(icon=ft.Icons.DOWNLOAD_ROUNDED)
                        ], alignment=ft.MainAxisAlignment.END, tight=True),
                    )
                )
            )
        )

    def refresh_list():
        query = search_field.value.strip().lower()
        filtered = []
        for name, details in game_data.items():
            if query and query not in name.lower():
                continue
            if selected_platforms and details.get("Platform") not in selected_platforms:
                continue
            if selected_phases and details.get("DevelopmentPhase") not in selected_phases:
                continue
            filtered.append(create_game_card(name, details))

        list_view.controls = filtered if filtered else [ft.Text("No games found", color="red")]
        page.update()

    def make_chip(label, group):
        return ft.Chip(
            label=ft.Text(label, color=AppColors.mainBack, size=10),
            height=30,
            border_side=ft.BorderSide(width=0),
            color=AppColors.orange,
            selected=label in group,
            check_color=AppColors.mainBack,
            on_select=lambda e: toggle_chip(e, label, group)
        )

    def toggle_chip(e, label, group):
        if e.control.selected:
            group.add(label)
        else:
            group.discard(label)
        refresh_list()

    platform_chips_row = ft.Row([make_chip(p, selected_platforms) for p in platforms], wrap=True, spacing=8, run_spacing=4)
    phase_chips_row = ft.Row([make_chip(p, selected_phases) for p in phases], wrap=True, spacing=8, run_spacing=4)

    search_field = ft.TextField(
        label="Search games...",
        border_color=AppColors.specialBack,
        bgcolor=AppColors.altBack,
        color=AppColors.mainText,
        cursor_color=AppColors.orange,
        selection_color=AppColors.orange,
        label_style=ft.TextStyle(color=AppColors.orange),
        expand=False,
        on_change=lambda e: refresh_list(),
    )

    view = ft.View(
        route="/generate",
        controls=[
            ft.AppBar(
                title=ft.Row(
                    controls=[
                        ft.Icon(name=ft.Icons.VIDEOGAME_ASSET_ROUNDED, color=AppColors.mainBack),
                        ft.Text("Games", color=AppColors.mainBack, size=20),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=AppColors.orange,
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    icon_color=AppColors.mainBack,
                    on_click=lambda e: page.go("/")
                )
            ),
            ft.Container(content=search_field, padding=10),
            ft.Container(
                ft.ExpansionTile(
                    controls=[
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        ft.Text("Filter by Platform", color=AppColors.mainText, size=12),
                                        padding=ft.padding.only(left=10),
                                        alignment=ft.alignment.top_left  # Ensure left alignment of this text
                                    ),
                                    ft.Container(
                                        platform_chips_row,
                                        padding=ft.padding.only(left=10),
                                        alignment=ft.alignment.top_left  # Left align platform chips row
                                    ),
                                    ft.Container(
                                        ft.Text("Filter by Phase", color=AppColors.mainText, size=12),
                                        padding=ft.padding.only(left=10),
                                        alignment=ft.alignment.top_left  # Ensure left alignment of this text
                                    ),
                                    ft.Container(
                                        phase_chips_row,
                                        padding=ft.padding.only(left=10),
                                        alignment=ft.alignment.top_left  # Left align phase chips row
                                    ),
                                ],
                                alignment=ft.alignment.top_left  # Left align the entire Column
                            ),
                            expand=True,
                            padding=10
                        )
                    ],
                    title=ft.Text("Filter"),
                ),
                alignment=ft.alignment.center_left,  # Align the ExpansionTile to the left
                padding=ft.padding.only(left=15, right=15)
            ),
            list_view,
        ],
        padding=ft.padding.only(bottom=20),
        bgcolor=AppColors.mainBack
    )

    refresh_list()
    page.views.append(view)
    page.update()