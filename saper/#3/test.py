    if s:
        if(buttons[f'btn ({x},{y})']["bg"] == 'black'):
            buttons[f'btn ({x},{y})']["bg"] = default_color
    else:
        buttons[f'btn ({x},{y})']["bg"] = active
        #root.destroy()