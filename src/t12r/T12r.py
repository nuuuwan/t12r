from t12r.langs import Lang


class T12r:
    def __init__(self, lang_source: Lang, lang_target: Lang):
        self.lang_source = lang_source
        self.lang_target = lang_target
