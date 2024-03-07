import random

class Pendu():
    def __init__(self) -> None:
        self._words = ['gagne', 'raptor', 'bouteille', 'ville', 'femme', 'Pays', 'balle', 'cuire', 'football']
        self._hidden_word = ''
        self._user_input = ''
        self._word_under_construction = ''
        self.collect_user_input = []

    def choose_word(self):
        self._hidden_word = random.choice(self._words)

    def get_user_input(self):
        self._user_input = input('Choisissez une lettre (S pour saisir le mot) - > ')
        if self._user_input.lower() == 's':
            self.saisir_mot()
        else:
            self.collect_user_input.append(self._user_input.lower())

    def _print_under_construction_word(self):
        self._word_under_construction = ''
        for l in self._hidden_word:
            if l in self.collect_user_input:
                self._word_under_construction += l
            else:
                self._word_under_construction += '_'
        print(self._word_under_construction)

    def validate_word(self):
        if self._user_input not in self._hidden_word:
            print('Mot non trouvé. Un dessin fait en chaine de caractère.')
        elif self._user_input in self.collect_user_input:
            print(f'Lettre déjà saisie : {", ".join(self.collect_user_input)}')
        else:
            self._print_under_construction_word()

    def saisir_mot(self):
        mot_saisi = input('Saisissez le mot - > ')
        if mot_saisi.lower() == self._hidden_word.lower():
            print(f'Félicitations, vous avez trouvé le mot caché : {self._hidden_word}')
            exit()
        else:
            print('Mot incorrect. Pénalité appliquée.')

    def main(self):
        self.choose_word()
        i = 0
        while i < 10:
            print(f'\nEssai {i + 1}')
            self.get_user_input()
            self.validate_word()

            if self._hidden_word.lower() == self._word_under_construction.lower():
                print(f'Félicitations, vous avez trouvé le mot caché : {self._hidden_word}')
                break

            i += 1

        print('\nVous avez épuisé vos possibilités.')
        print(f'Le mot caché était : {self._hidden_word}')


if __name__ == '__main__':
    pendu = Pendu()
    pendu.main()
