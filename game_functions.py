import sys,pygame

def check_events(icon, ai_settings, screen, status, Start, GameScreen, GameOver):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and status.menu == 1:
            print("")
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_win(icon, status)
            check_mouse_click(ai_settings, icon, screen, status, Start, GameScreen, mouse_x, mouse_y)
            update_screen(icon, ai_settings, screen, status, Start, GameScreen, GameOver)
        elif event.type == pygame.MOUSEBUTTONDOWN and status.menu != 1:
            print("")
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_mouse_click(ai_settings, icon, screen, status, Start, GameScreen, mouse_x, mouse_y)
            update_screen(icon, ai_settings, screen, status, Start, GameScreen, GameOver)

def draw_boxes(ai_settings, screen, GameScreen):
    global box_rect_data
    pointer = 0
    box_rect_data = []
    for i in range (len(GameScreen.square_rect_data)):
        for j in range (0,1):
            a = GameScreen.square_rect_data[pointer][0]
            b = GameScreen.square_rect_data[pointer][1]
            box_rect = pygame.draw.rect(screen, ai_settings.bg_color, (a, b, 100, 100))
            box_rect_data.append(box_rect)
        pointer += 1

def check_box_clicked(ai_settings, icon, screen, status, GameScreen, mouse_x, mouse_y):
    draw_boxes(ai_settings, screen, GameScreen)
    status.pointer = 0
    for i in range(len(GameScreen.square_rect_data)):
        box_clicked = box_rect_data[status.pointer].collidepoint(mouse_x, mouse_y)
        if status.pointer < len(GameScreen.square_rect_data):
            if box_clicked:
                print("Box", status.pointer + 1, "Clicked")
                ai_settings.play_sound(2)
                icon.update(status)
                break
            elif not box_clicked:
                status.pointer += 1
        if status.pointer == len(GameScreen.square_rect_data):
            status.turn -= 1
            break


def check_mouse_click(ai_settings, icon, screen, status, Start, GameScreen, mouse_x, mouse_y):
    if status.menu == 0:
        logo_Start_clicked = Start.logo_rect.collidepoint(mouse_x, mouse_y)
        play_button_clicked = Start.start_rect.collidepoint(mouse_x, mouse_y)
        quit_button_clicked = Start.quit_rect.collidepoint(mouse_x, mouse_y)
        if logo_Start_clicked:
            print("Logo Clicked")
            ai_settings.play_sound(1)
        elif play_button_clicked:
            print("Play Button Clicked")
            ai_settings.play_sound(1)
            status.menu = 1
        elif quit_button_clicked:
            print("Quiting Game")
            sys.exit()

    elif status.menu == 1:
        check_box_clicked(ai_settings, icon, screen, status, GameScreen, mouse_x, mouse_y)

    #Universal Condition
    logo_Game_clicked = GameScreen.logo_rect.collidepoint(mouse_x, mouse_y)
    if logo_Game_clicked and status.menu != 0:
        print("Logo Clicked")
        ai_settings.play_sound(1)
        status.menu = 0

def check_win(icon, status):
    x_data = []
    o_data = []
    
    for i in range (len(icon.icons_rect_present_data)):
        if i % 2 == 0:
            x_data.append(icon.icons_rect_present_data[i])
        elif i % 2 != 0:
            o_data.append(icon.icons_rect_present_data[i])

    #Check if Player 1 (X) wins
    #Check Horizontally
    if icon.icons_rect_data[0] in x_data and icon.icons_rect_data[1] in x_data and icon.icons_rect_data[2] in x_data:
        status.menu = 2
    if icon.icons_rect_data[3] in x_data and icon.icons_rect_data[4] in x_data and icon.icons_rect_data[5] in x_data:
        status.menu = 2
    if icon.icons_rect_data[6] in x_data and icon.icons_rect_data[7] in x_data and icon.icons_rect_data[8] in x_data:
        status.menu = 2
    #Check Vertically
    if icon.icons_rect_data[0] in x_data and icon.icons_rect_data[3] in x_data and icon.icons_rect_data[6] in x_data:
        status.menu = 2
    if icon.icons_rect_data[1] in x_data and icon.icons_rect_data[4] in x_data and icon.icons_rect_data[7] in x_data:
        status.menu = 2
    if icon.icons_rect_data[2] in x_data and icon.icons_rect_data[5] in x_data and icon.icons_rect_data[8] in x_data:
        status.menu = 2
    #Check Diagonally
    if icon.icons_rect_data[0] in x_data and icon.icons_rect_data[4] in x_data and icon.icons_rect_data[8] in x_data:
        status.menu = 2
    if icon.icons_rect_data[2] in x_data and icon.icons_rect_data[4] in x_data and icon.icons_rect_data[6] in x_data:
        status.menu = 2

    #Check if Player 2 (O) wins
    #Check Horizontally
    if icon.icons_rect_data[0] in o_data and icon.icons_rect_data[1] in o_data and icon.icons_rect_data[2] in o_data:
        status.menu = 2
    if icon.icons_rect_data[3] in o_data and icon.icons_rect_data[4] in o_data and icon.icons_rect_data[5] in o_data:
        status.menu = 2
    if icon.icons_rect_data[6] in o_data and icon.icons_rect_data[7] in o_data and icon.icons_rect_data[8] in o_data:
        status.menu = 2
    # Check Vertically
    if icon.icons_rect_data[0] in o_data and icon.icons_rect_data[3] in o_data and icon.icons_rect_data[6] in o_data:
        status.menu = 2
    if icon.icons_rect_data[1] in o_data and icon.icons_rect_data[4] in o_data and icon.icons_rect_data[7] in o_data:
        status.menu = 2
    if icon.icons_rect_data[2] in o_data and icon.icons_rect_data[5] in o_data and icon.icons_rect_data[8] in o_data:
        status.menu = 2
    # Check Diagonally
    if icon.icons_rect_data[0] in o_data and icon.icons_rect_data[4] in o_data and icon.icons_rect_data[8] in o_data:
        status.menu = 2
    if icon.icons_rect_data[2] in o_data and icon.icons_rect_data[4] in o_data and icon.icons_rect_data[6] in o_data:
        status.menu = 2

def update_screen(icon, ai_settings, screen, status, Start, GameScreen, GameOver):
    if status.menu == 0:
        status.reset()
        screen.fill(ai_settings.bg_color)
        Start.draw_start()
        icon.icons_rect_present_data = []
    if status.menu == 1:
        screen.fill(ai_settings.bg_color)
        GameScreen.draw_game_screen()
        if status.turn == 0:
            status.turn += 1
        elif status.turn != 0:
            print("Turn", status.turn)
            icon.draw_icons(status)
            status.turn += 1
    if status.menu == 2:
        screen.fill(ai_settings.bg_color)
        screen.blit(GameScreen.logo, GameScreen.logo_rect)
        GameOver.draw_game_over_screen(status, icon)
    pygame.display.flip()