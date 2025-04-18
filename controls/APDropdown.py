import flet as ft

from app_colors import AppColors


class APDropdown(ft.Dropdown):
    def __init__(self, label="", options=[], value="", color=AppColors.mainText, *args, **kwargs):
        super().__init__(
            label=label,
            options=options,
            value=value,
            fill_color=AppColors.altBack,
            border_radius=10,
            border_width=1.2,
            bgcolor=AppColors.altBack,
            border_color=color,
            filled=True,
        ),