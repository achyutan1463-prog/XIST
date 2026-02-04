import numpy as np
import random
import matplotlib.pyplot as plt
no_intermediates = 10
all_allelicstates = []
j = 0
p=[0.0034006,0.82941,0.045608,0.19975,0.28022,2.58,3.5419,0.00074566,3.2904,1.0,2.4871,0.94048,2.9386,0.029961,0.00016983,3.2201,1.0,4.2752,2.8675,1.8392,1.0479,0.0012648,2.5819,1.0,4.06,4.996,2.3672,0.07807,0.031208,2.5765,1.0,1.0862
,0.00038566,0.038948,0.96874,0.0022941,4.0339,1.3746,0.80708,0.22018,2.9569,1.0,1.8739,2.925,2.9003,0.054618,0.00019123,2.4832,1.0,4.1802,2.4563,2.3781,0.41115,0.055927,1.1593,1.0,0.76152,1.4668,2.9215,4.8126,0.032447,0.9969,1.0,0.53676
,0.076184,0.66914,0.99516,0.0019673,4.7125,2.915,1.3816,0.00182,0.3292,1.0,1.8873,0.46413,2.9273,0.10517,0.00015908,3.0282,1.0,1.2153,0.07662,2.4736,0.023804,0.017744,0.2698,1.0,3.3137,0.13458,1.6572,9.2765,0.10602,0.34365,1.0,3.7981
,0.0064592,0.00026252,0.52835,0.00029374,4.4898,2.1855,2.9402,0.00019543,2.1407,1.0,4.6131,0.46672,2.0356,0.040103,0.0018612,3.1819,1.0,3.8855,0.003868,1.0622,0.015512,0.0016993,2.4869,1.0,0.34327,0.003778,1.7797,0.032818,0.0013746,2.4486,1.0,2.6645
,0.12854,0.025593,0.99629,0.00010645,4.7723,1.3102,0.12866,0.047328,2.2626,1.0,1.5631,0.45471,1.6262,0.019224,0.002614,3.1851,1.0,2.7976,0.69982,2.5793,3.2112,0.0056397,0.41133,1.0,4.3889,0.23302,1.9781,1.7246,0.066985,2.38,1.0,2.1825
,0.00011282,0.090422,0.001228,0.067874,0.36887,2.9331,4.8301,0.00030314,2.8131,1.0,2.0434,0.29377,1.6248,0.032295,0.00063707,2.2513,1.0,2.2935,0.32821,2.3857,0.011316,0.076359,0.34156,1.0,2.8856,0.10909,2.9851,0.076243,0.0046436,2.4191,1.0,4.94
,0.060521,1.0663,0.042604,0.0092316,2.1354,2.1642,6.0612,0.0023758,2.1696,1.0,4.1204,0.58337,2.185,0.01172,0.0019244,1.8322,1.0,1.5664,0.55013,2.1756,0.41829,0.030792,2.4458,1.0,3.1093,4.0511,1.9885,0.53805,0.022936,1.8566,1.0,4.8593
,0.044351,0.00028367,0.8229,0.0032539,3.4811,2.22,0.021058,0.00034305,1.7014,1.0,2.572,0.74294,2.1273,0.045899,0.0039904,2.4841,1.0,4.9823,0.014024,1.5312,0.19841,0.0016791,2.3923,1.0,3.0679,1.0077,2.0253,0.18352,0.89644,3.3125,1.0,1.6462
,1.2995,0.0023525,0.001995,0.065064,0.54323,2.8083,4.585,0.00033725,1.9608,1.0,1.4942,0.21004,1.9739,0.021214,0.0017034,2.2846,1.0,1.5473,0.36727,1.1223,5.627,0.0036096,2.8629,1.0,4.7655,0.0015197,1.9457,0.74825,0.00090701,3.3519,1.0,4.2693
,0.0084837,0.0011002,0.070644,0.0010214,0.75546,2.4275,1.8668,0.00065488,2.6417,1.0,2.7919,1.76,2.9024,0.035207,0.00066951,3.1674,1.0,1.2179,4.0908,2.0988,0.1721,0.00079095,3.3813,1.0,3.8135,3.8983,1.2739,0.090902,0.00097653,0.44971,1.0,4.0954
,3.9662,0.45549,0.0057613,0.028445,1.1345,2.1867,9.142,0.00066475,3.0856,1.0,4.087,0.82579,1.931,0.013838,0.0033453,2.4654,1.0,4.9088,0.0024061,2.5458,0.027539,0.0010367,1.9918,1.0,0.52644,0.013606,2.1676,3.5781,0.0021776,1.7492,1.0,4.5006
,1.7401,0.0032496,0.39777,0.0001102,1.6065,1.0663,0.92692,0.0019906,2.3176,1.0,1.7801,0.90395,2.7508,0.093695,0.00014049,1.8468,1.0,4.5723,0.0010642,1.4198,0.028686,0.00014327,2.6401,1.0,3.2192,0.031052,1.1347,0.28009,0.0007665,1.2606,1.0,3.1269
,0.019036,0.0029401,0.011261,0.00053047,0.91022,2.6129,4.9743,0.00023017,3.415,1.0,4.2322,0.57284,2.3925,0.010646,0.00087956,3.0655,1.0,3.832,2.8084,1.3209,2.6926,0.44012,1.3741,1.0,4.9609,0.98871,1.8347,0.30955,0.045246,3.409,1.0,4.8033
,0.0044323,0.0015386,0.39179,0.0014347,3.0069,2.2442,0.019318,0.068197,2.9016,1.0,0.15846,0.85482,2.6804,0.013477,0.010762,3.4736,1.0,4.7808,0.0058993,1.3993,0.41896,0.00024853,1.2065,1.0,1.8027,0.91909,2.9239,1.561,0.0022613,0.91241,1.0,3.1725
,0.0021067,0.09341,0.28755,0.0005963,3.2869,1.0743,0.37529,0.0010559,3.2152,1.0,0.53901,0.38137,2.8851,0.28558,0.00010935,3.072,1.0,1.3521,0.011151,2.8129,0.013421,0.005452,2.2101,1.0,4.7637,0.28147,1.8118,1.3975,0.0070999,0.22595,1.0,0.72136
,0.0020217,0.00085826,0.38218,0.0011414,3.0761,1.5586,3.5961,0.27771,2.7154,1.0,3.9306,1.1279,1.8233,0.017655,0.00099994,3.2516,1.0,3.888,0.90239,2.7987,0.9479,0.010316,3.4191,1.0,0.1752,0.034372,1.1362,7.0609,0.0098221,0.95155,1.0,4.1782
,0.26043,0.018619,0.019011,0.16643,0.92386,2.8917,5.915,0.0015665,1.809,1.0,1.9842,0.074904,2.2767,0.016703,0.00012735,2.2451,1.0,1.0153,0.3845,2.6677,0.91072,0.014861,2.9652,1.0,4.8184,2.8729,1.5428,0.030658,0.028667,1.3634,1.0,3.7671
,0.11269,0.013078,0.2719,0.00026263,0.75957,2.5944,1.3769,0.11221,2.7808,1.0,0.95494,0.28939,2.9186,0.12628,0.0012287,3.1098,1.0,2.5779,0.30681,1.4716,2.4552,0.085741,3.1195,1.0,0.34866,3.3027,1.722,0.029809,0.18257,0.8385,1.0,4.5226
,1.7425,0.00062486,0.18762,0.00045907,0.63613,2.8609,0.92297,0.0025066,0.5552,1.0,0.080618,0.29695,2.2656,0.020574,0.0055886,3.0712,1.0,2.1141,0.72137,1.7507,0.29743,0.035256,0.86654,1.0,3.322,4.1548,2.493,0.010502,0.02643,0.53019,1.0,4.3671
,0.053943,0.002721,1.9767,3.8729,2.2163,2.9955,6.3708,0.0011159,1.634,1.0,0.30933,0.37547,1.3063,0.02501,0.0020872,3.4181,1.0,4.8589,1.1747,2.6338,7.2414,0.0042123,0.93933,1.0,1.7007,0.73496,2.0122,7.4747,0.01772,1.7066,1.0,4.2499
]
#p = [0.00344522849931101, 0.000244668015007329, 0.000196877966742394, 1.04406552435891, 2.53346838089726, 2.66215919797784, 4.58283257973953, 0.00190521501392072, 1.1460596347986, 1.0, 3.22784563884992, 0.62787089824395, 2.97121341787434, 0.419394766480721, 0.00529281891556774, 3.4294190161876, 1.0, 3.4299107666584, 4.39199702115881, 2.35897920972145, 0.386789806814769, 0.0734920675981562, 2.24808276452116, 1.0, 0.712990204530988, 0.000327686430412258, 1.948453786486, 0.459889711174946, 0.000119449755567358, 1.55326992573811, 1.0, 3.76379936035856, 0.333538131670129, 1.1684028375267, 0.0264334804860487, 1.72583160580587, 1.08581615319654, 1.87000550771895, 8.00549887130292, 0.00070488033683387, 1.36099931810989, 1.0, 1.79700238531654, 0.536912979579372, 2.41897063061821, 0.202751696108466, 0.00113204315674362, 1.32868477745119, 1.0, 3.88699151184495, 0.288241007798376, 1.42694388570411, 1.47044781746171, 0.0252508282797445, 2.80485648176307, 1.0, 3.14442788402006, 0.033986308256127, 1.18867255114553, 3.06252099479106, 0.0173954454052677, 2.00641653842344, 1.0, 3.6766690027566, 0.072531281075391, 4.46339355850269, 0.351851858007128, 1.69819700925227, 0.799340156851844, 2.81133882023647, 5.60766488381086, 0.000634283182334323, 1.19853647187695, 1.0, 4.63308398969186, 0.246068368370524, 2.62238802718807, 0.233877094440795, 0.000472824609250757, 1.33815736603439, 1.0, 3.94042401081639, 0.0242408752993162, 2.86810316091048, 6.14482909540306, 0.0214316025742574, 3.00321780595005, 1.0, 1.69187337471979, 0.795003387899923, 2.75211059026148, 0.0385032601516517, 0.000561993643015897, 1.29659395622108, 1.0, 2.28301265340703, 0.00184915257226087, 0.0205990174036924, 0.00846943007904509, 0.85060259278954, 0.298129522309603, 2.53369058158362, 3.4826184467426, 0.000921213097995796, 3.33004856478513, 1.0, 4.65703852102315, 4.73534086238366, 2.74503468145893, 0.0857217971687244, 0.0022365022890531, 3.16932256427562, 1.0, 4.82881066987262, 0.884473579100686, 2.79549547736585, 0.558759696113987, 0.0010716004983422, 0.876109650813701, 1.0, 3.24681658295335, 0.169689135507209, 1.64379756563056, 0.757034180131072, 0.160778520788208, 2.56906092068752, 1.0, 0.252344124244875, 0.114893605365068, 0.0764367797652852, 0.00729911938979399, 0.481989375748537, 1.41826155938461, 2.99306222668021, 4.20514995108452, 0.0378353707055683, 0.961031492785037, 1.0, 3.0797585199769, 1.47649700267669, 2.43232599822961, 0.188026642415834, 0.000887701904385176, 3.20958867437463, 1.0, 2.51018324815326, 0.024555986783472, 1.86520151071282, 0.015714809417191, 0.0129745103910961, 2.72997629651141, 1.0, 0.554010632773187, 0.437588837759006, 2.5503667583579, 0.0248997661295203, 0.148340023170092, 0.962883265915484, 1.0, 3.31345915024015, 0.0370624477684989, 0.0127598957608053, 0.00824889269278125, 0.000774574019337072, 1.04915285740535, 2.38714589324555, 3.90656225844581, 0.00221541896147578, 3.00276547331634, 1.0, 0.791430901393052, 0.151516782430968, 1.63650647610671, 0.419034796455671, 0.00133497028512593, 1.20360952670982, 1.0, 3.81084437432577, 0.00922009823124248, 2.32117610095961, 0.039733034801346, 0.00658087501942244, 1.25188123007734, 1.0, 1.92768567359946, 0.193415794692876, 2.34795585459366, 1.20271733719125, 0.123199585510732, 2.88803409342465, 1.0, 2.2757565675437, 0.159496017975293, 0.052174889594654, 0.00672695573135524, 0.00317543695832518, 0.455757511570957, 2.32635189280195, 5.73106630958803, 0.0102629019350964, 3.30499701096933, 1.0, 2.16554183329256, 0.0811686254062768, 2.9423469991671, 0.358926200092043, 0.000363145955123231, 1.92184890912183, 1.0, 4.69296591889715, 0.292232044266691, 2.17445600859041, 0.960063465828121, 0.0541949777012965, 2.4802168032848, 1.0, 2.43847442483013, 2.69368408700156, 1.91712356977983, 3.17072970240359, 0.000820160746157777, 2.45380628655251, 1.0, 3.22635360052742, 0.0173279210754244, 0.000392137282672311, 0.0457483426466287, 0.0106859817045095, 3.4844845212661, 2.84146506088302, 3.40857555583906, 0.00592730503249254, 0.844213876605768, 1.0, 0.434352616344763, 0.162764579137044, 2.66533803960898, 0.345516207015118, 0.0108209064870869, 2.79864048651222, 1.0, 1.14187487339451, 1.22745690028522, 1.88657064247463, 5.81288605506814, 0.0134043786192379, 0.808913820993531, 1.0, 1.59390894772822, 0.00113502995888343, 1.85655814118011, 0.429974468869748, 0.000216399325502973, 1.39471927515444, 1.0, 1.21148329340546, 0.0123219506528574, 1.05255191814621, 0.00414277639990193, 2.34477716367297, 4.92040807876749, 2.84193583791954, 7.27226814700495, 0.00830565111047544, 1.60737631672716, 1.0, 1.06259137421077, 2.67655213706589, 2.46340559639512, 0.134245976470813, 0.000147666483392997, 2.01220948649037, 1.0, 4.3483944329773, 0.132649879680456, 1.24773240454853, 0.500186575895968, 0.00514790227124881, 3.07147042837216, 1.0, 1.31966285795487, 0.360910017407632, 2.11843621811258, 0.0137878122356122, 0.000339680991427878, 1.6784239208754, 1.0, 1.55416516376045, 0.279862964257694, 1.60835817633231, 0.0129697480158568, 0.0442419319121899, 0.193632213478463, 2.75414753304106, 2.95360844204567, 0.00059762158225375, 2.15575660765596, 1.0, 2.57680675672495, 0.542655024323819, 1.89179186331721, 0.0963490337685256, 0.00121105328064253, 2.19764711104137, 1.0, 4.28995826952019, 1.71850035854102, 1.8781360454921, 0.0143001177342517, 0.0615309536065931, 1.87377204892139, 1.0, 3.75961403448117, 0.026233325416698, 1.33645374543749, 5.40633701608794, 0.00230925080098269, 1.03113576125511, 1.0, 2.50863578798132, 0.00643343821222101, 0.000203784168921093, 0.000125212869346187, 0.00150611847380449, 0.170003410068729, 2.87565892497167, 1.17842912107363, 0.000790534467401572, 1.33343531756337, 1.0, 3.46000556272156, 1.16401783236755, 2.85394277341519, 0.233726737068962, 0.000150896881436981, 2.81541599371824, 1.0, 4.06358998547777, 0.642076113008848, 1.84236469132272, 0.824336281689908, 0.379445416243245, 0.999044555132822, 1.0, 3.54234358509713, 0.384126558377924, 1.26370919916861, 0.505836152011183, 0.00185872879039954, 2.36746343549489, 1.0, 4.3652859694084, 0.000343230813665065, 0.145908628997613, 0.000983136836740513, 0.00190958856608861, 2.01722652991358, 2.90020920516912, 4.40370721306722, 0.000196136091226055, 2.24819521606114, 1.0, 3.32071694267866, 0.231719980279286, 2.82490253183396, 0.620429458367693, 0.000103337849295088, 2.74679191014902, 1.0, 3.56150004768027, 3.44685348868087, 1.73234176950112, 9.74188902818891, 0.237348815045616, 1.57882725727258, 1.0, 2.1805981976396, 1.91850146468747, 2.18063786632714, 0.275766080464354, 0.00163770991263111, 0.815178283725705, 1.0, 2.29320551970752, 0.2128223172261, 0.000400908600879106, 0.0892101110359474, 0.00022224907703267, 0.670881355708342, 2.9548737172909, 0.205645191545259, 0.0016219478566726, 3.18976875633971, 1.0, 1.66779433714877, 3.89179694307826, 2.84052012921869, 0.136218833542532, 0.00144002827397975, 0.849031735976146, 1.0, 2.05992569147467, 0.674380716376934, 2.57986824936587, 0.052627719504546, 0.0558316234489368, 2.91291222388076, 1.0, 1.35062921905078, 0.00329014391748038, 2.47615895103753, 2.35028122899768, 0.000521012825783816, 2.97701057972111, 1.0, 3.11189867166201, 0.0335326255744675, 0.000107190521638887, 0.103998647627571, 0.00195464107742474, 1.2862772652432, 2.92415719666695, 1.6389852531365, 0.00114696853289175, 1.4857804197324, 1.0, 1.22436355503077, 0.272828758958592, 2.56808863412301, 0.335861442248158, 0.00014159567748617, 1.50273627959185, 1.0, 2.40405531552346, 0.00370401659904655, 2.82515501960227, 0.77061794518919, 0.000880266546407369, 1.96408581132564, 1.0, 1.99879631163353, 0.00200895437377882, 2.87263542821208, 0.0925664441920048, 0.000469236108503706, 3.03667063853268, 1.0, 3.36066367026249, 0.482484072960376, 0.0608634021540303, 0.0613054035716773, 1.10812938715298, 1.85573882788668, 2.66476871016618, 5.50021165278738, 0.0116411189300077, 2.47841071050716, 1.0, 4.26173036639592, 0.182812172117865, 2.87710421951424, 0.31977784334249, 0.00103210080199899, 2.37137744474833, 1.0, 0.562437172899168, 0.360537385585975, 1.37661097302585, 0.0106199266891913, 0.0265213911702611, 1.35090722909378, 1.0, 4.03054443931462, 0.0436166643342571, 2.12463339037783, 0.0285267944165798, 0.0014585212921788, 1.58760222791661, 1.0, 3.86222354134687, 4.63138018142158, 0.00162582421340464, 0.0959756517916416, 0.00332522102597358, 2.09777584563246, 1.07584932782922, 9.01499524927906, 0.0831128428168552, 0.663369469093815, 1.0, 4.67626907323378, 1.691093081658, 2.24327222446101, 0.10752280095355, 0.00612474015098729, 2.18456906538813, 1.0, 3.81191355432353, 0.612385163686844, 2.94813272739743, 1.22328576500695, 0.00226510790591611, 2.96858255576657, 1.0, 4.76888935118799, 0.10757925539122, 1.40477462574411, 0.0101208159643423, 0.0025138589868045, 1.72759856178007, 1.0, 0.353786983052564, 0.00121509083540008, 0.0339803722013362, 0.802035249645557, 0.00014577913245087, 4.17743484891009, 2.24636091123726, 1.36039998257124, 0.0291019450069985, 0.987927781521014, 1.0, 3.07647222163984, 2.02491802371731, 2.09926333673545, 0.0742126654658247, 0.000480554790311052, 3.00156225726738, 1.0, 4.85686606452483, 0.0296996225554634, 1.41335264220087, 0.296332103410466, 0.00448927089952065, 1.03363559582823, 1.0, 4.73554077102469, 1.51073982597794, 1.41086473368614, 5.65663239734456, 0.000360152039417019, 3.20409778779124, 1.0, 3.284416086193, 2.04414373740503, 1.67685099049515, 0.00198854183384301, 0.000280695819167294, 0.764611535623416, 2.03354622832414, 5.10144976813538, 0.00383679966839277, 2.29559143007987, 1.0, 1.47066715912162, 0.208793327519342, 2.30097267092848, 0.366010002540475, 0.00571605683989241, 1.6879900359874, 1.0, 3.75888460360308, 0.104015712719025, 1.36812421288292, 0.167780836591706, 0.000209922269088604, 1.88340740565922, 1.0, 0.228125211149263, 0.203874336952442, 1.88293847306242, 0.183627803545739, 0.0742640093140294, 2.61726998296716, 1.0, 0.542323767187544, 0.00184092027070851, 0.571809039843109, 0.00123262954382488, 0.0281123196048372, 1.07903497801271, 2.60223420601153, 5.4376683917849, 0.00791960243119625, 3.16697003713818, 1.0, 1.69263622948573, 0.228665476518496, 2.94419040047054, 0.43198853419532, 0.00188087412266846, 1.62969413466313, 1.0, 3.02290684774451, 0.179153955801354, 1.354574921589, 0.284992221742433, 0.000653159936616965, 1.61635294336516, 1.0, 1.07842567214294, 0.187083904266272, 1.84331675902091, 0.0122344905689508, 0.0597293875771851, 1.11463373678834, 1.0, 2.93690749723551, 0.000101512211986865, 0.0197283328261442, 0.0720645614384866, 0.000648087493444517, 2.12567603143422, 2.25469798151928, 3.40838903836315, 0.202913214939736, 0.513792241053879, 1.0, 4.10242505241611, 2.2428563980844, 2.31386540256199, 0.110458268822487, 0.0010546935805695, 1.00167595009232, 1.0, 3.73289690137637, 2.15526641530822, 2.39548705505804, 0.0972778260065576, 0.727124718439659, 1.41407565140351, 1.0, 0.423241067927656, 0.00349501078817384, 1.02114805520132, 0.120231423483691, 0.000485043874225219, 1.41757001885963, 1.0, 0.756589716379947, 0.000303724850436058, 0.000744787722071458, 0.0497252443263104, 0.00225030071773467, 2.10699082882432, 2.34409757872614, 3.78686882338361, 0.0078004579730656, 1.44742691400178, 1.0, 0.244577980799549, 4.59083461382819, 2.45081034689663, 0.0641435812827439, 0.000755743184471113, 1.95040338965736, 1.0, 2.35228474090712, 0.0620561141596705, 2.68346432205349, 4.69429188696932, 0.00136393312382835, 3.28428920840796, 1.0, 4.21826799539186, 1.62379091772087, 2.49699600415601, 5.61841785264966, 0.000730893807100582, 1.24120399625239, 1.0, 0.516602286404936]
def sets(p , totalparams): 
   q = []
   a = 0
   b = 32
   for i in range (0,len(p)//totalparams):
 
    q.append(p[a:b])
    b += 32
    a+=32
   return q

q = sets(p,32)

for set in range (6,7): #loop for each parameter set

 k_fo,k_of = [1,1]
 k_ffr = q[set][2]
 k_frf = q[set][3]
# Regulated OFF-->ON (xXF_A)
 kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1  = q[set][4:11]
# Regulated ON-->OFF (Activator 2)
 kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]

# Regulated OFF-->OFFrepr (Activator 1)
 kA3_max, n3, K3, kA3_min, ksA3, gamma_A3, kA3 = q[set][18:25]
 kA3_max,kA3,kA3_min = [0,0,0]
# Regulated OFFrepr-->OFF (xXF_D)
 #k4_max, n4, K4, k4_min, k4_delay, k4_off, k4_on = q[set][25:32]
 counts_2 = []
 counts_1 = []
 counts_0 = []

while j < 100:
    #tetraploid
    #the whole gillespie code
                                       
    #Initial states
    S1 = [0]    # promoter state chromosome 1
    S2 = [0]    # promoter state chromosome 2
    S3 = [0]    # promoter state chromosome 3
    S4 = [0]    # promoter state chromosome 4
    A1_1 = [1]  # activator1 from chromosome 1
    A2_1 = [1]  # activator2 from chromosome 1
    A1_2 = [1]  # activator1 from chromosome 2
    A2_2 = [1]  # activator2 from chromosome 2
    A1_3 = [1]  # activator1 from chromosome 3
    A2_3 = [1]  # activator2 from chromosome 3
    A1_4 = [1]  # activator1 from chromosome 4
    A2_4 = [1]  # activator2 from chromosome 4
    A3_1 = [1]  # activator3 from chromosome 1
    A3_2 = [1]  # activator3 from chromosome 2
    A3_3 = [1]  # activator3 from chromosome 3
    A3_4 = [1]  # activator3 from chromosome 4
    t = [0]     # time
    I1_1 = [0] # intermediate levels
    I2_1 = [0]
    I1_2 = [0]
    I2_2 = [0]
    I1_3 = [0]
    I2_3 = [0]
    I1_4 = [0]
    I2_4 = [0]
    I3_1 = [0]
    I3_2 = [0]
    I3_3 = [0]
    I3_4 = [0]
    tend = 52
    df1 = 2
    df2 = 2 
    while t[-1] < tend:
        current_S1 = S1[-1]
        current_S2 = S2[-1]
        current_S3 = S3[-1]
        current_S4 = S4[-1]
        current_A1_1 = A1_1[-1]
        current_A2_1 = A2_1[-1]
        current_A1_2 = A1_2[-1]
        current_A2_2 = A2_2[-1]
        current_A1_3 = A1_3[-1]
        current_A2_3 = A2_3[-1]
        current_A1_4 = A1_4[-1]
        current_A2_4 = A2_4[-1]
        current_A3_1 = A3_1[-1]
        current_A3_2 = A3_2[-1]
        current_A3_3 = A3_3[-1]
        current_A3_4 = A3_4[-1]
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]
        current_I1_2 = I1_2[-1]
        current_I2_2 = I2_2[-1]
        current_I1_3 = I1_3[-1]
        current_I2_3 = I2_3[-1]
        current_I1_4 = I1_4[-1]
        current_I2_4 = I2_4[-1]
        current_I3_1 = I3_1[-1]
        current_I3_2 = I3_2[-1]
        current_I3_3 = I3_3[-1]
        current_I3_4 = I3_4[-1]
        
        # for I1_1
        if I1_1[-1] < no_intermediates:
            i1_1 = ksA1 * int(current_S1 == 1)
        else:
            i1_1 = 0

        # for I2_1
        if I2_1[-1] < no_intermediates:
            i2_1 = ksA2 * int(current_S1 == 1)
        else:
            i2_1 = 0

        # for I3_1
        if I3_1[-1] < no_intermediates:
            i3_1 = ksA3 * int(current_S1 == 1)
        else:
            i3_1 = 0

        # for I1_2
        if I1_2[-1] < no_intermediates:
            i1_2 = ksA1 * int(current_S2 == 1)
        else:
            i1_2 = 0

        #  for I2_2
        if I2_2[-1] < no_intermediates:
            i2_2 = ksA2 * int(current_S2 == 1)
        else:
            i2_2 = 0  

        # for I3_2
        if I3_2[-1] < no_intermediates:
            i3_2 = ksA3 * int(current_S2 == 1)
        else:
            i3_2 = 0 

       # for I1_3
        if I1_3[-1] < no_intermediates:
            i1_3 = ksA1 * int(current_S3 == 1)
        else:
            i1_3 = 0

        #  for I2_3
        if I2_3[-1] < no_intermediates:
            i2_3 = ksA2 * int(current_S3 == 1)
        else:
            i2_3 = 0

        # for I3_3
        if I3_3[-1] < no_intermediates:
            i3_3 = ksA3 * int(current_S3 == 1)
        else:
            i3_3 = 0

        # for I1_4
        if I1_4[-1] < no_intermediates:
            i1_4 = ksA1 * int(current_S4 == 1)
        else:
            i1_4 = 0
            
        #  for I2_4
        if I2_4[-1] < no_intermediates:
            i2_4 = ksA2 * int(current_S4 == 1)
        else:
            i2_4 = 0

        # for I3_4
        if I3_4[-1] < no_intermediates:
            i3_4 = ksA3 * int(current_S4 == 1)
        else:
            i3_4 = 0
            
        # combined hill function , activator 1
        total_activator1 = (current_A1_1 + current_A1_2 + current_A1_3 + current_A1_4) / df1
        total_activator3 = (current_A3_1 + current_A3_2 + current_A3_3 + current_A3_4) / df1
        k_prod_eff1 = ((kA1_max-kA1_min) * k_fo * ((total_activator1*total_activator3)**n1) / ((K1**n1) + ((total_activator1*total_activator3)**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3 + current_A2_4) / df2
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
        #chromosome 1
        a1_1 = k_frf * int(current_S1 == -1) 
        a2_1 = k_ffr * int(current_S1 == 0) 
        a3_1 = k_prod_eff1 * int(current_S1 == 0) 
        a4_1 = k_prod_eff2 * int(current_S1 == 1) 
        a5_1 = kA1 * int(current_A1_1==0) * int(current_S1!=1)
        a6_1 = gamma_A1 * int(current_A1_1==1) * int(current_S1==1) * int(current_I1_1 >= no_intermediates) 
        a7_1 = kA2 * int (current_A2_1==0) * int(current_S1!=1) 
        a8_1 = gamma_A2 * int(current_A2_1==1) * int(current_S1==1) * int(current_I2_1 >= no_intermediates) 
        a9_1 = kA3 * int (current_A3_1==0) * int(current_S1!=1) 
        a10_1 = gamma_A3 * int(current_A3_1==1) * int(current_S1==1) * int(current_I3_1 >= no_intermediates)
        #chromosome 2
        a1_2 = k_frf * int (current_S2 == -1) 
        a2_2 = k_ffr * int(current_S2 == 0) 
        a3_2 = k_prod_eff1 * int(current_S2 == 0) 
        a4_2 = k_prod_eff2 * int(current_S2 == 1) 
        a5_2 = kA1 * int(current_A1_2==0) * int(current_S2!=1) 
        a6_2 = gamma_A1 * int(current_A1_2==1) * int(current_S2==1) * int(current_I1_2 >= no_intermediates)
        a7_2 = kA2 * int(current_A2_2==0) * int(current_S2!=1) 
        a8_2 = gamma_A2 * int(current_A2_2==1) * int(current_S2==1) * int(current_I2_2 >= no_intermediates) 
        a9_2 = kA3 * int (current_A3_2==0) * int(current_S2!=1) 
        a10_2 = gamma_A3 * int(current_A3_2==1) * int(current_S2==1) * int(current_I3_2 >= no_intermediates)

        #chromosome 3
        a1_3 = k_frf * int(current_S3 == -1) #off repressed to off
        a2_3 = k_ffr * int(current_S3 == 0) #off to off repressed
        a3_3 = k_prod_eff1 * int(current_S3 == 0) #off to on
        a4_3 = k_prod_eff2 * int(current_S3 == 1) #on to off
        a5_3 = kA1 * int(current_A1_3==0 and current_S3!=1) #activator 1 OFF to ON
        a6_3 = gamma_A1 * int(current_A1_3==1 and current_S3==1 and current_I1_3 >= no_intermediates) #activator 1 ON to OFF
        a7_3 = kA2 * int(current_A2_3==0 and current_S3!=1) #activator2 OFF to ON
        a8_3 = gamma_A2 * int(current_A2_3==1 and current_S3==1 and current_I2_3 >= no_intermediates)  #activator 2  ON to OFF
        a9_3 = kA3 * int(current_A3_3==0 and current_S3!=1) 
        a10_3 = gamma_A3 * int(current_A3_3==1 and current_S3==1 and current_I3_3 >= no_intermediates)

        #chromosome 4
        a1_4 = k_frf * int(current_S4 == -1) #off repressed to off
        a2_4 = k_ffr * int(current_S4 == 0) #off to off repressed
        a3_4 = k_prod_eff1 * int(current_S4 == 0) #off to on
        a4_4 = k_prod_eff2 * int(current_S4 == 1) #on to off
        a5_4 = kA1 * int(current_A1_4==0 and current_S4!=1) #activator 1 OFF to ON
        a6_4 = gamma_A1 * int(current_A1_4==1 and current_S4==1 and current_I1_4 >= no_intermediates) #activator 1 ON to OFF
        a7_4 = kA2 * int(current_A2_4==0 and current_S4!=1) #activator2 OFF to ON
        a8_4 = gamma_A2 * int(current_A2_4==1 and current_S4==1 and current_I2_4 >= no_intermediates)  #activator 2  ON to OFF
        a9_4 = kA3 * int(current_A3_4==0 and current_S4!=1)
        a10_4 = gamma_A3 * int(current_A3_4==1 and current_S4==1 and current_I3_4 >= no_intermediates)

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1, a9_1, a10_1,
                 a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2, a9_2, a10_2,
                 a1_3, a2_3, a3_3, a4_3, a5_3, a6_3, a7_3, a8_3, a9_3, a10_3,
                 a1_4, a2_4, a3_4, a4_4, a5_4, a6_4, a7_4, a8_4, a9_4, a10_4,
                 i1_1, i2_1, i3_1, i1_2, i2_2, i3_2, i1_3, i2_3, i3_3, i1_4, i2_4, i3_4]
 
        rate_sum = sum(rates)

        # time update
        if rate_sum == 0:
            tau = float('inf')
            t.append(t[-1] + tau)
            break
        else:
            tau = np.random.exponential(scale=1 / rate_sum)
        t.append(t[-1] + tau)

        rand = random.uniform(0, 1)
        cumulative_rates = np.cumsum(rates)

        # event - chromosome 1
        if rand * rate_sum <= cumulative_rates[0]:
            S1.append(0); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[1]:
            S1.append(-1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[2]:
            S1.append(1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[3]:
            S1.append(0); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[4]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[5]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(0); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[6]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[7]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(0); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[8]: # a9_1 Production A3
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[9]: # a10_1 Degradation A3
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(0); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        # event - chromosome 2
        elif rand * rate_sum <= cumulative_rates[10]:
            S1.append(current_S1); S2.append(0); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[11]:
            S1.append(current_S1); S2.append(-1); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[12]:
            S1.append(current_S1); S2.append(1); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[13]:
            S1.append(current_S1); S2.append(0); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[14]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(1); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[15]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(0); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[16]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(1)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[17]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(0)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[18]: # a9_2 Production A3
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(1); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[19]: # a10_2 Degradation A3
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(0); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)
            
        # event - chromosome 3
        elif rand * rate_sum <= cumulative_rates[20]:
            S1.append(current_S1); S2.append(current_S2); S3.append(0); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[21]:
            S1.append(current_S1); S2.append(current_S2); S3.append(-1); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[22]:
            S1.append(current_S1); S2.append(current_S2); S3.append(1); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[23]:
            S1.append(current_S1); S2.append(current_S2); S3.append(0); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[24]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(1); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[25]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(0); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[26]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(1); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[27]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(0); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[28]: # a9_3 Production A3
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(1); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[29]: # a10_3 Degradation A3
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(0); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        # event - chromosome 4
        elif rand * rate_sum <= cumulative_rates[30]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(0)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[31]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(-1)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[32]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(1)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[33]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(0)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[34]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(1); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[35]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(0); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[36]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(1)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[37]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(0)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[38]: # a9_4 Production A3
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(1)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[39]: # a10_4 Degradation A3
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(0)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        #intermediates
        elif rand * rate_sum <= cumulative_rates[40]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1 + 1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[41]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1 + 1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[42]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1 + 1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[43]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2 + 1); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[44]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2 + 1)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[45]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2 + 1); I3_3.append(current_I3_3); I3_4.append(current_I3_4)
            
        elif rand * rate_sum <= cumulative_rates[46]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3 + 1); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)
            
        elif rand * rate_sum <= cumulative_rates[47]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3 + 1); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[48]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3 + 1); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[49]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4 + 1); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)
            
        elif rand * rate_sum <= cumulative_rates[50]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4 + 1)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4)

        elif rand * rate_sum <= cumulative_rates[51]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            A3_1.append(current_A3_1); A3_2.append(current_A3_2); A3_3.append(current_A3_3); A3_4.append(current_A3_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            I3_1.append(current_I3_1); I3_2.append(current_I3_2); I3_3.append(current_I3_3); I3_4.append(current_I3_4 + 1)

# plotting
plt.figure(figsize=(10, 14))  # taller figure for 4x2 grid

# ---- Column headers ----
plt.text(0.3, 0.97, 'Chromosome 1', ha='center', va='center',
         fontsize=28, fontweight='bold', transform=plt.gcf().transFigure)
plt.text(0.75, 0.97, 'Chromosome 2', ha='center', va='center',
         fontsize=28, fontweight='bold', transform=plt.gcf().transFigure)

# ---- Plot 1 ----
plt.subplot(4,2,1)
plt.plot(t, S1, color='blue')
plt.ylabel('Xist promoter', fontsize=25, labelpad=20)
plt.yticks([-1, 0, 1])
plt.minorticks_off()
plt.box(True)

# ---- Plot 2 ----
plt.subplot(4,2,2)
plt.plot(t, S2, color='red')
plt.yticks([-1, 0, 1])
plt.minorticks_off()
plt.box(True)

# ---- Plot 3 ----
plt.subplot(4,2,3)
plt.plot(t, S3, color='blue')
plt.ylabel('Xist promoter', fontsize=25, labelpad=20)
plt.yticks([-1, 0, 1])
plt.minorticks_off()
plt.box(True)

# ---- Plot 4 ----
plt.subplot(4,2,4)
plt.plot(t, S4, color='red')
plt.yticks([-1, 0, 1])
plt.minorticks_off()
plt.box(True)

# ---- Plot 5 (Zic3) ----
plt.subplot(4,2,5)
plt.plot(t, A1_1, color='green')
plt.ylabel('Zic3', fontsize=25, labelpad=20)
plt.yticks([-1, 0, 1])
plt.minorticks_off()
plt.box(True)

# ---- Plot 6 (Zic3) ----
plt.subplot(4,2,6)
plt.plot(t, A1_2, color='green')
plt.yticks([-1, 0, 1])
plt.minorticks_off()
plt.box(True)

# ---- Plot 7 (Rnf12) ----
plt.subplot(4,2,7)
plt.plot(t, A3_1, color='purple')
plt.ylabel('Rnf12', fontsize=25, labelpad=20)
plt.xlabel('Time (hours)', fontsize=25, labelpad=40)
plt.yticks([-1, 0, 1])
plt.minorticks_off()
plt.box(True)

# ---- Plot 8 (Rnf12) ----
plt.subplot(4,2,8)
plt.plot(t, A3_2, color='purple')
plt.xlabel('Time (hours)', fontsize=25, labelpad=40)
plt.yticks([-1, 0, 1])
plt.minorticks_off()
plt.box(True)

# layout adjustments
plt.tight_layout(pad=2.0, w_pad=1.5, h_pad=1.5)

#plt.savefig('/home/madhusud/modeling_gene_expression/FinalPlots/Promoterplot.png', dpi=600, bbox_inches="tight")
plt.show()