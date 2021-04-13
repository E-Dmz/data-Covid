reg_name = {
    '01': 'Guadeloupe',
    '02': 'Martinique',
    '03': 'Guyane',
    '04': 'La Réunion',
    '06': 'Mayotte',
    '11': 'Île-de-France',
    '24': 'Centre-Val de Loire',
    '27': 'Bourgogne-Franche-Comté',
    '28': 'Normandie',
    '32': 'Hauts-de-France',
    '44': 'Grand Est',
    '52': 'Pays de la Loire',
    '53': 'Bretagne',
    '75': 'Nouvelle-Aquitaine',
    '76': 'Occitanie',
    '84': 'Auvergne-Rhône-Alpes',
    '93': "Provence-Alpes-Côte d'Azur",
    '94': 'Corse'
    }

reg2dep = {
    'Auvergne-Rhône-Alpes': ['01','03','07','15','26','38','42','43','63','69','73','74'],
    'Bourgogne-Franche-Comté': ['21', '25', '39', '58', '70', '71', '89', '90'],
    'Bretagne': ['35', '22', '56', '29'],
    'Centre-Val de Loire': ['18', '28', '36', '37', '41', '45'],
    'Corse': ['2A', '2B'],
    'Grand Est': ['08', '10', '51', '52', '54', '55', '57', '67', '68', '88'],
    'Guadeloupe': ['971'],
    'Guyane': ['973'],
    'Hauts-de-France': ['02', '59', '60', '62', '80'],
    'Île-de-France': ['75', '77', '78', '91', '92', '93', '94', '95'],
    'La Réunion': ['974'],
    'Martinique': ['972'],
    'Normandie': ['14', '27', '50', '61', '76'],
    'Nouvelle-Aquitaine': ['16', '17', '19', '23', '24', '33', '40', '47', '64', '79', '86', '87'],
    'Occitanie': ['09', '11', '12', '30', '31', '32', '34', '46', '48', '65', '66', '81', '82'],
    'Pays de la Loire': ['44', '49', '53', '72', '85'],
    "Provence-Alpes-Côte d'Azur": ['04', '05', '06', '13', '83', '84'],
    'Outre-mer (DROM)': ['971', '972', '973', '974', '976',]
    }

dep_name = {
    '01': 'Ain',
    '02': 'Aisne',
    '03': 'Allier',
    '04': 'Alpes-de-Haute-Provence',
    '05': 'Hautes-Alpes',
    '06': 'Alpes-Maritimes',
    '07': 'Ardèche',
    '08': 'Ardennes',
    '09': 'Ariège',
    '10': 'Aube',
    '11': 'Aude',
    '12': 'Aveyron',
    '13': 'Bouches-du-Rhône',
    '14': 'Calvados',
    '15': 'Cantal',
    '16': 'Charente',
    '17': 'Charente-Maritime',
    '18': 'Cher',
    '19': 'Corrèze',
    '2A': 'Corse-du-Sud',
    '2B': 'Haute-Corse',
    '21': "Côte-d'Or",
    '22': "Côtes-d'Armor",
    '23': 'Creuse',
    '24': 'Dordogne',
    '25': 'Doubs',
    '26': 'Drôme',
    '27': 'Eure',
    '28': 'Eure-et-Loir',
    '29': 'Finistère',
    '30': 'Gard',
    '31': 'Haute-Garonne',
    '32': 'Gers',
    '33': 'Gironde',
    '34': 'Hérault',
    '35': 'Ille-et-Vilaine',
    '36': 'Indre',
    '37': 'Indre-et-Loire',
    '38': 'Isère',
    '39': 'Jura',
    '40': 'Landes',
    '41': 'Loir-et-Cher',
    '42': 'Loire',
    '43': 'Haute-Loire',
    '44': 'Loire-Atlantique',
    '45': 'Loiret',
    '46': 'Lot',
    '47': 'Lot-et-Garonne',
    '48': 'Lozère',
    '49': 'Maine-et-Loire',
    '50': 'Manche',
    '51': 'Marne',
    '52': 'Haute-Marne',
    '53': 'Mayenne',
    '54': 'Meurthe-et-Moselle',
    '55': 'Meuse',
    '56': 'Morbihan',
    '57': 'Moselle',
    '58': 'Nièvre',
    '59': 'Nord',
    '60': 'Oise',
    '61': 'Orne',
    '62': 'Pas-de-Calais',
    '63': 'Puy-de-Dôme',
    '64': 'Pyrénées-Atlantiques',
    '65': 'Hautes-Pyrénées',
    '66': 'Pyrénées-Orientales',
    '67': 'Bas-Rhin',
    '68': 'Haut-Rhin',
    '69': 'Rhône',
    '70': 'Haute-Saône',
    '71': 'Saône-et-Loire',
    '72': 'Sarthe',
    '73': 'Savoie',
    '74': 'Haute-Savoie',
    '75': 'Paris',
    '76': 'Seine-Maritime',
    '77': 'Seine-et-Marne',
    '78': 'Yvelines',
    '79': 'Deux-Sèvres',
    '80': 'Somme',
    '81': 'Tarn',
    '82': 'Tarn-et-Garonne',
    '83': 'Var',
    '84': 'Vaucluse',
    '85': 'Vendée',
    '86': 'Vienne',
    '87': 'Haute-Vienne',
    '88': 'Vosges',
    '89': 'Yonne',
    '90': 'Territoire de Belfort',
    '91': 'Essonne',
    '92': 'Hauts-de-Seine',
    '93': 'Seine-Saint-Denis',
    '94': 'Val-de-Marne',
    '95': "Val-d'Oise",
    '971': 'Guadeloupe',
    '972': 'Martinique',
    '973': 'Guyane',
    '974': 'La Réunion',
    '975': 'Saint-Pierre-et-Miquelon',
    '976': 'Mayotte',
    '977': 'Saint-Barthélémy',
    '978': 'Saint-Martin'
    }

dep2reg = {
    '01': 'Auvergne-Rhône-Alpes',
    '03': 'Auvergne-Rhône-Alpes',
    '07': 'Auvergne-Rhône-Alpes',
    '15': 'Auvergne-Rhône-Alpes',
    '26': 'Auvergne-Rhône-Alpes',
    '38': 'Auvergne-Rhône-Alpes',
    '42': 'Auvergne-Rhône-Alpes',
    '43': 'Auvergne-Rhône-Alpes',
    '63': 'Auvergne-Rhône-Alpes',
    '69': 'Auvergne-Rhône-Alpes',
    '73': 'Auvergne-Rhône-Alpes',
    '74': 'Auvergne-Rhône-Alpes',
    '21': 'Bourgogne-Franche-Comté',
    '25': 'Bourgogne-Franche-Comté',
    '39': 'Bourgogne-Franche-Comté',
    '58': 'Bourgogne-Franche-Comté',
    '70': 'Bourgogne-Franche-Comté',
    '71': 'Bourgogne-Franche-Comté',
    '89': 'Bourgogne-Franche-Comté',
    '90': 'Bourgogne-Franche-Comté',
    '35': 'Bretagne',
    '22': 'Bretagne',
    '56': 'Bretagne',
    '29': 'Bretagne',
    '18': 'Centre-Val de Loire',
    '28': 'Centre-Val de Loire',
    '36': 'Centre-Val de Loire',
    '37': 'Centre-Val de Loire',
    '41': 'Centre-Val de Loire',
    '45': 'Centre-Val de Loire',
    '2A': 'Corse',
    '2B': 'Corse',
    '08': 'Grand Est',
    '10': 'Grand Est',
    '51': 'Grand Est',
    '52': 'Grand Est',
    '54': 'Grand Est',
    '55': 'Grand Est',
    '57': 'Grand Est',
    '67': 'Grand Est',
    '68': 'Grand Est',
    '88': 'Grand Est',
    '971': 'Outre-mer (DROM)', # Guadeloupe, DROM (DOM et ROM)
    '973': 'Outre-mer (DROM)', # Guyane, DROM (CTU)
    '02': 'Hauts-de-France',
    '59': 'Hauts-de-France',
    '60': 'Hauts-de-France',
    '62': 'Hauts-de-France',
    '80': 'Hauts-de-France',
    '75': 'Île-de-France',
    '77': 'Île-de-France',
    '78': 'Île-de-France',
    '91': 'Île-de-France',
    '92': 'Île-de-France',
    '93': 'Île-de-France',
    '94': 'Île-de-France',
    '95': 'Île-de-France',
    '974': 'Outre-mer (DROM)', # La Réunion, DROM (DOM et ROM)
    '972': 'Outre-mer (DROM)', # Martinique, DROM (CTU)
    '14': 'Normandie',
    '27': 'Normandie',
    '50': 'Normandie',
    '61': 'Normandie',
    '76': 'Normandie',
    '16': 'Nouvelle-Aquitaine',
    '17': 'Nouvelle-Aquitaine',
    '19': 'Nouvelle-Aquitaine',
    '23': 'Nouvelle-Aquitaine',
    '24': 'Nouvelle-Aquitaine',
    '33': 'Nouvelle-Aquitaine',
    '40': 'Nouvelle-Aquitaine',
    '47': 'Nouvelle-Aquitaine',
    '64': 'Nouvelle-Aquitaine',
    '79': 'Nouvelle-Aquitaine',
    '86': 'Nouvelle-Aquitaine',
    '87': 'Nouvelle-Aquitaine',
    '09': 'Occitanie',
    '11': 'Occitanie',
    '12': 'Occitanie',
    '30': 'Occitanie',
    '31': 'Occitanie',
    '32': 'Occitanie',
    '34': 'Occitanie',
    '46': 'Occitanie',
    '48': 'Occitanie',
    '65': 'Occitanie',
    '66': 'Occitanie',
    '81': 'Occitanie',
    '82': 'Occitanie',
    '44': 'Pays de la Loire',
    '49': 'Pays de la Loire',
    '53': 'Pays de la Loire',
    '72': 'Pays de la Loire',
    '85': 'Pays de la Loire',
    '04': "Provence-Alpes-Côte d'Azur",
    '05': "Provence-Alpes-Côte d'Azur",
    '06': "Provence-Alpes-Côte d'Azur",
    '13': "Provence-Alpes-Côte d'Azur",
    '83': "Provence-Alpes-Côte d'Azur",
    '84': "Provence-Alpes-Côte d'Azur",
    # '975': 'Outre-mer', (Saint-Pierre-et-Miquelon, COM)
    '976': 'Outre-mer (DROM)', # Mayotte, DROM (CTU)
    # '977': 'Outre-mer', (Saint-Barthélémy, COM)
    # '978': 'Outre-mer' (Saint-Martin, COM)
    }

reg_3C_pop = {'01': {'0-29': 233162, '30-59': 265057, '60+': 158736, 'whole': 656955},
 '02': {'0-29': 181295, '30-59': 197763, '60+': 146992, 'whole': 526050},
 '03': {'0-29': 94800, '30-59': 118653, '60+': 117862, 'whole': 331315},
 '04': {'0-29': 47550, '30-59': 60968, '60+': 56679, 'whole': 165197},
 '05': {'0-29': 41995, '30-59': 53829, '60+': 45932, 'whole': 141756},
 '06': {'0-29': 332679, '30-59': 409246, '60+': 337471, 'whole': 1079396},
 '07': {'0-29': 96850, '30-59': 122997, '60+': 107028, 'whole': 326875},
 '08': {'0-29': 85646, '30-59': 101020, '60+': 78865, 'whole': 265531},
 '09': {'0-29': 43700, '30-59': 56230, '60+': 52468, 'whole': 152398},
 '10': {'0-29': 107678, '30-59': 114529, '60+': 87700, 'whole': 309907},
 '11': {'0-29': 109430, '30-59': 136313, '60+': 126962, 'whole': 372705},
 '12': {'0-29': 78243, '30-59': 101784, '60+': 98333, 'whole': 278360},
 '13': {'0-29': 710300, '30-59': 776651, '60+': 547518, 'whole': 2034469},
 '14': {'0-29': 237080, '30-59': 252920, '60+': 201453, 'whole': 691453},
 '15': {'0-29': 37394, '30-59': 52528, '60+': 52889, 'whole': 142811},
 '16': {'0-29': 103458, '30-59': 128407, '60+': 116315, 'whole': 348180},
 '17': {'0-29': 183823, '30-59': 230945, '60+': 232312, 'whole': 647080},
 '18': {'0-29': 87574, '30-59': 108464, '60+': 100366, 'whole': 296404},
 '19': {'0-29': 68716, '30-59': 86672, '60+': 84948, 'whole': 240336},
 '21': {'0-29': 187079, '30-59': 197382, '60+': 148425, 'whole': 532886},
 '22': {'0-29': 179086, '30-59': 214063, '60+': 203037, 'whole': 596186},
 '23': {'0-29': 29443, '30-59': 41113, '60+': 45714, 'whole': 116270},
 '24': {'0-29': 107442, '30-59': 146591, '60+': 154360, 'whole': 408393},
 '25': {'0-29': 195833, '30-59': 202373, '60+': 141243, 'whole': 539449},
 '26': {'0-29': 173066, '30-59': 196800, '60+': 150694, 'whole': 520560},
 '27': {'0-29': 207302, '30-59': 234082, '60+': 159303, 'whole': 600687},
 '28': {'0-29': 145614, '30-59': 164794, '60+': 119017, 'whole': 429425},
 '29': {'0-29': 291361, '30-59': 337136, '60+': 278057, 'whole': 906554},
 '2A': {'0-29': 45883, '30-59': 65969, '60+': 50569, 'whole': 162421},
 '2B': {'0-29': 56033, '30-59': 70830, '60+': 55395, 'whole': 182258},
 '30': {'0-29': 240726, '30-59': 279798, '60+': 227944, 'whole': 748468},
 '31': {'0-29': 539419, '30-59': 553435, '60+': 308081, 'whole': 1400935},
 '32': {'0-29': 51482, '30-59': 70044, '60+': 68514, 'whole': 190040},
 '33': {'0-29': 583909, '30-59': 636855, '60+': 412676, 'whole': 1633440},
 '34': {'0-29': 412066, '30-59': 435285, '60+': 328794, 'whole': 1176145},
 '35': {'0-29': 408447, '30-59': 415285, '60+': 258341, 'whole': 1082073},
 '36': {'0-29': 60811, '30-59': 76938, '60+': 79390, 'whole': 217139},
 '37': {'0-29': 207312, '30-59': 225115, '60+': 172953, 'whole': 605380},
 '38': {'0-29': 462200, '30-59': 488885, '60+': 313894, 'whole': 1264979},
 '39': {'0-29': 80151, '30-59': 97073, '60+': 80625, 'whole': 257849},
 '40': {'0-29': 117790, '30-59': 158040, '60+': 136149, 'whole': 411979},
 '41': {'0-29': 100935, '30-59': 120994, '60+': 105906, 'whole': 327835},
 '42': {'0-29': 266546, '30-59': 278180, '60+': 220011, 'whole': 764737},
 '43': {'0-29': 68752, '30-59': 85058, '60+': 73091, 'whole': 226901},
 '44': {'0-29': 531273, '30-59': 558131, '60+': 347733, 'whole': 1437137},
 '45': {'0-29': 245097, '30-59': 257213, '60+': 180580, 'whole': 682890},
 '46': {'0-29': 44797, '30-59': 60962, '60+': 67407, 'whole': 173166},
 '47': {'0-29': 98425, '30-59': 119986, '60+': 111925, 'whole': 330336},
 '48': {'0-29': 22585, '30-59': 28147, '60+': 25554, 'whole': 76286},
 '49': {'0-29': 293749, '30-59': 299434, '60+': 222698, 'whole': 815881},
 '50': {'0-29': 149117, '30-59': 179458, '60+': 162094, 'whole': 490669},
 '51': {'0-29': 204890, '30-59': 211753, '60+': 147180, 'whole': 563823},
 '52': {'0-29': 50950, '30-59': 62248, '60+': 56052, 'whole': 169250},
 '53': {'0-29': 103116, '30-59': 112210, '60+': 90039, 'whole': 305365},
 '54': {'0-29': 264854, '30-59': 273994, '60+': 191550, 'whole': 730398},
 '55': {'0-29': 57443, '30-59': 68269, '60+': 55929, 'whole': 181641},
 '56': {'0-29': 231049, '30-59': 278704, '60+': 245813, 'whole': 755566},
 '57': {'0-29': 340828, '30-59': 411344, '60+': 283694, 'whole': 1035866},
 '58': {'0-29': 53680, '30-59': 69421, '60+': 76495, 'whole': 199596},
 '59': {'0-29': 1005422, '30-59': 981892, '60+': 601674, 'whole': 2588988},
 '60': {'0-29': 301721, '30-59': 327864, '60+': 195492, 'whole': 825077},
 '61': {'0-29': 83751, '30-59': 98601, '60+': 94551, 'whole': 276903},
 '62': {'0-29': 522280, '30-59': 555423, '60+': 375075, 'whole': 1452778},
 '63': {'0-29': 222772, '30-59': 247422, '60+': 190046, 'whole': 660240},
 '64': {'0-29': 208299, '30-59': 261406, '60+': 213464, 'whole': 683169},
 '65': {'0-29': 64264, '30-59': 82277, '60+': 80298, 'whole': 226839},
 '66': {'0-29': 145044, '30-59': 172592, '60+': 161364, 'whole': 479000},
 '67': {'0-29': 399593, '30-59': 444563, '60+': 288451, 'whole': 1132607},
 '68': {'0-29': 253913, '30-59': 303342, '60+': 205949, 'whole': 763204},
 '69': {'0-29': 745524, '30-59': 711677, '60+': 418850, 'whole': 1876051},
 '70': {'0-29': 71915, '30-59': 88665, '60+': 72614, 'whole': 233194},
 '71': {'0-29': 163376, '30-59': 199934, '60+': 184514, 'whole': 547824},
 '72': {'0-29': 190889, '30-59': 204725, '60+': 164613, 'whole': 560227},
 '73': {'0-29': 142034, '30-59': 169742, '60+': 120772, 'whole': 432548},
 '74': {'0-29': 292071, '30-59': 348598, '60+': 187736, 'whole': 828405},
 '75': {'0-29': 792882, '30-59': 869271, '60+': 486118, 'whole': 2148271},
 '76': {'0-29': 446016, '30-59': 463017, '60+': 334755, 'whole': 1243788},
 '77': {'0-29': 557352, '30-59': 574493, '60+': 291762, 'whole': 1423607},
 '78': {'0-29': 543417, '30-59': 578277, '60+': 326931, 'whole': 1448625},
 '79': {'0-29': 117528, '30-59': 140021, '60+': 115078, 'whole': 372627},
 '80': {'0-29': 205711, '30-59': 212205, '60+': 151853, 'whole': 569769},
 '81': {'0-29': 117950, '30-59': 143783, '60+': 126165, 'whole': 387898},
 '82': {'0-29': 86530, '30-59': 100406, '60+': 75682, 'whole': 262618},
 '83': {'0-29': 319301, '30-59': 397118, '60+': 357417, 'whole': 1073836},
 '84': {'0-29': 186896, '30-59': 211169, '60+': 162932, 'whole': 560997},
 '85': {'0-29': 212122, '30-59': 252097, '60+': 218968, 'whole': 683187},
 '86': {'0-29': 152821, '30-59': 157001, '60+': 127576, 'whole': 437398},
 '87': {'0-29': 117309, '30-59': 133821, '60+': 119644, 'whole': 370774},
 '88': {'0-29': 108776, '30-59': 133280, '60+': 117464, 'whole': 359520},
 '89': {'0-29': 102060, '30-59': 123065, '60+': 106971, 'whole': 332096},
 '90': {'0-29': 48923, '30-59': 53162, '60+': 38060, 'whole': 140145},
 '91': {'0-29': 524231, '30-59': 524375, '60+': 270795, 'whole': 1319401},
 '92': {'0-29': 610171, '30-59': 670166, '60+': 333425, 'whole': 1613762},
 '93': {'0-29': 707322, '30-59': 684201, '60+': 278626, 'whole': 1670149},
 '94': {'0-29': 548476, '30-59': 569447, '60+': 288118, 'whole': 1406041},
 '95': {'0-29': 509031, '30-59': 498065, '60+': 241258, 'whole': 1248354},
 '971': {'0-29': 125175, '30-59': 146601, '60+': 105103, 'whole': 376879},
 '972': {'0-29': 108501, '30-59': 139918, '60+': 110330, 'whole': 358749},
 '973': {'0-29': 161102, '30-59': 101385, '60+': 28204, 'whole': 290691},
 '974': {'0-29': 354358, '30-59': 343780, '60+': 161821, 'whole': 859959},
 '975': {'0-29': 1902, '30-59': 2759, '60+': 1334, 'whole': 5997},
 '976': {'0-29': 186908, '30-59': 80597, '60+': 11966, 'whole': 279471},
 '977': {'0-29': 3474, '30-59': 5108, '60+': 1379, 'whole': 9961},
 '978': {'0-29': 15451, '30-59': 15252, '60+': 4629, 'whole': 35334},
 'Auvergne-Rhône-Alpes': {'0-29': 2835171,
  '30-59': 3085597,
  '60+': 2111609,
  'whole': 8032377},
 'Bourgogne-Franche-Comté': {'0-29': 903017,
  '30-59': 1031075,
  '60+': 848947,
  'whole': 2783039},
 'Bretagne': {'0-29': 1109943,
  '30-59': 1245188,
  '60+': 985248,
  'whole': 3340379},
 'Centre-Val de Loire': {'0-29': 847343,
  '30-59': 953518,
  '60+': 758212,
  'whole': 2559073},
 'Corse': {'0-29': 101916, '30-59': 136799, '60+': 105964, 'whole': 344679},
 'France': {'0-29': 23576479,
  '30-59': 25680932,
  '60+': 17857583,
  'whole': 67114995},
 'Grand Est': {'0-29': 1874571,
  '30-59': 2124342,
  '60+': 1512834,
  'whole': 5511747},
 'Hauts-de-France': {'0-29': 2216429,
  '30-59': 2275147,
  '60+': 1471086,
  'whole': 5962662},
 'Normandie': {'0-29': 1123266,
  '30-59': 1228078,
  '60+': 952156,
  'whole': 3303500},
 'Nouvelle-Aquitaine': {'0-29': 1888963,
  '30-59': 2240858,
  '60+': 1870161,
  'whole': 5999982},
 'Occitanie': {'0-29': 1956236,
  '30-59': 2221056,
  '60+': 1747566,
  'whole': 5924858},
 'Outre-mer (DROM)': {'0-29': 956872,
  '30-59': 835401,
  '60+': 424767,
  'whole': 2217041},
 'Pays de la Loire': {'0-29': 1331149,
  '30-59': 1426597,
  '60+': 1044051,
  'whole': 3801797},
 "Provence-Alpes-Côte d'Azur": {'0-29': 1638721,
  '30-59': 1908981,
  '60+': 1507949,
  'whole': 5055651},
 'Île-de-France': {'0-29': 4792882,
  '30-59': 4968295,
  '60+': 2517033,
  'whole': 12278210}}

class_2_3C = {0: 'whole',
               9: '0-29',
               19: '0-29',
               29: '0-29',
               39: '30-59',
               49: '30-59',
               59: '30-59',
               69: '60+',
               79: '60+',
               89: '60+',
               90: '60+',
              }

classvac_2_3C = {0: 'whole',
               24: '0-29',
               29: '0-29',
               39: '30-59',
               49: '30-59',
               59: '30-59',
               64: '60+',
               69: '60+',
               74: '60+',
               79: '60+',
               80: '60+',
              }

reg_2lignes = {'Auvergne-Rhône-Alpes': 'Auvergne-\nRhône-Alpes',
 'Bourgogne-Franche-Comté': 'Bourgogne-\nFranche-Comté',
 'Bretagne': 'Bretagne',
 'Centre-Val de Loire': 'Centre-\nVal de Loire',
 'Corse': 'Corse',
 'Grand Est': 'Grand Est',
 'Hauts-de-France': 'Hauts-de-France',
 'Normandie': 'Normandie',
 'Nouvelle-Aquitaine': 'Nouvelle-\nAquitaine',
 'Occitanie': 'Occitanie',
 'Outre-mer (DROM)': 'Outre-mer\n(DROM)',
 'Pays de la Loire': 'Pays\nde la Loire',
 "Provence-Alpes-Côte d'Azur": "Provence-\nAlpes-Côte d'Azur",
 'Île-de-France': 'Île-de-France'}

deps = ['01', '02', '03', '04', '05', '06', '07', '08',
       '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19','2A', '2B',
       '21', '22', '23', '24', '25', '26', '27', '28', '29', 
       '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
       '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51',
       '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62',
       '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73',
       '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84',
       '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95',
       '971', '972', '973', '974', '975', '976', '977', '978']

regs = ['Auvergne-Rhône-Alpes',
 'Bourgogne-Franche-Comté',
 'Bretagne',
 'Centre-Val de Loire',
 'Corse',
 'Grand Est',
 'Hauts-de-France',
 'Île-de-France',
 'Normandie',
 'Nouvelle-Aquitaine',
 'Occitanie',
 'Pays de la Loire',
 "Provence-Alpes-Côte d'Azur",
 'Outre-mer (DROM)']

deps_outlay_fig_synthese = {
    13: [ 0, 1, 2,
        4, 5, 6,
        8, 9, 10,
        12, 13, 14, 15,     ],
    12: [ 0, 1, 2,
        4, 5, 6,
        8, 9, 10, 
        12, 13, 14,  ],
    10: [0, 1, 2, 
        4, 5, 6,
         8, 9, 10,],
    8:  [0, 1,
        4, 5, 6, 
        8, 9, 10,    ],
    6:  [0, 1, 2,
        4, 5, 6,],
    5:  [0, 1,
        4,  5,    6,],
    4:  [0, 1,
        4, 5,  ],
    2:  [0, 1,
        ],   
}