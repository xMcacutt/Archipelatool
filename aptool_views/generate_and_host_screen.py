import flet as ft
from functools import partial
from datetime import datetime
import random

from app_colors import AppColors
from controls.APDropdown import APDropdown
from controls.APTextField import APTextField

dummy_yamls = ["AMattInTime.yaml", "SuperMattioWorld.yaml", "Mattenger.yaml", "Mattcraft.yaml", "Mattctorio.yaml", "MegaMatt2.yaml", "SonicAdventure2Mattle.yaml"]

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
        radio_theme=ft.RadioTheme(
            fill_color=AppColors.red
        ),
        divider_color=AppColors.specialBack,
        font_family="Roboto",
        use_material3=True,
    )
    page.controls.clear()
    page.update()

    folder_mode = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="temp", label="Use temporary folder"),
            ft.Radio(value="existing", label="Use existing folder"),
        ]),
        value="temp",
    )

    output_mode = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="recent", label="Use most recent"),
            ft.Radio(value="selected", label="Select output file"),
        ]),
        value="recent",
    )

    output_input = ft.Row(
        visible=False,
        controls=[
            ft.TextField(
                label="Select file...",
                expand=True,
                color=AppColors.mainText,
                bgcolor=AppColors.altBack,
                suffix=ft.ElevatedButton(
                    on_click=lambda e: print("Browse for output file..."),
                    text="Browse",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
                )
            ),
        ]
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

    yaml_files_column = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    def edit_yaml(yaml_name):
        pass

    def delete_yaml(yaml_name):
        pass

    def test_yaml(yaml_name):
        pass

    def update_yaml_list():
        yaml_files_column.controls.clear()
        for yaml_name in dummy_yamls:
            yaml_files_column.controls.append(
                ft.ListTile(
                    height=35,
                    leading=ft.IconButton(
                        icon=ft.Icons.DELETE_ROUNDED,
                        on_click=partial(lambda y, e: delete_yaml(y), yaml_name)
                    ),
                    title=ft.Text(yaml_name),
                    trailing=ft.Row(controls=[
                        ft.IconButton(
                            icon=ft.Icons.EDIT_ROUNDED,
                            on_click=partial(lambda y, e: edit_yaml(y), yaml_name)
                        ),
                        ft.IconButton(
                            icon=ft.Icons.SCIENCE_ROUNDED,
                            on_click=partial(lambda y, e: test_yaml(y), yaml_name)
                        ),
                    ], tight=True)
                )
            )
        page.update()

    def toggle_folder_mode(e):
        if folder_mode.value == "existing":
            folder_input.visible = True
        else:
            folder_input.visible = False
        page.update()

    def toggle_output_mode(e):
        if output_mode.value == "selected":
            output_input.visible = True
        else:
            output_input.visible = False
        page.update()

    folder_mode.on_change = toggle_folder_mode
    output_mode.on_change = toggle_output_mode
    toggle_folder_mode(None)
    toggle_output_mode(None)

    update_yaml_list()

    generate_button = ft.ElevatedButton(
        text="Generate",
        on_click=lambda e: print("Generating..."),
        width=150,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )

    open_folder_button = ft.ElevatedButton(
        text="Open Folder",
        on_click=lambda e: print("Select a folder..."),
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )

    local_host_button = ft.ElevatedButton(text="Local Host", disabled=True, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)), width=150)
    web_host_button = ft.ElevatedButton(text="Web Host", disabled=True, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)), width=150)

    def update_host_buttons(e):
        is_selected = True
        local_host_button.disabled = not is_selected
        web_host_button.disabled = not is_selected
        page.update()

    host_settings = ft.Column([
        ft.Container(
            ft.Row(controls=[
                APTextField(label="Hint cost (%)", color=AppColors.red, width=200),
                APDropdown(
                    label="Release mode",
                    options=[ft.dropdown.Option(opt) for opt in ["disabled", "enabled", "auto", "auto-enabled", "goal"]],
                    value="goal",
                    color=AppColors.red
                ),
                APDropdown(
                    label="Collect mode",
                    options=[ft.dropdown.Option(opt) for opt in ["disabled", "enabled", "auto", "auto-enabled", "goal"]],
                    value="goal",
                    color=AppColors.red
                ),
                APDropdown(
                    label="Remaining mode",
                    options=[ft.dropdown.Option(opt) for opt in ["disabled", "enabled", "goal"]],
                    value="goal",
                    color=AppColors.red
                ),
                APTextField(label="Auto shutdown (seconds)", color=AppColors.red, width=200),
            ]),
            padding=10
        )
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
                        ft.Column(controls=[
                            host_settings,
                        ]),
                    ], title=ft.Text("Settings"), initially_expanded=False),
                    ft.ExpansionTile(controls=[
                        ft.Column(controls=[
                            ft.Container(content=folder_mode, padding=ft.padding.only(top=10)),
                            folder_input,
                            open_folder_button,
                        ]),
                        ft.Divider(),

                        ft.Text("YAML Files", size=16, color=AppColors.mainText),
                        ft.Container(
                            ft.Column(controls=[
                                ft.Container(
                                    content=yaml_files_column,
                                    bgcolor=AppColors.altBack,
                                    height=300,
                                    border_radius=10,
                                    padding=ft.padding.only(top=10, bottom=10),
                                ),
                                ft.Container(
                                    ft.Row(
                                        controls=[
                                            ft.Text("Total: " + str(len(dummy_yamls))),
                                            generate_button,
                                        ],
                                        alignment=ft.MainAxisAlignment.END
                                    ),
                                    alignment=ft.alignment.center_right,
                                    padding=10,
                                )
                            ]),
                            padding=10
                        )
                    ], title=ft.Text("Generate"), initially_expanded=True),
                    ft.ExpansionTile(controls=[
                        ft.Container(content=
                            ft.Column(controls=[
                                output_mode,
                                output_input,
                                ft.Container(
                                    ft.Row(
                                        controls=[local_host_button, web_host_button],
                                        spacing=10,
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                    alignment=ft.alignment.center,
                                    padding=10,
                                )
                            ]),
                            padding=10
                        )
                    ], title=ft.Text("Host")),
                ]),
                padding=10
            )
        ],
        scroll=ft.ScrollMode.AUTO,
        bgcolor=AppColors.mainBack
    )

