
is_menu_bar_clicked = False
def drag_window_setup(dpg, size):
    def mouse_drag_callback(_, app_data):
        if is_menu_bar_clicked:
            _, drag_delta_x, drag_delta_y = app_data
            viewport_pos_x, viewport_pos_y = dpg.get_viewport_pos()
            new_pos_x = viewport_pos_x + drag_delta_x
            new_pos_y = viewport_pos_y + drag_delta_y
            dpg.set_viewport_pos([new_pos_x, new_pos_y])
    def mouse_click_callback():
        global is_menu_bar_clicked
        mouse_pos_temp = dpg.get_mouse_pos(local=False)
        if mouse_pos_temp[1] < size:
            if mouse_pos_temp[1] <= 31 or mouse_pos_temp[1] >= 7:
                if mouse_pos_temp[0] >= 490 or mouse_pos_temp[0] <= 465:is_menu_bar_clicked = True   
                else: is_menu_bar_clicked = False   
            else:is_menu_bar_clicked = True   
        else:is_menu_bar_clicked = False   
    with dpg.handler_registry():
        dpg.add_mouse_drag_handler(button=0, threshold=0, callback=mouse_drag_callback)
        dpg.add_mouse_click_handler(button=0, callback=mouse_click_callback)