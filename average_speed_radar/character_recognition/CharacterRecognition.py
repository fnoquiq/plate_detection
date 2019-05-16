import pytesseract


class CharacterRecognition:
    img_in = None
    result = "Desconhecido"

    __characters = None
    __special_chars_to_remove = "!@#%¨&*()_+:;><^^}{`?|~¬\/=,.'ºª»‘"

    def recognition(self, img_in):
        self.img_in = img_in
        self.__characters = self.__image_to_string()
        self.__remove_noise()

        return self.result

    def __image_to_string(self):
        return pytesseract.image_to_string(self.img_in, lang='eng')

    def __remove_special_chars(self, text_to_remove_special_chars):
        for special_char in self.__special_chars_to_remove:
            text_to_remove_special_chars = text_to_remove_special_chars.replace(special_char, '')
        return text_to_remove_special_chars

    def __remove_noise(self):
        if len(self.__characters) > 0:
            print(self.__characters)
            self.result = self.__remove_special_chars(self.__characters)
            print(self.result)
