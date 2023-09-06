def draw_text(text, _font, color, surface, x, y):
    textobj = _font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)