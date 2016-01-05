
# Aineistotehtävä: Puupankin sisällöstä raportointi. Tehtävä olisi lukea oheen linkitetty FTB2-tiedosto
# Python-ohjelmalla ja laskea ja raportoida esimerkiksi virkkeiden määrät ja pituuksien minimi, maksimi, keskiarvo;
# sanemäärä, eri sanojen määrä; sanaluokkien taajuusjakauma.


# the variable needed for opening and reading the file
teksti = '/Users/jultsi/Desktop/Kieliteknologia/Ohjelmointi 1/ftb2x.txt'


class Kasittelija:
    def __init__(self, tiedosto):               # the demanded function for every class
        self.__tiedosto = tiedosto
        self.__sisalto = self.__lue_sisalto()

    def __lue_sisalto(self):                    # reads the file into a variable, and then closes it
        source = open(self.__tiedosto, 'rt', encoding='UTF-8')
        sisalto = source.read()
        source.close()
        return sisalto                          # returns the content of the file

    def virke_maara(self):                      # returns the amount of sentences

        lines = self.__sisalto.split("\n")      # separates the file into lines by "\n"
        virkkeet = 0                            # an empty variable to count the sentences
        for line in lines:
            if line.startswith("1\t"):          # if the line starts with "1" and a tab
                virkkeet += 1
        return virkkeet

    def hae_data(self):                         # returns the number of words in every sentence

        lines = self.__sisalto.split("\n")
        numerolista = []                        # an empty list to count the words of the sentences
        count = 0                               # an empty variable to count the words
        none_found = False

        for char in lines:
            if "#None" in char:                 # if there's "#None" in the line, none_found is true and continue
                none_found = True
                continue
            elif none_found and char != "":     # if none_found is true and there's not an empty line, add 1 to count
                count += 1
            elif char == "" and none_found:     # if none_found is true and there's an empty line, add count to the list
                numerolista.append(count)       # and start the listing from the beginning
                count = 0
                none_found = False
        return numerolista

    def virke_maksimi(self):                    # returns the maximum number of words in a sentence
        return max(self.hae_data())

    def virke_minimi(self):                     # returns the minimum number of words in a sentence
        return min(self.hae_data())

    def keskiarvo(self):                        # returns the average number of words in a sentence
        data = self.hae_data()
        return sum(data) / len(data)

    def sane_maara(self):                       # returns the number of words in the whole file
        lines = self.__sisalto.split("\n")

        yksittaiset_saneet = []                 # an empty list for the words

        for word in lines:
            saneet = word.split("\t")           # separates the lines by tab
            if len(saneet) > 1:                 # if the word is not an empty line
                sane = saneet[1]                # the 2nd word in line, a.k.a. the word
                yksittaiset_saneet.append(sane) # adds the words into the list
                if "." in sane:                 # these remove punctuation and backslash from the words
                    yksittaiset_saneet.remove(sane)
                elif "," in sane:
                    yksittaiset_saneet.remove(sane)
                elif ":" in sane:
                    yksittaiset_saneet.remove(sane)
                elif "\"" in sane:
                    yksittaiset_saneet.remove(sane)
        return len(yksittaiset_saneet)

    def erilaiset_saneet(self):                 # returns the number of different words
        lines = self.__sisalto.split("\n")

        eri_saneet = {}                         # an empty dictionary for every different word and the amount of it

        for word in lines:
            saneet = word.split("\t")           # separates the lines by tab
            if len(saneet) > 1:                 # if the line is not an empty line
                sana = saneet[3]                # the 4th word in line, a.k.a. the word in its basic form
                if sana in eri_saneet:          # if the word is already in the dictionary, add one count to it
                    eri_saneet[sana] += 1
                else:
                    eri_saneet[sana] = 1        # if it's not, add it there with one count
            if "." in eri_saneet:               # these remove punctuation and backslashes from the words
                del eri_saneet[sana]
            if "," in eri_saneet:
                del eri_saneet[sana]
            if ":" in eri_saneet:
                del eri_saneet[sana]
            if "\"" in eri_saneet:
                del eri_saneet[sana]
        return len(eri_saneet)

    def sanaluokkien_taajuus(self):             # returns the frequencies of word classes
        lines = self.__sisalto.split("\n")

        sanaluokat = {}                         # an empty dictionary for the word classes

        for word in lines:
            saneet = word.split("\t")           # separates the lines by tab
            if len(saneet) > 1:                 # if the line is not empty
                sanaluokka = saneet[4]          # the 5th word in the line, a.k.a. the word class
                if sanaluokka in sanaluokat:    # if the word class is already in the dictionary,
                    sanaluokat[sanaluokka] += 1 # add the word in it with one count
                else:
                    sanaluokat[sanaluokka] = 1  # if not, add it to the dictionary with one count
        return sanaluokat


ftb2x = Kasittelija(teksti)                     # a variable to call the file via the class Kasittelija
print("Tietoja ftb2x.txt-tiedostosta:", "\n")
print("Virkkeiden kokonaismäärä:", ftb2x.virke_maara())
print("Virkkeen maksimipituus:", ftb2x.virke_maksimi())
print("Virkkeen minimipituus:", ftb2x.virke_minimi())
print("Kokonaissanemäärä:", ftb2x.sane_maara())
print("Erilaisten sanojen määrä:", ftb2x.erilaiset_saneet())
print("Sanaluokkien taajuus sanaluokittain:", ftb2x.sanaluokkien_taajuus())
