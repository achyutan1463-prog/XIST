#% of cells graph for 3 state model for XO cells
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats
import matplotlib
matplotlib.use('TkAgg')
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
,0.053943,0.002721,1.9767,3.8729,2.2163,2.9955,6.3708,0.0011159,1.634,1.0,0.30933,0.37547,1.3063,0.02501,0.0020872,3.4181,1.0,4.8589,1.1747,2.6338,7.2414,0.0042123,0.93933,1.0,1.7007,0.73496,2.0122,7.4747,0.01772,1.7066,1.0,4.2499]

#All
p=[0.129017014418838, 0.000443146732826457, 0.000216005580358379, 0.0110728987642395, 0.38872344682115, 2.985985549164, 3.35621653933345, 0.00230891936339739, 2.07369139988922, 1.0, 1.89997724462203, 0.595245446051379, 2.64261050026489, 0.0772378537281, 0.00331945613279959, 2.12435111852672, 1.0, 3.39267324965798, 0.0556039156836611, 2.70983142447257, 0.0133787308917305, 0.00470710272067814, 0.35029828330521, 1.0, 0.794796338054708, 0.147401955408073, 2.11413822966859, 0.52666772925197, 0.09318370023072, 1.77590946385605, 1.0, 1.75287998033869, 0.000129124973436022, 0.000818741664088428, 0.23309145601231, 0.000472454532647125, 3.21919978615836, 1.23659003058092, 0.255685166847326, 0.789095373942153, 1.01663683294116, 1.0, 0.689923759330219, 0.262112898831207, 2.62130648821492, 0.197823164664066, 0.00149923303970358, 2.58647399931827, 1.0, 2.62888808874568, 0.086341911281309, 2.21409766403582, 0.772921857101651, 0.0105955442365675, 1.43285589473884, 1.0, 3.47695264082178, 0.0592308746778943, 1.63576119186371, 0.310337314578386, 0.000343877601028523, 3.09408632816679, 1.0, 0.732962182028522, 1.75128536471603, 0.314820394010197, 0.0509194971005418, 0.141501937421684, 1.05568875077986, 1.72773521366464, 5.4695677298694, 0.00285803400187244, 2.51177659434788, 1.0, 3.26065442681777, 0.507194793156672, 1.63995276860387, 0.0553556137953704, 0.0029515205563571, 3.23495362525137, 1.0, 2.82358291273901, 0.973179356356979, 1.79747085606489, 0.201663123665934, 0.000427261132080969, 0.549373378327898, 1.0, 2.68744073310346, 3.05615643323373, 1.60789892066436, 0.0239590537980031, 0.191099946172636, 3.22510333088498, 1.0, 1.43860926824973, 0.073137140452066, 0.0179087076918846, 0.0143199333641839, 0.000322048894548714, 0.37381701252678, 1.65209638157185, 2.85365998721075, 0.000111837800209746, 1.05709389011692, 1.0, 4.73061044464772, 2.06279789255085, 2.61295774416306, 0.0628661754589393, 0.000111936175915397, 1.10160905662239, 1.0, 2.23183776481372, 0.638510854405613, 2.88588894360632, 1.64455242102091, 0.20381931765918, 1.59038592596974, 1.0, 4.95047623210141, 0.0471250335392248, 1.20804851354981, 4.4553527717984, 0.000618590091345585, 0.210729808952705, 1.0, 4.64269672133178, 0.000199242164579981, 0.000566846201938813, 0.108193783248259, 0.39145727201614, 2.37241072333731, 2.08035849652831, 6.52010180117489, 0.000289169964894837, 1.4690186595033, 1.0, 3.31500109079174, 0.277101439755393, 2.86383135838447, 0.139416804175318, 0.0016995367315127, 3.10179998879461, 1.0, 2.50391590533402, 0.0925281029595468, 2.25806845011113, 0.261559987483707, 0.000612131924457002, 2.25236522450027, 1.0, 2.26474190200985, 1.85586551388632, 2.4473706923697, 0.0147897180778588, 0.0231810387334225, 1.34916561127968, 1.0, 3.20035245205979, 0.000177139823081852, 0.000329910790908228, 0.0364046376834263, 0.00565966504023608, 0.290746234620859, 2.84444466176043, 0.682069169742971, 0.0419575379725443, 2.04898981007521, 1.0, 3.1885424301584, 1.18316756868997, 2.93311424116335, 0.0896708825032131, 0.00371054849236314, 2.3669288971633, 1.0, 3.77716676734259, 0.131940131110955, 1.4469145861343, 0.211411645416494, 0.00193322188502867, 3.4832504268319, 1.0, 2.31439871551383, 0.442222106592662, 2.59390086839953, 0.0746167908829898, 0.0146738541494025, 2.8975698387309, 1.0, 3.16386201632571, 0.000734138064500747, 1.71507573428572, 0.17610126245992, 2.28145173335876, 0.159925323897498, 2.40276407461871, 2.01790608981803, 0.0103023966495868, 1.27681179427191, 1.0, 1.30058425146697, 0.0988223294031905, 2.65886262582011, 0.205182575286702, 0.000491351106847179, 1.6314259827724, 1.0, 2.27023317812128, 0.200518891175328, 2.72886905384452, 7.94560391668415, 0.14231583302972, 1.99795127219712, 1.0, 0.0975222446124316, 1.0240965642295, 1.96539531200349, 1.2383643513052, 0.0844572736905895, 2.53276982634804, 1.0, 0.487352948650262, 0.064826321324905, 0.00176759354552026, 0.744776659519439, 2.95068912577943, 0.550039472122504, 2.91395780871794, 3.44040374052178, 0.000351336027917739, 1.60463902529945, 1.0, 1.41034960413615, 0.644397624090169, 2.25316385397931, 0.0701800880553944, 0.00170781525890271, 0.573490463246309, 1.0, 4.32726437447495, 2.69431138797068, 1.91120448324324, 2.19330557689009, 0.216813553664388, 1.05514315713238, 1.0, 1.14811759290069, 0.00386854415453904, 2.31657096718685, 4.27442061524165, 0.000550080418295594, 3.07461703583746, 1.0, 3.12130508135366, 0.000341368731592812, 1.41856202398013, 0.0419448099214336, 0.000845571539883427, 2.52566716356689, 1.49230235774672, 3.64902907786684, 0.00028032720012112, 2.24486374068065, 1.0, 3.84035892933055, 3.73677032839622, 1.43154262147405, 0.0167119296424451, 0.0012467565068737, 1.3985624554943, 1.0, 4.96884028211626, 0.0773497656417862, 1.03319530400389, 1.10299994291327, 0.0124926472220413, 2.26011024728348, 1.0, 4.3215505011974, 4.17743843759824, 1.45756079833851, 1.64310810469299, 0.124931689956253, 1.37366503053666, 1.0, 3.80708523685949, 0.000115413855188614, 2.37764046254413, 0.0783806070992542, 0.00964750906018589, 2.7840433498184, 2.09528281189242, 3.67210083235035, 0.0289464719873491, 3.27399580250258, 1.0, 2.73715953170785, 3.84185625872831, 1.61036449965356, 0.016403032229764, 0.00162402831364587, 1.90941463608804, 1.0, 3.85679886557327, 0.0110219145210375, 1.50270596002841, 5.77330319064836, 0.000299722223946463, 1.87467532518421, 1.0, 2.1203806065779, 0.0619726691523024, 2.00255267385832, 8.29833006604851, 0.00299175892496222, 0.438256198702845, 1.0, 2.71493668060598, 0.000572247205321955, 0.000508701646684262, 0.00854544351633231, 0.00296513774173141, 0.330760996345774, 2.81915450836553, 3.50670539750107, 0.00374460329285392, 1.21285949375461, 1.0, 3.90789139763426, 0.256547653085588, 2.47943680634742, 0.0869137986639818, 0.000228746113808601, 3.14432760245176, 1.0, 2.89142557368367, 1.79998519351861, 1.45547143512611, 0.0832039514535567, 0.0417878904387996, 1.64115186006532, 1.0, 2.73714066395989, 0.526775876855213, 1.30418787506982, 8.37191154053878, 0.36554701412363, 3.2140702399331, 1.0, 2.73830389432139, 0.4393323901655, 0.00138634643999778, 0.438342524764994, 0.00176644151003161, 3.26971480989963, 1.51143403012219, 0.0858068953175357, 0.184134348828767, 0.590951354790455, 1.0, 3.11505731984755, 1.75018090743392, 2.52978625887063, 0.068789616367452, 0.00137725395729389, 0.831216769593171, 1.0, 2.87329070767118, 0.170508794271623, 1.2464766228204, 1.71124139367142, 0.00954968512609462, 1.86556536533148, 1.0, 3.38251089066431, 3.09697042349449, 2.61815540303649, 0.072054584036859, 0.0045116695520648, 1.4045726956943, 1.0, 3.55265862448, 2.51804815437399, 0.000779460211493941, 0.0392318200576027, 0.0152241916009374, 1.80511767447397, 2.29209300516651, 4.12101103674522, 0.0181223086956628, 2.66902154279517, 1.0, 0.227940435534595, 0.328301061010539, 1.97933693414292, 0.0741926088893552, 0.000875923955834106, 3.21360928327022, 1.0, 2.64141268466926, 0.0089299619714369, 1.52234572381141, 2.0835444412737, 0.000139003267627548, 1.21241465265237, 1.0, 0.290057685444073, 0.243013883104922, 2.04951016869885, 5.6573353095427, 0.120435012911716, 3.4917603300114, 1.0, 0.755301317541729]

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
mean_c1 = []
mean_c0 = []

for set in range(0,len(q)): #loop for each parameter set
 k_fo,k_of = [1,1]
 k_ffr = q[set][2]
 k_frf = q[set][3]
# Regulated OFF-->ON (xXF_A)
 kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1  = q[set][4:11]

# Regulated ON-->OFF (Activator 2)
#  kA2_max, n2 = q[set][11:13]
#  K2 = 0.17
#  kA2_min, ksA2, gamma_A2, kA2 = q[set][14:18]
 kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]

# Regulated OFF-->OFFrepr (Activator 1)
 #kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = q[set][18:25]

# Regulated OFFrepr-->OFF (xXF_D)
 #k4_max, n4, K4, k4_min, k4_delay, k4_off, k4_on = q[set][25:32]
 df1 = 1
 df2 = 1
 no_intermediates = 10
 all_allelicstates = []
 j = 0
 while j < 100:
    #the whole gillespie code
    S1 = [0]    
    A1_1 = [1]  
    A2_1 = [1]  
    t = [0]     
    I1_1 = [0] 
    I2_1 = [0]
    tend = 52
 

    while t[-1] < tend:
        current_A1_1 = A1_1[-1]
        current_S1 = S1[-1]
        current_A2_1 = A2_1[-1]
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]

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

        # combined hill function , activator 1
        total_activator1 = (current_A1_1)
        if total_activator1 > 0.5:
            total_activator1 -= 0.5
        else:
            total_activator1 = 0
        k_prod_eff1 = ((kA1_max-kA1_min) * k_fo * (total_activator1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1)
        if total_activator2 > 0.5:
            total_activator2 -= 0.5
        else:
            total_activator2 = 0
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

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1, i1_1 , i2_1]

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
        # event - chromosome 1
        if rand * rate_sum <= a1_1:
            S1.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1:
            S1.append(-1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
            S1.append(1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
            S1.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
            S1.append(current_S1)
            A1_1.append(1)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
            S1.append(current_S1)
            A1_1.append(0)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
            S1.append(current_S1)
            A1_1.append(current_A1_1)
            A2_1.append(1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
            S1.append(current_S1)
            A1_1.append(current_A1_1)
            A2_1.append(0)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        # intermediates
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + i1_1:
            S1.append(current_S1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1 + 1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + i1_1 + i2_1:
            S1.append(current_S1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1 + 1)

    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    if a == 1 : 
            all_allelicstates.append(1)
    else:
            all_allelicstates.append(0)
    j += 1
 c1 = c0 = 0
 for row in all_allelicstates:
            if row == 1:
                c1 += 1
            elif row == 0:
                c0 += 1

       
 mean_c1.append(c1)
 mean_c0.append(c0)   
 


t_crit_1 = stats.t.ppf(0.975, len(mean_c1)-1)
ci_1 = t_crit_1 * (np.std(mean_c1, ddof=1) / np.sqrt(len(mean_c1)))

t_crit_0 = stats.t.ppf(0.975, len(mean_c0)-1)
ci_0 = t_crit_0 * (np.std(mean_c0, ddof=1) / np.sqrt(len(mean_c0)))
print(np.mean(mean_c0))
plt.figure(figsize = (4,4))

plt.bar('XO', np.mean(mean_c0), label="XaO (Inactive)", color="#E69F00",  width = 0.5,capsize=5,yerr=ci_0 , ecolor = 'black')
bottom =  np.mean(mean_c0)
plt.bar('XO', np.mean(mean_c1), label="XaXi (Monoallelic)", color="#AA3377", bottom=bottom, width = 0.5,capsize=5,yerr=ci_1,ecolor = 'red')

mean_c2 = []
mean_c1 = []
mean_c0 = []
for set in range(0,len(q)): #loop for each parameter set

 k_fo,k_of = [1,1]
 k_ffr = q[set][2]
 k_frf = q[set][3]
# Regulated OFF-->ON (xXF_A)
 kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1  = q[set][4:11]

# Regulated ON-->OFF (Activator 2)
#  kA2_max, n2 = q[set][11:13]
#  K2 = 0.17
#  kA2_min, ksA2, gamma_A2, kA2 = q[set][14:18]
 kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]

# Regulated OFF-->OFFrepr (Activator 1)
 #kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = q[set][18:25]

# Regulated OFFrepr-->OFF (xXF_D)
 #k4_max, n4, K4, k4_min, k4_delay, k4_off, k4_on = q[set][25:32]
 df1 = 1
 df2 = 1
 no_intermediates = 10
 all_allelicstates = []
 j = 0
 while j < 100:
    
    #the whole gillespie code
    S1 = [0]    
    S2 = [0]    
    A1_1 = [1]  
    A2_1 = [1]  
    A1_2 = [1]  
    A2_2 = [1]  
    t = [0]     
    I1_1 = [0] 
    I2_1 = [0]
    I1_2 = [0]
    I2_2 = [0]
    tend = 52
 

    while t[-1] < tend:
        current_A1_1 = A1_1[-1]
        current_A1_2 = A1_2[-1]
        current_S2 = S2[-1]
        current_S1 = S1[-1]
        current_A2_1 = A2_1[-1]
        current_A2_2 = A2_2[-1]
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]
        current_I1_2 = I1_2[-1]
        current_I2_2 = I2_2[-1]
        
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

        # combined hill function , activator 1
        total_activator1 = (current_A1_1 + current_A1_2 )
        if total_activator1 > 0.5:
            total_activator1 -= 0.5
        else:
            total_activator1 = 0
        k_prod_eff1 = ((kA1_max-kA1_min) * k_fo * (total_activator1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2)
        if total_activator2 > 0.5:
            total_activator2 -= 0.5
        else:
            total_activator2 = 0
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

        #chromosome 2
        a1_2 = k_frf * int (current_S2 == -1) 
        a2_2 = k_ffr * int(current_S2 == 0) 
        a3_2 = k_prod_eff1 * int(current_S2 == 0) 
        a4_2 = k_prod_eff2 * int(current_S2 == 1) 
        a5_2 = kA1 * int(current_A1_2==0) * int(current_S2!=1) 
        a6_2 = gamma_A1 * int(current_A1_2) * int(current_S2==1) * int(current_I1_2 >= no_intermediates) 
        a7_2 = kA2 * int(current_A2_2==0) * int(current_S2!=1) 
        a8_2 = gamma_A2 * int(current_A2_2==1) * int(current_S2==1) * int(current_I2_2 >= no_intermediates) 

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2 , i1_1 , i2_1, i1_2 , i2_2]

        rate_sum = sum(rates)

        # time update
        if rate_sum == 0:
            tau = float('inf')
        else:
            tau = np.random.exponential(scale=1 / rate_sum)
        t.append(t[-1] + tau)

        rand = random.uniform(0, 1)
        # event - chromosome 1
        if rand * rate_sum <= a1_1:
            S1.append(0)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1:
            S1.append(-1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
            S1.append(1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
            S1.append(0)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(0)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(0)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        # event - chromosome 2
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2:
            S1.append(current_S1)
            S2.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2:
            S1.append(current_S1)
            S2.append(-1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2:
            S1.append(current_S1)
            S2.append(1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2:
            S1.append(current_S1)
            S2.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(1)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(0)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(0)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        # intermediates
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1 + 1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1 + 1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1 + i1_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2 + 1)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1 + i1_2 + i2_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2 + 1)

    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    b = S2[index]
    if a == 1 and b == 1: 
            all_allelicstates.append(2)
    elif (a == 1 or b == 1) and not (a == 1 and b == 1):
            all_allelicstates.append(1)
    else:
            all_allelicstates.append(0)
    j += 1
 c2 = c1 = c0 = 0
 for row in all_allelicstates:
            if row == 2:
                c2 += 1
            elif row == 1:
                c1 += 1
            elif row == 0:
                c0 += 1
 mean_c2.append(c2)          
 mean_c1.append(c1)
 mean_c0.append(c0)   
 
t_crit_2 = stats.t.ppf(0.975, len(mean_c2)-1)
ci_2 = t_crit_2 * (np.std(mean_c2,ddof=1)/np.sqrt(len(mean_c2))) 

t_crit_1 = stats.t.ppf(0.975, len(mean_c1)-1)
ci_1 = t_crit_1 * (np.std(mean_c1, ddof=1) / np.sqrt(len(mean_c1)))

t_crit_0 = stats.t.ppf(0.975, len(mean_c0)-1)
ci_0 = t_crit_0 * (np.std(mean_c0, ddof=1) / np.sqrt(len(mean_c0)))

print(np.mean(mean_c1))
plt.bar('XX',np.mean(mean_c1), label="XaXi (Monoallelic)", color="#AA3377", width = 0.5,capsize=5,yerr=ci_1 ,ecolor = 'black')
bottom =  np.mean(mean_c1)
plt.bar('XX', np.mean(mean_c2), label="XiXi (Biallelic)", color="#F0E442", bottom=bottom, width = 0.5,capsize=5,yerr=ci_2, ecolor = 'red')
bottom += np.mean(mean_c2)  
plt.bar('XX', np.mean(mean_c0), label="XaXa (Inactive)", color="#E69F00", bottom=bottom, width = 0.5,capsize=5,yerr=ci_0, ecolor = 'black')

mean_c3 = []
mean_c2 = []
mean_c1 = []
mean_c0 = []
for set in range(0,len(q)): #loop for each parameter set

 k_fo,k_of = [1,1]
 k_ffr = q[set][2]
 k_frf = q[set][3]
# Regulated OFF-->ON (xXF_A)
 kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1  = q[set][4:11]

# Regulated ON-->OFF (Activator 2)
 kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]

# Regulated OFF-->OFFrepr (Activator 1)
 #kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = q[set][18:25]

# Regulated OFFrepr-->OFF (xXF_D)
 #k4_max, n4, K4, k4_min, k4_delay, k4_off, k4_on = q[set][25:32]
 df1 = 1
 df2 = 1
 no_intermediates = 10
 all_allelicstates = []
 j = 0
 while j < 100:
    
    #the whole gillespie code
                                       
    #Initial states
    S1 = [0]    # promoter state chromosome 1
    S2 = [0]    # promoter state chromosome 2
    S3 = [0]    # promoter state chromosome 3 
    A1_1 = [1]  # activator1 from chromosome 1
    A2_1 = [1]  # activator2 from chromosome 1
    A1_2 = [1]  # activator1 from chromosome 2
    A2_2 = [1]  # activator2 from chromosome 2
    A1_3 = [1]  # activator1 from chromosome 3
    A2_3 = [1]  # activator2 from chromosome 3
    t = [0]     # time
    I1_1 = [0] # intermediate levels
    I2_1 = [0]
    I1_2 = [0]
    I2_2 = [0]
    I1_3 = [0]
    I2_3 = [0]
    tend = 51
    
    while t[-1] < tend:
        current_S1 = S1[-1]
        current_S2 = S2[-1]
        current_S3 = S3[-1] 
        current_A1_1 = A1_1[-1]
        current_A2_1 = A2_1[-1]
        current_A1_2 = A1_2[-1]
        current_A2_2 = A2_2[-1]
        current_A1_3 = A1_3[-1] 
        current_A2_3 = A2_3[-1] 
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]
        current_I1_2 = I1_2[-1]
        current_I2_2 = I2_2[-1]
        current_I1_3 = I1_3[-1]
        current_I2_3 = I2_3[-1]
        
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
            
        # combined hill function , activator 1
        total_activator1 = (current_A1_1 + current_A1_2 + current_A1_3)
        if total_activator1 > 0.5:
            total_activator1 -= 0.5
        else:
            total_activator1 = 0
        k_prod_eff1 = ((kA1_max-kA1_min) * k_fo * (total_activator1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3)
        if total_activator2 > 0.5:
            total_activator2 -= 0.5
        else:
            total_activator2 = 0
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
        #chromosome 1
        a1_1 = k_frf * int(current_S1 == -1) 
        a2_1 = k_ffr * int(current_S1 == 0) 
        a3_1 = k_prod_eff1 * int(current_S1 == 0) 
        a4_1 = k_prod_eff2 * int(current_S1 == 1) 
        a5_1 = kA1 * int(current_A1_1==0 and current_S1!=1)
        a6_1 = gamma_A1 * int(current_A1_1==1 and current_S1==1 and current_I1_1 >= no_intermediates)
        a7_1 = kA2 * int(current_A2_1==0 and current_S1!=1) 
        a8_1 = gamma_A2 * int(current_A2_1==1 and current_S1==1 and current_I2_1 >= no_intermediates) 

        #chromosome 2
        a1_2 = k_frf * int(current_S2 == -1) 
        a2_2 = k_ffr * int(current_S2 == 0) 
        a3_2 = k_prod_eff1 * int(current_S2 == 0) 
        a4_2 = k_prod_eff2 * int(current_S2 == 1) 
        a5_2 = kA1 * int(current_A1_2==0 and current_S2!=1) 
        a6_2 = gamma_A1 * int(current_A1_2==1 and current_S2==1 and current_I1_2 >= no_intermediates) 
        a7_2 = kA2 * int(current_A2_2==0 and current_S2!=1) 
        a8_2 = gamma_A2 * int(current_A2_2==1 and current_S2==1 and current_I2_2 >= no_intermediates) 

        #chromosome 3
        a1_3 = k_frf * int(current_S3 == -1) #off repressed to off
        a2_3 = k_ffr * int(current_S3 == 0) #off to off repressed
        a3_3 = k_prod_eff1 * int(current_S3 == 0) #off to on
        a4_3 = k_prod_eff2 * int(current_S3 == 1) #on to off
        a5_3 = kA1 * int(current_A1_3==0 and current_S3!=1) #activator 1 OFF to ON
        a6_3 = gamma_A1 * int(current_A1_3==1 and current_S3==1 and current_I1_3 >= no_intermediates) #activator 1 ON to OFF
        a7_3 = kA2 * int(current_A2_3==0 and current_S3!=1) #activator2 OFF to ON
        a8_3 = gamma_A2 * int(current_A2_3==1 and current_S3==1 and current_I2_3 >= no_intermediates)  #activator 2  ON to OFF

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,
                 a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2,
                 a1_3, a2_3, a3_3, a4_3, a5_3, a6_3, a7_3, a8_3,
                 i1_1, i2_1, i1_2, i2_2, i1_3, i2_3]
 

        rate_sum = sum(rates)

        # time update
        if rate_sum == 0:
            tau = float('inf') # No more reactions possible
            t.append(t[-1] + tau)
            break
        else:
            tau = np.random.exponential(scale=1 / rate_sum)
        
        t.append(t[-1] + tau)
        rand = random.uniform(0, 1)

        # event - chromosome 1
        if rand * rate_sum <= a1_1:
            S1.append(0)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1:
            S1.append(-1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
            S1.append(1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
            S1.append(0)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(0)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(0)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        # event - chromosome 2
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2:
            S1.append(current_S1)
            S2.append(0)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2:
            S1.append(current_S1)
            S2.append(-1)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2:
            S1.append(current_S1)
            S2.append(1)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2:
            S1.append(current_S1)
            S2.append(0)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(1)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(0)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(1)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(0)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
         # event - chromosome 3
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(-1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(1)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(0)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(0)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)   

                   #intermediates

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1 + 1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1 + 1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2 + 1)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2 + i2_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2 + 1)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2 + i2_2 + i1_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3 + 1)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2 + i2_2 + i1_3 + i2_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3 + 1)
        

    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    b = S2[index]
    c = S3[index]
    if  a == 1 and b ==1 and c == 1:
                all_allelicstates.append(3)
    elif (a == 1 and b == 1) or (b == 1 and c == 1) or (a == 1 and c == 1) : 
                all_allelicstates.append(2)
    elif (a == 1 or b == 1 or c == 1) and not (a == 1 and b == 1 and c == 1):
                all_allelicstates.append(1)
    else:
                all_allelicstates.append(0)
    j += 1

 c3 = c2 = c1 = c0 = 0
 for row in all_allelicstates:
            if row == 3:
                c3 += 1
            elif row == 2:
                c2 += 1
            elif row == 1:
                c1 += 1
            elif row == 0:
                c0 += 1
 mean_c2.append(c2)
 mean_c1.append(c1)
 mean_c0.append(c0)
 mean_c3.append(c3)  
print(np.mean(mean_c2))
# Confidence intervals
t_crit_2 = stats.t.ppf(0.975, len(mean_c2)-1)
ci_2 = t_crit_2 * (np.std(mean_c2, ddof=1) / np.sqrt(len(mean_c2)))

t_crit_1 = stats.t.ppf(0.975, len(mean_c1)-1)
ci_1 = t_crit_1 * (np.std(mean_c1, ddof=1) / np.sqrt(len(mean_c1)))

t_crit_0 = stats.t.ppf(0.975, len(mean_c0)-1)
ci_0 = t_crit_0 * (np.std(mean_c0, ddof=1) / np.sqrt(len(mean_c0)))

t_crit_3 = stats.t.ppf(0.975, len(mean_c3)-1)
ci_3 = t_crit_3 * (np.std(mean_c3, ddof=1) / np.sqrt(len(mean_c3)))  

# Plotting
plt.bar('XXX(2n)', np.mean(mean_c2), label="XiXi (Biallelic)", color="#F0E442", width = 0.5,capsize=5,yerr=ci_2, ecolor="black")
bottom = np.mean(mean_c2)
plt.bar('XXX(2n)', np.mean(mean_c1), label="XaXi (Monoallelic)", color="#AA3377", bottom=bottom, width = 0.5,capsize=5,yerr=ci_1, ecolor="red")
bottom += np.mean(mean_c1)
plt.bar('XXX(2n)', np.mean(mean_c3), label="XiXiXi (Triallelic)", color="#0072B2", bottom=bottom, width = 0.5,capsize=5,yerr=ci_3, ecolor="black")
bottom += np.mean(mean_c3)
plt.bar('XXX(2n)', np.mean(mean_c0), label="XaXa (Inactive)", color="#E69F00", bottom=bottom, width = 0.5,capsize=5,yerr=ci_0, ecolor="red")

mean_c4 = []
mean_c3 = []
mean_c2 = []
mean_c1 = []
mean_c0 = []
for set in range(0,len(q)): #loop for each parameter set

 k_fo,k_of = [1,1]
 k_ffr = q[set][2]
 k_frf = q[set][3]
# Regulated OFF-->ON (xXF_A)
 kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1  = q[set][4:11]

# Regulated ON-->OFF (Activator 2)
#  kA2_max, n2 = q[set][11:13]
#  K2 = 0.17
#  kA2_min, ksA2, gamma_A2, kA2 = q[set][14:18]
 kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]

# Regulated OFF-->OFFrepr (Activator 1)
 #kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = q[set][18:25]

# Regulated OFFrepr-->OFF (xXF_D)
 #k4_max, n4, K4, k4_min, k4_delay, k4_off, k4_on = q[set][25:32]
 df1 = 1
 df2 = 1
 no_intermediates = 10
 all_allelicstates = []
 j = 0
 while j < 100:
    
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
    t = [0]     # time
    I1_1 = [0] # intermediate levels
    I2_1 = [0]
    I1_2 = [0]
    I2_2 = [0]
    I1_3 = [0]
    I2_3 = [0]
    I1_4 = [0]
    I2_4 = [0]
    tend = 52
    
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
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]
        current_I1_2 = I1_2[-1]
        current_I2_2 = I2_2[-1]
        current_I1_3 = I1_3[-1]
        current_I2_3 = I2_3[-1]
        current_I1_4 = I1_4[-1]
        current_I2_4 = I2_4[-1]
        
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
            
        # combined hill function , activator 1
        total_activator1 = (current_A1_1 + current_A1_2 + current_A1_3 + current_A1_4)
        if total_activator1 > 0.5:
            total_activator1 -= 0.5
        else:
            total_activator1 = 0
        k_prod_eff1 = ((kA1_max-kA1_min) * k_fo * (total_activator1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3 + current_A2_4)
        if total_activator2 > 0.5:
            total_activator2 -= 0.5
        else:
            total_activator2 = 0
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
        #chromosome 1
        a1_1 = k_frf * int(current_S1 == -1) 
        a2_1 = k_ffr * int(current_S1 == 0) 
        a3_1 = k_prod_eff1 * int(current_S1 == 0) 
        a4_1 = k_prod_eff2 * int(current_S1 == 1) 
        a5_1 = kA1 * int(current_A1_1==0 and current_S1!=1)
        a6_1 = gamma_A1 * int(current_A1_1==1 and current_S1==1 and current_I1_1 >= no_intermediates)
        a7_1 = kA2 * int(current_A2_1==0 and current_S1!=1) 
        a8_1 = gamma_A2 * int(current_A2_1==1 and current_S1==1 and current_I2_1 >= no_intermediates) 

        #chromosome 2
        a1_2 = k_frf * int(current_S2 == -1) 
        a2_2 = k_ffr * int(current_S2 == 0) 
        a3_2 = k_prod_eff1 * int(current_S2 == 0) 
        a4_2 = k_prod_eff2 * int(current_S2 == 1) 
        a5_2 = kA1 * int(current_A1_2==0 and current_S2!=1) 
        a6_2 = gamma_A1 * int(current_A1_2==1 and current_S2==1 and current_I1_2 >= no_intermediates) 
        a7_2 = kA2 * int(current_A2_2==0 and current_S2!=1) 
        a8_2 = gamma_A2 * int(current_A2_2==1 and current_S2==1 and current_I2_2 >= no_intermediates) 

        #chromosome 3
        a1_3 = k_frf * int(current_S3 == -1) #off repressed to off
        a2_3 = k_ffr * int(current_S3 == 0) #off to off repressed
        a3_3 = k_prod_eff1 * int(current_S3 == 0) #off to on
        a4_3 = k_prod_eff2 * int(current_S3 == 1) #on to off
        a5_3 = kA1 * int(current_A1_3==0 and current_S3!=1) #activator 1 OFF to ON
        a6_3 = gamma_A1 * int(current_A1_3==1 and current_S3==1 and current_I1_3 >= no_intermediates) #activator 1 ON to OFF
        a7_3 = kA2 * int(current_A2_3==0 and current_S3!=1) #activator2 OFF to ON
        a8_3 = gamma_A2 * int(current_A2_3==1 and current_S3==1 and current_I2_3 >= no_intermediates)  #activator 2  ON to OFF

        #chromosome 4
        a1_4 = k_frf * int(current_S4 == -1) #off repressed to off
        a2_4 = k_ffr * int(current_S4 == 0) #off to off repressed
        a3_4 = k_prod_eff1 * int(current_S4 == 0) #off to on
        a4_4 = k_prod_eff2 * int(current_S4 == 1) #on to off
        a5_4 = kA1 * int(current_A1_4==0 and current_S4!=1) #activator 1 OFF to ON
        a6_4 = gamma_A1 * int(current_A1_4==1 and current_S4==1 and current_I1_4 >= no_intermediates) #activator 1 ON to OFF
        a7_4 = kA2 * int(current_A2_4==0 and current_S4!=1) #activator2 OFF to ON
        a8_4 = gamma_A2 * int(current_A2_4==1 and current_S4==1 and current_I2_4 >= no_intermediates)  #activator 2  ON to OFF

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,
                 a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2,
                 a1_3, a2_3, a3_3, a4_3, a5_3, a6_3, a7_3, a8_3,
                 a1_4, a2_4, a3_4, a4_4, a5_4, a6_4, a7_4, a8_4,
                 i1_1, i2_1, i1_2, i2_2, i1_3, i2_3, i1_4, i2_4]
 

        rate_sum = sum(rates)

        # time update
        if rate_sum == 0:
            tau = float('inf') # No more reactions possible
            t.append(t[-1] + tau)
            break
        else:
            tau = np.random.exponential(scale=1 / rate_sum)
        
        t.append(t[-1] + tau)
        rand = random.uniform(0, 1)

        # event - chromosome 1
        if rand * rate_sum <= a1_1:
            S1.append(0)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1:
            S1.append(-1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
            S1.append(1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
            S1.append(0)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(0)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(0)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        # event - chromosome 2
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2:
            S1.append(current_S1)
            S2.append(0)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2:
            S1.append(current_S1)
            S2.append(-1)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2:
            S1.append(current_S1)
            S2.append(1)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2:
            S1.append(current_S1)
            S2.append(0)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(1)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(0)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(1)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(0)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)
            
         # event - chromosome 3
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(0)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(-1)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(1)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(0)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(1)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(0)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(1)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(0)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        # event - chromosome 4
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(-1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4 + a5_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(1)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4 + a5_4 + a6_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(0)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4 + a5_4 + a6_4 + a7_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4 + a5_4 + a6_4 + a7_4 + a8_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(0)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

                   #intermediates
        elif rand * rate_sum <= sum(rates[:32]) + i1_1:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1 + 1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1 + 1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2 + 1); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2 + 1)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2 + i1_3:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3 + 1); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2 + i1_3 + i2_3:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3 + 1); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2 + i1_3 + i2_3 + i1_4:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4 + 1); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2 + i1_3 + i2_3 + i1_4 + i2_4:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4 + 1)
        
    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    b = S2[index]
    c = S3[index]
    d = S4[index]
    if a == 1 and b == 1 and c == 1 and d == 1:
                all_allelicstates.append(4)
    elif (a == 1 and b == 1 and c == 1) or \
                 (a == 1 and b == 1 and d == 1) or \
                 (a == 1 and c == 1 and d == 1) or \
                 (b == 1 and c == 1 and d == 1):
                all_allelicstates.append(3)
    elif (a == 1 and b == 1) or (a == 1 and c == 1) or (a == 1 and d == 1) or \
                 (b == 1 and c == 1) or (b == 1 and d == 1) or (c == 1 and d == 1):
                all_allelicstates.append(2)
    elif a == 1 or b == 1 or c == 1 or d == 1:
                all_allelicstates.append(1)
    else:
                all_allelicstates.append(0)
    j += 1

 c4 = c3 = c2 = c1 = c0 = 0
 for row in all_allelicstates:
            if row == 4:
                c4 += 1
            elif row == 3:
                c3 += 1
            elif row == 2:
                c2 += 1
            elif row == 1:
                c1 += 1
            elif row == 0:
                c0 += 1
   

 mean_c2.append(c2)
 mean_c1.append(c1)
 mean_c0.append(c0)
 mean_c3.append(c3)
 mean_c4.append(c4)

t_crit_2 = stats.t.ppf(0.975, len(mean_c2)-1)
ci_2 = t_crit_2 * (np.std(mean_c2, ddof=1) / np.sqrt(len(mean_c2)))

t_crit_1 = stats.t.ppf(0.975, len(mean_c1)-1)
ci_1 = t_crit_1 * (np.std(mean_c1, ddof=1) / np.sqrt(len(mean_c1)))

t_crit_0 = stats.t.ppf(0.975, len(mean_c0)-1)
ci_0 = t_crit_0 * (np.std(mean_c0, ddof=1) / np.sqrt(len(mean_c0)))

t_crit_3 = stats.t.ppf(0.975, len(mean_c3)-1)
ci_3 = t_crit_3 * (np.std(mean_c3, ddof=1) / np.sqrt(len(mean_c3)))

t_crit_4 = stats.t.ppf(0.975, len(mean_c4)-1)
ci_4 = t_crit_4 * (np.std(mean_c4, ddof=1) / np.sqrt(len(mean_c4)))

print(np.mean(mean_c3))
plt.bar('XXXX(2n)', np.mean(mean_c3), label="XiXiXi (Triallelic)", color="#0072B2", width = 0.5,capsize=5,yerr=ci_3, ecolor="black")
bottom = np.mean(mean_c3)
plt.bar('XXXX(2n)', np.mean(mean_c2), label="XiXi (Biallelic)", color="#F0E442", bottom=bottom, width = 0.5,capsize=5,yerr=ci_2, ecolor="red")
bottom += np.mean(mean_c2)
plt.bar('XXXX(2n)', np.mean(mean_c1), label="XaXi (Monoallelic)", color="#AA3377", bottom=bottom, width = 0.5,capsize=5,yerr=ci_1, ecolor="black")
bottom += np.mean(mean_c1)
plt.bar('XXXX(2n)', np.mean(mean_c0), label="Inactive", color="#E69F00", bottom=bottom, width = 0.5,capsize=5,yerr=ci_0, ecolor="red")
bottom +=np.mean(mean_c0)
plt.bar('XXXX(2n)', np.mean(mean_c4), label="XiXiXiXi(Tetra-allelic)", color="#D55E00", bottom=bottom, width = 0.5,capsize=5,yerr=ci_4, ecolor="black")


mean_c3 = []
mean_c2 = []
mean_c1 = []
mean_c0 = []
for set in range(0,len(q)): #loop for each parameter set

 k_fo,k_of = [1,1]
 k_ffr = q[set][2]
 k_frf = q[set][3]
# Regulated OFF-->ON (xXF_A)
 kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1  = q[set][4:11]

# Regulated ON-->OFF (Activator 2)

 kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]

# Regulated OFF-->OFFrepr (Activator 1)
 #kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = q[set][18:25]

# Regulated OFFrepr-->OFF (xXF_D)
 #k4_max, n4, K4, k4_min, k4_delay, k4_off, k4_on = q[set][25:32]
 df1 = 1.5
 df2 = 1.5
 no_intermediates = 10
 all_allelicstates = []
 j = 0
 while j < 100:
    
    #the whole gillespie code
                                       
    #Initial states
    S1 = [0]    # promoter state chromosome 1
    S2 = [0]    # promoter state chromosome 2
    S3 = [0]    # promoter state chromosome 3 
    A1_1 = [1]  # activator1 from chromosome 1
    A2_1 = [1]  # activator2 from chromosome 1
    A1_2 = [1]  # activator1 from chromosome 2
    A2_2 = [1]  # activator2 from chromosome 2
    A1_3 = [1]  # activator1 from chromosome 3
    A2_3 = [1]  # activator2 from chromosome 3
    t = [0]     # time
    I1_1 = [0] # intermediate levels
    I2_1 = [0]
    I1_2 = [0]
    I2_2 = [0]
    I1_3 = [0]
    I2_3 = [0]
    tend = 51
    
    while t[-1] < tend:
        current_S1 = S1[-1]
        current_S2 = S2[-1]
        current_S3 = S3[-1] 
        current_A1_1 = A1_1[-1]
        current_A2_1 = A2_1[-1]
        current_A1_2 = A1_2[-1]
        current_A2_2 = A2_2[-1]
        current_A1_3 = A1_3[-1] 
        current_A2_3 = A2_3[-1] 
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]
        current_I1_2 = I1_2[-1]
        current_I2_2 = I2_2[-1]
        current_I1_3 = I1_3[-1]
        current_I2_3 = I2_3[-1]
        
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
            
        # combined hill function , activator 1
        total_activator1 = (current_A1_1 + current_A1_2 + current_A1_3)
        if total_activator1 > 0.75:
            total_activator1 -= 0.75
        else:
            total_activator1 = 0
        k_prod_eff1 = ((kA1_max-kA1_min) * k_fo * (total_activator1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3)
        if total_activator2 > 0.75:
            total_activator2 -= 0.75
        else:
            total_activator2 = 0
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        #chromosome 1
        a1_1 = k_frf * int(current_S1 == -1) 
        a2_1 = k_ffr * int(current_S1 == 0) 
        a3_1 = k_prod_eff1 * int(current_S1 == 0) 
        a4_1 = k_prod_eff2 * int(current_S1 == 1) 
        a5_1 = kA1 * int(current_A1_1==0 and current_S1!=1)
        a6_1 = gamma_A1 * int(current_A1_1==1 and current_S1==1 and current_I1_1 >= no_intermediates)
        a7_1 = kA2 * int(current_A2_1==0 and current_S1!=1) 
        a8_1 = gamma_A2 * int(current_A2_1==1 and current_S1==1 and current_I2_1 >= no_intermediates) 

        #chromosome 2
        a1_2 = k_frf * int(current_S2 == -1) 
        a2_2 = k_ffr * int(current_S2 == 0) 
        a3_2 = k_prod_eff1 * int(current_S2 == 0) 
        a4_2 = k_prod_eff2 * int(current_S2 == 1) 
        a5_2 = kA1 * int(current_A1_2==0 and current_S2!=1) 
        a6_2 = gamma_A1 * int(current_A1_2==1 and current_S2==1 and current_I1_2 >= no_intermediates) 
        a7_2 = kA2 * int(current_A2_2==0 and current_S2!=1) 
        a8_2 = gamma_A2 * int(current_A2_2==1 and current_S2==1 and current_I2_2 >= no_intermediates) 

        #chromosome 3
        a1_3 = k_frf * int(current_S3 == -1) #off repressed to off
        a2_3 = k_ffr * int(current_S3 == 0) #off to off repressed
        a3_3 = k_prod_eff1 * int(current_S3 == 0) #off to on
        a4_3 = k_prod_eff2 * int(current_S3 == 1) #on to off
        a5_3 = kA1 * int(current_A1_3==0 and current_S3!=1) #activator 1 OFF to ON
        a6_3 = gamma_A1 * int(current_A1_3==1 and current_S3==1 and current_I1_3 >= no_intermediates) #activator 1 ON to OFF
        a7_3 = kA2 * int(current_A2_3==0 and current_S3!=1) #activator2 OFF to ON
        a8_3 = gamma_A2 * int(current_A2_3==1 and current_S3==1 and current_I2_3 >= no_intermediates)  #activator 2  ON to OFF

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,
                 a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2,
                 a1_3, a2_3, a3_3, a4_3, a5_3, a6_3, a7_3, a8_3,
                 i1_1, i2_1, i1_2, i2_2, i1_3, i2_3]
 

        rate_sum = sum(rates)

        # time update
        if rate_sum == 0:
            tau = float('inf') # No more reactions possible
            t.append(t[-1] + tau)
            break
        else:
            tau = np.random.exponential(scale=1 / rate_sum)
        
        t.append(t[-1] + tau)
        rand = random.uniform(0, 1)

        # event - chromosome 1
        if rand * rate_sum <= a1_1:
            S1.append(0)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1:
            S1.append(-1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
            S1.append(1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
            S1.append(0)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(0)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(0)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        # event - chromosome 2
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2:
            S1.append(current_S1)
            S2.append(0)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2:
            S1.append(current_S1)
            S2.append(-1)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2:
            S1.append(current_S1)
            S2.append(1)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2:
            S1.append(current_S1)
            S2.append(0)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(1)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(0)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(1)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(0)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
         # event - chromosome 3
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(-1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(1)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(0)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(0)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)   

                   #intermediates

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1 + 1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1 + 1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2 + 1)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2 + i2_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2 + 1)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2 + i2_2 + i1_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3 + 1)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2 + i2_2 + i1_3 + i2_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3 + 1)
        

    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    b = S2[index]
    c = S3[index]
    if  a == 1 and b ==1 and c == 1:
                all_allelicstates.append(3)
    elif (a == 1 and b == 1) or (b == 1 and c == 1) or (a == 1 and c == 1) : 
                all_allelicstates.append(2)
    elif (a == 1 or b == 1 or c == 1) and not (a == 1 and b == 1 and c == 1):
                all_allelicstates.append(1)
    else:
                all_allelicstates.append(0)
    j += 1

 c3 = c2 = c1 = c0 = 0
 for row in all_allelicstates:
            if row == 3:
                c3 += 1
            elif row == 2:
                c2 += 1
            elif row == 1:
                c1 += 1
            elif row == 0:
                c0 += 1
 mean_c2.append(c2)
 mean_c1.append(c1)
 mean_c0.append(c0)
 mean_c3.append(c3)  

# Confidence intervals
t_crit_2 = stats.t.ppf(0.975, len(mean_c2)-1)
ci_2 = t_crit_2 * (np.std(mean_c2, ddof=1) / np.sqrt(len(mean_c2)))

t_crit_1 = stats.t.ppf(0.975, len(mean_c1)-1)
ci_1 = t_crit_1 * (np.std(mean_c1, ddof=1) / np.sqrt(len(mean_c1)))

t_crit_0 = stats.t.ppf(0.975, len(mean_c0)-1)
ci_0 = t_crit_0 * (np.std(mean_c0, ddof=1) / np.sqrt(len(mean_c0)))

t_crit_3 = stats.t.ppf(0.975, len(mean_c3)-1)
ci_3 = t_crit_3 * (np.std(mean_c3, ddof=1) / np.sqrt(len(mean_c3)))  
print([np.mean(mean_c1),np.mean(mean_c2)])
# Plotting
plt.bar('XXX(3n)', np.mean(mean_c2), label="XiXi (Biallelic)", color="#F0E442", width = 0.5,capsize=5,yerr=ci_2, ecolor="black")
bottom = np.mean(mean_c2)
plt.bar('XXX(3n)', np.mean(mean_c1), label="XaXi (Monoallelic)", color="#AA3377", bottom=bottom, width = 0.5,capsize=5,yerr=ci_1, ecolor="red")
bottom += np.mean(mean_c1)
plt.bar('XXX(3n)', np.mean(mean_c3), label="XiXiXi (Triallelic)", color="#0072B2", bottom=bottom, width = 0.5,capsize=5,yerr=ci_3, ecolor="black")
bottom += np.mean(mean_c3)
plt.bar('XXX(3n)', np.mean(mean_c0), label="XaXa (Inactive)", color="#E69F00", bottom=bottom, width = 0.5,capsize=5,yerr=ci_0, ecolor="red")

mean_c4 = []
mean_c3 = []
mean_c2 = []
mean_c1 = []
mean_c0 = []
for set in range(0,len(q)): #loop for each parameter set

 k_fo,k_of = [1,1]
 k_ffr = q[set][2]
 k_frf = q[set][3]
# Regulated OFF-->ON (xXF_A)
 kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1  = q[set][4:11]

# Regulated ON-->OFF (Activator 2)
#  kA2_max, n2 = q[set][11:13]
#  K2 = 0.17
#  kA2_min, ksA2, gamma_A2, kA2 = q[set][14:18]
 kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]

# Regulated OFF-->OFFrepr (Activator 1)
 #kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = q[set][18:25]

# Regulated OFFrepr-->OFF (xXF_D)
 #k4_max, n4, K4, k4_min, k4_delay, k4_off, k4_on = q[set][25:32]
 df1 = 2
 df2 = 2
 no_intermediates = 10
 all_allelicstates = []
 j = 0
 while j < 100:
    
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
    t = [0]     # time
    I1_1 = [0] # intermediate levels
    I2_1 = [0]
    I1_2 = [0]
    I2_2 = [0]
    I1_3 = [0]
    I2_3 = [0]
    I1_4 = [0]
    I2_4 = [0]
    tend = 51
    
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
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]
        current_I1_2 = I1_2[-1]
        current_I2_2 = I2_2[-1]
        current_I1_3 = I1_3[-1]
        current_I2_3 = I2_3[-1]
        current_I1_4 = I1_4[-1]
        current_I2_4 = I2_4[-1]
        
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
            
        # combined hill function , activator 1
        total_activator1 = (current_A1_1 + current_A1_2 + current_A1_3 + current_A1_4)
        if total_activator1 > 1:
            total_activator1 -= 1
        else:
            total_activator1 = 0
        k_prod_eff1 = ((kA1_max-kA1_min) * k_fo * (total_activator1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3 + current_A2_4)
        if total_activator2 > 1:
            total_activator2 -= 1
        else:
            total_activator2 = 0
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
        #chromosome 1
        a1_1 = k_frf * int(current_S1 == -1) 
        a2_1 = k_ffr * int(current_S1 == 0) 
        a3_1 = k_prod_eff1 * int(current_S1 == 0) 
        a4_1 = k_prod_eff2 * int(current_S1 == 1) 
        a5_1 = kA1 * int(current_A1_1==0 and current_S1!=1)
        a6_1 = gamma_A1 * int(current_A1_1==1 and current_S1==1 and current_I1_1 >= no_intermediates)
        a7_1 = kA2 * int(current_A2_1==0 and current_S1!=1) 
        a8_1 = gamma_A2 * int(current_A2_1==1 and current_S1==1 and current_I2_1 >= no_intermediates) 

        #chromosome 2
        a1_2 = k_frf * int(current_S2 == -1) 
        a2_2 = k_ffr * int(current_S2 == 0) 
        a3_2 = k_prod_eff1 * int(current_S2 == 0) 
        a4_2 = k_prod_eff2 * int(current_S2 == 1) 
        a5_2 = kA1 * int(current_A1_2==0 and current_S2!=1) 
        a6_2 = gamma_A1 * int(current_A1_2==1 and current_S2==1 and current_I1_2 >= no_intermediates) 
        a7_2 = kA2 * int(current_A2_2==0 and current_S2!=1) 
        a8_2 = gamma_A2 * int(current_A2_2==1 and current_S2==1 and current_I2_2 >= no_intermediates) 

        #chromosome 3
        a1_3 = k_frf * int(current_S3 == -1) #off repressed to off
        a2_3 = k_ffr * int(current_S3 == 0) #off to off repressed
        a3_3 = k_prod_eff1 * int(current_S3 == 0) #off to on
        a4_3 = k_prod_eff2 * int(current_S3 == 1) #on to off
        a5_3 = kA1 * int(current_A1_3==0 and current_S3!=1) #activator 1 OFF to ON
        a6_3 = gamma_A1 * int(current_A1_3==1 and current_S3==1 and current_I1_3 >= no_intermediates) #activator 1 ON to OFF
        a7_3 = kA2 * int(current_A2_3==0 and current_S3!=1) #activator2 OFF to ON
        a8_3 = gamma_A2 * int(current_A2_3==1 and current_S3==1 and current_I2_3 >= no_intermediates)  #activator 2  ON to OFF

        #chromosome 4
        a1_4 = k_frf * int(current_S4 == -1) #off repressed to off
        a2_4 = k_ffr * int(current_S4 == 0) #off to off repressed
        a3_4 = k_prod_eff1 * int(current_S4 == 0) #off to on
        a4_4 = k_prod_eff2 * int(current_S4 == 1) #on to off
        a5_4 = kA1 * int(current_A1_4==0 and current_S4!=1) #activator 1 OFF to ON
        a6_4 = gamma_A1 * int(current_A1_4==1 and current_S4==1 and current_I1_4 >= no_intermediates) #activator 1 ON to OFF
        a7_4 = kA2 * int(current_A2_4==0 and current_S4!=1) #activator2 OFF to ON
        a8_4 = gamma_A2 * int(current_A2_4==1 and current_S4==1 and current_I2_4 >= no_intermediates)  #activator 2  ON to OFF

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,
                 a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2,
                 a1_3, a2_3, a3_3, a4_3, a5_3, a6_3, a7_3, a8_3,
                 a1_4, a2_4, a3_4, a4_4, a5_4, a6_4, a7_4, a8_4,
                 i1_1, i2_1, i1_2, i2_2, i1_3, i2_3, i1_4, i2_4]
 

        rate_sum = sum(rates)

        # time update
        if rate_sum == 0:
            tau = float('inf') # No more reactions possible
            t.append(t[-1] + tau)
            break
        else:
            tau = np.random.exponential(scale=1 / rate_sum)
        
        t.append(t[-1] + tau)
        rand = random.uniform(0, 1)

        # event - chromosome 1
        if rand * rate_sum <= a1_1:
            S1.append(0)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1:
            S1.append(-1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
            S1.append(1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
            S1.append(0)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(0)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(0)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        # event - chromosome 2
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2:
            S1.append(current_S1)
            S2.append(0)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2:
            S1.append(current_S1)
            S2.append(-1)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2:
            S1.append(current_S1)
            S2.append(1)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2:
            S1.append(current_S1)
            S2.append(0)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(1)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(0)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(1)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(0)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)
            
         # event - chromosome 3
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(0)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(-1)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(1)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(0)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(1)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(0)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(1)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(0)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        # event - chromosome 4
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(-1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4 + a5_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(1)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4 + a5_4 + a6_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(0)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4 + a5_4 + a6_4 + a7_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4 + a5_4 + a6_4 + a7_4 + a8_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(0)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

                   #intermediates
        elif rand * rate_sum <= sum(rates[:32]) + i1_1:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1 + 1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1 + 1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2 + 1); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2 + 1)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2 + i1_3:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3 + 1); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2 + i1_3 + i2_3:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3 + 1); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2 + i1_3 + i2_3 + i1_4:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4 + 1); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2 + i1_3 + i2_3 + i1_4 + i2_4:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4 + 1)
        
    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    b = S2[index]
    c = S3[index]
    d = S4[index]
    if a == 1 and b == 1 and c == 1 and d == 1:
                all_allelicstates.append(4)
    elif (a == 1 and b == 1 and c == 1) or \
                 (a == 1 and b == 1 and d == 1) or \
                 (a == 1 and c == 1 and d == 1) or \
                 (b == 1 and c == 1 and d == 1):
                all_allelicstates.append(3)
    elif (a == 1 and b == 1) or (a == 1 and c == 1) or (a == 1 and d == 1) or \
                 (b == 1 and c == 1) or (b == 1 and d == 1) or (c == 1 and d == 1):
                all_allelicstates.append(2)
    elif a == 1 or b == 1 or c == 1 or d == 1:
                all_allelicstates.append(1)
    else:
                all_allelicstates.append(0)
    j += 1

 c4 = c3 = c2 = c1 = c0 = 0
 for row in all_allelicstates:
            if row == 4:
                c4 += 1
            elif row == 3:
                c3 += 1
            elif row == 2:
                c2 += 1
            elif row == 1:
                c1 += 1
            elif row == 0:
                c0 += 1

 mean_c2.append(c2)
 mean_c1.append(c1)
 mean_c0.append(c0)
 mean_c3.append(c3)
 mean_c4.append(c4)

t_crit_2 = stats.t.ppf(0.975, len(mean_c2)-1)
ci_2 = t_crit_2 * (np.std(mean_c2, ddof=1) / np.sqrt(len(mean_c2)))

t_crit_1 = stats.t.ppf(0.975, len(mean_c1)-1)
ci_1 = t_crit_1 * (np.std(mean_c1, ddof=1) / np.sqrt(len(mean_c1)))

t_crit_0 = stats.t.ppf(0.975, len(mean_c0)-1)
ci_0 = t_crit_0 * (np.std(mean_c0, ddof=1) / np.sqrt(len(mean_c0)))

t_crit_3 = stats.t.ppf(0.975, len(mean_c3)-1)
ci_3 = t_crit_3 * (np.std(mean_c3, ddof=1) / np.sqrt(len(mean_c3)))

t_crit_4 = stats.t.ppf(0.975, len(mean_c4)-1)
ci_4 = t_crit_4 * (np.std(mean_c4, ddof=1) / np.sqrt(len(mean_c4)))

print(np.mean(mean_c2))
plt.bar('XXXX(4n)', np.mean(mean_c2), label="XiXi (Biallelic)", color="#F0E442", width = 0.5,capsize=5,yerr=ci_2, ecolor="black")
bottom = np.mean(mean_c2)

plt.bar('XXXX(4n)', np.mean(mean_c3), label="XiXiXi (Triallelic)", color="#0072B2", bottom=bottom, width = 0.5,capsize=5,yerr=ci_3, ecolor="red")
bottom += np.mean(mean_c3)

plt.bar('XXXX(4n)', np.mean(mean_c1), label="XaXi (Monoallelic)", color="#AA3377", bottom=bottom, width = 0.5,capsize=5,yerr=ci_1, ecolor = "black")
bottom += np.mean(mean_c1)

plt.bar('XXXX(4n)', np.mean(mean_c4), label="XiXiXiXi (Tetra-allelic)", color="#D55E00", bottom=bottom, width = 0.5,capsize=5,yerr=ci_4, ecolor="red")
bottom += np.mean(mean_c4)

plt.bar('XXXX(4n)', np.mean(mean_c0), label="XaO (Inactive)", color="#E69F00",bottom = bottom,  width = 0.5,capsize=5,yerr=ci_0 , ecolor = 'black')
                      
#                            #XXXY
# mean_c4 = []
# mean_c3 = []
# mean_c2 = []
# mean_c1 = []
# mean_c0 = []
# for set in range(0,len(q)): #loop for each parameter set

#  k_fo,k_of = [1,1]
#  k_ffr = q[set][2]
#  k_frf = q[set][3]
# # Regulated OFF-->ON (xXF_A)
#  kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1  = q[set][4:11]

# # Regulated ON-->OFF (Activator 2)
# #  kA2_max, n2 = q[set][11:13]
# #  K2 = 0.17
# #  kA2_min, ksA2, gamma_A2, kA2 = q[set][14:18]
#  kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]

# # Regulated OFF-->OFFrepr (Activator 1)
#  #kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = q[set][18:25]

# # Regulated OFFrepr-->OFF (xXF_D)
#  #k4_max, n4, K4, k4_min, k4_delay, k4_off, k4_on = q[set][25:32]
#  df1 = 2
#  df2 = 2
#  no_intermediates = 10
#  all_allelicstates = []
#  j = 0
#  while j < 100:
    
#     #the whole gillespie code
                                       
#     #Initial states
#     S1 = [0]    # promoter state chromosome 1
#     S2 = [0]    # promoter state chromosome 2
#     S3 = [0]    # promoter state chromosome 3 
#     A1_1 = [1]  # activator1 from chromosome 1
#     A2_1 = [1]  # activator2 from chromosome 1
#     A1_2 = [1]  # activator1 from chromosome 2
#     A2_2 = [1]  # activator2 from chromosome 2
#     A1_3 = [1]  # activator1 from chromosome 3
#     A2_3 = [1]  # activator2 from chromosome 3
#     t = [0]     # time
#     I1_1 = [0] # intermediate levels
#     I2_1 = [0]
#     I1_2 = [0]
#     I2_2 = [0]
#     I1_3 = [0]
#     I2_3 = [0]
#     tend = 51
    
#     while t[-1] < tend:
#         current_S1 = S1[-1]
#         current_S2 = S2[-1]
#         current_S3 = S3[-1] 
#         current_A1_1 = A1_1[-1]
#         current_A2_1 = A2_1[-1]
#         current_A1_2 = A1_2[-1]
#         current_A2_2 = A2_2[-1]
#         current_A1_3 = A1_3[-1] 
#         current_A2_3 = A2_3[-1] 
#         current_I1_1 = I1_1[-1]
#         current_I2_1 = I2_1[-1]
#         current_I1_2 = I1_2[-1]
#         current_I2_2 = I2_2[-1]
#         current_I1_3 = I1_3[-1]
#         current_I2_3 = I2_3[-1]
        
#         # for I1_1
#         if I1_1[-1] < no_intermediates:
#             i1_1 = ksA1 * int(current_S1 == 1)
#         else:
#             i1_1 = 0

#         # for I2_1
#         if I2_1[-1] < no_intermediates:
#             i2_1 = ksA2 * int(current_S1 == 1)
#         else:
#             i2_1 = 0

#         # for I1_2
#         if I1_2[-1] < no_intermediates:
#             i1_2 = ksA1 * int(current_S2 == 1)
#         else:
#             i1_2 = 0

#         #  for I2_2
#         if I2_2[-1] < no_intermediates:
#             i2_2 = ksA2 * int(current_S2 == 1)
#         else:
#             i2_2 = 0   

#        # for I1_3
#         if I1_3[-1] < no_intermediates:
#             i1_3 = ksA1 * int(current_S3 == 1)
#         else:
#             i1_3 = 0

#         #  for I2_3
#         if I2_3[-1] < no_intermediates:
#             i2_3 = ksA2 * int(current_S3 == 1)
#         else:
#             i2_3 = 0         
            
#         # combined hill function , activator 1
#         total_activator1 = (current_A1_1 + current_A1_2 + current_A1_3)  /  df1
#         k_prod_eff1 = ((kA1_max-kA1_min) * k_fo * (total_activator1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min

#         # combined hill function , activator 2
#         total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3)  / df2
#         k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min
        
#         #chromosome 1
#         a1_1 = k_frf * int(current_S1 == -1) 
#         a2_1 = k_ffr * int(current_S1 == 0) 
#         a3_1 = k_prod_eff1 * int(current_S1 == 0) 
#         a4_1 = k_prod_eff2 * int(current_S1 == 1) 
#         a5_1 = kA1 * int(current_A1_1==0 and current_S1!=1)
#         a6_1 = gamma_A1 * int(current_A1_1==1 and current_S1==1 and current_I1_1 >= no_intermediates)
#         a7_1 = kA2 * int(current_A2_1==0 and current_S1!=1) 
#         a8_1 = gamma_A2 * int(current_A2_1==1 and current_S1==1 and current_I2_1 >= no_intermediates) 

#         #chromosome 2
#         a1_2 = k_frf * int(current_S2 == -1) 
#         a2_2 = k_ffr * int(current_S2 == 0) 
#         a3_2 = k_prod_eff1 * int(current_S2 == 0) 
#         a4_2 = k_prod_eff2 * int(current_S2 == 1) 
#         a5_2 = kA1 * int(current_A1_2==0 and current_S2!=1) 
#         a6_2 = gamma_A1 * int(current_A1_2==1 and current_S2==1 and current_I1_2 >= no_intermediates) 
#         a7_2 = kA2 * int(current_A2_2==0 and current_S2!=1) 
#         a8_2 = gamma_A2 * int(current_A2_2==1 and current_S2==1 and current_I2_2 >= no_intermediates) 

#         #chromosome 3
#         a1_3 = k_frf * int(current_S3 == -1) #off repressed to off
#         a2_3 = k_ffr * int(current_S3 == 0) #off to off repressed
#         a3_3 = k_prod_eff1 * int(current_S3 == 0) #off to on
#         a4_3 = k_prod_eff2 * int(current_S3 == 1) #on to off
#         a5_3 = kA1 * int(current_A1_3==0 and current_S3!=1) #activator 1 OFF to ON
#         a6_3 = gamma_A1 * int(current_A1_3==1 and current_S3==1 and current_I1_3 >= no_intermediates) #activator 1 ON to OFF
#         a7_3 = kA2 * int(current_A2_3==0 and current_S3!=1) #activator2 OFF to ON
#         a8_3 = gamma_A2 * int(current_A2_3==1 and current_S3==1 and current_I2_3 >= no_intermediates)  #activator 2  ON to OFF

#         rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,
#                  a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2,
#                  a1_3, a2_3, a3_3, a4_3, a5_3, a6_3, a7_3, a8_3,
#                  i1_1, i2_1, i1_2, i2_2, i1_3, i2_3]
 

#         rate_sum = sum(rates)

#         # time update
#         if rate_sum == 0:
#             tau = float('inf') # No more reactions possible
#             t.append(t[-1] + tau)
#             break
#         else:
#             tau = np.random.exponential(scale=1 / rate_sum)
        
#         t.append(t[-1] + tau)
#         rand = random.uniform(0, 1)

#         # event - chromosome 1
#         if rand * rate_sum <= a1_1:
#             S1.append(0)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1:
#             S1.append(-1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
#             S1.append(1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
#             S1.append(0)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(0)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(0)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         # event - chromosome 2
#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2:
#             S1.append(current_S1)
#             S2.append(0)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2:
#             S1.append(current_S1)
#             S2.append(-1)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2:
#             S1.append(current_S1)
#             S2.append(1)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2:
#             S1.append(current_S1)
#             S2.append(0)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(1)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(0)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(1)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(0)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)
#          # event - chromosome 3
#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
#              a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(0)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
#              a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(-1)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
#              a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(1)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
#              a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(0)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
#              a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(1)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
#              a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(0)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
#              a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(1)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
#              a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(0)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)   

#                    #intermediates

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
#              a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
#              a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1 + 1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
#              a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
#              a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1 + 1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
#              a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
#              a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2 + 1)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
#              a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
#              a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2 + i2_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2 + 1)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
#              a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
#              a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2 + i2_2 + i1_3:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3 + 1)
#             I2_3.append(current_I2_3)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
#              a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
#              a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2 + i2_2 + i1_3 + i2_3:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             S3.append(current_S3)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             A1_3.append(current_A1_3)
#             A2_3.append(current_A2_3)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)
#             I1_3.append(current_I1_3)
#             I2_3.append(current_I2_3 + 1)
        

#     index = np.searchsorted(t,50,side = 'right') - 1
#     a = S1[index]
#     b = S2[index]
#     c = S3[index]
#     if  a == 1 and b ==1 and c == 1:
#                 all_allelicstates.append(3)
#     elif (a == 1 and b == 1) or (b == 1 and c == 1) or (a == 1 and c == 1) : 
#                 all_allelicstates.append(2)
#     elif (a == 1 or b == 1 or c == 1) and not (a == 1 and b == 1 and c == 1):
#                 all_allelicstates.append(1)
#     else:
#                 all_allelicstates.append(0)
#     j += 1

#  c3 = c2 = c1 = c0 = 0
#  for row in all_allelicstates:
#             if row == 3:
#                 c3 += 1
#             elif row == 2:
#                 c2 += 1
#             elif row == 1:
#                 c1 += 1
#             elif row == 0:
#                 c0 += 1

#  mean_c2.append(c2)
#  mean_c1.append(c1)
#  mean_c0.append(c0)
#  mean_c3.append(c3)

# t_crit_2 = stats.t.ppf(0.975, len(mean_c2)-1)
# ci_2 = t_crit_2 * (np.std(mean_c2, ddof=1) / np.sqrt(len(mean_c2)))

# t_crit_1 = stats.t.ppf(0.975, len(mean_c1)-1)
# ci_1 = t_crit_1 * (np.std(mean_c1, ddof=1) / np.sqrt(len(mean_c1)))

# t_crit_0 = stats.t.ppf(0.975, len(mean_c0)-1)
# ci_0 = t_crit_0 * (np.std(mean_c0, ddof=1) / np.sqrt(len(mean_c0)))

# t_crit_3 = stats.t.ppf(0.975, len(mean_c3)-1)
# ci_3 = t_crit_3 * (np.std(mean_c3, ddof=1) / np.sqrt(len(mean_c3)))


# print(np.mean(mean_c1))
# plt.bar('XXXY', np.mean(mean_c1), label="XaXi (Monoallelic)", color="#AA3377", width = 0.5,capsize=5,yerr=ci_1, ecolor="red")
# bottom = np.mean(mean_c1)

# plt.bar('XXXY', np.mean(mean_c2), label="XiXi (Biallelic)", color="#F0E442", width = 0.5,capsize=5,yerr=ci_2, bottom=bottom, ecolor="red")
# bottom += np.mean(mean_c2)

# plt.bar('XXXY', np.mean(mean_c3), label="XiXiXi (Triallelic)", color="#0072B2", bottom=bottom, width = 0.5,capsize=5,yerr=ci_3, ecolor="red")
# bottom += np.mean(mean_c3)

# plt.bar('XXXY', np.mean(mean_c0), label="XaXaXaY (Inactive)", color="#E69F00",bottom = bottom,  width = 0.5,capsize=5,yerr=ci_0 , ecolor = 'red')


 
#                                  #XXY

# mean_c2 = []
# mean_c1 = []
# mean_c0 = []
# for set in range(0,len(q)): #loop for each parameter set

#  k_fo,k_of = [1,1]
#  k_ffr = q[set][2]
#  k_frf = q[set][3]
# # Regulated OFF-->ON (xXF_A)
#  kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1  = q[set][4:11]

# # Regulated ON-->OFF (Activator 2)
# #  kA2_max, n2 = q[set][11:13]
# #  K2 = 0.17
# #  kA2_min, ksA2, gamma_A2, kA2 = q[set][14:18]
#  kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]

# # Regulated OFF-->OFFrepr (Activator 1)
#  #kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = q[set][18:25]

# # Regulated OFFrepr-->OFF (xXF_D)
#  #k4_max, n4, K4, k4_min, k4_delay, k4_off, k4_on = q[set][25:32]
#  df1 = 1.5
#  df2 = 1.5
#  no_intermediates = 10
#  all_allelicstates = []
#  j = 0
#  while j < 100:
    
#     #the whole gillespie code
#     S1 = [0]    
#     S2 = [0]    
#     A1_1 = [1]  
#     A2_1 = [1]  
#     A1_2 = [1]  
#     A2_2 = [1]  
#     t = [0]     
#     I1_1 = [0] 
#     I2_1 = [0]
#     I1_2 = [0]
#     I2_2 = [0]
#     tend = 52
 

#     while t[-1] < tend:
#         current_A1_1 = A1_1[-1]
#         current_A1_2 = A1_2[-1]
#         current_S2 = S2[-1]
#         current_S1 = S1[-1]
#         current_A2_1 = A2_1[-1]
#         current_A2_2 = A2_2[-1]
#         current_I1_1 = I1_1[-1]
#         current_I2_1 = I2_1[-1]
#         current_I1_2 = I1_2[-1]
#         current_I2_2 = I2_2[-1]
        
#         # for I1_1
#         if I1_1[-1] < no_intermediates:
#             i1_1 = ksA1 * int(current_S1 == 1)
#         else:
#             i1_1 = 0

#         # for I2_1
#         if I2_1[-1] < no_intermediates:
#             i2_1 = ksA2 * int(current_S1 == 1)
#         else:
#             i2_1 = 0

#         # for I1_2
#         if I1_2[-1] < no_intermediates:
#             i1_2 = ksA1 * int(current_S2 == 1)
#         else:
#             i1_2 = 0

#         #  for I2_2
#         if I2_2[-1] < no_intermediates:
#             i2_2 = ksA2 * int(current_S2 == 1)
#         else:
#             i2_2 = 0         

#         # combined hill function , activator 1
#         total_activator1 = (current_A1_1 + current_A1_2) / df1
#         k_prod_eff1 = ((kA1_max-kA1_min) * k_fo * (total_activator1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

#         # combined hill function , activator 2
#         total_activator2 = (current_A2_2 + current_A2_1) / df2
#         k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
#         #chromosome 1
#         a1_1 = k_frf * int(current_S1 == -1) 
#         a2_1 = k_ffr * int(current_S1 == 0) 
#         a3_1 = k_prod_eff1 * int(current_S1 == 0) 
#         a4_1 = k_prod_eff2 * int(current_S1 == 1) 
#         a5_1 = kA1 * int(current_A1_1==0) * int(current_S1!=1)
#         a6_1 = gamma_A1 * int(current_A1_1==1) * int(current_S1==1) * int(current_I1_1 >= no_intermediates)
#         a7_1 = kA2 * int (current_A2_1==0) * int(current_S1!=1) 
#         a8_1 = gamma_A2 * int(current_A2_1==1) * int(current_S1==1) * int(current_I2_1 >= no_intermediates) 

#         #chromosome 2
#         a1_2 = k_frf * int (current_S2 == -1) 
#         a2_2 = k_ffr * int(current_S2 == 0) 
#         a3_2 = k_prod_eff1 * int(current_S2 == 0) 
#         a4_2 = k_prod_eff2 * int(current_S2 == 1) 
#         a5_2 = kA1 * int(current_A1_2==0) * int(current_S2!=1) 
#         a6_2 = gamma_A1 * int(current_A1_2) * int(current_S2==1) * int(current_I1_2 >= no_intermediates) 
#         a7_2 = kA2 * int(current_A2_2==0) * int(current_S2!=1) 
#         a8_2 = gamma_A2 * int(current_A2_2==1) * int(current_S2==1) * int(current_I2_2 >= no_intermediates) 

#         rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2 , i1_1 , i2_1, i1_2 , i2_2]

#         rate_sum = sum(rates)

#         # time update
#         if rate_sum == 0:
#             tau = float('inf')
#         else:
#             tau = np.random.exponential(scale=1 / rate_sum)
#         t.append(t[-1] + tau)

#         rand = random.uniform(0, 1)
#         # event - chromosome 1
#         if rand * rate_sum <= a1_1:
#             S1.append(0)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1:
#             S1.append(-1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
#             S1.append(1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
#             S1.append(0)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(0)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(0)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         # event - chromosome 2
#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2:
#             S1.append(current_S1)
#             S2.append(0)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2:
#             S1.append(current_S1)
#             S2.append(-1)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2:
#             S1.append(current_S1)
#             S2.append(1)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2:
#             S1.append(current_S1)
#             S2.append(0)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(1)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(0)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(1)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(0)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         # intermediates
#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1 + 1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1 + 1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1 + i1_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2 + 1)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1 + i1_2 + i2_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2 + 1)

#     index = np.searchsorted(t,50,side = 'right') - 1
#     a = S1[index]
#     b = S2[index]
#     if a == 1 and b == 1: 
#             all_allelicstates.append(2)
#     elif (a == 1 or b == 1) and not (a == 1 and b == 1):
#             all_allelicstates.append(1)
#     else:
#             all_allelicstates.append(0)
#     j += 1
#  c2 = c1 = c0 = 0
#  for row in all_allelicstates:
#             if row == 2:
#                 c2 += 1
#             elif row == 1:
#                 c1 += 1
#             elif row == 0:
#                 c0 += 1

#  mean_c2.append(c2)
#  mean_c1.append(c1)
#  mean_c0.append(c0)

# t_crit_2 = stats.t.ppf(0.975, len(mean_c2)-1)
# ci_2 = t_crit_2 * (np.std(mean_c2, ddof=1) / np.sqrt(len(mean_c2)))

# t_crit_1 = stats.t.ppf(0.975, len(mean_c1)-1)
# ci_1 = t_crit_1 * (np.std(mean_c1, ddof=1) / np.sqrt(len(mean_c1)))

# t_crit_0 = stats.t.ppf(0.975, len(mean_c0)-1)
# ci_0 = t_crit_0 * (np.std(mean_c0, ddof=1) / np.sqrt(len(mean_c0)))


# print(np.mean(mean_c1))
# plt.bar('XXY', np.mean(mean_c1), label="XaXi (Monoallelic)", color="#AA3377", width = 0.5,capsize=5,yerr=ci_1, ecolor="red")
# bottom = np.mean(mean_c1)
# plt.bar('XXY', np.mean(mean_c2), label="XiXi (Biallelic)", color="#F0E442", width = 0.5,capsize=5,yerr=ci_2, bottom=bottom, ecolor="red")
# bottom += np.mean(mean_c2)
# plt.bar('XXY', np.mean(mean_c0), label="XaO (Inactive)", color="#E69F00",bottom = bottom,  width = 0.5,capsize=5,yerr=ci_0 , ecolor = 'red')



#       #XXYY

# mean_c4 = []
# mean_c3 = []
# mean_c2 = []
# mean_c1 = []
# mean_c0 = []
# for set in range(0,len(q)): #loop for each parameter set

#  k_fo,k_of = [1,1]
#  k_ffr = q[set][2]
#  k_frf = q[set][3]
# # Regulated OFF-->ON (xXF_A)
#  kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1  = q[set][4:11]

# # Regulated ON-->OFF (Activator 2)
# #  kA2_max, n2 = q[set][11:13]
# #  K2 = 0.17
# #  kA2_min, ksA2, gamma_A2, kA2 = q[set][14:18]
#  kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]

# # Regulated OFF-->OFFrepr (Activator 1)
#  #kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = q[set][18:25]

# # Regulated OFFrepr-->OFF (xXF_D)
#  #k4_max, n4, K4, k4_min, k4_delay, k4_off, k4_on = q[set][25:32]
#  df1 = 2
#  df2 = 2
#  no_intermediates = 10
#  all_allelicstates = []
#  j = 0
#  while j < 100:
    
#     #the whole gillespie code
#     S1 = [0]    
#     S2 = [0]    
#     A1_1 = [1]  
#     A2_1 = [1]  
#     A1_2 = [1]  
#     A2_2 = [1]  
#     t = [0]     
#     I1_1 = [0] 
#     I2_1 = [0]
#     I1_2 = [0]
#     I2_2 = [0]
#     tend = 52
 

#     while t[-1] < tend:
#         current_A1_1 = A1_1[-1]
#         current_A1_2 = A1_2[-1]
#         current_S2 = S2[-1]
#         current_S1 = S1[-1]
#         current_A2_1 = A2_1[-1]
#         current_A2_2 = A2_2[-1]
#         current_I1_1 = I1_1[-1]
#         current_I2_1 = I2_1[-1]
#         current_I1_2 = I1_2[-1]
#         current_I2_2 = I2_2[-1]
        
#         # for I1_1
#         if I1_1[-1] < no_intermediates:
#             i1_1 = ksA1 * int(current_S1 == 1)
#         else:
#             i1_1 = 0

#         # for I2_1
#         if I2_1[-1] < no_intermediates:
#             i2_1 = ksA2 * int(current_S1 == 1)
#         else:
#             i2_1 = 0

#         # for I1_2
#         if I1_2[-1] < no_intermediates:
#             i1_2 = ksA1 * int(current_S2 == 1)
#         else:
#             i1_2 = 0

#         #  for I2_2
#         if I2_2[-1] < no_intermediates:
#             i2_2 = ksA2 * int(current_S2 == 1)
#         else:
#             i2_2 = 0         

#         # combined hill function , activator 1
#         total_activator1 = (current_A1_1 + current_A1_2) / df1
#         k_prod_eff1 = ((kA1_max-kA1_min) * k_fo * (total_activator1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

#         # combined hill function , activator 2
#         total_activator2 = (current_A2_2 + current_A2_1) / df2
#         k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
#         #chromosome 1
#         a1_1 = k_frf * int(current_S1 == -1) 
#         a2_1 = k_ffr * int(current_S1 == 0) 
#         a3_1 = k_prod_eff1 * int(current_S1 == 0) 
#         a4_1 = k_prod_eff2 * int(current_S1 == 1) 
#         a5_1 = kA1 * int(current_A1_1==0) * int(current_S1!=1)
#         a6_1 = gamma_A1 * int(current_A1_1==1) * int(current_S1==1) * int(current_I1_1 >= no_intermediates)
#         a7_1 = kA2 * int (current_A2_1==0) * int(current_S1!=1) 
#         a8_1 = gamma_A2 * int(current_A2_1==1) * int(current_S1==1) * int(current_I2_1 >= no_intermediates) 

#         #chromosome 2
#         a1_2 = k_frf * int (current_S2 == -1) 
#         a2_2 = k_ffr * int(current_S2 == 0) 
#         a3_2 = k_prod_eff1 * int(current_S2 == 0) 
#         a4_2 = k_prod_eff2 * int(current_S2 == 1) 
#         a5_2 = kA1 * int(current_A1_2==0) * int(current_S2!=1) 
#         a6_2 = gamma_A1 * int(current_A1_2) * int(current_S2==1) * int(current_I1_2 >= no_intermediates) 
#         a7_2 = kA2 * int(current_A2_2==0) * int(current_S2!=1) 
#         a8_2 = gamma_A2 * int(current_A2_2==1) * int(current_S2==1) * int(current_I2_2 >= no_intermediates) 

#         rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2 , i1_1 , i2_1, i1_2 , i2_2]

#         rate_sum = sum(rates)

#         # time update
#         if rate_sum == 0:
#             tau = float('inf')
#         else:
#             tau = np.random.exponential(scale=1 / rate_sum)
#         t.append(t[-1] + tau)

#         rand = random.uniform(0, 1)
#         # event - chromosome 1
#         if rand * rate_sum <= a1_1:
#             S1.append(0)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1:
#             S1.append(-1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
#             S1.append(1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
#             S1.append(0)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(0)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(0)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         # event - chromosome 2
#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2:
#             S1.append(current_S1)
#             S2.append(0)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2:
#             S1.append(current_S1)
#             S2.append(-1)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2:
#             S1.append(current_S1)
#             S2.append(1)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2:
#             S1.append(current_S1)
#             S2.append(0)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(1)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(0)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(1)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(0)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         # intermediates
#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1 + 1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1 + 1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1 + i1_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2 + 1)
#             I2_2.append(current_I2_2)

#         elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1 + i1_2 + i2_2:
#             S1.append(current_S1)
#             S2.append(current_S2)
#             A1_1.append(current_A1_1)
#             A2_1.append(current_A2_1)
#             A1_2.append(current_A1_2)
#             A2_2.append(current_A2_2)
#             I1_1.append(current_I1_1)
#             I2_1.append(current_I2_1)
#             I1_2.append(current_I1_2)
#             I2_2.append(current_I2_2 + 1)

#     index = np.searchsorted(t,50,side = 'right') - 1
#     a = S1[index]
#     b = S2[index]
#     if a == 1 and b == 1: 
#             all_allelicstates.append(2)
#     elif (a == 1 or b == 1) and not (a == 1 and b == 1):
#             all_allelicstates.append(1)
#     else:
#             all_allelicstates.append(0)
#     j += 1
#  c2 = c1 = c0 = 0
#  for row in all_allelicstates:
#             if row == 2:
#                 c2 += 1
#             elif row == 1:
#                 c1 += 1
#             elif row == 0:
#                 c0 += 1

#  mean_c2.append(c2)
#  mean_c1.append(c1)
#  mean_c0.append(c0)


# t_crit_2 = stats.t.ppf(0.975, len(mean_c2)-1)
# ci_2 = t_crit_2 * (np.std(mean_c2, ddof=1) / np.sqrt(len(mean_c2)))

# t_crit_1 = stats.t.ppf(0.975, len(mean_c1)-1)
# ci_1 = t_crit_1 * (np.std(mean_c1, ddof=1) / np.sqrt(len(mean_c1)))

# t_crit_0 = stats.t.ppf(0.975, len(mean_c0)-1)
# ci_0 = t_crit_0 * (np.std(mean_c0, ddof=1) / np.sqrt(len(mean_c0)))

# print(np.mean(mean_c0))

# plt.bar('XXYY', np.mean(mean_c0), label="XaO (Inactive)", color="#E69F00", width = 0.5,capsize=5,yerr=ci_0 , ecolor = 'red')
# bottom = np.mean(mean_c0)
# plt.bar('XXYY', np.mean(mean_c1), label="XaXi (Monoallelic)", color="#AA3377",bottom = bottom,  width = 0.5,capsize=5,yerr=ci_1, ecolor="red")
# bottom += np.mean(mean_c1)
# plt.bar('XXYY', np.mean(mean_c2), label="XiXi (Biallelic)", color="#F0E442", width = 0.5,capsize=5,yerr=ci_2, bottom=bottom, ecolor="red")

plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.margins(x=0.03)
plt.ylabel("Mean % of cells",weight="bold", fontsize=12)
plt.xlabel("Ploidy",weight="bold", fontsize=12)
plt.xticks(rotation=45)
plt.show()
#plt.savefig('/home/madhusud/modeling_gene_expression/FinalPlots/n1-10', dpi=600, bbox_inches="tight")