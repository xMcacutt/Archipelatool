import flet as ft

from app_colors import AppColors


class APTextField(ft.TextField):
    def __init__(self, label="", color=AppColors.mainText, *args, **kwargs):
        # Call the parent constructor to initialize the base properties
        super().__init__(
            label=label,
            border_color=AppColors.specialBack,
            bgcolor=AppColors.altBack,
            color=AppColors.mainText,
            cursor_color=color,
            selection_color=color,
            label_style=ft.TextStyle(color=color),
            expand=False,
            *args, **kwargs
        )
