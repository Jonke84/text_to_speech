
# -*- encoding: utf-8 -*-
from gtts import gTTS
from pydub import AudioSegment




article = [
    """  Prebytok ľahkého kovu a problémy na trhu s elektromobilmi dlhodobo ťahali cenu lítia nadol

Na pozadí meniaceho sa trhu elektromobilov zažíva trh s lítiom rovnako zásadné zmeny. Po dlhom páde pre prebytok ľahkého kovu a problémy na trhu s elektromobilmi totiž zaznamenáva vývoj jeho cien obrat a mierne rastie. A to aj napriek predpovediam analytikov, ktorí očakávajú jeho pokles aj v aktuálnom roku.

Nie je však jedinou komoditou, ktorej súčasný vývoj praje. Pribúdajú totiž očakávania, že čínska ekonomika bude naďalej podporovaná vládnymi stimulmi a že globálna ekonomika sa nespomalí. V dôsledku toho vzrástli aj ceny medi od konca októbra 2023 o viac ako štrnásť percent a len minulý týždeň o viac ako päť percent.""",
    """ Investori sa vracajú
Po mesiacoch neustáleho znižovania produkcie baní, ako sú Anglo American, Rio Tinto, Vale a Teck, a po odstavení bane Cobre Panama, najväčšej na svete, sa trh medi dostal z prebytku do deficitu, čo pochopiteľne zvyšuje cenu komodity.

Tento pokles produkcie je pripisovaný tlmeniu čínskeho dopytu aj neuspokojivým predajom na americkom trhu s elektromobilmi.

To má priamy vplyv aj na ostatné suroviny, ktoré sú s elektromobilitou užšie prepojené. Je ňou aj lítium, ktoré sa primárne využíva pre lítium-iónové batérie v elektrických vozidlách.

Tento trh bol v poklese ceny od konca roku 2022, keď Elon Musk vyhlásil, že ceny lítia sú neudržateľné, a spojil sa s čínskym CATL, najväčším výrobcom batérií na svete, s cieľom znížiť ceny lítia.

Podľa Petra Garnryho, akciového stratéga Saxo Bank, sa však od začiatku roka ceny uhličitanu lítneho v Číne zvýšili, čo odráža zdravšiu situáciu v oblasti ponuky a dopytu. Očakáva sa teda, že elektromobily budú aj v nadchádzajúcom desaťročí rásť tempom 25 percent ročne, čo znamená, že trh s lítiom sa bude naďalej rozširovať.

Investícia do komodity je alternatívnym spôsobom, ako zarobiť na trende elektromobility bez nutnosti nakupovať akcie konkrétnych firiem ako Tesla, BYD či Volkswagen, konštatuje analytik Saxo Bank.

Aj preto z pohľadu finančných trhov môžu byť investície do týchto komoditných portfólií v ďalšom období ziskové, hoci si naďalej udržujú rizikovejší charakter.

Trh s lítiom v Číne preto aj pod vplyvom rastúceho dopytu investorov v ostatných týždňoch naďalej rozširoval svoju veľkosť, čo do počtu investorov a dopytu.

Cena najobchodovanejšieho kontraktu na uhličitan lítny na burze Guangzhou Futures Exchange (GFEX) dosiahla zatiaľ najvyššiu tohtoročnú hodnotu bezmála 120-tisíc jüanov za tonu. V porovnaní s novembrom 2022 je to len pätina. """,
    """ Nové alternatívy
Lítium má za posledný rok za sebou divokú jazdu. Spomalenie predaja elektromobilov v polovici roku 2023, najmä v Číne, Európe a Spojených štátoch, prispelo v danom čase k prebytku tohto kovu a následnému strmému poklesu jeho cien.

Celosvetový predaj úplne elektrických a plug-in hybridných vozidiel vzrástol len o 31 percent v roku 2023, čo je výrazný pokles oproti 60-percentnému rastu v roku 2022.

Spoločnosť UBS predpovedá, že lítia je dnes toľko, že jeho ďalší deficit sa očakáva najskôr v roku 2028, čo je výrazný rozdiel oproti špekuláciám z novembra 2022, keď rast ceny poháňala panika a filozofia prvý berie. V niečom vývoj cien pod jej vplyvom pripomínal až takmer povestnú tulipánovú mániu.

Navyše celosvetový nárast ťažby lítia ešte viac prispieva k jeho prebytku, pričom Austrália, Čína a Čile sú dnes krajinami, ktoré určujú túto cestu.

Na strane automotivu bude kľúčové, ako sa dodávatelia a výrobcovia rozhodnú túto výhodu, pred opätovným i miernym rastom cien, zužitkovať. Či sa o lacnejšie ceny vstupov do elektrických áut, kde cena batérie údajne tvorí 80 percent ceny vozidla, podelia s kupujúcimi alebo sa budú chcieť s rovnakými pravidlami hrať na zamrznutom trhu s elektromobilmi.

Medzičasom sa svet obzerá už aj po iných alternatívach. Pozornosť púta sodík. Výrobcovia batérií a áut totiž naznačujú, že sodík by mohol byť alternatívou k doteraz preferovanej lítium-iónovej technológii pre batérie budúcich elektromobilov.

Alkalický kov je podľa nich dokonca vhodnejšou náhradou s nižšími nákladmi na spracovanie, lepšou dostupnosťou a menšou horľavosťou, zato s dostatočným výkonom aj pri nízkych teplotách.

K novej alternatíve sa preto obracajú už aj najväčšie firmy z batériového biznisu a svoj diel záujmu prikladajú aj samotné automobilky. Veľkú váhu takzvaným sodík-iónovým batériám prikladá istý čas už aj najväčší svetový výrobca – čínsky gigant Contemporary Amperex Technology Ltd. (CATL). """,
    """ Rastúci trh
Batérie na báze iónov sodíka nie sú úplnou novinkou a testujú sa už niekoľko desaťročí, hoci až teraz existuje možnosť ich použitia prvýkrát v masovej výrobe pre elektromobily.

Po úvodných plánoch menších firiem, ako je napríklad Altris zo Švédska či americká firma Natron, sa tejto technológie chytajú Číňania. Gigant CATL sa chce s týmito batériami dokonca postaviť na čelo dodávateľského reťazca.

Napriek dnešným vyšším cenám sodíka je jeho použitie v batériách oveľa lacnejšie než v prípade lítia. Primárne to vychádza z toho, že sodík je v porovnaní s lítiom omnoho dostupnejší. Zem ho obsahuje obrovské množstvo.

Podľa prieskumu Allied Market Research bola veľkosť globálneho trhu sodík-iónových batérií v roku 2021 približne 0,3 miliardy dolárov. Predpokladá sa však, že trh s týmito batériami dosiahne do roku 2031 veľkosť niekoľkých miliárd dolárov.

Navyše sodíkové batérie majú lepšie kapacity pre rýchle nabíjanie. CATL uvádza, že pri izbovej teplote by sa na 80 percent mali nabiť za štvrťhodinu. A znesú aj niekoľkonásobne viac dobíjacích cyklov než lítium-iónové batérie. Veľkým plusom tejto technológie je teda dlhá životnosť a nižšia environmentálna záťaž.

Okrem toho sú batérie bezpečné, tepelne stabilné a dobre fungujú aj počas mrazov. Najväčším nedostatkom v porovnaní s modernými lítiovými článkami je ich menšia energetická hustota, preto sú sodíkové batérie nateraz rozmernejšie a tým ťažšie. """,
]

i = 1
for item in article:
    tts1 = gTTS(text=item, lang='sk')
    tts1.save(f"sound{i}.mp3")
    i = i + 1


#
# audio1 = AudioSegment.from_mp3("sound1.mp3")
# audio2 = AudioSegment.from_mp3("sound2.mp3")
# audio3 = AudioSegment.from_mp3("sound3.mp3")
# audio4 = AudioSegment.from_mp3("sound4.mp3")
# audio5 = AudioSegment.from_mp3("sound5.mp3")
# pauza = AudioSegment.from_mp3("pauza.mp3")
# koniec = AudioSegment.from_mp3("koniec.mp3")
#
#
# combine_audio = (
#         audio1 +
#         pauza +
#         audio2 +
#         pauza +
#         audio3 +
#         koniec
# )
#
# combine_audio.export("output.mp3", format="mp3")
# Export the combined audio to a new MP3 file

# tts2 = gTTS(text=text2)

