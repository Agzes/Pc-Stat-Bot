big_let_start = 0x00C0
big_let_end = 0x00DF
small_let_end = 0x00FF
remap_big_let = 0x0410
alph_len = big_let_end - big_let_start + 1
alph_shift = remap_big_let - big_let_start

def init_font_with_cyr_support(dpg, font_path, font_registry):
    with dpg.font(font_path, 15, parent=font_registry) as cyr_support_font: 
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        biglet = remap_big_let
        for i1 in range(big_let_start, big_let_end + 1):
            dpg.add_char_remap(i1, biglet)
            dpg.add_char_remap(i1 + alph_len, biglet + alph_len)
            biglet += 1
    return cyr_support_font

def to_cyr(data_no_cyr):
    out = []
    for i in range(0, len(data_no_cyr)):
        if ord(data_no_cyr[i]) in range(big_let_start, small_let_end + 1):
            out.append(chr(ord(data_no_cyr[i]) + alph_shift))
        else:
            out.append(data_no_cyr[i])
    return ''.join(out)


