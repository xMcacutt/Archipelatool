import flet as ft
from functools import partial
from datetime import datetime
import random

from app_colors import AppColors


def generate_and_host_screen(page: ft.Page):
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
        elevated_button_theme=ft.ElevatedButtonTheme(
            bgcolor=AppColors.red,
            foreground_color=AppColors.mainBack,
        ),
        divider_color=AppColors.specialBack,
        font_family="Roboto",
        use_material3=True,
    )

    # Folder mode switch
    folder_mode = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="temp", label="Use temporary folder"),
            ft.Radio(value="existing", label="Use existing folder"),
        ]),
        value="temp",
    )

    folder_input = ft.Row(
        visible=False,
        controls=[
            ft.TextField(
                label="Select folder...",
                expand=True,
                color=AppColors.mainText,
                bgcolor=AppColors.altBack,
                suffix=ft.ElevatedButton(
                    on_click=lambda e: print("Browse for folder..."),
                    text="Browse",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
                )
            ),
        ]
    )

    def toggle_folder_mode(e):
        if folder_mode.value == "existing":
            folder_input.visible = True
        else:
            folder_input.visible = False
        page.update()

    folder_mode.on_change = toggle_folder_mode

    # Simulated YAML files
    yaml_files_column = ft.Column([
        ft.Text(f"config_{i}.yaml", color=AppColors.mainText)
        for i in range(3)
    ], scroll=ft.ScrollMode.AUTO)

    drag_target = ft.Container(
        content=ft.Text("Drag files here", color=AppColors.mainText),
        bgcolor=AppColors.specialBack,
        height=100,
        border_radius=10,
        alignment=ft.alignment.center,
    )

    generate_button = ft.ElevatedButton(
        text="Generate",
        on_click=lambda e: print("Generating..."),
        bgcolor=AppColors.red,
        color=AppColors.mainBack
    )

    # Dummy generated output list
    dummy_outputs = [
        {
            "name": f"output_{i}.yaml",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        for i in range(5)
    ]

    selected_output = ft.Ref[ft.RadioGroup]()

    outputs_radio_group = ft.RadioGroup(
        ref=selected_output,
        content=ft.Column([
            ft.Radio(value=o["name"], label=f"{o['name']} ({o['timestamp']})", fill_color=AppColors.red)
            for o in dummy_outputs
        ])
    )

    # Host buttons
    local_host_button = ft.ElevatedButton(text="Local Host", disabled=True)
    web_host_button = ft.ElevatedButton(text="Web Host", disabled=True)

    def update_host_buttons(e):
        is_selected = selected_output.current.value is not None
        local_host_button.disabled = not is_selected
        web_host_button.disabled = not is_selected
        page.update()

    outputs_radio_group.on_change = update_host_buttons

    # Host settings
    host_settings = ft.Column([
        ft.TextField(label="Hint cost (%)", width=200),
        ft.Dropdown(label="Release mode", options=[ft.dropdown.Option(opt) for opt in
                                                   ["disabled", "enabled", "auto", "auto-enabled", "goal"]]),
        ft.Dropdown(label="Collect mode", options=[ft.dropdown.Option(opt) for opt in
                                                   ["disabled", "enabled", "auto", "auto-enabled", "goal"]]),
        ft.Dropdown(label="Remaining mode",
                    options=[ft.dropdown.Option(opt) for opt in ["disabled", "enabled", "goal"]]),
        ft.TextField(label="Auto shutdown (seconds)", width=200),
    ], spacing=10)

    return ft.View(
        route="/generate",
        controls=[
            ft.AppBar(
                title=ft.Row(
                    controls=[
                        ft.Icon(name=ft.Icons.WIFI_PROTECTED_SETUP_ROUNDED, color=AppColors.mainBack),
                        ft.Text("Generate & Host", color=AppColors.mainBack, size=20),
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
            ft.Container(content=
                ft.Column(controls=[
                    ft.ExpansionTile(controls=[
                        ft.Container(content=folder_mode, padding=ft.padding.only(top=10, bottom=10)),
                        folder_input,
                        ft.Divider(),
                        ft.Row([
                            ft.ElevatedButton(text="Open Folder", on_click=lambda e: print("Open folder in explorer")),
                            drag_target
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Text("YAML Files", size=16, color=AppColors.mainText),
                        yaml_files_column,
                        generate_button,
                    ], title=ft.Text("Generate"), initially_expanded=True),
                    ft.ExpansionTile(controls=[
                        host_settings,
                        ft.Text("Generated Outputs", size=16, color=AppColors.mainText),
                        outputs_radio_group,
                        ft.Row([local_host_button, web_host_button], spacing=10),
                    ], title=ft.Text("Host")),
                ]),
                padding=10
            )
        ],
        bgcolor=AppColors.mainBack
    )

