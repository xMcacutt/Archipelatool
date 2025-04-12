import flet as ft

from app_colors import AppColors

world_templates = {
    "Jigsaw": {
        "number_of_pieces": {
            "type": "Range",
            "min": 25,
            "max": 1000,
            "values": {25: 50, "random": 0}
        },
        "orientation_of_image": {
            "type": "Choice",
            "options": ["square", "landscape", "portrait"],
            "default": "square"
        },
        "toggle_test": {
            "type": "DefaultOnToggle",
            "enabled": True
        },
        "default_on_toggle_test": {
            "type": "Toggle",
            "enabled": False
        }
    }
}


def yamls_screen(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=AppColors.blue,
            primary_container=AppColors.specialBack,
            surface_container=AppColors.specialBack,
            secondary=AppColors.blue,
            background=AppColors.mainBack,
            surface=AppColors.altBack,
            on_primary=AppColors.mainBack,
            on_background=AppColors.mainText,
        ),
        font_family="Roboto",
        use_material3=True,
    )
    page.theme.divider_color = AppColors.specialBack

    selected_world = ft.Text("No world selected", size=16, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    options_column = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    def render_yaml_settings(world_name):
        options_column.controls.clear()
        selected_world.value = f"Editing: {world_name}"

        options_column.controls.append(
            ft.ExpansionTile(
                title=ft.Text("Core Settings"),
                initially_expanded=True,
                tile_padding=ft.padding.only(left=20, right=20),
                controls_padding=15,
                controls=[
                    ft.Column([
                        ft.Row([
                            ft.TextField(
                                label="Name",
                                border_radius=10,
                                border_width=1.2,
                                bgcolor=AppColors.altBack,
                                border_color=AppColors.blue,
                                expand=True
                            ),
                            ft.Dropdown(
                                fill_color=AppColors.altBack,
                                border_radius=10,
                                border_width=1.2,
                                bgcolor=AppColors.altBack,
                                border_color=AppColors.blue,
                                filled=True,
                                options=[ft.dropdown.Option(opt) for opt in ["full", "minimal"]],
                                value="full",
                                label="Accessibility",
                                expand=True  # Broken until next flet update as of 10/04/2025
                            )
                        ], expand=True),
                        ft.Container(
                            content=ft.Column([
                                ft.Text("Progression Balancing"),
                                ft.Container(
                                    ft.Slider(min=0, max=100, value=50, label="{value}", divisions=20),
                                    padding=ft.padding.only(bottom=0, top=-10)
                                ),
                            ]),
                            padding=ft.padding.only(top=5)
                        ),
                    ])
                ]
            ),
        )

        options = world_templates[world_name]

        for key, setting in options.items():
            label = ft.Text(key.replace("_", " ").title())
            if setting["type"] == "Toggle" or setting["type"] == "DefaultOnToggle":
                options_column.controls.append(
                    ft.Row([
                        ft.Switch(value=setting.get("enabled"), label=key.replace("_", " ").title())
                    ])
                )
            elif setting["type"] == "Range":
                options_column.controls.append(
                    ft.Container(
                        content=ft.Column([
                            label,
                            ft.Container(
                                content=ft.Slider(min=setting["min"], max=setting["max"], divisions=10, value=50,
                                                  label="{value}"),
                                padding=ft.padding.only(bottom=0, top=-10)
                            ),
                        ]),
                        padding=ft.padding.only(top=5)
                    ),
                )
            elif setting["type"] == "Choice":
                dropdown = ft.Dropdown(
                    fill_color=AppColors.altBack,
                    border_radius=10,
                    border_width=1.2,
                    bgcolor=AppColors.altBack,
                    filled=True,
                    border_color=AppColors.blue,
                    options=[ft.dropdown.Option(opt) for opt in setting["options"]],
                    value=setting.get("default", setting["options"][0]),
                    label=key.replace("_", " ").title()
                )
                options_column.controls.append(
                    ft.Column([dropdown])
                )
            options_column.controls.append(ft.Container(height=5))

        page.update()

    # Left Drawer UI
    world_buttons = []
    for world in world_templates.keys():
        world_buttons.append(
            ft.ListTile(
                title=ft.Text(world),
                on_click=lambda e, w=world: render_yaml_settings(w)
            )
        )

    left_drawer = ft.Container(
        bgcolor=ft.colors.SURFACE_VARIANT,
        padding=20,
        width=250,
        content=ft.Column(
            controls=[
                ft.Text("Worlds", size=20),
                *world_buttons
            ],
            spacing=10
        )
    )

    # Final layout with two halves
    return ft.View(
        controls=[
            ft.AppBar(
                title=ft.Row(
                    controls=[
                        ft.Icon(name=ft.Icons.SETTINGS_ROUNDED, color=AppColors.mainBack),
                        ft.Text("Yamls", color=AppColors.mainBack, size=20),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=AppColors.blue,
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    icon_color=AppColors.mainBack,
                    on_click=lambda e: page.go("/")
                )
            ),
            ft.Row(
                controls=[
                    left_drawer,
                    ft.Container(
                        expand=True,
                        padding=20,
                        content=ft.Column(
                            controls=[
                                selected_world,
                                options_column
                            ],
                            expand=True,
                            spacing=20
                        )
                    )
                ],
                expand=True
            )
        ],
        bgcolor=AppColors.mainBack
    )
