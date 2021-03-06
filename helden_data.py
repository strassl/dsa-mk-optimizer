from enum import Enum

seq = 0

def auto():
    global seq
    seq += 1
    return seq

class SpellTrait(Enum):
    ANTI = auto()
    BESCHW = auto()
    DAEMON = auto()
    DAEMON_AGR = auto()
    DAEMON_AMZ = auto()
    DAEMON_ASF = auto()
    DAEMON_BLH = auto()
    DAEMON_BLK = auto()
    DAEMON_LGM = auto()
    DAEMON_BLZ = auto()
    DAEMON_TGT = auto()
    EIGN = auto()
    EINFL = auto()
    ELE = auto()
    ELE_EIS = auto()
    ELE_ERZ = auto()
    ELE_FEUER = auto()
    ELE_HUMUS = auto()
    ELE_LUFT = auto()
    ELE_WASSER = auto()
    FORM = auto()
    GEIST = auto()
    HEIL = auto()
    HELL = auto()
    HERB = auto()
    HERR = auto()
    ILLU = auto()
    KRAFT = auto()
    LIMBUS = auto()
    META = auto()
    OBJEKT = auto()
    SCHADEN = auto()
    TELE = auto()
    TEMP = auto()
    UMWELT = auto()
    VERST = auto()



spell_to_traits = {
    'Abvenenum reine Speise': 'ob',
    'Accuratum Zaubernadel': 'ob',
    'Adamantium Erzstruktur': 'erob',
    'Adlerauge Luchsenohr': 'eihl',
    'Adlerschwinge Wolfsgestalt': 'fo',
    'Aeolitus Windgebraus': 'euum',
    'Aerofugo Vakuum': 'euum',
    'Aerogelo Atemqual': 'euum',
    'Alpgestalt': 'eshr',
    'Analys Arkanstruktur': 'hlme',
    'Ängste lindern': 'es',
    'Animatio stummer Diener': 'te',
    'Applicatus Zauberspeicher': 'meob',
    'Aquafaxius Wasserstrahl': 'ewsc',
    'Aquasphaero Wasserball': 'ewscte',
    'Arachnea Krabbeltier': 'hb',
    'Arcanovi Artefakt': 'meob',
    'Archofaxius Erzstrahl': 'ersc',
    'Archosphaero Erzball': 'erscte',
    'Armatrutz': 'eier',
    'Atemnot': 'ei',
    'Attributo': 'ei',
    'Aufgeblasen Abgehoben': 'eufo',
    'Auge des Limbus': 'krli',
    'Aureolus Güldenglanz': 'il',
    'Auris Nasus Oculus': 'il',
    'Axxeleratus Blitzgeschwind': 'ei',
    'Balsam Salabunde': 'fohe',
    'Band und Fessel': 'es',
    'Bannbaladin': 'es',
    'Bärenruhe Winterschlaf': 'fo',
    'Beherrschung brechen': 'anhr',
    'Beschwörung vereiteln': 'anbe',
    'Bewegung stören': 'ante',
    'Blendwerk': 'il',
    'Blick aufs Wesen': 'hl',
    'Blick durch fremde Augen': 'hlve',
    'Blick in die Gedanken': 'hl',
    'Blick in die Vergangenheit': 'hltp',
    'Blitz dich find': 'es',
    'Böser Blick': 'es',
    'Brenne toter Stoff!': 'efob',
    'Caldofrigo heiß und kalt': 'efeeobum',
    'Chamaelioni Mimikry': 'il',
    'Chimaeroform Hybridgestalt': 'dsfo',
    'Chronoklassis Urfossil': 'hbtp',
    'Chrononautos Zeitenfahrt': 'tp',
    'Claudibus Clavistibor': 'ob',
    'Corpofesso Gliederschmerz': 'ei',
    'Corpofrigo Kälteschock': 'eiee',
    'Cryptographo Zauberschrift': 'obve',
    'Custodosigil Diebesbann': 'efmeob',
    'Dämonenbann': 'anda',
    'Delicioso Gaumenschmaus': 'il',
    'Desintegratus Pulverstaub': 'obsc',
    'Destructibo Arcanitas': 'ankrme',
    'Dichter und Denker': 'hr',
    'Dschinnenruf': 'elhb',
    'Dunkelheit': 'um',
    'Duplicatus Doppelbild': 'il',
    'Ecliptifactus Schattenkraft': 'dafo',
    'Eigenschaft wiederherstellen': 'anei',
    'Eigne Ängste quälen dich!': 'eies',
    'Einfluss bannen': 'anes',
    'Eins mit der Natur': 'eiel',
    'Eisenrost und Patina': 'obtp',
    'Eiseskälte Kämpferherz': 'ei',
    'Elementarbann': 'anel',
    'Elementarer Diener': 'elhb',
    'Elfenstimme Flötenton': 've',
    'Erinnerung verlasse dich!': 'hr',
    'Exposami Lebenskraft': 'hl',
    'Falkenauge Meisterschuss': 'ei',
    'Favilludo Funkentanz': 'il',
    'Feuerlauf': 'eief',
    'Firnlauf': 'eiee',
    'Flim Flam Funkel': 'um',
    'Fluch der Pestilenz': 'db',
    'Foramen Foraminor': 'hlte',
    'Fortifex arkane Wand': 'erum',
    'Frigifaxius Eisstrahl': 'eesc',
    'Frigisphaero Eisball': 'eescte',
    'Fulminictus Donnerkeil': 'krsc',
    'Gardianum Zauberschild': 'ankrme',
    'Gedankenbilder Elfenruf': 've',
    'Gefäß der Jahre': 'fotp',
    'Gefunden!': 'hl',
    'Geisterbann': 'ange',
    'Geisterruf': 'gehb',
    'Gletscherwand': 'ee',
    'Granit und Marmor': 'erfo',
    'Große Gier': 'eshr',
    'Große Verwirrung': 'ei',
    'Halluzination': 'hr',
    'Harmlose Gestalt': 'esil',
    'Hartes schmelze!': 'ewob',
    'Haselbusch und Ginsterkraut': 'eiehfo',
    'Heilkraft bannen': 'anhe',
    'Hellsicht trüben': 'anhl',
    'Herbeirufung vereiteln': 'anhb',
    'Herr über das Tierreich': 'hr',
    'Herzschlag ruhe!': 'dleies',
    'Hexenblick': 've',
    'Hexengalle': 'sc',
    'Hexenholz': 'te',
    'Hexenknoten': 'esil',
    'Hexenkrallen': 'eifo',
    'Hexenspeichel': 'he',
    'Hilfreiche Tatze, rettende Schwinge': 'esve',
    'Höllenpein zerreiße dich!': 'es',
    'Holterdipolter': 'um',
    'Horriphobus Schreckgestalt': 'es',
    'Humofaxius Humusstrahl': 'ehsc',
    'Humosphaero Humusball': 'ehscte',
    'Ignifaxius Flammenstrahl': 'efsc',
    'Ignisphaero Feuerball': 'efscte',
    'Ignorantia Ungesehn': 'esil',
    'Illusion auflösen': 'anil',
    'Immortalis Lebenszeit': 'fotp',
    'Imperavi Handlungszwang': 'hr',
    'Impersona Maskenbild': 'il',
    'Infinitum Immerdar': 'metp',
    'Invercano Spiegeltrick': 'ankrme',
    'Invocatio maior': 'beda',
    'Invocatio minor': 'beda',
    'Iribaars Hand': 'dmessc',
    'Juckreiz, dämlicher!': 'es',
    'Karnifilio Raserei': 'eies',
    'Katzenaugen': 'ei',
    'Klarum Purum': 'fohe',
    'Klickeradomms': 'te',
    'Koboldgeschenk': 'hr',
    'Koboldovision': 'hlli',
    'Komm Kobold Komm': 'hb',
    'Körperlose Reise': 'live',
    'Krabbelnder Schrecken': 'dbhb',
    'Kraft des Erzes': 'erob',
    'Krähenruf': 'eshbli',
    'Krötensprung': 'ei',
    'Kulminatio Kugelblitz': 'sc',
    'Kusch!': 'es',
    'Lach dich gesund': 'eshe',
    'Lachkrampf': 'es',
    'Langer Lulatsch': 'foob',
    'Last des Alters': 'fotp',
    'Leib der Erde': 'ehfo',
    'Leib der Wogen': 'ewfo',
    'Leib des Eises': 'eefo',
    'Leib des Erzes': 'erfo',
    'Leib des Feuers': 'effo',
    'Leib des Windes': 'eufo',
    'Leidensbund': 'heve',
    'Levthans Feuer': 'esve',
    'Limbus versiegeln': 'anli',
    'Lockruf und Feenfüße': 'ilte',
    'Lunge des Leviatan': 'he',
    'Madas Spiegel': 'hlve',
    'Magischer Raub': 'krve',
    'Mahlstrom': 'ewum',
    'Manifesto Element': 'el',
    'Meister der Elemente': 'elhb',
    'Meister minderer Geister': 'hb',
    'Memorabia Falsifir': 'hr',
    'Memorans Gedächtniskraft': 'eihl',
    'Menetekel Flammenschrift': 'il',
    'Metamagie neutralisieren': 'anme',
    'Metamorpho Gletscherform': 'eeob',
    'Metamorpho Felsenform': 'erob',
    'Motoricus': 'te',
    'Movimento Dauerlauf': 'ei',
    'Murks und Patz': 'es',
    'Nackedei': 'obte',
    'Nebelleib': 'euewfo',
    'Nebelwand und Morgendunst': 'euewum',
    'Nekropathia Seelenreise': 'geve',
    'Nihilogravo Schwerelos': 'um',
    'Nuntiovolo Botenvogel': 'bedo',
    'Objecto Obscuro': 'ob',
    'Objectofixo': 'obtp',
    'Objectovoco': 've',
    'Objekt entzaubern': 'anob',
    'Oculus Astralis': 'hlkrmeli',
    'Odem Arcanum': 'hlkr',
    'Orcanofaxius Luftstrahl': 'eusc',
    'Orcanosphaero Orkanball': 'euscte',
    'Pandaemonium': 'beda',
    'Panik überkomme euch!': 'dmes',
    'Papperlapapp': 'es',
    'Paralysis starr wie Stein': 'erfo',
    'Pectetondo Zauberhaar': 'fo',
    'Penetrizzel Tiefenblick': 'hl',
    'Pentagramma Sphärenbann': 'anbedage',
    'Pestilenz erspüren': 'hl',
    'Pfeil des Feuers': 'efob',
    'Pfeil des Wassers': 'ewob',
    'Pfeil des Erzes': 'erob',
    'Pfeil der Luft': 'euob',
    'Pfeil des Humus': 'ehob',
    'Pfeil des Eises': 'eeob',
    'Planastrale Anderswelt': 'li',
    'Plumbumbarum schwerer Arm': 'es',
    'Projektimago Ebenbild': 'ilve',
    'Protectionis Kontrabann': 'ankrme',
    'Psychostabilis': 'anei',
    'Radau': 'eute',
    'Reflectimago Spiegelschein': 'il',
    'Reptilea Natternest': 'hb',
    'Respondami': 'hr',
    'Reversalis Revidum': 'me',
    'Ruhe Körper, ruhe Geist': 'he',
    'Salander Mutander': 'fo',
    'Sanftmut': 'es',
    'Sapefacta Zauberschwamm': 'euewte',
    'Satuarias Herrlichkeit': 'eiil',
    'Schabernack': 'es',
    'Schadenszauber bannen': 'ansc',
    'Schelmenkleister': 'um',
    'Schelmenlaune': 'es',
    'Schelmenmaske': 'il',
    'Schelmenrausch': 'es',
    'Schleier der Unwissenheit': 'eime',
    'Schwarz und Rot': 'eisc',
    'Schwarzer Schrecken': 'es',
    'Seelentier erkennen': 'hl',
    'Seelenwanderung': 'eive',
    'Seidenweich Schuppengleich': 'il',
    'Seidenzunge Elfenwort': 'es',
    'Sensattacco Meisterstreich': 'eihl',
    'Sensibar Empathicus': 'hl',
    'Serpentialis Schlangenleib': 'fo',
    'Silentium': 'um',
    'Sinesigil unerkannt': 'il',
    'Skelettarius': 'dt',
    'Solidirid Weg aus Licht': 'euum',
    'Somnigravis tiefer Schlaf': 'es',
    'Spinnenlauf': 'ei',
    'Spurlos Trittlos': 'um',
    'Standfest Katzengleich': 'ei',
    'Staub wandle!': 'er',
    'Stein wandle!': 'beda',
    'Stillstand': 'eeum',
    'Sumus Elixiere': 'eh',
    'Tauschrausch': 'li',
    'Tempus Stasis': 'tp',
    'Tiere besprechen': 'fohe',
    'Tiergedanken': 'hlve',
    'Tlalucs Odem Pestgestank': 'bedasc',
    'Totes handle!': 'bedt',
    'Transformatio Formgestalt': 'ob',
    'Transmutare Körperform': 'fo',
    'Transversalis Teleport': 'li',
    'Traumgestalt': 've',
    'Unberührt von Satinav': 'obtp',
    'Unitatio Geistesbund': 'krve',
    'Unsichtbarer Jäger': 'il',
    'Veränderung aufheben': 'anum',
    'Verschwindibus': 'li',
    'Verständigung stören': 'anve',
    'Verwandlung beenden': 'anfo',
    'Vipernblick': 'es',
    'Visibili Vanitar': 'fo',
    'Vocolimbo hohler Klang': 'il',
    'Vogelzwitschern Glockenspiel': 'il',
    'Wand aus Dornen': 'eh',
    'Wand aus Erz': 'er',
    'Wand aus Flammen': 'ef',
    'Orkanwand': 'eu',
    'Wand aus Wogen': 'ew',
    'Warmes Blut': 'eiefhl',
    'Wasseratem': 'fo',
    'Weiches erstarre!': 'erum',
    'Weihrauchwolke Wohlgeruch': 'il',
    'Weisheit der Bäume': 'ehfo',
    'Weiße Mähn und goldener Huf': 'be',
    'Wellenlauf': 'eiew',
    'Wettermeisterschaft': 'euum',
    'Widerwille Ungemach': 'esil',
    'Windhose': 'euum',
    'Windstille': 'euum',
    'Wipfellauf': 'eieh',
    'Xenographus Schriftenkunde': 'hl',
    'Zagibu Ubigaz': 'erob',
    'Zappenduster': 'anum',
    'Zauberklinge Geisterspeer': 'krob',
    'Zaubernahrung Hungerbann': 'eies',
    'Zauberwesen der Natur': 'hbve',
    'Zauberzwang': 'hrsc',
    'Zorn der Elemente': 'elsc',
    'Zunge lähmen': 'ei',
    'Zwingtanz': 'hr',
    'Niederhöllen Eisgestalt': 'eefo',
    'Seelenfeuer Lichterloh': 'effo',
    'Eiswirbel': 'eeum',
    'Sumpfstrudel': 'ehum',
    'Malmkreis': 'erum',
    'Feuersturm': 'efum',
    'Agrimothbann': 'andg',
    'Belzhorashbann': 'andb',
    'Bienenschwarm': 'fo',
    'Entfesselung des Getiers': 'fo',
    'Gebieter der Tiefe': 'fo',
    'Geschoss der Niederhöllen': 'dasc',
    'Grolmenseele': 'begete',
    'Hauch der Tiefen Tochter': 'efes',
    'Hexagramma Dschinnenbann': 'anbeel',
    'Hornissenruf': 'eshbli',
    'Igniflumen Flammenspur': 'efsc',
    'Igniplano Flächenbrand': 'efscum',
    'Igniqueris Feuerkragen': 'efes',
    'Leib aus tausend Fliegen': 'fo',
    'Seelenfeuer Lichterloh (DDZ)': 'effo',
    'Schlangenruf': 'eshbli',
    'Sphaerovisio Schreckensbild': 'dalive',
    'Spinnennetz': 'ei',
    'Spinnenruf': 'eshbli',
    'Tanz der Erlösung': 'aneshr',
    'Thargunitothhbann': 'andt',
    'Tierruf': 'eshbli',
    'Unsichtbare Glut': 'ob',
    'Valetudo Lebenskraft': 'krhe',
    'Weisheit der Steine': 'erfo',
    'Glacoflumen Fluss aus Eis': 'eeum',
    'Aquaqueris Wasserfluch': 'ewsc',
    'Aeropulvis sanfter Fall': 'eute',
    'Fesselranken': 'ehum',
    'Feuermähne Flammenhuf': 'hbef',
    'Ignifugo Feuerbann': 'efum',
    'Ignimorpho Feuerform': 'efob',
    'Kraft des Humus': 'ehhe',
    'Kraft des Eises': 'ehee',
    'Kraft der Luft': 'eheu',
    'Stimmen des Windes': 'foeu',
    'Eiskaltes Strategem': 'foee',
    'Warmes Gefriere': 'obee',
    'Festes Verwehe': 'obeu',
    'Windgeflüster': 'veeu',
    'Dornenkrallen': 'eifoeh',
    'Adamantium Erzstruktur (Agm)': 'dgob',
    'Aeolitus Windgebraus (Agm)': 'dgum',
    'Aerofugo Vakuum (Agm)': 'dgum',
    'Aerogelo Atemqual (Agm)': 'dgum',
    'Armatrutz (Agm)': 'eidg',
    'Brenne toter Stoff! (Agm)': 'dgob',
    'Caldofrigo heiß und kalt (Agm)': 'dgobum',
    'Fortifex arkane Wand (Agm)': 'dgum',
    'Granit und Marmor (Agm)': 'dgfo',
    'Humofaxius Humusstrahl (Agm)': 'dgsc',
    'Ignisphaero Feuerball (Agm)': 'dgscte',
    'Ignifaxius Flammenstrahl (Agm)': 'dgsc',
    'Kraft des Erzes (Agm)': 'dgob',
    'Leib des Feuers (Agm)': 'dgfo',
    'Orcanofaxius Luftstrahl (Agm)': 'dgsc',
    'Sumus Elixiere (Agm)': 'dg',
    'Wand aus Dornen (Agm)': 'dg',
    'Wand aus Erz (Agm)': 'dg',
    'Weiches erstarre! (Agm)': 'dgum',
    'Windhose (Agm)': 'dgum',
    'Umbraporta Schattentüre': 'dali',
    'Tenebaro Schattentanz': 'il',
    'Pantenebrum': 'beda',
    'Schattenodem': 'bedasc',
    'Nuntiovolo Botenvogel (obsk.)': 'beda',
    'Opacitas Schattenleib': 'da',
    'Ecliptifactus Schattenkraft (obsk.)': 'dafo'
}

trait_str_short_to_trait = {
    'an': SpellTrait.ANTI,
    'be': SpellTrait.BESCHW,
    'da': SpellTrait.DAEMON,
    'dg': SpellTrait.DAEMON_AGR,
    'dm': SpellTrait.DAEMON_AMZ,
    'ds': SpellTrait.DAEMON_ASF,
    # 'dh': SpellTrait.DAEMON_BLH, # TODO
    'bl': SpellTrait.DAEMON_BLK,
    'do': SpellTrait.DAEMON_LGM,
    'db': SpellTrait.DAEMON_BLZ,
    'dt': SpellTrait.DAEMON_TGT,
    'ei': SpellTrait.EIGN,
    'es': SpellTrait.EINFL,
    'el': SpellTrait.ELE,
    'ee': SpellTrait.ELE_EIS,
    'er': SpellTrait.ELE_ERZ,
    'ef': SpellTrait.ELE_FEUER,
    'eh': SpellTrait.ELE_HUMUS,
    'eu': SpellTrait.ELE_LUFT,
    'ew': SpellTrait.ELE_WASSER,
    'fo': SpellTrait.FORM,
    'ge': SpellTrait.GEIST,
    'he': SpellTrait.HEIL,
    'hl': SpellTrait.HELL,
    'hb': SpellTrait.HERB,
    'hr': SpellTrait.HERR,
    'il': SpellTrait.ILLU,
    'kr': SpellTrait.KRAFT,
    'li': SpellTrait.LIMBUS,
    'me': SpellTrait.META,
    'ob': SpellTrait.OBJEKT,
    'sc': SpellTrait.SCHADEN,
    'te': SpellTrait.TELE,
    'tp': SpellTrait.TEMP,
    'um': SpellTrait.UMWELT,
    've': SpellTrait.VERST,
}

def get_traits(spell):
    return parse_trait_str(spell_to_traits[spell])

def parse_trait_str(s):
    str_parts = [s[i:i+2] for i in range(0, len(s), 2)]
    traits = []
    for part in str_parts:
        traits.append(trait_str_short_to_trait[part])
    return traits

class SkillGroup(Enum):
    KAMPF = auto()
    SPRACHEN = auto()
    SCHRIFTEN = auto()

    KOERPER = auto()
    GESELLSCHAFT = auto()
    NATUR = auto()
    WISSEN = auto()
    HANDWERK = auto()
    GABEN = auto()
    RITUALKENNTIS = auto()
    LITURGIEKENNTNIS = auto()
    RITUALFERTIGKEIT = auto()
    SCHWARZE_GABE = auto()

skill_group_str_to_group = {
  'Kampf': SkillGroup.KAMPF,
  'Körperlich': SkillGroup.KOERPER,
  'Gesellschaft': SkillGroup.GESELLSCHAFT,
  'Natur': SkillGroup.NATUR,
  'Wissen': SkillGroup.WISSEN,
  'Sprachen': SkillGroup.SPRACHEN,
  'Schriften': SkillGroup.SCHRIFTEN,
  'Handwerk': SkillGroup.HANDWERK,
  'Gaben': SkillGroup.GABEN,
  'Ritualkenntnis': SkillGroup.RITUALKENNTIS,
  'Liturgiekenntnis': SkillGroup.LITURGIEKENNTNIS,
  'Ritualfertigkeit': SkillGroup.RITUALFERTIGKEIT,
  'Schwarze Gabe': SkillGroup.SCHWARZE_GABE,
}

skill_group_to_skills = {
    SkillGroup.KOERPER: [
        'Akrobatik',
        'Athletik',
        'Fliegen',
        'Gaukeleien',
        'Klettern',
        'Körperbeherrschung',
        'Reiten',
        'Schleichen',
        'Schwimmen',
        'Selbstbeherrschung',
        'Sich verstecken',
        'Singen',
        'Sinnenschärfe',
        'Skifahren',
        'Stimmen imitieren',
        'Tanzen',
        'Taschendiebstahl',
        'Zechen',
        'Freies Fliegen',
    ],

    SkillGroup.GESELLSCHAFT: [
        'Betören',
        'Etikette',
        'Galanterie',
        'Gassenwissen',
        'Lehren',
        'Menschenkenntnis',
        'Schauspielerei',
        'Schriftlicher Ausdruck',
        'Sich verkleiden',
        'Überreden',
        'Überzeugen',
    ],

    SkillGroup.NATUR: [
        'Fährtensuchen',
        'Fallen stellen',
        'Fesseln/Entfesseln',
        'Fischen/Angeln',
        'Orientierung',
        'Seefischerei',
        'Wettervorhersage',
        'Wildnisleben',
    ],

    SkillGroup.WISSEN: [
        'Anatomie',
        'Baukunst',
        'Brett-/Kartenspiel',
        'Geografie',
        'Geschichtswissen',
        'Gesteinskunde',
        'Götter und Kulte',
        'Heraldik',
        'Hüttenkunde',
        'Kriegskunst',
        'Kryptographie',
        'Magiekunde',
        'Mechanik',
        'Pflanzenkunde',
        'Philosophie',
        'Rechnen',
        'Rechtskunde',
        'Sagen und Legenden',
        'Schätzen',
        'Schiffbau',
        'Sprachenkunde',
        'Staatskunst',
        'Sternkunde',
        'Tierkunde',
    ],

    SkillGroup.HANDWERK: [
        'Abrichten',
        'Ackerbau',
        'Alchimie',
        'Bergbau',
        'Bogenbau',
        'Boote fahren',
        'Brauer',
        'Drucker',
        'Eissegler fahren',
        'Fahrzeug lenken',
        'Falschspiel',
        'Feinmechanik',
        'Feuersteinbearbeitung',
        'Fleischer',
        'Gerber/Kürschner',
        'Glaskunst',
        'Grobschmied',
        'Handel',
        'Hauswirtschaft',
        'Heilkunde: Gift',
        'Heilkunde: Krankheiten',
        'Heilkunde: Seele',
        'Heilkunde: Wunden',
        'Holzbearbeitung',
        'Hundeschlitten fahren',
        'Instrumentenbauer',
        'Kapellmeister',
        'Kartografie',
        'Kochen',
        'Kristallzucht',
        'Lederarbeiten',
        'Malen/Zeichnen',
        'Maurer',
        'Metallguss',
        'Musizieren',
        'Schlösser knacken',
        'Schnaps brennen',
        'Schneidern',
        'Seefahrt',
        'Seiler',
        'Steinmetz',
        'Steinschneider/Juwelier',
        'Stellmacher',
        'Steuermann',
        'Stoffe färben',
        'Tätowieren',
        'Töpfern',
        'Viehzucht',
        'Webkunst',
        'Winzer',
        'Zimmermann',
        'Fluggeräte steuern',
    ],

    SkillGroup.GABEN: [
        'Deuten der Zeichen',
        'Empathie',
        'Tierempathie (alle)',
        'Tierempathie (speziell)',
        'Gefahreninstinkt',
        'Prophezeien',
        'Zwergennase',
        'Magiegespür',
        'Geräuschhexerei',
    ],

    SkillGroup.RITUALKENNTIS: [
        'Ritualkenntnis: Alchimist',
        'Ritualkenntnis: Derwisch',
        'Ritualkenntnis: Druide',
        'Ritualkenntnis: Durro-Dûn',
        'Ritualkenntnis: Geode',
        'Ritualkenntnis: Hexe',
        'Ritualkenntnis: Kristallomantie',
        'Ritualkenntnis: Gildenmagie',
        'Ritualkenntnis: Runenzauberei',
        'Ritualkenntnis: Scharlatan',
        'Ritualkenntnis: Zaubertänzer',
        'Ritualkenntnis: Zaubertänzer (Hazaqi)',
        'Ritualkenntnis: Zaubertänzer (Majuna)',
        'Ritualkenntnis: Zaubertänzer (tulamidische Sharisad)',
        'Ritualkenntnis: Zaubertänzer (novadische Sharisad)',
        'Ritualkenntnis: Zibilja',

        'Ritualkenntnis: Seher',
        'Ritualkenntnis: Alhanisch',
        'Ritualkenntnis: Druidisch-Geodisch',
        'Ritualkenntnis: Güldenländisch',
        'Ritualkenntnis: Grolmisch',
        'Ritualkenntnis: Kophtanisch',
        'Ritualkenntnis: Mudramulisch',
        'Ritualkenntnis: Satuarisch',
        'Ritualkenntnis: Tapasuul',

        'Ritualkenntnis: Optimatik',
        'Ritualkenntnis: Aygon',
        'Ritualkenntnis: BaLoa',
        'Ritualkenntnis: Bashide',
        'Ritualkenntnis: Geisterkalb',
        'Ritualkenntnis: Geisterwerker',
        'Ritualkenntnis: G\'Rolmur',
        'Ritualkenntnis: Hornherren',
        'Ritualkenntnis: Icemna',
        'Ritualkenntnis: Kentori',
        'Ritualkenntnis: Leonir',
        'Ritualkenntnis: maritim',
        'Ritualkenntnis: Medizinleute',
        'Ritualkenntnis: Monddeuter',
        'Ritualkenntnis: Neristu',
        'Ritualkenntnis: Saithakenner',
        'Ritualkenntnis: Satudur',
        'Ritualkenntnis: Shanwada',
        'Ritualkenntnis: Sherkumar',
        'Ritualkenntnis: Shindramatha',
        'Ritualkenntnis: Shurhokach',
        'Ritualkenntnis: Sibyllen',
        'Ritualkenntnis: Sternensänger',
        'Ritualkenntnis: Weihertänzer',
        'Ritualkenntnis: Windflüsterer',
        'Ritualkenntnis: Wolfalben',
        'Ritualkenntnis: Yachzuq',
        'Ritualkenntnis: Zharzhuri',
        'Ritualkenntnis: Petromantie',
        'Ritualkenntnis: Glyphenkunde (Alhani)',

        'Ritualkenntnis: Runenmagie',
        'Ritualkenntnis: Kymanai',
    ],

    SkillGroup.LITURGIEKENNTNIS: [
        'Liturgiekenntnis (Angrosch)',
        'Liturgiekenntnis (Aves)',
        'Liturgiekenntnis (Boron)',
        'Liturgiekenntnis (Efferd)',
        'Liturgiekenntnis (Firun)',
        'Liturgiekenntnis (Gravesh)',
        'Liturgiekenntnis (Hesinde)',
        'Liturgiekenntnis (H\'Ranga)',
        'Liturgiekenntnis (H\'Szint)',
        'Liturgiekenntnis (Ifirn)',
        'Liturgiekenntnis (Ingerimm)',
        'Liturgiekenntnis (Kor)',
        'Liturgiekenntnis (Nandus)',
        'Liturgiekenntnis (Namenloser)',
        'Liturgiekenntnis (Peraine)',
        'Liturgiekenntnis (Phex)',
        'Liturgiekenntnis (Praios)',
        'Liturgiekenntnis (Rahja)',
        'Liturgiekenntnis (Rondra)',
        'Liturgiekenntnis (Travia)',
        'Liturgiekenntnis (Tsa)',
        'Liturgiekenntnis (Zsahh)',
        'Liturgiekenntnis (Swafnir)',
        'Liturgiekenntnis (Brajan)',
        'Liturgiekenntnis (Nereton)',
        'Liturgiekenntnis (Gyldara)',
        'Liturgiekenntnis (Shinxir)',
        'Liturgiekenntnis (Siminia)',
        'Liturgiekenntnis (Chrysir)',
        'Liturgiekenntnis (Zatura)',
        'Liturgiekenntnis (Raia)',
        'Liturgiekenntnis (Pheronos)',
        'Liturgiekenntnis (Ephar)',
        'Liturgiekenntnis (Brazoracus)',
        'Liturgiekenntnis (Levtha)',
        'Liturgiekenntnis (Urschlange)',
        'Liturgiekenntnis (Widersacher)',
        'Liturgiekenntnis (Myranor)',

        'Liturgiekenntnis (Dunkle Zeiten)',

        'Liturgiekenntnis (Sindayru)',
        'Liturgiekenntnis (Nanurta)',
        'Liturgiekenntnis (Shin-Xirit)',
        'Liturgiekenntnis (Zirraku)',
        'Liturgiekenntnis (Pateshi)',
        'Liturgiekenntnis (Ojo\'Sombri)',
        'Liturgiekenntnis (Numinoru)',
        'Liturgiekenntnis (Arkan\'Zin)',
    ],

    SkillGroup.SCHWARZE_GABE: [
        'Schwarze Gabe: Alpträume erzeugen',
        'Schwarze Gabe: Amrychoths Tanz',
        'Schwarze Gabe: Austrocknen',
        'Schwarze Gabe: Befehl der Lamijah',
        'Schwarze Gabe: Begehren überkomme euch!',
        'Schwarze Gabe: Belkelels Ekstase',
        'Schwarze Gabe: Beutesinn',
        'Schwarze Gabe: Brünstigkeit erzeugen',
        'Schwarze Gabe: Chimärenerschaffung',
        'Schwarze Gabe: Ertränken',
        'Schwarze Gabe: Fischgift',
        'Schwarze Gabe: Geschwindigkeit',
        'Schwarze Gabe: Gier erzeugen',
        'Schwarze Gabe: Goldene Hand',
        'Schwarze Gabe: Hauch der Pestilenz',
        'Schwarze Gabe: Herrschaft über Dschinne',
        'Schwarze Gabe: Herrschaft über Geister',
        'Schwarze Gabe: Katzenruf',
        'Schwarze Gabe: Kornfäule',
        'Schwarze Gabe: Krakenhaut',
        'Schwarze Gabe: Krakenruf',
        'Schwarze Gabe: Lähmende Furcht',
        'Schwarze Gabe: Leichengespür',
        'Schwarze Gabe: Lodernder Blick',
        'Schwarze Gabe: Macht des Wahnsinns',
        'Schwarze Gabe: Magnum Opus des Erzdämons',
        'Schwarze Gabe: Meister der Form',
        'Schwarze Gabe: Meister der Maritimen',
        'Schwarze Gabe: Nagrachs Hauch',
        'Schwarze Gabe: Orkanbö',
        'Schwarze Gabe: Raub der Lebenskraft',
        'Schwarze Gabe: Schleichen in den Schatten',
        'Schwarze Gabe: Spur des Missetäters',
        'Schwarze Gabe: Todeshauch',
        'Schwarze Gabe: Trugwelten erschaffen',
        'Schwarze Gabe: Unsichtbarer Jäger',
        'Schwarze Gabe: Verborgenes Wissen erspüren',
        'Schwarze Gabe: Wahrheitssinn',
        'Schwarze Gabe: Wundschmerz',
        'Schwarze Gabe: Zwist und Hader',
    ],
# 'Augenamulett',
# 'Reittierempathie',
# 'Geister rufen',
# 'Geister bannen',
# 'Geister binden',
# 'Geister aufnehmen',
# 'Abishant',
# 'Auflösung',
# 'Einschüchterndes Gebrüll',
# 'Bedrohliches Knurren',
# 'Farbwandel',
# 'Galopp',
# 'Geschlechtswandel',
# 'Heilsames Schnurren',
# 'Prospektorensinn',
# 'Unsichtbarkeit',
# 'Immanspiel',
# 'Ansitzjagd incl Waffe',
# 'Pirschjagd incl Waffe',
# 'Hetzjagd incl Waffe',
# 'Tierfallen aufstellen',
# 'Speerfischen',
# 'Nahrung sammeln',
# 'Kräuter suchen',
# 'Wachehalten',
# 'Elementare Kunstfertigkeit',
# 'Elementare Hellsicht',
# 'Astralsinn',
# 'Telekinese',
# 'Manifestationsstärke',
# 'Lebenssinn',
# 'Tarnung',
# 'Spionage',
# 'Wesenskontrolle',
# 'Springen',

# SkillGroup.KAMPF: 'D',
# SkillGroup.SPRACHEN: 'D',
# SkillGroup.SCHRIFTEN: 'D',
# SkillGroup.RITUALFERTIGKEIT: 'E',
}

skill_group_to_complexity = {
    SkillGroup.KOERPER: 'D',
    SkillGroup.GESELLSCHAFT: 'B',
    SkillGroup.NATUR: 'B',
    SkillGroup.WISSEN: 'B',
    SkillGroup.HANDWERK: 'B',
    SkillGroup.GABEN: 'F',
    SkillGroup.RITUALKENNTIS: 'E',
    SkillGroup.LITURGIEKENNTNIS: 'F',
    SkillGroup.RITUALFERTIGKEIT: 'E',
    SkillGroup.SCHWARZE_GABE: 'F'
}


def get_skill_group_for_skill(skill):
    for group, skills in skill_group_to_skills.items():
        if skill in skills:
            return group
    return None

def get_complexity_for_skill(skill):
    group = get_skill_group_for_skill(skill)
    if group is None:
        # TODO if no group matches
        return None
    return skill_group_to_complexity[group]
