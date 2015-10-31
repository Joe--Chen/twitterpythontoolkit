#!/usr/bin/python
# import pprint
# from pymongo import MongoClient
# import datetime 
# import pprint


import os
import sys
import random
print os.path
from sets import Set

sys.path.insert(0, "/usr/local/lib/python2.7/site-packages")
sys.path.insert(0, "/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/python_louvain-0.3-py2.7.egg")
print sys.path
# sys.path.insert(0, "/opt/local/")
#import cairo

#import matplotlib.pyplot as plt
import networkx as nx
import community
import pickle
#from igraph import *
# g = Graph.Famous("petersen")
# plot(g)



def loadDicFromFile(filename):
	
	# save a dictionary
	# pickle.dump( dic_name, open( "save.p", "wb" ) )
	#
	# load a dictionary
	print "start loading the pickle"
	user_fol = pickle.load( open(filename, "rb" ) )

	# get relevant user_fol dictionary
	# print "start updating the dictionary-------->"
	# for key in user_fol.keys():
	# 	print "finish one key"
	# 	# change it to set operation; set intersection
	# 	new_val = [val for val in user_fol[key] if val in user_fol.keys()]
	# 	user_fol[key] = new_val

	print "finish loading, return dictionary now --------->"
	return user_fol
# mashable
#user_follower = {1142467586: [], 2673011204L: [], 558454789: [], 401338374: [], 834953227: [54525773], 615864844: [16816972, 2367105482], 466671618: [], 52027918: [], 2506303503L: [], 89022992: [14241791, 16816972], 474761233: [], 14362642: [61270769], 54047252: [45513177], 1444655126: [433618925], 436910103: [494009898, 1109059640, 465446581, 115123902], 2464475908L: [1583138989], 1900226587: [], 488527901: [944195358, 486835275, 486760124, 486734725, 493355457, 493200158, 485807610, 485782675, 485716927, 484964484, 484938930], 166875166: [16816972, 60570739, 296493118, 80327968], 270061599: [503676533, 60570739], 18383195: [47382788], 1876217893: [], 492950054: [], 149159975: [], 30214697: [], 1631433770: [1249556076], 1633522219: [68333543], 188325932: [208703637, 15816164], 207990830: [78568928, 102442385], 41867311: [], 1946548272: [], 486711345: [486629157, 485807610, 485782675, 485716927, 485528902, 484964484, 484938930, 486810954, 486760124], 1109059640: [24210409, 2556173600, 14921361, 68333543, 502098794, 436910103, 296493118], 2212419642L: [572737928], 249511995: [152441856, 245173212, 17633714, 288093542, 147832136, 256702081, 52809495, 144501148], 73977917: [], 10946622: [199463965, 14241791, 548845041, 189208035], 479230017: [], 296749448: [522321139, 115123902, 172768971, 174303316, 17633714, 293688609], 434423875: [], 486448196: [486690813, 485807610, 485782675, 485716927, 484964484, 484938930, 486835275, 486810954, 486760124, 486734725, 486711345, 486629157, 486585393], 2598641738L: [], 1350084686: [], 21065809: [], 484946003: [], 174303316: [2845611159, 1722848880, 25492496], 384917592: [1462664562, 389770680], 506314843: [797598200], 2209976418L: [], 237166691: [2164710140, 2793148179, 2286995652], 485696018: [493355457, 493200158, 485528902, 484964484, 484938930, 484291000, 488527901, 487955043, 486880717, 486835275, 486810954, 486760124, 486734725, 486711345, 486690813, 486629157, 486585393, 486562691, 486448196, 485807610, 485782675], 108374127: [484018605], 172064882: [458604801], 15908981: [], 1498746487: [], 74375289: [49271414], 716079235: [], 484964484: [487955043, 493355457, 493200158, 484291000, 488527901, 486835275, 486810954, 486760124, 486734725, 486711345, 486690813, 486629157, 486585393, 486562691, 486448196, 485807610, 485782675, 485716927, 485696018], 574326917: [], 383995927: [68333543], 597289103: [], 15585424: [522321139], 2440132755L: [], 80359572: [14222100, 21280216], 208703637: [548845041, 115123902], 78876832: [82956754], 124954787: [], 359004324: [208703637, 20192527, 18383195], 1285105831: [503756459], 49172648: [462420179], 2799808681L: [], 43712967: [], 104204460: [522321139], 1583138989: [], 263006749: [208703637], 601948336: [42369676, 237166691, 2437610144, 474761233, 16816972, 437650573, 484018605], 558772413: [], 2286995652L: [620296965, 382299568, 16816972], 818202823: [], 21608650: [2367105482, 1583138989, 32162450], 159428811: [16816972, 68333543, 121631815, 32162450, 100426508], 622635213: [33672294], 226146514: [552473488], 253633235: [], 994528004: [1466274925], 2491226329L: [2821346164], 2365038810L: [], 132573403: [], 50155740: [14241791, 16816972], 754129117: [], 244343014: [], 207657193: [], 14407914: [], 16609515: [15326241], 462420179: [1004850542], 493037813: [], 24314103: [1358558509, 22668187, 16458689, 987505262], 178315001: [24691666], 17842426: [], 458604801: [104204460, 104478609, 502098794, 502071749, 262340575, 137482856, 172064882], 101517570: [16816972, 14241791, 223710555], 47382788: [2207430032, 18383195], 620296965: [], 225726730: [], 2336942347L: [], 424255759: [], 595603729: [116244879], 50559251: [], 2496854293L: [16816972], 2188186329L: [], 45484313: [16816972], 55521563: [], 498192670: [], 121465119: [881185128, 167182842, 334617939, 27995488], 621293868: [], 400030066: [], 19759409: [], 516100406: [502098794, 137482856, 104204460], 179351870: [], 240390465: [], 454947138: [], 504731972: [2464708274, 983395976], 81148229: [82956754, 86129574], 47878471: [9221802], 1248684362: [], 335239503: [], 306213202: [], 1875583316: [], 24973710: [100426508], 118024534: [], 23930200: [], 223710555: [101517570], 359485788: [], 66691421: [529622870, 172768971, 2286995652, 437650573, 270061599, 68333543, 142300945, 321659355], 76908897: [1039252075, 104478609, 147832136, 138454325], 246944099: [], 366974308: [], 1969015526: [1023460549], 881185128: [503756459, 329952566, 967369477], 35831145: [], 31712618: [121631815, 136736469, 14222100, 21280216], 296079726: [503676533, 60570739, 80327968, 296493118], 1462664562: [338928425, 384917592, 1266313153], 2279174516L: [], 296493118: [330429183, 515447515, 1249556076, 68333543, 166875166, 174303316, 522321139, 967369477, 1109059640], 409241975: [890323814, 797598200, 68333543], 15866233: [16816972, 14241791], 2314826107L: [], 2846436074L: [], 20402581: [590312609, 14921361, 24691666, 82956754], 2221631875L: [1512455426, 173556553], 283156870: [208703637, 17633714], 572737928: [2212419642], 785527178: [], 1105416590: [2183636785, 1952957179], 116244879: [595603729], 379758659: [], 260727189: [], 2200238490L: [], 153876973: [], 144501148: [881185128, 288093542, 256702081, 249511995, 245173212, 152441856, 100458294, 52809495], 212810156: [529622870, 121631815], 484018605: [108374127], 18516400: [21280216], 56147377: [415753384], 17633714: [590312609, 25492496, 174303316], 2595916214L: [], 484291000: [493355457, 487955043, 486760124, 486448196, 485807610, 485716927, 485696018, 484964484, 484938930], 2499901884L: [], 1712882113: [], 502071749: [556649719, 18794068, 17633714, 212810156, 104204460], 35972039: [245173212, 20402581], 2367105482L: [68333543, 615864844], 53031375: [22978174], 82956754: [], 38832596: [], 29109718: [], 45513177: [54047252], 321659355: [16816972, 66691421], 1562053086: [68333543, 32162450, 14241791], 100127201: [], 459815396: [], 433618925: [1888191674, 750632095], 27273711: [], 344619505: [], 797598200: [409241975, 890323814, 506314843, 321659355], 931850324: [], 167182842: [121465119, 189208035], 450808316: [14921361], 28494334: [14241791], 152441856: [249511995, 256702081, 118964050, 144501148, 245173212, 52809495], 20966395: [], 821331486: [], 256780037: [17633714], 380329513: [529622870, 1285105831, 166875166], 2668972591L: [], 16689712: [], 2473204274L: [115123902], 3078921: [], 97600057: [68333543, 60570739, 80327968], 429617727: [], 2696718914L: [], 274926148: [], 1875581509: [], 2156364362L: [], 143968844: [967369477, 208703637], 1466995280: [], 366863800: [], 44841556: [622857704], 954739286: [], 477811288: [], 469619289: [], 150307419: [16816972], 578277980: [], 487955043: [944195358, 486942049, 485807610, 485528902], 2248735334L: [], 137482856: [], 1039252075: [76908897], 987505262: [1358558509, 24314103, 16458689], 2384869999L: [], 853088881: [338928425], 187465846: [], 1597096567: [], 14222100: [2164710140, 14241791, 24691666], 731636346: [750632095, 1952957179], 37161596: [], 14584447: [14921361], 508164737: [], 37995138: [15816164], 182176389: [], 16458689: [1358558509, 22668187, 24314103, 987505262], 2321035915L: [68333543], 2421721740L: [], 297947789: [], 66581134: [], 32162450: [1562053086, 503676533], 2334087828L: [], 28888215: [], 15268506: [16816972, 174303316, 137482856, 81720388], 146768539: [115123902], 2437610144L: [16816972, 237166691, 601948336], 150598818: [522321139, 104204460, 137482856, 208703637, 104478609, 147832136], 2583132323L: [14241791, 16816972], 53037220: [26159676, 19266960], 264104614: [323938158, 208703637], 238501031: [], 1449507504: [], 932944561: [], 493200158: [944195358, 486810954, 486760124], 214237884: [], 75193022: [], 49271414: [14921361, 74375289], 53035720: [21280216, 16411361, 19266960], 19235529: [], 558521037: [], 350747343: [], 79925971: [], 52462292: [], 80919253: [], 1303136983: [], 177156824: [], 2259202777L: [], 515447515: [296493118], 1383135966: [], 16411361: [21280216], 404832998: [], 1480950506: [], 2335279855L: [], 576791280: [433618925, 750632095], 61270769: [14362642], 560526071: [], 1952957179: [2183636785, 731636346, 1105416590], 2164710140L: [237166691, 16816972, 14222100], 309515005: [], 330429183: [], 1530409729: [], 2468750082L: [], 2570976043L: [], 1909428996: [], 967369477: [296493118, 881185128], 53037830: [], 1876081416: [], 2416163593L: [], 100426508: [590312609, 24691666, 24973710], 53034769: [19266960], 53033746: [21280216], 1875260180: [], 70888214: [], 2441622300L: [], 944195358: [493355457, 493200158, 488527901, 487955043, 486734725, 486760124, 485716927, 485667398, 115123902], 734657311: [], 1614704773: [], 424045345: [], 2765566939L: [], 486629157: [485807610, 485782675, 485716927, 485528902, 484964484, 484938930, 486835275, 486810954, 486760124, 486734725, 486711345], 338928425: [1462664562, 389770680, 384917592], 50246443: [590312609, 14921361, 104204460, 18951555, 102442385], 999547694: [], 246778672: [208703637], 54081329: [14921361, 19266960], 90712884: [14241791, 437650573], 2795825976L: [68333543, 102442385], 310100793: [], 323160891: [2756408664, 16816972], 819516222: [], 1457705798: [], 173556553: [2221631875, 1512455426], 16816972: [890323814, 25492496], 2648970061L: [], 2794785592L: [], 1926626131: [1912792202], 386771797: [], 558779223: [], 2203345754L: [], 371962717: [], 343221086: [], 890323814: [16816972, 2754247836, 14241791, 36880984], 502098794: [1109059640, 556649719, 467502233, 18794068], 200274798: [80327968], 95509363: [], 2821346164L: [2491226329], 420352830: [], 24210409: [2797409917, 1109059640, 42369676, 237166691, 14241791], 1169751188: [], 612490107: [], 79094653: [26159676], 2164630398L: [], 1589038464: [], 90569603: [14493027], 486734725: [486711345, 944195358, 493355457, 493200158, 486629157, 485807610, 485782675, 485716927, 485528902, 484964484, 484938930, 486835275, 486810954], 36012935: [], 1467962250: [], 552473488: [226146514], 903369618: [], 1920936852: [], 159998357: [23600276, 222155852], 635478934: [], 1922276251: [18951555], 449036455: [], 488711075: [], 589323173: [], 86129574: [81148229], 2813797362L: [], 57809840: [21280216], 389770680: [529622870, 1462664562, 1416828066, 384917592, 338928425], 1957235700: [44592420], 223348158: [115123902], 485716927: [944195358, 493355457, 493200158, 485528902, 484964484, 484938930, 488527901, 486835275, 486810954, 486760124, 486734725, 486711345, 486690813, 486629157, 486585393, 486562691, 486448196, 485807610], 493355457: [944195358, 486810954], 2496523207L: [], 215337932: [], 54525773: [], 24691666: [], 275536855: [], 2277491161L: [], 25080283: [], 245173212: [881185128, 249511995, 35972039, 288093542, 256702081, 144501148, 152441856, 52809495], 95157242: [81720388], 70462431: [881185128, 21280216, 27452134], 2852074465L: [42369676], 900424675: [], 2493044713L: [], 1122959527: [], 1254696428: [], 17882093: [], 17831406: [147832136], 14500848: [], 104121841: [], 88477170: [], 924283892: [], 2688358904L: [], 322054650: [193718183], 459874299: [], 177890300: [91320170], 431155014: [],2457031682L: [], 929938435: [], 613682180: [], 63329452: [2164630398], 2344193034L: [], 25492496: [16816972, 414016645, 2375716122, 172768971, 174303316, 14921361, 344619505], 5499922: [], 344569347: [], 1120713902: [], 16944663: [], 1152220188: [], 199463965: [14241791, 10946622, 68333543, 81720388, 172768971, 60570739, 16816972, 334617939, 620296965], 15326241: [24691666], 32408612: [16816972], 2212340778L: [], 134224940: [44324207], 250147885: [], 2162613295L: [], 251132976: [], 486585393: [487955043, 493200158, 485807610, 485782675, 485716927, 485667398, 485528902, 484964484, 484938930, 486835275, 486810954, 486760124, 486734725, 486711345, 486690813], 760957490: [], 18138164: [243264343, 296493118, 80327968, 166875166, 503676533], 2864129081L: [], 26159676: [68333543], 20479038: [115123902, 82956754, 60860438], 356682816: [], 612289601: [], 81720388: [95157242, 199463965, 115123902, 1085906131, 80327968], 121631815: [212810156, 159428811, 26159676, 556649719, 138196324, 80327968, 296493118, 31712618], 486835275: [486810954, 486690813, 486585393, 486760124, 493355457, 493200158, 486629157, 485807610, 485782675, 485716927, 485667398, 485528902, 484964484, 484938930], 222155852: [146768539], 209976397: [], 511251534: [68333543], 2369907793L: [], 155462740: [], 406826073: [967369477], 121173085: [208703637], 498533472: [], 1678077025: [], 33672294: [14241791, 16816972], 350968935: [1444655126], 1461636200: [16816972, 14241791], 1466274925: [], 2324350056L: [], 742016113: [595924889, 174303316, 522321139, 16816972, 18794068], 60570739: [330429183, 166875166, 296493118, 104204460, 81720388, 465446581, 199463965, 137482856, 296079726, 522321139, 22259704], 291001461: [115123902, 82956754, 17633714], 2549917034L: [], 2847368321L: [], 414016645: [2396315521, 25492496, 68333543], 62569606: [], 591146177: [], 983395976: [2464708274, 504731972], 1912792202: [1926626131], 437650573: [], 2714995856L: [2696718914], 485782675: [493355457, 487955043, 493200158, 485716927, 484964484, 484938930, 488527901, 486835275, 486810954, 486760124, 486734725, 486711345, 486690813, 486629157, 486585393, 486562691, 486448196], 23600276: [159998357], 402183317: [], 2845611159L: [172768971], 2393298072L: [], 467502233: [502098794, 262340575, 137482856], 2754247836L: [], 271985821: [], 750632095: [1512455426, 2533547450, 731636346, 1888191674, 1383135966, 433618925, 576791280], 590312609: [], 1416828066: [389770680], 118342823: [82956754], 415753384: [172768971], 101988524: [137482856], 240862382: [], 435502255: [], 2171880624L: [], 484938930: [493355457, 493200158, 487955043, 484291000, 488527901, 486835275, 486810954, 486760124, 486734725, 486711345, 486690813, 486629157, 486585393, 486562691, 486448196, 485807610, 485782675, 485716927, 485696018], 1108426099: [620296965], 1485499573: [], 606698678: [172064882], 2770046137L: [], 1888191674: [750632095, 433618925, 576791280], 1685304512: [], 2713973953L: [14241791], 174820548: [881185128], 1023460549: [1969015526], 1570200775: [], 42833101: [], 512227533: [], 2536649936L: [], 437525713: [], 1085906131: [81720388], 109491412: [], 2329025755L: [], 538856668: [], 309648615: [], 350303464: [], 2741698794L: [], 1629502704: [], 522321139: [28494334, 104204460, 26159676, 138196324, 296749448], 281906421: [], 556649719: [16816972, 174303316, 494009898, 606281620, 121631815, 502098794, 502071749, 262340575, 137482856, 620296965, 18794068, 81720388], 1133137146: [], 2579743999L: [], 93601026: [], 912087812: [], 34282758: [], 52129033: [], 23876874: [16816972], 558750987: [], 633376012: [], 16553230: [], 20192527: [212810156, 366974308], 2224491793L: [], 1875774738: [], 18951555: [1922276251, 50246443, 104478609, 82956754], 1942013204: [], 2327729430L: [], 16137497: [], 2375716122L: [25492496], 15776303: [], 1955325212: [], 2556173600L: [], 293688609: [115123902, 440860374, 17633714, 24691666, 296749448], 1533668642: [237166691], 44592420: [1957235700], 16389414: [1133137146], 132097320: [635478934, 18383195, 102442385], 2459607260L: [], 250162474: [503756459, 291001461], 1588260140: [], 53036340: [22978174], 138454325: [76908897], 329952566: [522321139, 881185128], 224687417: [], 325793082: [], 388408640: [], 85339458: [], 86836547: [84215501], 485528902: [493355457, 493200158, 484964484, 484938930, 484291000, 488527901, 487955043, 486880717, 486835275, 486810954, 486760124, 486734725, 486711345, 486690813, 486629157, 486585393, 486562691, 486448196, 485807610, 485782675, 485716927], 147832136: [51197523, 20192527], 486810954: [486711345, 486760124, 493355457, 493200158, 486629157, 485807610, 485782675, 485716927, 485528902, 484964484, 484938930], 1482603852: [], 1875764558: [], 1612719440: [], 334617939: [199463965, 620296965, 121465119], 243264343: [], 297137496: [], 356547931: [1281437306], 27995488: [121465119, 323597924], 486942049: [486585393, 486629157, 485667398, 485807610, 487955043], 860589410: [2212419642], 14493027: [21280216, 90569603], 138196324: [14241791, 14921361, 522321139, 881185128, 121631815, 18794068], 288093542: [152441856, 52809495, 144501148, 249511995, 256702081, 245173212], 102442385: [2795825976, 50246443, 132097320, 82956754], 470801768: [], 94332778: [], 1004850542: [503756459], 44324207: [574326917, 134224940], 426538354: [], 1849873267: [], 2285289534L: [], 99067254: [], 2688572791L: [], 511585664: [], 53698433: [], 486562691: [485807610, 485782675, 485716927, 485667398, 485528902, 484964484, 484938930, 487955043, 486942049, 486880717, 486835275, 486810954, 486760124, 486734725, 486711345, 486690813, 486629157], 55143812: [16816972, 80327968], 627093902: [], 805618063: [], 2207430032L: [], 104478609: [150598818, 458604801, 18383195, 137482856, 76908897], 1876110738: [], 22668187: [1358558509, 16458689, 24314103, 987505262, 168476512], 58260903: [16816972, 68333543], 798122: [68333543], 455454124: [104478609], 382299568: [2286995652, 137482856], 268174769: [], 919469490: [], 125699508: [], 2353079736L: [], 2533547450L: [750632095], 1679504827: [16816972, 14241791, 68333543], 93773245: [], 1876501950: [], 73270719: [20402581], 2591794627L: [], 2436408774L: [], 23420360: [], 532381129: [], 608920823: [], 313341388: [], 486880717: [486585393, 485782675, 485807610, 485528902, 487955043], 23954895: [2399241728, 492950054], 829842900: [], 2399241728L: [], 1176722947: [], 355083780: [], 55166469: [], 559799896: [], 1874730782: [], 1653394963: [], 60860438: [], 2772833815L: [], 65636379: [], 2460555139L: [], 1875500574: [], 2382457435L: [24210409], 614360617: [262340575], 494009898: [115123902, 80327968, 18794068, 436910103, 137482856, 81720388, 556649719, 606281620], 2493484596L: [], 1875770934: [], 819171: [], 1572384318: [], 2389929542L: [], 794687047: [], 16784971: [], 2587316816L: [], 51197523: [147832136], 18794068: [28494334, 2845611159, 620296965, 24210409, 68333543], 33893974: [], 25237079: [], 36880984: [16816972, 890323814], 2278184538L: [16816972], 2242439771L: [], 800276466: [620296965], 16131683: [], 323597924: [208703637], 1160670822: [], 10339942: [], 980960875: [], 1249556076: [1631433770, 80327968, 296493118, 68333543], 1076354671: [], 172908144: [], 417564276: [], 503676533: [24210409, 16816972, 174303316, 166875166, 967369477, 137482856, 465446581, 296079726, 18794068], 381652598: [], 374556279: [], 1281437306: [356547931], 1875584636: [], 2797409917L: [2375716122, 2286995652, 24210409], 22978174: [53031375, 53036340, 19266960], 256702081: [152441856, 24691666, 52809495, 288093542, 100458294, 144501148, 249511995, 245173212], 64777858: [], 55371713: [], 154588808: [], 1977767532: [], 1190496907: [], 42369676: [], 277083789: [522321139, 344619505], 262932110: [], 2674087567L: [], 14921361: [2795825976, 14241791, 1470861990], 274194067: [], 1039687591: [], 51030297: [16816972], 2282512027L: [], 377226909: [881185128], 748222111: [], 1722848880: [174303316], 40615588: [], 64091814: [], 1281326761: [], 9221802: [], 503756459: [881185128, 1004850542], 2464708274L: [504731972, 983395976], 465446581: [24210409, 440860374, 436910103, 80327968, 18794068, 174303316, 16816972, 60570739, 503676533, 296493118, 502071749, 502098794, 262340575, 137482856], 27416249: [590312609, 147832136], 160857786: [881185128, 967369477], 1864158907: [], 486760124: [493355457, 486711345, 944195358, 493200158, 486629157, 485807610, 485782675, 485716927, 485528902, 484964484, 484938930, 486835275], 115123902: [], 629084145: [493355457, 488527901, 487955043, 486835275, 485667398], 172768971: [2845611159, 14241791, 25492496, 394123103, 237166691, 115123902], 84215501: [86129574], 37193424: [212810156, 193718183], 158059731: [], 136736469: [31712618], 440860374: [465446581, 270489544, 293688609], 2292913879L: [], 2219884248L: [], 748134108: [], 57480826: [], 27452134: [104478609, 82956754, 70462431], 254664423: [1583138989], 519233256: [415753384], 92695164: [], 873385706: [], 486139633: [622857704], 440258771: [], 2191197944L: [], 76013305: [], 89886458: [52027918, 21280216], 561913597: [], 1512455426: [750632095, 2221631875, 173556553], 48655108: [], 2588866309L: [], 979113734: [], 1293459073: [], 916466954: [], 22480651: [], 14251791: [], 808902416: [], 142300945: [66691421], 2793148179L: [16816972, 237166691, 622857704], 47859478: [], 52809495: [288093542, 256702081, 249511995, 245173212, 152441856, 100458294, 144501148], 113904921: [], 2262646554L: [], 319402270: [208703637], 80327968: [55143812, 16816972, 68333543, 1249556076, 494009898, 81720388, 18138164, 465446581, 166875166, 296079726], 16049954: [], 1875662629: [], 2495297321L: [], 487577386: [], 2475286316L: [], 1358558509: [987505262, 22668187, 24314103, 16458689], 2183636785L: [1952957179, 1105416590], 87615282: [97388365], 1876158259: [], 1639214900: [], 100458294: [288093542, 256702081, 245173212, 152441856, 144501148, 52809495], 1704544057: [275536855], 27565882: [], 585260861: [], 301328193: [208703637], 1466097438: [], 146943812: [], 2575163360L: [], 1254659041: [], 97388365: [], 273747791: [], 20483921: [], 118964050: [], 473151459: [], 152233812: [109148031], 529622870: [50155740, 193679211, 66691421], 2756408664L: [323160891], 280540986: [296493118], 20930398: [], 394123103: [172768971, 16816972, 487577386, 68333543, 115123902], 168476512: [54525773, 17633714, 14921361], 2182130019L: [], 74329959: [], 129120104: [166875166], 87609686: [], 91320170: [177890300], 193679211: [], 323938158: [264104614], 105183092: [172768971, 174303316], 16244603: [2845611159], 1619859326: [], 109148031: [152233812], 2396315521L: [68333543, 414016645], 582852483: [], 217323400: [], 302460909: [301328193], 19266960: [14921361, 18383195, 21280216, 53034769, 54081329, 53037220, 53035720, 22978174], 186335121: [], 606281620: [104204460, 18794068, 174303316, 1004850542, 81720388, 16816972, 208703637, 494009898, 556649719, 620296965], 154861464: [], 595924889: [742016113], 142342047: [], 41002916: [], 193718183: [], 125417385: [], 480303090: [], 65724344: [], 38817727: [], 1266313153: [1462664562], 366694338: [388408640], 2471206853L: [2464475908], 270489544: [440860374, 17633714, 208703637], 85331916: [620296965, 208703637], 863180749: [], 518381560: [], 278511061: [], 540397015: [], 21280216: [590312609, 14921361], 93112282: [18383195], 88616411: [], 1197354972: [], 53534686: [21280216], 262340575: [115123902], 78568928: [207990830], 743265872: [47878471], 189208035: [620296965, 10946622, 47878471, 16816972, 167182842], 15816164: [121631815, 14921361], 1470861990: [484018605, 14921361], 68333543: [60570739, 503676533, 2795825976, 2845611159], 622857704: [2793148179, 42369676], 836533225: [], 593374187: [], 2367834092L: [415753384, 68333543], 2724623341L: [2696718914], 1875537390: [], 1254708720: [], 265553905: [], 187588082: [881185128], 548845041: [208703637, 10946622, 115123902], 81321972: [2286995652, 166875166, 268174769, 101988524], 2375694327L: [], 22259704: [68333543, 23600276, 24210409, 81720388, 522321139, 16816972, 115123902, 60570739, 104204460], 485807610: [493355457, 485782675, 485716927, 485528902, 484964484, 484938930, 488527901, 487955043, 486942049, 486880717, 486835275, 486810954, 486760124, 486734725, 486711345, 486690813, 486629157, 486585393, 486562691, 486448196], 67049467: [14241791], 66964476: [], 486690813: [487955043, 486942049, 488527901, 486880717, 493355457, 493200158, 486629157, 485807610, 485782675, 485716927, 484964484, 484938930, 486835275, 486810954, 486760124, 486734725], 14241791: [28494334, 58260903]}

user_follower = {}

user_used = {}

class Graph():
	"""Graph is a wrapper for making graphs for Twitter social network"""
	def __init__(self, user_dic, direction = "undirected"):
		if direction == "undirected":
			self.graph = nx.Graph()
		elif direction == "directed":
			self.graph = nx.DiGraph() 
		self.user_dic = user_dic
		self.color_dic = {}
		self.node_color = []

	def build_graph(self):
		""" insert notes and edges based on user dictionary"""
		#  for key in self.user_dic.keys():
		#  self.graph.add_node(key)
		print "start building the graph"
		distinct_user = Set([])

		distinct_user.union(set( self.user_dic.keys() ))

		for value in self.user_dic.values():
			distinct_user.union(set(value))

		for eachuser in distinct_user:
			self.graph.add_node(key)

		for key in self.user_dic.keys():
			for value in self.user_dic[key]:
				# g.add_edges( [(1,2)] )
				self.graph.add_edge(key, value)

		for node in self.graph.nodes():
			self.color_dic[node] = "white"

		self.node_color = [self.color_dic[node] for node in self.graph.nodes()]

		allgraph = list(nx.connected_component_subgraphs(self.graph))

		mincut = nx.minimum_edge_cut(self.graph)
		print "mincut is ", mincut
		print "length of all connected component is ", len(allgraph)

		for graph in allgraph:

			# min_weighted_dominating_set(graphUD, weight=None)

			print graph.number_of_nodes()

		print "finish building the graph"

	def print_nodes(self):
		print self.graph.nodes(data=False)

	def check_degree(self, cutoff, printout=False):
		""" the number of edges incident to the vertex"""


		# bot_group_1 = [2422719109L, 2474717201, 2470547848, 2468361964, 2439092234, 2468532497, 2485044753, 2472545555, 2472547347, 2477447571, 2472552814, 2485064471, 2472559258, 2477451676, 2455959581, 2434361119, 2434392866, 2472532517, 2434387370, 2474717488, 2472953393, 2434341810, 2474707005, 2468284989, 2472545470, 2485052735, 2434381273, 2468360080, 2472543706, 2470541661, 2472547432, 2477453032, 2468224233, 2434356716, 2485055470, 2468172016, 2485050100, 2434366842, 2434390268, 2472539104, 2472557483, 2434374007, 2453583454, 2434357008, 2434387717, 2472552503, 2474722037, 2474711092, 2456072807L]
		# bot_group_2 = [2873065834L, 2873121797, 2871683339L, 2871866435L, 2873125907, 2896965530, 2896924472, 2897014201, 2873031885, 2873113186, 2871886571L, 2896907376, 2871634625L, 2871622851L, 2872901589L, 2897007655, 2873040615, 2897033485, 2871595503L, 2871869037L, 2872891600L, 2896926698, 2895961844L, 2872893065L, 2872874249L]
		# bot_group_3 = [2451104093L, 2439003525, 2440837900, 2424355231, 2441033374, 2456299299, 2426338616, 2456317889, 2450865783, 2453494095, 2426330833, 2456433364, 2440922967, 2426308320, 2453445989, 2451132772, 2443263982, 2426355572, 2453414907, 2438977991, 2438779804, 2426311591, 2426294034, 2426389790, 2440861233L]
		# bot_group_4 = [2446303390L, 2443799033, 2444921223, 2458308119, 2457874061, 2446291469, 2450996237, 2446354882, 2446398094, 2457880463, 2421243373, 2457645975, 2421254941, 2457887902, 2457640353, 2457887009, 2444973346, 2446281257, 2451274810, 2450987842, 2451123784, 2457631947, 2457621964, 2451150286, 2450945632, 2425073005, 2444977648, 2444966393, 2444917486, 2450956655, 2457646193, 2451220707, 2446366167, 2444966488, 2446336245, 2425094617, 2444969596, 2444970749, 2457880702, 2450969183, 2444923408L, 2457887523, 2425964454]
		# bot_group_5 = [2364596246L, 2366296453, 2361203334, 2357878406, 2364021126, 2366789126, 2368401162, 2363949709, 2369819023, 2357861940, 2362504081, 2358871572, 2366075797, 2359824277, 2366064217, 2362779800, 2366397722, 2364452252, 2370008096, 2362326050, 2367104420, 2368617770, 2368711346, 2366226420, 2366045251, 2358142789, 2364199231, 2366167220, 2367155654, 2360379080, 2357371112, 2360016714, 2366135402, 2368427467, 2366777036, 2366259949, 2357481907, 2367104724, 2362699700, 2367771481, 2366294874, 2358866516, 2367648638, 2366412799]
		# bot_group_6 = [2560438300L, 2462051330, 2560476226L, 2560424981, 2560432155, 2560441635, 2462060736, 2462063682, 2560478788L, 2560432037, 2462058342, 2560467946L, 2560435539, 2560434263L, 2560447564, 2560446839, 2560463085, 2560461171L, 2463365972, 2462071412, 2560421819L, 2463369054, 2463366367, 2560426738L, 2462070450]
		# bot_group_7 = [2411776015L, 2428130696, 2428079438, 2413322143, 2414985541L, 2413460767, 2413421484L, 2413270958, 2428152782, 2432365134, 2428141142, 2416376023, 2414950873, 2428091102, 2414885220, 2414864239L, 2442841588, 2442912117L, 2415020797L, 2413387129, 173149322, 2428019012L, 2414797176L, 2428033531L, 2428002770L, 843655993]
		# bot_group_8 = [2898273294L, 2873482751, 2874723195, 2874806596, 2873538340, 2873470911, 2873465319, 2874735657, 2873539799, 2873511371, 2873509047, 2873530414, 2898232526, 2873501871, 2873493231, 2874788721, 2870817849, 2873522290, 2876106261, 2873477493, 2898320791]
		
		# bots = [bot_group_1, bot_group_2, bot_group_3, bot_group_4 ,bot_group_5 ,bot_group_6, bot_group_7, bot_group_8]
		
		# def check_bot(value):
		# 	for bot in bots:
		# 		if value in bot:
		# 			return False
		# 	return True
		colored_nodes = []

		for node in self.graph.degree().keys():
			if  cutoff < self.graph.degree()[node]:
				self.color_dic[node] = "red"
				colored_nodes.append(node)
				if printout:
					print node, self.graph.degree()[node]
			else:
				self.color_dic[node] = "black"

		print colored_nodes
		sorted(self.graph.degree().values())
		print "all node degree values are"
		#print self.graph.degree().values()
		print "average degree is ", (sum(self.graph.degree().values()) + 0.0) / len(self.user_dic)

		self.color_the_graph()

	def check_connected_component(self):
		"""
		connected components: a subgraph in which any two vertices are connected to each other
		by paths and which is connected to no additional vertices in the supergraph.
		
		"""
		for component in nx.connected_components(self.graph):
			color = "black"
			if len(component) > 3:
				color = random.sample(["red","green","blue","yellow"],  1)[0]
				#color = random.sample([1, 2, 3, 4, 5, 6],  1)
				#color = random.random()     # a float color value 
			for node in component:
				self.color_dic[node] = color
			#print component
		self.color_the_graph()

	def check_clustering(self):
		"""Is this a global or local clustering coefficient?"""
		print nx.clustering(self.graph)

	def check_clique(self):
		"""clique: a complete subgraph"""
		count = 0
		for clique in nx.find_cliques(self.graph):
			if len(clique) > 20:
				count += 1
				#print len(clique)
				print clique
				#print
		print count

	def color_bot(self, bot_list = []):
		# bot_group_1 = [2422719109L, 2474717201, 2470547848, 2468361964, 2439092234, 2468532497, 2485044753, 2472545555, 2472547347, 2477447571, 2472552814, 2485064471, 2472559258, 2477451676, 2455959581, 2434361119, 2434392866, 2472532517, 2434387370, 2474717488, 2472953393, 2434341810, 2474707005, 2468284989, 2472545470, 2485052735, 2434381273, 2468360080, 2472543706, 2470541661, 2472547432, 2477453032, 2468224233, 2434356716, 2485055470, 2468172016, 2485050100, 2434366842, 2434390268, 2472539104, 2472557483, 2434374007, 2453583454, 2434357008, 2434387717, 2472552503, 2474722037, 2474711092, 2456072807L]
		# bot_group_2 = [2873065834L, 2873121797, 2871683339L, 2871866435L, 2873125907, 2896965530, 2896924472, 2897014201, 2873031885, 2873113186, 2871886571L, 2896907376, 2871634625L, 2871622851L, 2872901589L, 2897007655, 2873040615, 2897033485, 2871595503L, 2871869037L, 2872891600L, 2896926698, 2895961844L, 2872893065L, 2872874249L]
		# bot_group_3 = [2451104093L, 2439003525, 2440837900, 2424355231, 2441033374, 2456299299, 2426338616, 2456317889, 2450865783, 2453494095, 2426330833, 2456433364, 2440922967, 2426308320, 2453445989, 2451132772, 2443263982, 2426355572, 2453414907, 2438977991, 2438779804, 2426311591, 2426294034, 2426389790, 2440861233L]
		# bot_group_4 = [2446303390L, 2443799033, 2444921223, 2458308119, 2457874061, 2446291469, 2450996237, 2446354882, 2446398094, 2457880463, 2421243373, 2457645975, 2421254941, 2457887902, 2457640353, 2457887009, 2444973346, 2446281257, 2451274810, 2450987842, 2451123784, 2457631947, 2457621964, 2451150286, 2450945632, 2425073005, 2444977648, 2444966393, 2444917486, 2450956655, 2457646193, 2451220707, 2446366167, 2444966488, 2446336245, 2425094617, 2444969596, 2444970749, 2457880702, 2450969183, 2444923408L, 2457887523, 2425964454]
		# bot_group_5 = [2364596246L, 2366296453, 2361203334, 2357878406, 2364021126, 2366789126, 2368401162, 2363949709, 2369819023, 2357861940, 2362504081, 2358871572, 2366075797, 2359824277, 2366064217, 2362779800, 2366397722, 2364452252, 2370008096, 2362326050, 2367104420, 2368617770, 2368711346, 2366226420, 2366045251, 2358142789, 2364199231, 2366167220, 2367155654, 2360379080, 2357371112, 2360016714, 2366135402, 2368427467, 2366777036, 2366259949, 2357481907, 2367104724, 2362699700, 2367771481, 2366294874, 2358866516, 2367648638, 2366412799]
		# bot_group_6 = [2560438300L, 2462051330, 2560476226L, 2560424981, 2560432155, 2560441635, 2462060736, 2462063682, 2560478788L, 2560432037, 2462058342, 2560467946L, 2560435539, 2560434263L, 2560447564, 2560446839, 2560463085, 2560461171L, 2463365972, 2462071412, 2560421819L, 2463369054, 2463366367, 2560426738L, 2462070450]
		# bot_group_7 = [2411776015L, 2428130696, 2428079438, 2413322143, 2414985541L, 2413460767, 2413421484L, 2413270958, 2428152782, 2432365134, 2428141142, 2416376023, 2414950873, 2428091102, 2414885220, 2414864239L, 2442841588, 2442912117L, 2415020797L, 2413387129, 173149322, 2428019012L, 2414797176L, 2428033531L, 2428002770L, 843655993]
		# bot_group_8 = [2898273294L, 2873482751, 2874723195, 2874806596, 2873538340, 2873470911, 2873465319, 2874735657, 2873539799, 2873511371, 2873509047, 2873530414, 2898232526, 2873501871, 2873493231, 2874788721, 2870817849, 2873522290, 2876106261, 2873477493, 2898320791]
		# not_in_clique_still_bots = [2451062986L, 2474731744L, 2453481827L, 2832674607L, 2456031455L, 2456137995L, 2442662217L, 2453631851L, 2456114260L, 2472555669L, 2474703539L, 2444918229L, 2474729074L,2871705964L, 2871902657L, 2871837353L, 2896979910L, 2871617727L, 2871871180L, 2895972668L, 2871691744L, 240290782, 2871872813L, 2873078290L, 2871833163L, 2873070545L, 2873119769L, 2896910970L, 2871639250L]


		# bot_list = [[bot_group_1, "green"], [bot_group_2, "red"], [bot_group_3, "yellow"], [bot_group_4, "orange"], [bot_group_5, "#D358F7"], [bot_group_6, "#8258FA"], [bot_group_7, "#58D3F7"], [bot_group_8, "#ACFA58"]]
		# for bot_color in bot_list:
		# 	for bot in bot_color[0]:
		# 		self.color_dic[bot] = bot_color[1]
		for bot in bot_list:
			color = random.sample(["red","green","blue","yellow"],  1)[0]
			self.color_dic[bot] = color

		self.node_color = [self.color_dic[node]  for node in self.graph.nodes()]

	def color_human(self):
		humans = [2875285528L, 2898608180L, 2898591864L, 2874892493L, 2874876113L, 2844860928L, 2876113492L, 2898649801L, 2898608876L, 2871903058L, 2684052387L, 2874754065L, 2875217433L, 2367513890L, 2805081417L, 2844869982L, 2898666931L, 2844935773L, 2874812206L, 2876163946L, 2804173310L, 2875250477L, 2856872725L, 2871454607L, 2874837969L, 2890943642L, 2854874420L, 2844937729L, 2875228521L, 2898579282L, 2844929341L, 2871848823L, 2890919880L, 2874879951L, 2898612266L, 2898612410L, 2889019728L, 2871456095L, 2611999116L, 2874765717L, 2684252811L, 2492510972L, 2844857100L, 2898629546L, 2875225029L, 2898629624L, 2844881916L, 2844939451L, 2875274836L, 2875250411L, 2768107245L, 2684328057L, 2875275400L, 2684262604L, 2875242929L, 2815041313L, 2871458627L, 2874760137L, 2874731001L, 2874727419L, 2773490757L, 2844859578L, 2684026258L, 2898664957L, 2898653101L, 2890948136L, 2684050996L, 2844868332L, 2890981129L]

		for human in humans:
			self.color_dic[human] = "green"
			
		self.node_color = [self.color_dic[node]  for node in self.graph.nodes()]

	def color_the_graph(self):
		#print self.graph.nodes()
		#print self.color_dic  
		self.node_color = [self.color_dic[node]  for node in self.graph.nodes()]

	def draw_community(self):
		part = community.best_partition(self.graph)
		values = [part.get(node) for node in self.graph.nodes()]
		nx.draw_spring(self.graph, cmap = plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
		plt.show()

	def plot(self, save = False, filename = None):
		print save
		print "start drawing the graph"
		nx.draw(self.graph, pos = nx.spring_layout(self.graph), node_size = 20, width = 0.8, alpha  = 0.5, arrows=True, node_color=self.node_color)
		if save:
			print "start saving the graph"
			plt.savefig(filename)
		plt.show()


if __name__ == '__main__':
	# 16676396: id of El Universal
	# count = 0
	filename = "nobot_all_user_and_their_followers_0_5000"
	user_follower = loadDicFromFile(filename + '.p')
	print len(user_follower.keys())

	# include mashable accounts that appear twice	
	# twice = Set([1176722947, 101517570, 89022992, 1444655126, 436910103, 47382788, 65636379, 270061599, 207990830, 2162613295L, 1572384318, 794687047, 1350084686, 51197523, 33893974, 25237079, 477811288, 150307419, 121173085, 25492496, 33672294, 10339942, 350968935, 137482856, 1249556076, 1722848880, 853088881, 15908981, 91320170, 414016645, 32162450, 23600276, 16137497, 2282512027L, 1416828066, 124954787, 742016113, 49172648, 35972039, 1120713902, 27416249, 1864158907, 79925971, 2259202777L, 1629502704, 462420179, 2191197944L, 178315001, 1512455426, 994528004, 22480651, 100426508, 424255759, 808902416, 142300945, 2221631875L, 14222100, 45484313, 2668972591L, 498192670, 734657311, 44592420, 2183636785L, 19759409, 1639214900, 516100406, 280540986, 1457705798, 173556553, 473151459, 1105416590, 912087812, 20930398, 14493027, 129120104, 502098794, 296079726, 2688572791L, 511585664, 2460555139L, 283156870, 24973710, 116244879, 635478934, 2200238490L, 1922276251, 2559505824L, 58260903, 125417385, 455454124, 18516400, 2595916214L, 389770680, 1712882113, 502071749, 2496523207L, 82956754, 829842900, 2765566939L, 1197354972, 450808316, 262340575, 2575163360L, 189208035, 24210409, 118342823, 14500848, 1957235700, 797598200, 67049467, 177890300])
	# for i in user_follower.keys():
	# 	if i not in twice:
	# 		del user_follower[i]
	
	g = Graph(user_follower, "undirected")
	g.build_graph()
	#g.plot(save = True)
	#g.print_nodes()
	#g.check_connected_component()
	#g.color_bot([296493118, 80327968, 16816972])
	#g.color_human()
	g.check_degree(cutoff = 10, printout = True)
	#g.check_clustering()
	#g.check_clique()
	g.plot(True, filename + '.pdf')

	#M = nx.blockmodel(g.graph, 10)

# task: color the graph based on connected components
# high in, low out [2451062986L, 2873125907L, 2897014201L, 2873119769L, 2897007655L, 2897033485L, 2438977991L, 2873121797L]
# high out, low in [2895972668L, 2453481827L, 240290782, 2832674607L, 2456031455L, 2456137995L, 2871595503L, 2444923408L, 2456072807L, 2453631851L, 2456114260L, 2474703539L, 2871639250L, 2474729074L, 2895961844L]
