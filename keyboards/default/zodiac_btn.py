from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

CALLBACK_BUTTON1_aries = "callback_button1_aries"
CALLBACK_BUTTON2_taurus = "callback_button2_taurus"
CALLBACK_BUTTON3_gemini = "callback_button3_gemini"
CALLBACK_BUTTON4_cancer = "callback_button4_cancer"
CALLBACK_BUTTON5_leo = "callback_button5_leo"
CALLBACK_BUTTON6_virgo = "callback_button6_virgo"
CALLBACK_BUTTON7_libra = "callback_button7_libra"
CALLBACK_BUTTON8_scorpio = "callback_button8_scorpio"
CALLBACK_BUTTON9_sagittarius = "callback_button9_sagittarius"
CALLBACK_BUTTON10_capricorn = "callback_button10_capricorn"
CALLBACK_BUTTON11_aquarius = "callback_button11_aquarius"
CALLBACK_BUTTON12_pisces = "callback_button12_pisces"

# сchange callback

CALLBACK_SBUTTON1_aries = "callback_sbutton1_aries"
CALLBACK_SBUTTON2_taurus = "callback_sbutton2_taurus"
CALLBACK_SBUTTON3_gemini = "callback_sbutton3_gemini"
CALLBACK_SBUTTON4_cancer = "callback_sbutton4_cancer"
CALLBACK_SBUTTON5_leo = "callback_sbutton5_leo"
CALLBACK_SBUTTON6_virgo = "callback_sbutton6_virgo"
CALLBACK_SBUTTON7_libra = "callback_sbutton7_libra"
CALLBACK_SBUTTON8_scorpio = "callback_sbutton8_scorpio"
CALLBACK_SBUTTON9_sagittarius = "callback_sbutton9_sagittarius"
CALLBACK_SBUTTON10_capricorn = "callback_sbutton10_capricorn"
CALLBACK_SBUTTON11_aquarius = "callback_sbutton11_aquarius"
CALLBACK_SBUTTON12_pisces = "callback_sbutton12_pisces"

# end callback
CALLBACK_BUTTON13_yesterday = "callback_button13_yesterday"
CALLBACK_BUTTON14_ = "callback_button14_"
CALLBACK_BUTTON15_tomorrow = "callback_button15_tomorrow"
CALLBACK_BUTTON16_weekly = "callback_button16_weekly"
CALLBACK_BUTTON17_monthly = "callback_button17_monthly"

CALLBACK_BUTTON18_ = "callback_button18_"
CALLBACK_BUTTON19_erotic = "callback_button19_erotic"
CALLBACK_BUTTON20_career = "callback_button20_career"

CALLBACK_BUTTON21_start = "callback_button21_start"
CALLBACK_BUTTON22_firststart = 'callback_button22_firststart'



TITLES_zodiac = {
    CALLBACK_BUTTON1_aries: "Овен ♈",
    CALLBACK_BUTTON2_taurus: "Телец ♉",
    CALLBACK_BUTTON3_gemini: "Близнецы ♊",
    CALLBACK_BUTTON4_cancer: "Рак ♋",
    CALLBACK_BUTTON5_leo: "Лев ♌",
    CALLBACK_BUTTON6_virgo: "Дева ♍",
    CALLBACK_BUTTON7_libra: "Весы ♎",
    CALLBACK_BUTTON8_scorpio: "Скорпион ♏",
    CALLBACK_BUTTON9_sagittarius: "Стрелец ♐",
    CALLBACK_BUTTON10_capricorn: "Козерог ♑",
    CALLBACK_BUTTON11_aquarius: "Водолей ♒",
    CALLBACK_BUTTON12_pisces: "Рыбы ♓",
}

# lang = InlineKeyboardMarkup(
#     keyboard=[
#         [
#             InlineKeyboardButton(text="Овен ♈", callback_data=CALLBACK_BUTTON1_aries),
#             InlineKeyboardButton(text="Телец ♉", callback_data=CALLBACK_BUTTON2_taurus),
#             InlineKeyboardButton(text="Близнецы ♊", callback_data=CALLBACK_BUTTON3_gemini),
#             InlineKeyboardButton(text="Рак ♋", callback_data=CALLBACK_BUTTON4_cancer),
#         ],
#         [
#             InlineKeyboardButton(text="Лев ♌", callback_data=CALLBACK_BUTTON5_leo),
#             InlineKeyboardButton(text="Дева ♍", callback_data=CALLBACK_BUTTON6_virgo),
#             InlineKeyboardButton(text="Весы ♎", callback_data=CALLBACK_BUTTON7_libra),
#             InlineKeyboardButton(text="Скорпион ♏", callback_data=CALLBACK_BUTTON8_scorpio),
#         ],
#         [
#             InlineKeyboardButton(text="Стрелец ♐", callback_data=CALLBACK_BUTTON9_sagittarius),
#             InlineKeyboardButton(text="Козерог ♑", callback_data=CALLBACK_BUTTON10_capricorn),
#             InlineKeyboardButton(text="Водолей ♒", callback_data=CALLBACK_BUTTON11_aquarius),
#             InlineKeyboardButton(text="Рыбы ♓", callback_data=CALLBACK_BUTTON12_pisces),
#         ],
#     ]
# )
show_item = CallbackData("catalog_item", "zdk")
langs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Овен ♈",
                                 callback_data=show_item.new(zdk=CALLBACK_SBUTTON1_aries)),
            InlineKeyboardButton(text="Телец ♉",
                                 callback_data=show_item.new(zdk=CALLBACK_BUTTON2_taurus)),
            InlineKeyboardButton(text="Близнецы ♊",
                                 callback_data=show_item.new(zdk=CALLBACK_BUTTON3_gemini)),
            InlineKeyboardButton(text="Рак ♋",
                                 callback_data=show_item.new(zdk=CALLBACK_BUTTON3_gemini)),

        ],
        [
            InlineKeyboardButton(text="Лев ♌",
                                 callback_data=show_item.new(zdk=CALLBACK_BUTTON5_leo)),
            InlineKeyboardButton(text="Дева ♍",
                                 callback_data=show_item.new(zdk=CALLBACK_BUTTON6_virgo)),
            InlineKeyboardButton(text="Весы ♎",
                                 callback_data=show_item.new(zdk=CALLBACK_BUTTON7_libra)),
            InlineKeyboardButton(text="Скорпион ♏",
                                 callback_data=show_item.new(zdk=CALLBACK_BUTTON8_scorpio)),
        ],
        [
            InlineKeyboardButton(text="Стрелец ♐",
                                 callback_data=show_item.new(zdk=CALLBACK_BUTTON9_sagittarius)),
            InlineKeyboardButton(text="Козерог ♑",
                                 callback_data=show_item.new(zdk=CALLBACK_BUTTON10_capricorn)),
            InlineKeyboardButton(text="Водолей ♒",
                                 callback_data=show_item.new(zdk=CALLBACK_BUTTON11_aquarius)),
            InlineKeyboardButton(text="Рыбы ♓",
                                 callback_data=show_item.new(zdk=CALLBACK_BUTTON12_pisces)),
        ]

    ]
)

langschenge = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Овен ♈", callback_data=CALLBACK_SBUTTON1_aries),
            InlineKeyboardButton(text="Телец ♉", callback_data=CALLBACK_SBUTTON2_taurus),
            InlineKeyboardButton(text="Близнецы ♊", callback_data=CALLBACK_SBUTTON3_gemini),
            InlineKeyboardButton(text="Рак ♋", callback_data=CALLBACK_SBUTTON4_cancer),

        ],
        [
            InlineKeyboardButton(text="Лев ♌", callback_data=CALLBACK_SBUTTON5_leo),
            InlineKeyboardButton(text="Дева ♍", callback_data=CALLBACK_SBUTTON6_virgo),
            InlineKeyboardButton(text="Весы ♎", callback_data=CALLBACK_SBUTTON7_libra),
            InlineKeyboardButton(text="Скорпион ♏", callback_data=CALLBACK_SBUTTON8_scorpio),
        ],
        [
            InlineKeyboardButton(text="Стрелец ♐", callback_data=CALLBACK_SBUTTON9_sagittarius),
            InlineKeyboardButton(text="Козерог ♑", callback_data=CALLBACK_SBUTTON10_capricorn),
            InlineKeyboardButton(text="Водолей ♒", callback_data=CALLBACK_SBUTTON11_aquarius),
            InlineKeyboardButton(text="Рыбы ♓", callback_data=CALLBACK_SBUTTON12_pisces),
        ]

    ]
)



