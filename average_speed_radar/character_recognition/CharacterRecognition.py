import pytesseract
import cv2


class CharacterRecognition:
    img_in = None
    enchanted_image = None
    result = "Desconhecido"

    __characters = None
    __special_chars_to_remove = "!@#%¨&*()_+:;><^^}{`?|~¬\/=,.'ºª»‘"

    def recognition(self, img_in):
        self.img_in = img_in
        self.__enchant_characters_in_the_image()
        self.__characters = self.__image_to_string()
        self.__remove_noise()

        return self.result

    def __enchant_characters_in_the_image(self):
        y, cr, cb = cv2.split(cv2.cvtColor(self.img_in, cv2.COLOR_RGB2YCrCb))
        y = cv2.equalizeHist(y)
        self.enchanted_image = cv2.cvtColor(cv2.merge([y, cr, cb]), cv2.COLOR_YCrCb2RGB)

    def __image_to_string(self):
        return pytesseract.image_to_string(self.img_in, lang='eng')

    def __remove_special_chars(self, text_to_remove_special_chars):
        for special_char in self.__special_chars_to_remove:
            text_to_remove_special_chars = text_to_remove_special_chars.replace(special_char, '')
        return text_to_remove_special_chars

    def __remove_noise(self):
        if len(self.__characters) > 0:
            self.result = self.__remove_special_chars(self.__characters)
