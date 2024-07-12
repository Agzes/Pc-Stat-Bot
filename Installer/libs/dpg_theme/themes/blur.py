# Author: dev0-1
from __future__ import annotations

from typing import Optional, Sequence

import dearpygui.dearpygui as dpg

name = """Blur"""
styles: dict[int, Sequence[float]] = {
    dpg.mvStyleVar_Alpha: [1.0],
    dpg.mvStyleVar_WindowPadding: [8.0, 8.0],
    dpg.mvStyleVar_WindowRounding: [10.0],
    dpg.mvStyleVar_WindowBorderSize: [0.0],
    dpg.mvStyleVar_WindowMinSize: [30.0, 30.0],
    dpg.mvStyleVar_WindowTitleAlign: [0.5, 0.5],
    dpg.mvStyleVar_ChildRounding: [5.0],
    dpg.mvStyleVar_ChildBorderSize: [1.0],
    dpg.mvStyleVar_PopupRounding: [10.0],
    dpg.mvStyleVar_PopupBorderSize: [0.0],
    dpg.mvStyleVar_FramePadding: [5.0, 3.5],
    dpg.mvStyleVar_FrameRounding: [5.0],
    dpg.mvStyleVar_FrameBorderSize: [0.0],
    dpg.mvStyleVar_ItemSpacing: [5.0, 4.0],
    dpg.mvStyleVar_ItemInnerSpacing: [5.0, 5.0],
    dpg.mvStyleVar_CellPadding: [4.0, 2.0],
    dpg.mvStyleVar_IndentSpacing: [5.0],
    dpg.mvStyleVar_ScrollbarSize: [15.0],
    dpg.mvStyleVar_ScrollbarRounding: [9.0],
    dpg.mvStyleVar_GrabMinSize: [15.0],
    dpg.mvStyleVar_GrabRounding: [5.0],
    dpg.mvStyleVar_TabRounding: [5.0],
    dpg.mvStyleVar_ButtonTextAlign: [0.5, 0.5],
    dpg.mvStyleVar_SelectableTextAlign: [0.0, 0.0],
}

colors: dict[int, Sequence[int, int, int, Optional[int]]] = {
    dpg.mvThemeCol_Text: [255, 255, 255, 255],
    dpg.mvThemeCol_Button: [50, 50, 50, 100],
    dpg.mvThemeCol_ButtonHovered: [70, 70, 70, 100],
    dpg.mvThemeCol_FrameBgHovered: [70, 70, 70, 100],
    dpg.mvThemeCol_FrameBgActive: [90, 90, 90, 100],
    dpg.mvThemeCol_ButtonActive: [90, 90, 90, 100],
    dpg.mvThemeCol_TitleBgActive: [40, 40, 40, 100],
    dpg.mvThemeCol_Tab: [50, 50, 50, 200],
    dpg.mvThemeCol_TabHovered: [70, 70, 70, 200],
    dpg.mvThemeCol_TabActive: [90, 90, 90, 200],
    dpg.mvThemeCol_ChildBg: [40, 40, 40, 30],
    dpg.mvThemeCol_FrameBg: [40, 40, 40, 100],
    dpg.mvThemeCol_CheckMark: [255, 255, 255, 100],
    dpg.mvThemeCol_WindowBg: [40, 40, 40, 30],
    dpg.mvThemeCol_Separator: [90, 90, 90, 140],
    dpg.mvThemeCol_PopupBg: [25, 25, 25, 255],
    dpg.mvThemeCol_Border: [90, 90, 90, 140],
    dpg.mvThemeCol_MenuBarBg: [0, 0, 0, 0],
    dpg.mvThemeCol_ScrollbarBg: [40, 40, 40, 0],
    dpg.mvThemeCol_ScrollbarGrab: [40, 40, 40, 255],
    dpg.mvThemeCol_ScrollbarGrabHovered: [60, 60, 60, 255],
    dpg.mvThemeCol_ScrollbarGrabActive: [75, 75, 75, 255],
    dpg.mvThemeCol_SliderGrab: [90, 90, 90, 140],
    dpg.mvThemeCol_SliderGrabActive: [50, 50, 50, 140],
    dpg.mvThemeCol_Header: [50, 50, 50, 140],
    dpg.mvThemeCol_HeaderHovered: [90, 90, 90, 140],
    dpg.mvThemeCol_HeaderActive: [40, 40, 40, 140],
}
