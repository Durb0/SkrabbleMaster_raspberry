def header(title, cursor):
    height = 25
    return ([
        "fill?color=0x0000;",
        "rectangle_fill?color=0xEEEE;x_start=0;y_start={};x_end={};y_end={};".format(cursor, 240, cursor+ height),
        "text?value={};color=0xFFFF;size=2;x_start=10;y_start={};".format(title, cursor+5),
        ],
        cursor + height + 5
    )