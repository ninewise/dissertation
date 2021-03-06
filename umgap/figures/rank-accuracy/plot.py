from collections import defaultdict

import drawSvg as draw # pip install drawSvg


def plot(data):
	height = 200

	max_length = max(l for l, r in data.keys())
	lengths = [ [0] * len(colors) for _ in range(max_length + 1) ]
	for (length, rank), freq in data.items():
		lengths[length][rank2color[rank]] += freq

	d = draw.Drawing(2 * max_length + 2, height)
	max_count = max(sum(l) for l in lengths)
	for length, splits in enumerate(lengths):
		cumsum = 0
		for i, new in enumerate(splits):
			d.append(draw.Line(length * 2,
			                   cumsum / max_count * height,
			                   length * 2,
			                   (cumsum + new) / max_count * height,
			                   stroke=colors[i]))
			cumsum += new
	d.saveSvg('totals-raw.svg')
	print("heighest:", max_count)
	print("total:", sum(sum(l) for l in lengths))

	d = draw.Drawing(2 * max_length * (len(colors) + 1), height)
	max_count = max(v for l in lengths for v in l)
	for length, splits in enumerate(lengths):
		for rank, freq in enumerate(splits):
			d.append(draw.Line(2 * (length * (len(colors) + 1) + rank),
			                   0,
			                   2 * (length * (len(colors) + 1) + rank),
			                   freq / max_count * height,
			                   stroke=colors[rank]))
	d.saveSvg('separate-raw.svg')

	d = draw.Drawing(2 * max_length, height)
	for length, splits in enumerate(lengths):
		length_total = sum(splits) or 1
		cumsum = 0
		for rank, freq in enumerate(splits):
			d.append(draw.Line(length * 2,
			                   cumsum / length_total * height,
			                   length * 2,
			                   (cumsum + freq) / length_total * height,
			                   stroke=colors[rank]))
			cumsum += freq
	d.saveSvg('ratios-raw.svg')

right = "#2e7d32"
wrong = "#f44336"
blue = "#1565c0"
yellow = "#ff8f00"
colors = ["#500909", "#8ccc4f", "#ae45d3", "#eebb79", "#61895f", "#fa6a6f", "#655380", "#c1dfc1", "#181ca0"]

rank2color = {"subspecies": 0, "varietas": 0, "forma": 0,
              "species": 1,
              "genus": 2, "subgenus": 2, "species group": 2, "species subgroup": 2,
              "family": 3, "subfamily": 3, "tribe": 3, "subtribe": 3,
              "order": 4, "suborder": 4, "infraorder": 4, "parvorder": 4, "superfamily": 4,
              "class": 5, "subclass": 5, "infraclass": 5, "superorder": 5,
              "phylum": 6, "subphylum": 6, "superclass": 6,
              "superkingdom": 7, "kingdom": 7, "subkingdom": 7, "superphylum": 7,
              "no rank": 8}

data = {(38, 'phylum'): 203044, (23, 'superorder'): 6025, (45, 'superfamily'): 401,
        (34, 'infraclass'): 7781, (50, 'forma'): 2339, (17, 'species'): 27287460,
        (16, 'superfamily'): 11597, (22, 'subspecies'): 292082, (18, 'subspecies'): 393530,
        (46, 'subfamily'): 4451, (44, 'parvorder'): 1346, (8, 'phylum'): 4045579,
        (5, 'parvorder'): 700, (13, 'order'): 1372542, (45, 'infraorder'): 425,
        (19, 'superkingdom'): 492797, (10, 'suborder'): 64921, (40, 'superorder'): 963,
        (36, 'infraclass'): 6024, (20, 'genus'): 9293166, (49, 'superorder'): 344,
        (16, 'suborder'): 31401, (14, 'subkingdom'): 1416, (33, 'subspecies'): 117051,
        (10, 'infraclass'): 124615, (42, 'superkingdom'): 45499, (44, 'superkingdom'): 36385,
        (45, 'subspecies'): 42391, (48, 'subclass'): 117, (29, 'superorder'): 3340,
        (12, 'parvorder'): 30062, (21, 'no rank'): 342999, (21, 'infraclass'): 32047,
        (50, 'phylum'): 72267, (49, 'order'): 44078, (20, 'species subgroup'): 11713,
        (42, 'order'): 78637, (41, 'superorder'): 886, (48, 'parvorder'): 910,
        (10, 'species subgroup'): 31112, (28, 'subclass'): 1346, (33, 'no rank'): 101442,
        (49, 'infraorder'): 298, (22, 'no rank'): 312619, (20, 'subkingdom'): 370,
        (15, 'species group'): 184235, (38, 'species'): 4301124, (26, 'subphylum'): 2491,
        (25, 'species group'): 86681, (39, 'genus'): 1672181, (14, 'parvorder'): 24499,
        (20, 'tribe'): 35163, (27, 'subtribe'): 4972, (13, 'genus'): 16062746,
        (14, 'genus'): 14804128, (39, 'phylum'): 183382, (47, 'subtribe'): 585,
        (6, 'parvorder'): 4269, (22, 'superorder'): 6729, (35, 'class'): 131192,
        (21, 'subtribe'): 8137, (17, 'infraclass'): 49966, (7, 'class'): 926241,
        (22, 'superkingdom'): 364349, (30, 'family'): 381334, (7, 'order'): 690545,
        (17, 'subtribe'): 11734, (37, 'subtribe'): 1683, (37, 'forma'): 6818,
        (26, 'class'): 346691, (42, 'subtribe'): 1023, (18, 'subfamily'): 72368,
        (9, 'order'): 2026885, (40, 'infraorder'): 791, (13, 'species group'): 217146,
        (20, 'family'): 1033071, (37, 'superclass'): 398, (34, 'superclass'): 672,
        (33, 'superkingdom'): 113560, (38, 'subphylum'): 380, (49, 'subgenus'): 4189,
        (42, 'no rank'): 42452, (50, 'suborder'): 865, (34, 'varietas'): 38844,
        (30, 'superorder'): 2955, (19, 'order'): 751266, (16, 'species subgroup'): 16835,
        (36, 'parvorder'): 2889, (13, 'subgenus'): 146622, (30, 'superfamily'): 2355,
        (10, 'varietas'): 301476, (18, 'subgenus'): 85805, (17, 'forma'): 36923,
        (28, 'no rank'): 169553, (50, 'species'): 1648426, (41, 'subkingdom'): 9,
        (5, 'subspecies'): 8742, (22, 'infraorder'): 5402, (41, 'kingdom'): 1759,
        (28, 'subspecies'): 179445, (14, 'species subgroup'): 20409, (41, 'phylum'): 150656,
        (17, 'subclass'): 7574, (28, 'phylum'): 590033, (27, 'infraclass'): 17269,
        (34, 'species'): 6263073, (41, 'genus'): 1390663, (7, 'kingdom'): 170068,
        (45, 'parvorder'): 1188, (38, 'class'): 97130, (7, 'species'): 11265765,
        (32, 'subphylum'): 968, (50, 'superfamily'): 252, (48, 'order'): 46817,
        (43, 'kingdom'): 1562, (41, 'infraclass'): 3599, (11, 'tribe'): 93817,
        (45, 'superkingdom'): 33065, (12, 'order'): 1533479, (37, 'tribe'): 6145,
        (26, 'infraclass'): 17856, (14, 'forma'): 47326, (16, 'species group'): 169990,
        (29, 'superclass'): 1141, (8, 'species group'): 276721, (21, 'subclass'): 3893,
        (49, 'family'): 60064, (31, 'parvorder'): 4594, (29, 'varietas'): 61101,
        (24, 'suborder'): 13134, (16, 'infraorder'): 10707, (23, 'forma'): 22438,
        (11, 'superkingdom'): 1339550, (32, 'subtribe'): 2808, (26, 'superorder'): 4380,
        (48, 'subphylum'): 84, (49, 'suborder'): 978, (10, 'tribe'): 103292,
        (23, 'genus'): 7312802, (8, 'genus'): 17227080, (24, 'kingdom'): 9383,
        (38, 'infraclass'): 4629, (7, 'suborder'): 31407, (15, 'suborder'): 35287,
        (31, 'order'): 234608, (21, 'infraorder'): 5860, (37, 'superfamily'): 1103,
        (27, 'species group'): 73414, (40, 'kingdom'): 1850, (42, 'phylum'): 138886,
        (16, 'parvorder'): 19208, (11, 'species'): 45696975, (43, 'superkingdom'): 39752,
        (41, 'class'): 71394, (35, 'parvorder'): 3034, (22, 'parvorder'): 10715,
        (15, 'infraorder'): 12332, (33, 'species subgroup'): 3541, (44, 'phylum'): 114870,
        (41, 'subclass'): 190, (33, 'class'): 165656, (10, 'species'): 48964942,
        (24, 'superclass'): 2130, (5, 'class'): 31713, (21, 'superorder'): 8075,
        (23, 'subgenus'): 52350, (5, 'species subgroup'): 378, (26, 'genus'): 5695017,
        (27, 'genus'): 5237036, (21, 'kingdom'): 11920, (31, 'species subgroup'): 4386,
        (21, 'forma'): 26391, (39, 'subtribe'): 1365, (11, 'superclass'): 14046,
        (44, 'subtribe'): 801, (45, 'infraclass'): 2163, (20, 'species'): 21552366,
        (19, 'kingdom'): 15079, (15, 'class'): 1047593, (8, 'order'): 1842292,
        (14, 'superkingdom'): 879839, (37, 'kingdom'): 2704, (22, 'family'): 859809,
        (48, 'subkingdom'): 1, (40, 'infraclass'): 3944, (15, 'subspecies'): 501600,
        (44, 'tribe'): 2894, (19, 'infraorder'): 7383, (44, 'no rank'): 35025,
        (26, 'subfamily'): 32913, (19, 'subtribe'): 9747, (37, 'subkingdom'): 17,
        (20, 'superclass'): 3782, (36, 'tribe'): 6983, (11, 'forma'): 62064,
        (12, 'family'): 2312139, (13, 'subfamily'): 125257, (7, 'phylum'): 1719171,
        (25, 'superkingdom'): 268494, (23, 'superclass'): 2389, (29, 'no rank'): 152501,
        (41, 'subgenus'): 8824, (28, 'kingdom'): 6146, (24, 'tribe'): 23804,
        (39, 'species'): 3929089, (26, 'varietas'): 79112, (43, 'phylum'): 124936,
        (47, 'subspecies'): 37329, (20, 'infraclass'): 35823, (36, 'class'): 119155,
        (12, 'no rank'): 844134, (5, 'subgenus'): 1542, (27, 'tribe'): 18193,
        (10, 'subkingdom'): 5201, (10, 'subgenus'): 203765, (21, 'superkingdom'): 408635,
        (8, 'suborder'): 69958, (43, 'subclass'): 147, (23, 'species'): 16830857,
        (48, 'no rank'): 25947, (34, 'subphylum'): 787, (16, 'subspecies'): 461718,
        (20, 'phylum'): 1328005, (43, 'subkingdom'): 7, (5, 'suborder'): 634,
        (10, 'parvorder'): 38096, (11, 'varietas'): 281990, (41, 'subfamily'): 8404,
        (17, 'species group'): 158924, (32, 'superkingdom'): 122770, (9, 'subclass'): 32231,
        (30, 'superclass'): 1020, (47, 'superfamily'): 336, (9, 'species'): 50828734,
        (25, 'parvorder'): 8226, (39, 'tribe'): 5005, (21, 'superfamily'): 6370,
        (24, 'subclass'): 2536, (46, 'infraorder'): 396, (46, 'superclass'): 150,
        (19, 'no rank'): 408293, (48, 'subspecies'): 33592, (34, 'forma'): 8809,
        (42, 'subfamily'): 6570, (15, 'superorder'): 15844, (41, 'family'): 119584,
        (40, 'subphylum'): 263, (5, 'infraorder'): 356, (5, 'infraclass'): 2566,
        (47, 'superclass'): 147, (10, 'superorder'): 29127, (31, 'infraorder'): 1979,
        (29, 'order'): 286892, (29, 'infraorder'): 2575, (24, 'subtribe'): 6190,
        (32, 'phylum'): 381114, (50, 'species group'): 10188, (36, 'genus'): 2194804,
        (32, 'species group'): 45159, (6, 'species group'): 23939, (11, 'genus'): 19053818,
        (29, 'subclass'): 1202, (35, 'species'): 5670917, (49, 'subphylum'): 73,
        (21, 'subphylum'): 6410, (46, 'family'): 74544, (11, 'subkingdom'): 3615,
        (28, 'parvorder'): 6175, (39, 'order'): 103839, (36, 'phylum'): 248347,
        (44, 'species group'): 15379, (35, 'superkingdom'): 89416, (32, 'class'): 184614,
        (9, 'infraorder'): 27894, (16, 'subgenus'): 105478, (23, 'infraorder'): 4667,
        (9, 'family'): 3061698, (48, 'suborder'): 1045, (33, 'infraorder'): 1763,
        (33, 'varietas'): 41632, (43, 'infraclass'): 2643, (22, 'order'): 578754,
        (15, 'subgenus'): 118999, (40, 'genus'): 1519665, (30, 'parvorder'): 5109,
        (44, 'species subgroup'): 1167, (39, 'subfamily'): 8836, (29, 'genus'): 4362676,
        (30, 'genus'): 4003600, (41, 'subspecies'): 60336, (31, 'subtribe'): 3043,
        (46, 'species group'): 13533, (40, 'forma'): 5173, (40, 'tribe'): 4658,
        (48, 'species'): 1880226, (45, 'phylum'): 103868, (6, 'superkingdom'): 1252496,
        (14, 'family'): 1860305, (22, 'varietas'): 110365, (38, 'forma'): 6323,
        (31, 'no rank'): 124796, (13, 'phylum'): 2644037, (40, 'subfamily'): 9025,
        (43, 'class'): 58849, (37, 'species'): 4695279, (41, 'tribe'): 4240,
        (25, 'order'): 435200, (34, 'class'): 148264, (13, 'no rank'): 751748,
        (6, 'class'): 150147, (21, 'subfamily'): 54328, (17, 'superkingdom'): 614444,
        (21, 'species'): 19886105, (33, 'subgenus'): 19328, (26, 'no rank'): 208504,
        (18, 'infraclass'): 44052, (48, 'superfamily'): 357, (37, 'species subgroup'): 2359,
        (35, 'phylum'): 275981, (36, 'species group'): 31646, (10, 'kingdom'): 49628,
        (35, 'subspecies'): 97632, (8, 'infraclass'): 153408, (38, 'kingdom'): 2377,
        (13, 'superkingdom'): 998844, (21, 'subkingdom'): 240, (28, 'species group'): 67061,
        (35, 'no rank'): 81841, (22, 'superfamily'): 5948, (12, 'superfamily'): 20277,
        (18, 'subtribe'): 10623, (44, 'subphylum'): 147, (27, 'parvorder'): 6924,
        (28, 'suborder'): 8765, (35, 'forma'): 8311, (23, 'superfamily'): 4949,
        (37, 'subphylum'): 459, (18, 'order'): 825326, (30, 'subphylum'): 1388,
        (16, 'superclass'): 6406, (18, 'subkingdom'): 567, (24, 'superkingdom'): 295845,
        (43, 'family'): 96473, (35, 'superorder'): 1668, (35, 'infraorder'): 1217,
        (26, 'subtribe'): 5095, (13, 'superfamily'): 17457, (49, 'class'): 36452,
        (28, 'order'): 316851, (21, 'tribe'): 32020, (17, 'kingdom'): 18447,
        (28, 'infraclass'): 14925, (16, 'species'): 29616524, (38, 'superclass'): 344,
        (47, 'tribe'): 2234, (49, 'superfamily'): 268, (7, 'superorder'): 18669,
        (33, 'family'): 274500, (14, 'suborder'): 39088, (13, 'infraorder'): 15969,
        (45, 'varietas'): 14804, (33, 'species'): 6890812, (6, 'order'): 98855,
        (11, 'subtribe'): 21268, (34, 'subspecies'): 106370, (12, 'superclass'): 11830,
        (16, 'subtribe'): 13205, (24, 'phylum'): 899248, (18, 'species subgroup'): 14161,
        (50, 'subfamily'): 3060, (24, 'genus'): 6710330, (37, 'species group'): 28462,
        (7, 'genus'): 5301205, (5, 'subclass'): 456, (34, 'kingdom'): 3700,
        (47, 'order'): 50996, (14, 'kingdom'): 26378, (15, 'parvorder'): 21975,
        (12, 'infraclass'): 94728, (50, 'subspecies'): 29640, (5, 'forma'): 395,
        (8, 'subphylum'): 113155, (42, 'species subgroup'): 1580, (7, 'species subgroup'): 14914,
        (27, 'superkingdom'): 216885, (38, 'subgenus'): 11411, (20, 'subgenus'): 71626,
        (43, 'subgenus'): 7028, (17, 'species subgroup'): 15350, (41, 'forma'): 4822,
        (25, 'superorder'): 5040, (25, 'varietas'): 86566, (47, 'subkingdom'): 5,
        (45, 'superorder'): 543, (32, 'forma'): 10398, (7, 'subgenus'): 96885,
        (22, 'species group'): 110169, (42, 'genus'): 1293216, (43, 'genus'): 1158633,
        (5, 'kingdom'): 6884, (44, 'species'): 2551254, (13, 'species subgroup'): 22774,
        (17, 'genus'): 11649368, (7, 'subtribe'): 13575, (39, 'species subgroup'): 1996,
        (17, 'parvorder'): 17203, (45, 'suborder'): 1364, (19, 'parvorder'): 14209,
        (31, 'class'): 205647, (24, 'order'): 474056, (23, 'infraclass'): 24893,
        (6, 'family'): 141778, (14, 'varietas'): 215245, (9, 'suborder'): 72358,
        (33, 'infraclass'): 8666, (23, 'class'): 470152, (47, 'kingdom'): 1180,
        (30, 'tribe'): 12855, (19, 'superorder'): 9515, (32, 'species subgroup'): 3821,
        (14, 'subspecies'): 543658, (10, 'subspecies'): 749734, (16, 'varietas'): 180083,
        (34, 'subfamily'): 15084, (14, 'class'): 1166981, (10, 'no rank'): 1093587,
        (28, 'superclass'): 1339, (46, 'subtribe'): 708, (18, 'suborder'): 24416,
        (29, 'species group'): 62747, (8, 'superfamily'): 31062, (25, 'subgenus'): 43618,
        (15, 'subkingdom'): 1156, (8, 'tribe'): 113425, (45, 'subgenus'): 5924,
        (24, 'infraclass'): 22942, (5, 'subkingdom'): 1178, (50, 'subgenus'): 3881,
        (34, 'tribe'): 8476, (43, 'order'): 70216, (25, 'subspecies'): 230778,
        (9, 'superfamily'): 30740, (37, 'subspecies'): 81473, (5, 'superkingdom'): 343456,
        (34, 'superfamily'): 1463, (48, 'infraclass'): 1444, (10, 'subfamily'): 175681,
        (12, 'infraorder'): 18441, (24, 'superfamily'): 4596, (17, 'phylum'): 1755009,
        (21, 'subspecies'): 316295, (6, 'infraorder'): 2625, (36, 'infraorder'): 1204,
        (21, 'suborder'): 18023, (34, 'no rank'): 91295, (30, 'species'): 9210440,
        (32, 'parvorder'): 4119, (45, 'tribe'): 2665, (16, 'superkingdom'): 690439,
        (27, 'superorder'): 4402, (48, 'family'): 63930, (35, 'family'): 220810,
        (32, 'subgenus'): 21613, (41, 'parvorder'): 2005, (25, 'superclass'): 1987,
        (47, 'superorder'): 406, (50, 'superclass'): 79, (45, 'kingdom'): 1340,
        (6, 'phylum'): 232240, (48, 'subtribe'): 564, (6, 'species'): 1837805,
        (38, 'subtribe'): 1551, (46, 'phylum'): 96561, (12, 'subphylum'): 35708,
        (50, 'superorder'): 322, (15, 'subclass'): 10670, (25, 'family'): 636691,
        (16, 'no rank'): 549989, (39, 'species group'): 23819, (20, 'subclass'): 4618,
        (45, 'family'): 79936, (50, 'family'): 56531, (29, 'superfamily'): 2705,
        (45, 'order'): 58805, (5, 'varietas'): 2096, (38, 'subspecies'): 74914,
        (28, 'subtribe'): 4161, (7, 'forma'): 15167, (26, 'parvorder'): 7185,
        (9, 'subphylum'): 74069, (42, 'subclass'): 186, (48, 'infraorder'): 293,
        (47, 'species group'): 12452, (50, 'no rank'): 22532, (13, 'subclass'): 15158,
        (46, 'subphylum'): 108, (43, 'forma'): 4164, (49, 'superclass'): 87,
        (27, 'varietas'): 73953, (15, 'tribe'): 59496, (10, 'superclass'): 16148,
        (40, 'superfamily'): 1112, (18, 'phylum'): 1571966, (25, 'tribe'): 21048,
        (49, 'subspecies'): 32111, (30, 'subgenus'): 26833, (42, 'species'): 3048136,
        (30, 'suborder'): 7145, (35, 'subgenus'): 15799, (42, 'class'): 65916,
        (9, 'tribe'): 113569, (20, 'subspecies'): 340582, (49, 'varietas'): 10884,
        (50, 'parvorder'): 806, (29, 'class'): 252820, (38, 'order'): 112821,
        (33, 'superclass'): 695, (26, 'species'): 13104820, (46, 'parvorder'): 1061,
        (21, 'class'): 578328, (12, 'varietas'): 258875, (45, 'genus'): 985786,
        (46, 'genus'): 923588, (9, 'forma'): 68676, (14, 'tribe'): 66156,
        (24, 'forma'): 20758, (32, 'superorder'): 2679, (20, 'no rank'): 376001,
        (41, 'species group'): 19888, (47, 'phylum'): 88394, (48, 'varietas'): 11267,
        (19, 'subphylum'): 8700, (38, 'varietas'): 27279, (22, 'forma'): 24399,
        (12, 'subfamily'): 141015, (11, 'superorder'): 26490, (26, 'superkingdom'): 241000,
        (10, 'subtribe'): 22954, (39, 'parvorder'): 1999, (41, 'order'): 85425,
        (50, 'class'): 34630, (50, 'infraorder'): 297, (6, 'subphylum'): 20963,
        (5, 'order'): 17866, (17, 'subgenus'): 95364, (26, 'species group'): 79450,
        (23, 'phylum'): 988587, (37, 'subgenus'): 12831, (46, 'tribe'): 2490,
        (42, 'subgenus'): 7790, (12, 'genus'): 17508168, (50, 'infraclass'): 1230,
        (23, 'suborder'): 14332, (16, 'class'): 944926, (35, 'species group'): 34791,
        (7, 'parvorder'): 25185, (7, 'subkingdom'): 56203, (45, 'subclass'): 136,
        (9, 'subkingdom'): 12531, (8, 'class'): 2132202, (44, 'infraclass'): 2273,
        (46, 'subclass'): 103, (43, 'parvorder'): 1541, (9, 'phylum'): 4061150,
        (39, 'subkingdom'): 9, (40, 'species group'): 22020, (9, 'subspecies'): 775720,
        (46, 'subkingdom'): 4, (34, 'order'): 170872, (25, 'subkingdom'): 141,
        (44, 'infraorder'): 435, (32, 'subspecies'): 128299, (15, 'superfamily'): 13339,
        (45, 'forma'): 3448, (45, 'species group'): 14547, (8, 'superkingdom'): 5742159,
        (19, 'subgenus'): 78337, (27, 'family'): 521324, (24, 'subgenus'): 48403,
        (17, 'no rank'): 502448, (28, 'forma'): 14650, (47, 'family'): 69971,
        (39, 'superorder'): 958, (28, 'tribe'): 15570, (31, 'superfamily'): 1917,
        (5, 'genus'): 134227, (6, 'genus'): 823472, (40, 'subtribe'): 1224,
        (11, 'parvorder'): 34256, (19, 'subclass'): 5343, (30, 'subtribe'): 3553,
        (27, 'kingdom'): 6865, (20, 'subphylum'): 7586, (19, 'species group'): 135434,
        (17, 'family'): 1372630, (20, 'suborder'): 20091, (18, 'forma'): 33999,
        (37, 'family'): 176830, (9, 'superclass'): 19794, (42, 'family'): 108939,
        (35, 'superclass'): 520, (37, 'subclass'): 390, (31, 'subfamily'): 20079,
        (32, 'infraclass'): 9290, (6, 'subfamily'): 9572, (35, 'subphylum'): 579,
        (23, 'family'): 770194, (35, 'subclass'): 452, (37, 'no rank'): 67644,
        (35, 'infraclass'): 6509, (46, 'kingdom'): 1168, (18, 'kingdom'): 16286,
        (41, 'superclass'): 290, (16, 'infraclass'): 57198, (29, 'parvorder'): 5710,
        (45, 'superclass'): 170, (8, 'kingdom'): 138088, (10, 'phylum'): 3702301,
        (38, 'species subgroup'): 2130, (23, 'no rank'): 280885, (11, 'order'): 1709818,
        (22, 'subgenus'): 58178, (15, 'species'): 32128801, (27, 'subgenus'): 36238,
        (50, 'superkingdom'): 24507, (50, 'species subgroup'): 767, (48, 'superkingdom'): 26489,
        (25, 'forma'): 19303, (40, 'subclass'): 247, (43, 'species group'): 16864,
        (41, 'varietas'): 20800, (7, 'infraorder'): 17380, (8, 'subspecies'): 660638,
        (28, 'varietas'): 66272, (13, 'suborder'): 44851, (17, 'infraorder'): 9399,
        (35, 'subfamily'): 13584, (8, 'forma'): 56899, (43, 'infraorder'): 570,
        (8, 'parvorder'): 42768, (33, 'genus'): 2974719, (15, 'kingdom'): 23885,
        (9, 'species subgroup'): 32857, (13, 'infraclass'): 83025, (33, 'parvorder'): 3851,
        (48, 'species subgroup'): 932, (40, 'varietas'): 22591, (35, 'species subgroup'): 2863,
        (40, 'order'): 93259, (23, 'species group'): 100385, (28, 'subfamily'): 27230,
        (30, 'varietas'): 56540, (47, 'infraorder'): 385, (49, 'infraclass'): 1448,
        (39, 'class'): 88103, (31, 'kingdom'): 4672, (40, 'subspecies'): 64156,
        (20, 'subfamily'): 59861, (13, 'subkingdom'): 1829, (36, 'species'): 5163439,
        (18, 'superkingdom'): 542230, (27, 'subphylum'): 2541, (49, 'subtribe'): 552,
        (29, 'phylum'): 530923, (11, 'infraorder'): 21283, (45, 'subphylum'): 169,
        (19, 'subspecies'): 363067, (30, 'class'): 230020, (29, 'subkingdom'): 85,
        (26, 'infraorder'): 3234, (32, 'subkingdom'): 40, (14, 'subphylum'): 22342,
        (22, 'class'): 522506, (18, 'parvorder'): 15637, (36, 'superclass'): 446,
        (15, 'phylum'): 2138954, (29, 'subgenus'): 29320, (34, 'superorder'): 1924,
        (18, 'tribe'): 43094, (27, 'species'): 12051451, (15, 'genus'): 13615184,
        (32, 'kingdom'): 4319, (24, 'class'): 426957, (14, 'infraclass'): 72101,
        (12, 'kingdom'): 35871, (5, 'no rank'): 461398, (23, 'order'): 522055,
        (28, 'species subgroup'): 5672, (26, 'superfamily'): 3643, (30, 'no rank'): 138361,
        (6, 'superfamily'): 1412, (29, 'forma'): 13860, (20, 'infraorder'): 6622,
        (30, 'subclass'): 969, (5, 'species group'): 4390, (28, 'subkingdom'): 66,
        (17, 'superorder'): 12351, (7, 'superfamily'): 13576, (42, 'superfamily'): 657,
        (12, 'forma'): 56682, (38, 'parvorder'): 2300, (11, 'subgenus'): 185547,
        (19, 'varietas'): 143393, (44, 'genus'): 1077255, (22, 'suborder'): 15930,
        (39, 'family'): 146358, (36, 'subgenus'): 14242, (18, 'genus'): 10696488,
        (48, 'forma'): 2789, (41, 'species subgroup'): 1597, (30, 'phylum'): 480288,
        (17, 'superclass'): 5509, (47, 'subphylum'): 90, (23, 'subfamily'): 43875,
        (12, 'species'): 41770490, (32, 'species'): 7545753, (8, 'subfamily'): 188932,
        (39, 'no rank'): 55522, (30, 'kingdom'): 5203, (29, 'family'): 418042,
        (42, 'superorder'): 756, (34, 'family'): 247078, (29, 'species'): 10013400,
        (35, 'suborder'): 4036, (41, 'subtribe'): 1141, (22, 'species subgroup'): 9915,
        (37, 'varietas'): 29230, (14, 'subfamily'): 111562, (7, 'varietas'): 79138,
        (19, 'forma'): 31644, (23, 'superkingdom'): 328522, (18, 'species group'): 146376,
        (17, 'subphylum'): 13395, (8, 'subtribe'): 24785, (27, 'forma'): 16466,
        (43, 'varietas'): 17451, (42, 'infraclass'): 2963, (36, 'kingdom'): 3157,
        (32, 'tribe'): 10456, (27, 'subspecies'): 198837, (15, 'family'): 1673387,
        (39, 'subspecies'): 67992, (10, 'infraorder'): 24873, (36, 'superorder'): 1555,
        (14, 'subgenus'): 131980, (35, 'tribe'): 7548, (24, 'superorder'): 5704,
        (24, 'subphylum'): 3873, (31, 'subphylum'): 1160, (35, 'subkingdom'): 15,
        (39, 'subgenus'): 10846, (44, 'subgenus'): 6519, (45, 'class'): 49247,
        (9, 'superorder'): 33470, (31, 'subclass'): 844, (45, 'species subgroup'): 1178,
        (34, 'suborder'): 4725, (42, 'parvorder'): 1610, (37, 'class'): 107003,
        (46, 'suborder'): 1251, (30, 'species group'): 56669,
        (19, 'infraclass'): 39054, (40, 'subkingdom'): 10, (6, 'subclass'): 2958,
        (50, 'subphylum'): 87, (16, 'subfamily'): 91082, (47, 'class'): 42054,
        (8, 'species'): 41487743, (39, 'superfamily'): 1030, (42, 'subspecies'): 54828,
        (10, 'superkingdom'): 1606305, (11, 'species group'): 260873, (48, 'subfamily'): 3443,
        (12, 'suborder'): 50249, (21, 'phylum'): 1212509, (46, 'no rank'): 29918,
        (25, 'species'): 14322551, (26, 'subspecies'): 212714, (34, 'infraorder'): 1427,
        (32, 'varietas'): 46456, (44, 'subclass'): 93, (21, 'order'): 637169,
        (28, 'superfamily'): 2946, (8, 'varietas'): 268297, (28, 'genus'): 4725542,
        (6, 'superorder'): 3035, (25, 'suborder'): 11778, (23, 'parvorder'): 9795,
        (29, 'subfamily'): 24952, (44, 'superfamily'): 466, (14, 'superfamily'): 15267,
        (13, 'forma'): 51781, (18, 'superfamily'): 8682, (5, 'species'): 291809,
        (43, 'superorder'): 643, (49, 'tribe'): 1908, (16, 'subkingdom'): 839,
        (37, 'superorder'): 1325, (49, 'forma'): 2570, (38, 'subkingdom'): 14,
        (50, 'order'): 41473, (33, 'phylum'): 349134, (50, 'varietas'): 9756,
        (9, 'parvorder'): 42549, (33, 'subkingdom'): 28, (49, 'subclass'): 59,
        (14, 'order'): 1240389, (8, 'subgenus'): 217757, (47, 'genus'): 859220,
        (31, 'family'): 340934, (28, 'subgenus'): 32431, (12, 'tribe'): 83423,
        (31, 'forma'): 11509, (32, 'subclass'): 739, (21, 'genus'): 8592851,
        (22, 'genus'): 7967261, (31, 'infraclass'): 10754, (38, 'tribe'): 5498,
        (31, 'superorder'): 2560, (6, 'species subgroup'): 1935, (11, 'suborder'): 57487,
        (19, 'subfamily'): 65813, (48, 'tribe'): 1974, (39, 'varietas'): 24195,
        (26, 'suborder'): 10611, (13, 'varietas'): 235466, (21, 'family'): 937456,
        (28, 'subphylum'): 2066, (26, 'family'): 569943, (33, 'superorder'): 2263,
        (6, 'subspecies'): 45046, (33, 'superfamily'): 1824, (46, 'subgenus'): 5394,
        (27, 'subfamily'): 31140, (46, 'superorder'): 439, (17, 'order'): 917348,
        (7, 'family'): 1012841, (15, 'superkingdom'): 771621, (5, 'subphylum'): 3596,
        (25, 'subphylum'): 3431, (42, 'superclass'): 190, (37, 'infraclass'): 5316,
        (13, 'species'): 38136242, (27, 'superclass'): 1561, (31, 'superclass'): 912,
        (48, 'superclass'): 113, (38, 'subclass'): 285, (29, 'subspecies'): 166269,
        (6, 'infraclass'): 19717, (45, 'subfamily'): 4974, (46, 'superkingdom'): 30468,
        (23, 'species subgroup'): 9214, (32, 'suborder'): 5910, (26, 'superclass'): 1746,
        (34, 'phylum'): 309229, (47, 'parvorder'): 919, (20, 'superfamily'): 7032,
        (44, 'kingdom'): 1516, (31, 'subgenus'): 23904, (13, 'subphylum'): 28296,
        (12, 'subkingdom'): 2690, (47, 'superkingdom'): 29268, (39, 'subclass'): 279,
        (31, 'suborder'): 6143, (22, 'species'): 18370547, (36, 'no rank'): 74524,
        (27, 'infraorder'): 3198, (10, 'order'): 1881199, (49, 'genus'): 752733,
        (19, 'subkingdom'): 464, (43, 'subtribe'): 937, (49, 'parvorder'): 798,
        (33, 'species group'): 42039, (9, 'kingdom'): 68211, (38, 'species group'): 26249,
        (47, 'subclass'): 112, (31, 'genus'): 3601836, (41, 'no rank'): 45715,
        (39, 'infraorder'): 800, (24, 'subfamily'): 40393, (43, 'species subgroup'): 1352,
        (9, 'infraclass'): 141939, (36, 'subfamily'): 13085, (20, 'order'): 699635,
        (29, 'tribe'): 14511, (25, 'kingdom'): 8530, (6, 'forma'): 2020,
        (39, 'infraclass'): 4069, (11, 'subfamily'): 158277, (11, 'subclass'): 22341,
        (27, 'suborder'): 10140, (42, 'forma'): 4359, (24, 'varietas'): 93993,
        (30, 'subspecies'): 153023, (14, 'superorder'): 17556, (34, 'parvorder'): 3422,
        (36, 'species subgroup'): 2706, (8, 'subkingdom'): 47617, (22, 'subphylum'): 5353,
        (29, 'superkingdom'): 171372, (44, 'superorder'): 609, (32, 'family'): 303727,
        (16, 'genus'): 12593648, (16, 'kingdom'): 20828, (40, 'class'): 79131,
        (30, 'infraclass'): 11862, (50, 'subclass'): 77, (14, 'subclass'): 12468,
        (30, 'superkingdom'): 155078, (17, 'subfamily'): 81141, (12, 'species subgroup'): 25082,
        (22, 'kingdom'): 11352, (36, 'subtribe'): 1739, (24, 'species subgroup'): 8417,
        (9, 'superkingdom'): 2377381, (19, 'family'): 1114256, (24, 'subkingdom'): 131,
        (19, 'species'): 23057973, (5, 'superfamily'): 247, (18, 'subclass'): 6248,
        (25, 'phylum'): 817102, (42, 'varietas'): 18623, (44, 'family'): 88833,
        (19, 'superfamily'): 8058, (5, 'tribe'): 1145, (25, 'subclass'): 2189,
        (40, 'parvorder'): 1941, (38, 'suborder'): 2853, (46, 'species subgroup'): 1017,
        (14, 'no rank'): 676044, (34, 'genus'): 2685360, (35, 'genus'): 2433725,
        (13, 'kingdom'): 30271, (36, 'superkingdom'): 80462, (11, 'infraclass'): 108744,
        (8, 'subclass'): 36653, (35, 'superfamily'): 1315, (9, 'genus'): 20954216,
        (14, 'phylum'): 2372338, (31, 'varietas'): 50123, (49, 'kingdom'): 841,
        (16, 'order'): 1012613, (30, 'subkingdom'): 34, (29, 'kingdom'): 5828,
        (27, 'phylum'): 662099, (13, 'family'): 2064586, (42, 'subphylum'): 190,
        (18, 'family'): 1232070, (43, 'superfamily'): 598, (44, 'varietas'): 15857,
        (22, 'subtribe'): 7383, (22, 'subclass'): 3419, (25, 'infraorder'): 3851,
        (37, 'infraorder'): 1100, (24, 'species group'): 92416, (30, 'subfamily'): 22216,
        (47, 'subfamily'): 4135, (24, 'infraorder'): 4295, (7, 'superkingdom'): 6826769,
        (47, 'no rank'): 28233, (22, 'subfamily'): 50300, (23, 'subkingdom'): 207,
        (15, 'superclass'): 7695, (12, 'subtribe'): 19331, (43, 'superclass'): 207,
        (16, 'tribe'): 53125, (41, 'superfamily'): 1159, (47, 'species'): 2031010,
        (17, 'suborder'): 27470, (46, 'species'): 2184632, (42, 'tribe'): 3662,
        (35, 'order'): 151785, (17, 'subspecies'): 425738, (26, 'subkingdom'): 95,
        (42, 'suborder'): 1886, (26, 'phylum'): 737446, (7, 'no rank'): 7686266,
        (27, 'subkingdom'): 93, (28, 'superorder'): 3707, (48, 'species group'): 11370,
        (40, 'superkingdom'): 54068, (39, 'superkingdom'): 61185, (21, 'superclass'): 3309,
        (39, 'subphylum'): 345, (29, 'species subgroup'): 5375, (43, 'no rank'): 38317,
        (37, 'subfamily'): 10577, (13, 'subspecies'): 593617, (24, 'subspecies'): 249018,
        (37, 'parvorder'): 2578, (36, 'subspecies'): 89241, (20, 'varietas'): 130855,
        (10, 'subphylum'): 55236, (9, 'species group'): 294216, (36, 'forma'): 7305,
        (11, 'phylum'): 3338760, (19, 'phylum'): 1438254, (44, 'subkingdom'): 2,
        (44, 'forma'): 3787, (7, 'subclass'): 21579, (5, 'superorder'): 399,
        (46, 'varietas'): 13162, (11, 'no rank'): 950505, (18, 'class'): 756686,
        (11, 'class'): 1662776, (45, 'subtribe'): 796, (50, 'subtribe'): 502,
        (24, 'no rank'): 254040, (31, 'phylum'): 429750, (42, 'infraorder'): 580,
        (21, 'parvorder'): 11634, (37, 'order'): 124813, (46, 'class'): 45608,
        (44, 'superclass'): 173, (31, 'tribe'): 11426, (15, 'forma'): 43247,
        (50, 'kingdom'): 869, (24, 'family'): 692936, (41, 'suborder'): 2225,
        (19, 'genus'): 9905228, (22, 'phylum'): 1102902, (42, 'species group'): 18210,
        (25, 'subfamily'): 36387, (18, 'varietas'): 154586, (6, 'superclass'): 4141,
        (23, 'tribe'): 25769, (42, 'subkingdom'): 13, (18, 'superclass'): 4592,
        (46, 'superfamily'): 381, (33, 'tribe'): 9575, (10, 'superfamily'): 27228,
        (33, 'forma'): 9769, (13, 'subtribe'): 17342, (19, 'species subgroup'): 12793,
        (36, 'subclass'): 422, (44, 'subfamily'): 5173, (48, 'subgenus'): 4518,
        (12, 'subspecies'): 644231, (11, 'superfamily'): 23651, (17, 'subkingdom'): 648,
        (33, 'subclass'): 771, (30, 'infraorder'): 2246, (12, 'phylum'): 2981669,
        (28, 'infraorder'): 2793, (18, 'species'): 24978869, (12, 'subgenus'): 164255,
        (37, 'genus'): 1997769, (38, 'genus'): 1822460, (22, 'tribe'): 28867,
        (36, 'suborder'): 3688, (49, 'species group'): 10742, (31, 'subkingdom'): 33,
        (38, 'superkingdom'): 63535, (20, 'superorder'): 8619, (28, 'species'): 10890513,
        (7, 'subfamily'): 83858, (10, 'family'): 2842870, (14, 'subtribe'): 15483,
        (36, 'subphylum'): 582, (31, 'species'): 8315361, (7, 'infraclass'): 103506,
        (30, 'order'): 260412, (23, 'subspecies'): 268825, (25, 'superfamily'): 4108,
        (33, 'order'): 189933, (5, 'superclass'): 619, (32, 'infraorder'): 1902,
        (44, 'suborder'): 1475, (46, 'infraclass'): 1958, (23, 'varietas'): 100663,
        (46, 'forma'): 3192, (48, 'superorder'): 359, (18, 'no rank'): 449066,
        (33, 'subphylum'): 874, (36, 'subkingdom'): 21, (19, 'superclass'): 4163,
        (48, 'genus'): 797104, (12, 'superorder'): 22430, (6, 'no rank'): 2089731,
        (8, 'infraorder'): 29630, (35, 'varietas'): 35496, (20, 'species group'): 127031,
        (9, 'varietas'): 314066, (31, 'superkingdom'): 139525, (18, 'superorder'): 10519,
        (13, 'class'): 1304369, (29, 'subtribe'): 3945, (47, 'suborder'): 1130,
        (32, 'superclass'): 825, (40, 'no rank'): 50265, (17, 'class'): 849469,
        (26, 'order'): 391881, (28, 'superkingdom'): 191316, (8, 'superclass'): 22234,
        (26, 'species subgroup'): 6876, (9, 'class'): 2088735, (38, 'no rank'): 60741,
        (40, 'species'): 3609458, (7, 'species group'): 130892, (33, 'kingdom'): 3925,
        (25, 'no rank'): 232973, (40, 'family'): 132312, (27, 'species subgroup'): 6367,
        (19, 'tribe'): 38895, (48, 'phylum'): 82260, (27, 'class'): 316681,
        (36, 'order'): 137123, (13, 'tribe'): 74057, (32, 'subfamily'): 18411,
        (26, 'subclass'): 1743, (24, 'species'): 15484203, (8, 'no rank'): 4920267,
        (7, 'subphylum'): 102611, (19, 'class'): 686362, (35, 'kingdom'): 3297,
        (45, 'subkingdom'): 1, (40, 'superclass'): 291, (11, 'subphylum'): 44726,
        (43, 'suborder'): 1724, (26, 'forma'): 17464, (32, 'no rank'): 112053,
        (43, 'subphylum'): 191, (43, 'tribe'): 3397, (33, 'subtribe'): 2518,
        (49, 'species'): 1766246, (13, 'superclass'): 10070, (18, 'infraorder'): 8299,
        (23, 'subtribe'): 6777, (32, 'superfamily'): 1976, (11, 'family'): 2587333,
        (16, 'subphylum'): 15280, (16, 'family'): 1512289, (32, 'genus'): 3246236,
        (7, 'superclass'): 16158, (36, 'family'): 199058, (26, 'kingdom'): 7496,
        (49, 'superkingdom'): 24161, (48, 'class'): 39146, (6, 'kingdom'): 29807,
        (31, 'subspecies'): 139326, (43, 'species'): 2767119, (8, 'species subgroup'): 32008,
        (47, 'subgenus'): 4945, (37, 'superkingdom'): 70957, (38, 'superfamily'): 920,
        (9, 'subgenus'): 222914, (12, 'class'): 1481839, (20, 'parvorder'): 12893,
        (10, 'species group'): 278557, (34, 'subgenus'): 17686, (40, 'subgenus'): 10008,
        (39, 'superclass'): 334, (38, 'infraorder'): 906, (5, 'subtribe'): 389,
        (40, 'suborder'): 2493, (30, 'species subgroup'): 4854, (14, 'species group'): 200674,
        (50, 'genus'): 708750, (48, 'kingdom'): 946, (20, 'superkingdom'): 448978,
        (40, 'species subgroup'): 1884, (5, 'family'): 24869, (40, 'phylum'): 162799,
        (25, 'genus'): 6239712, (23, 'kingdom'): 9950, (46, 'order'): 54299,
        (44, 'subspecies'): 45462, (37, 'suborder'): 3349, (14, 'superclass'): 8392,
        (27, 'superfamily'): 3567, (15, 'infraclass'): 64839, (32, 'order'): 209146,
        (22, 'superclass'): 2718, (20, 'subtribe'): 8708, (41, 'subphylum'): 232,
        (15, 'subfamily'): 102096, (25, 'infraclass'): 20718, (39, 'kingdom'): 2239,
        (24, 'parvorder'): 8948, (15, 'subphylum'): 19582, (6, 'subtribe'): 1987,
        (30, 'forma'): 13023, (36, 'superfamily'): 1321, (17, 'superfamily'): 10327,
        (44, 'class'): 54699, (11, 'subspecies'): 700804, (13, 'parvorder'): 27026,
        (45, 'species'): 2345201, (29, 'subphylum'): 1641, (38, 'subfamily'): 9867,
        (15, 'varietas'): 197921, (16, 'phylum'): 1940939, (5, 'phylum'): 59632,
        (21, 'species group'): 116981, (7, 'subspecies'): 219886, (39, 'forma'): 5771,
        (49, 'subfamily'): 3295, (33, 'suborder'): 5364, (12, 'subclass'): 18584,
        (26, 'tribe'): 19162, (34, 'superkingdom'): 99848, (29, 'suborder'): 7765,
        (8, 'superorder'): 33316, (22, 'infraclass'): 27935, (20, 'kingdom'): 13518,
        (43, 'subspecies'): 49481, (15, 'order'): 1115578, (50, 'tribe'): 1694,
        (15, 'species subgroup'): 18893, (27, 'no rank'): 190091, (27, 'order'): 354034,
        (25, 'species subgroup'): 7649, (22, 'subkingdom'): 209, (43, 'subfamily'): 5849,
        (25, 'class'): 388899, (42, 'kingdom'): 1634, (17, 'varietas'): 169585,
        (49, 'species subgroup'): 798, (36, 'varietas'): 31901, (6, 'subgenus'): 9625,
        (9, 'no rank'): 1622140, (20, 'forma'): 29152, (41, 'infraorder'): 818,
        (13, 'superorder'): 20057, (18, 'subphylum'): 10291, (11, 'kingdom'): 42107,
        (21, 'species subgroup'): 11107, (10, 'subclass'): 26671, (10, 'genus'): 20284416,
        (35, 'subtribe'): 2172, (47, 'species subgroup'): 973, (44, 'order'): 64404,
        (16, 'superorder'): 13746, (27, 'subclass'): 1680, (34, 'subclass'): 549,
        (9, 'subtribe'): 24681, (34, 'species subgroup'): 3203, (29, 'infraclass'): 13377,
        (10, 'forma'): 65744, (6, 'varietas'): 11872, (34, 'subtribe'): 2306,
        (15, 'no rank'): 607692, (31, 'species group'): 51413, (38, 'family'): 159316,
        (6, 'suborder'): 3650, (25, 'subtribe'): 5635, (23, 'subclass'): 2898,
        (37, 'phylum'): 224534, (41, 'species'): 3306841, (15, 'subtribe'): 14377,
        (46, 'subspecies'): 39955, (6, 'subkingdom'): 5512, (38, 'superorder'): 1138,
        (5, 'subfamily'): 1789, (8, 'family'): 2766417, (10, 'class'): 1858940,
        (28, 'family'): 462942, (41, 'superkingdom'): 47676, (11, 'species subgroup'): 27926,
        (45, 'no rank'): 31775, (19, 'suborder'): 21755, (7, 'tribe'): 52668,
        (28, 'class'): 280826, (33, 'subfamily'): 17265, (34, 'subkingdom'): 36,
        (17, 'tribe'): 47771, (20, 'class'): 634444, (12, 'species group'): 238246,
        (21, 'subgenus'): 64522, (9, 'subfamily'): 193505, (26, 'subgenus'): 39380,
        (16, 'subclass'): 8874, (39, 'suborder'): 2465, (50, 'subkingdom'): 2,
        (14, 'infraorder'): 13839, (14, 'species'): 35037255, (23, 'subphylum'): 4436,
        (49, 'phylum'): 78321, (47, 'forma'): 2929, (12, 'superkingdom'): 1159432,
        (47, 'infraclass'): 1778, (6, 'tribe'): 6186, (34, 'species group'): 37925,
        (16, 'forma'): 40473, (49, 'no rank'): 23909, (47, 'varietas'): 11919,
        (21, 'varietas'): 120052}