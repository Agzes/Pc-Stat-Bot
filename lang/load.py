import lang.ru as ru
import lang.en as en

def load_dark_translation(lang_code):
    translations_module = ru if lang_code == "ru" else en
    return translations_module.dark_translate
def load_parameters(lang_code):
    translations_module = ru if lang_code == "ru" else en
    return translations_module.parameters
def load_translation(lang_code):
    translations_module = ru if lang_code == "ru" else en
    return translations_module.translations,translations_module.telegram_bot,translations_module.parameters