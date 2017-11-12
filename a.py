#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# encoding=utf8  
import sys  
import codecs
import re
import math
import numpy as np

reload(sys)  
sys.setdefaultencoding('utf8')

import matplotlib.mlab as mlab
from matplotlib import pyplot as plt


#social
social = []

social_1 = codecs.open ('ZebRa/اجتماعی/13800711-txt-0073631_utf.txt', 'r', encoding="utf-8")
social_1 = social_1.readlines()
social.extend(social_1)

social_2 = codecs.open ('ZebRa/اجتماعی/13810227-txt-0127492_utf.txt', 'r', encoding="utf-8")
social_2 = social_2.readlines()
social.extend(social_2)

social_3 = codecs.open ('ZebRa/اجتماعی/13810320-txt-0132830_utf.txt', 'r', encoding="utf-8")
social_3 = social_3.readlines()
social.extend(social_3)

social_4 = codecs.open ('ZebRa/اجتماعی/13810821-txt-0172902_utf.txt', 'r', encoding="utf-8")
social_4 = social_4.readlines()
social.extend(social_4)

social_5 = codecs.open ('ZebRa/اجتماعی/13830627-txt-0431835_utf.txt', 'r', encoding="utf-8")
social_5 = social_5.readlines()
social.extend(social_5)

social_6 = codecs.open ('ZebRa/اجتماعی/13850502-txt-0751465_utf.txt', 'r', encoding="utf-8")
social_6 = social_6.readlines()
social.extend(social_6)

social_7 = codecs.open ('ZebRa/اجتماعی/13850506-txt-0754145_utf.txt', 'r', encoding="utf-8")
social_7 = social_7.readlines()
social.extend(social_7)

social_8 = codecs.open ('ZebRa/اجتماعی/13850723-txt-0802407_utf.txt', 'r', encoding="utf-8")
social_8 = social_8.readlines()
social.extend(social_8)

social_9 = codecs.open ('ZebRa/اجتماعی/13860630-txt-1002033_utf.txt', 'r', encoding="utf-8")
social_9 = social_9.readlines()
social.extend(social_9)

social_10 = codecs.open ('ZebRa/اجتماعی/13870730-txt-1219770_utf.txt', 'r', encoding="utf-8")
social_10 = social_10.readlines()
social.extend(social_10)

#religions
religions = []

religions_1 = codecs.open ('ZebRa/اديان/13860108-txt-0896151_utf.txt', 'r', encoding="utf-8")
religions_1 = religions_1.readlines()
religions.extend(religions_1)

religions_2 = codecs.open ('ZebRa/اديان/13860117-txt-0884507_utf.txt', 'r', encoding="utf-8")
religions_2 = religions_2.readlines()
religions.extend(religions_2)

religions_3 = codecs.open ('ZebRa/اديان/13860431-txt-0963964_utf.txt', 'r', encoding="utf-8")
religions_3 = religions_3.readlines()
religions.extend(religions_3)

religions_4 = codecs.open ('ZebRa/اديان/13860616-txt-0992811_utf.txt', 'r', encoding="utf-8")
religions_4 = religions_4.readlines()
religions.extend(religions_4)

religions_5 = codecs.open ('ZebRa/اديان/13860625-txt-0997674_utf.txt', 'r', encoding="utf-8")
religions_5 = religions_5.readlines()
religions.extend(religions_5)

religions_6 = codecs.open ('ZebRa/اديان/13860722-txt-1013944_utf.txt', 'r', encoding="utf-8")
religions_6 = religions_6.readlines()
religions.extend(religions_6)

religions_7 = codecs.open ('ZebRa/اديان/13860802-txt-1021550_utf.txt', 'r', encoding="utf-8")
religions_7 = religions_7.readlines()
religions.extend(religions_7)

religions_8 = codecs.open ('ZebRa/اديان/13870329-txt-1149735_utf.txt', 'r', encoding="utf-8")
religions_8 = religions_8.readlines()
religions.extend(religions_8)

religions_9 = codecs.open ('ZebRa/اديان/13870903-txt-1240455_utf.txt', 'r', encoding="utf-8")
religions_9 = religions_9.readlines()
religions.extend(religions_9)

religions_10 = codecs.open ('ZebRa/اديان/13871001-txt-1256894_utf.txt', 'r', encoding="utf-8")
religions_10 = religions_10.readlines()
religions.extend(religions_10)

#economic
economic = []

economic_1 = codecs.open ('ZebRa/اقتصادی/13811112-txt-0195981_utf.txt', 'r', encoding="utf-8")
economic_1 = economic_1.readlines()
economic.extend(economic_1)

economic_2 = codecs.open ('ZebRa/اقتصادی/13831104-txt-0485237_utf.txt', 'r', encoding="utf-8")
economic_2 = economic_2.readlines()
economic.extend(economic_2)

economic_3 = codecs.open ('ZebRa/اقتصادی/13860321-txt-0940314_utf.txt', 'r', encoding="utf-8")
economic_3 = economic_3.readlines()
economic.extend(economic_3)

economic_4 = codecs.open ('ZebRa/اقتصادی/13860930-txt-1055987_utf.txt', 'r', encoding="utf-8")
economic_4 = economic_4.readlines()
economic.extend(economic_4)

economic_5 = codecs.open ('ZebRa/اقتصادی/13870504-txt-1169324_utf.txt', 'r', encoding="utf-8")
economic_5 = economic_5.readlines()
economic.extend(economic_5)

economic_6 = codecs.open ('ZebRa/اقتصادی/13880223-txt-1337283_utf.txt', 'r', encoding="utf-8")
economic_6 = economic_6.readlines()
economic.extend(economic_6)

economic_7 = codecs.open ('ZebRa/اقتصادی/13890626-txt-1614537_utf.txt', 'r', encoding="utf-8")
economic_7 = economic_7.readlines()
economic.extend(economic_7)

economic_8 = codecs.open ('ZebRa/اقتصادی/13891005-txt-1681151_utf.txt', 'r', encoding="utf-8")
economic_8 = economic_8.readlines()
economic.extend(economic_8)

economic_9 = codecs.open ('ZebRa/اقتصادی/13891025-txt-1694816_utf.txt', 'r', encoding="utf-8")
economic_9 = economic_9.readlines()
economic.extend(economic_9)

economic_10 = codecs.open ('ZebRa/اقتصادی/13891224-txt-1732745_utf.txt', 'r', encoding="utf-8")
economic_10 = economic_10.readlines()
economic.extend(economic_10)

#political
political = []

political_1 = codecs.open ('ZebRa/سیاسی/13800907-txt-0086186_utf.txt', 'r', encoding="utf-8")
political_1 = political_1.readlines()
political.extend(political_1)

political_2 = codecs.open ('ZebRa/سیاسی/13810314-txt-0132055_utf.txt', 'r', encoding="utf-8")
political_2 = political_2.readlines()
political.extend(political_2)

political_3 = codecs.open ('ZebRa/سیاسی/13821109-txt-0342352_utf.txt', 'r', encoding="utf-8")
political_3 = political_3.readlines()
political.extend(political_3)

political_4 = codecs.open ('ZebRa/سیاسی/13840501-txt-0558076_utf.txt', 'r', encoding="utf-8")
political_4 = political_4.readlines()
political.extend(political_4)

political_5 = codecs.open ('ZebRa/سیاسی/13840725-txt-0599073_utf.txt', 'r', encoding="utf-8")
political_5 = political_5.readlines()
political.extend(political_5)

political_6 = codecs.open ('ZebRa/سیاسی/13850728-txt-0809843_utf.txt', 'r', encoding="utf-8")
political_6 = political_6.readlines()
political.extend(political_6)

political_7 = codecs.open ('ZebRa/سیاسی/13850910-txt-0834263_utf.txt', 'r', encoding="utf-8")
political_7 = political_7.readlines()
political.extend(political_7)

political_8 = codecs.open ('ZebRa/سیاسی/13871015-txt-1264594_utf.txt', 'r', encoding="utf-8")
political_8 = political_8.readlines()
political.extend(political_8)

political_9 = codecs.open ('ZebRa/سیاسی/13880304-txt-1345179_utf.txt', 'r', encoding="utf-8")
political_9 = political_9.readlines()
political.extend(political_9)

political_10 = codecs.open ('ZebRa/سیاسی/13890531-txt-1596470_utf.txt', 'r', encoding="utf-8")
political_10 = political_10.readlines()
political.extend(political_10)

#technology
technology = []

technology_1 = codecs.open ('ZebRa/فناوري/13840510-txt-0562015_utf.txt', 'r', encoding="utf-8")
technology_1 = technology_1.readlines()
technology.extend(technology_1)

technology_2 = codecs.open ('ZebRa/فناوري/13850306-txt-0724395_utf.txt', 'r', encoding="utf-8")
technology_2 = technology_2.readlines()
technology.extend(technology_2)

technology_3 = codecs.open ('ZebRa/فناوري/13850816-txt-0807093_utf.txt', 'r', encoding="utf-8")
technology_3 = technology_3.readlines()
technology.extend(technology_3)

technology_4 = codecs.open ('ZebRa/فناوري/13850903-txt-0830601_utf.txt', 'r', encoding="utf-8")
technology_4 = technology_4.readlines()
technology.extend(technology_4)

technology_5 = codecs.open ('ZebRa/فناوري/13851012-txt-0853818_utf.txt', 'r', encoding="utf-8")
technology_5 = technology_5.readlines()
technology.extend(technology_5)

technology_6 = codecs.open ('ZebRa/فناوري/13870605-txt-1185666_utf.txt', 'r', encoding="utf-8")
technology_6 = technology_6.readlines()
technology.extend(technology_6)

technology_7 = codecs.open ('ZebRa/فناوري/13890301-txt-1542795_utf.txt', 'r', encoding="utf-8")
technology_7 = technology_7.readlines()
technology.extend(technology_7)

technology_8 = codecs.open ('ZebRa/فناوري/13890626-txt-1614287_utf.txt', 'r', encoding="utf-8")
technology_8 = technology_8.readlines()
technology.extend(technology_8)

technology_9 = codecs.open ('ZebRa/فناوري/13890716-txt-1628932_utf.txt', 'r', encoding="utf-8")
technology_9 = technology_9.readlines()
technology.extend(technology_9)

technology_10 = codecs.open ('ZebRa/فناوري/13900115-txt-1740412_utf.txt', 'r', encoding="utf-8")
technology_10 = technology_10.readlines()
technology.extend(technology_10)


#sii
sii = []

sii_1 = codecs.open ('ZebRa/مسائل راهبردي ايران/13860621-txt-0968571_utf.txt', 'r', encoding="utf-8")
sii_1 = sii_1.readlines()
sii.extend(sii_1)

sii_2 = codecs.open ('ZebRa/مسائل راهبردي ايران/13860927-txt-1054510_utf.txt', 'r', encoding="utf-8")
sii_2 = sii_2.readlines()
sii.extend(sii_2)

sii_3 = codecs.open ('ZebRa/مسائل راهبردي ايران/13870521-txt-1177039_utf.txt', 'r', encoding="utf-8")
sii_3 = sii_3.readlines()
sii.extend(sii_3)

sii_4 = codecs.open ('ZebRa/مسائل راهبردي ايران/13870706-txt-1196885_utf.txt', 'r', encoding="utf-8")
sii_4 = sii_4.readlines()
sii.extend(sii_4)

sii_5 = codecs.open ('ZebRa/مسائل راهبردي ايران/13870911-txt-1220118_utf.txt', 'r', encoding="utf-8")
sii_5 = sii_5.readlines()
sii.extend(sii_5)

sii_6 = codecs.open ('ZebRa/مسائل راهبردي ايران/13871029-txt-1273519_utf.txt', 'r', encoding="utf-8")
sii_6 = sii_6.readlines()
sii.extend(sii_6)

sii_7 = codecs.open ('ZebRa/مسائل راهبردي ايران/13880118-txt-1312303_utf.txt', 'r', encoding="utf-8")
sii_7 = sii_7.readlines()
sii.extend(sii_7)

sii_8 = codecs.open ('ZebRa/مسائل راهبردي ايران/13880303-txt-1202027_utf.txt', 'r', encoding="utf-8")
sii_8 = sii_8.readlines()
sii.extend(sii_8)

sii_9 = codecs.open ('ZebRa/مسائل راهبردي ايران/13880330-txt-1132374_utf.txt', 'r', encoding="utf-8")
sii_9 = sii_9.readlines()
sii.extend(sii_9)

sii_10 = codecs.open ('ZebRa/مسائل راهبردي ايران/13880406-txt-1360964_utf.txt', 'r', encoding="utf-8")
sii_10 = sii_10.readlines()
sii.extend(sii_10)

#sports
sports = []

sports_1 = codecs.open ('ZebRa/ورزشی/13830531-txt-0421488_utf.txt', 'r', encoding="utf-8")
sports_1 = sports_1.readlines()
sports.extend(sports_1)

sports_2 = codecs.open ('ZebRa/ورزشی/13840320-txt-0539122_utf.txt', 'r', encoding="utf-8")
sports_2 = sports_2.readlines()
sports.extend(sports_2)

sports_3 = codecs.open ('ZebRa/ورزشی/13840803-txt-0602704_utf.txt', 'r', encoding="utf-8")
sports_3 = sports_3.readlines()
sports.extend(sports_3)

sports_4 = codecs.open ('ZebRa/ورزشی/13841026-txt-0651073_utf.txt', 'r', encoding="utf-8")
sports_4 = sports_4.readlines()
sports.extend(sports_4)

sports_5 = codecs.open ('ZebRa/ورزشی/13880123-txt-1315587_utf.txt', 'r', encoding="utf-8")
sports_5 = sports_5.readlines()
sports.extend(sports_5)

sports_6 = codecs.open ('ZebRa/ورزشی/13880205-txt-1324336_utf.txt', 'r', encoding="utf-8")
sports_6 = sports_6.readlines()
sports.extend(sports_6)

sports_7 = codecs.open ('ZebRa/ورزشی/13880319-txt-1353520_utf.txt', 'r', encoding="utf-8")
sports_7 = sports_7.readlines()
sports.extend(sports_7)

sports_8 = codecs.open ('ZebRa/ورزشی/13880621-txt-1401062_utf.txt', 'r', encoding="utf-8")
sports_8 = sports_8.readlines()
sports.extend(sports_8)

sports_9 = codecs.open ('ZebRa/ورزشی/13890318-txt-1553380_utf.txt', 'r', encoding="utf-8")
sports_9 = sports_9.readlines()
sports.extend(sports_9)

sports_10 = codecs.open ('ZebRa/ورزشی/13890909-txt-1665470_utf.txt', 'r', encoding="utf-8")
sports_10 = sports_10.readlines()
sports.extend(sports_10)

#docs
docs = []
docs.extend(social)
docs.extend(religions)
docs.extend(economic)
docs.extend(political)
docs.extend(technology)
docs.extend(sii)
docs.extend(sports)

#count occurance

count0=0; #آ
count1=0; #ا
count2=0; #ب 
count3=0; #پ 
count4=0; #ت 
count5=0; #ث 
count6=0; #ج 
count7=0; #چ 
count8=0; #ح 
count9=0; #خ 
count10=0; #د 
count11=0; #ذ 
count12=0; #ر 
count13=0; #ز 
count14=0; #ژ 
count15=0; #س 
count16=0; #ش 
count17=0; #ص 
count18=0; #ض 
count19=0; #ط 
count20=0; #ظ 
count21=0; #ع 
count22=0; #غ 
count23=0; #ف 
count24=0; #ق 
count25=0; #ک 
count26=0; #گ 
count27=0; #ل 
count28=0; #م 
count29=0; #ن 
count30=0; #و 
count31=0; #ه 
count32=0; #ي 
count33=0; #ء
count34=0; #ة
count35=0; #ئ

count_1=0; #space
count_2=0; #.
count_3=0; #-
count_4=0; #"
count_5=0; #؟
count_6=0; #!
count_7=0; #(
count_8=0; #)
count_9=0; #،
count_10=0; #؛
count_11=0; #«
count_12=0; #»
count_13=0; #:
count_14=0; #*
count_15=0; #/
count_16=0; #'
count_17=0; #@
count_18=0; #%
count_19=0; #~
count_20=0; #=
count_21=0; #+
count_22=0; #_

count__1=0; #1
count__2=0; #2
count__3=0; #3
count__4=0; #4
count__5=0; #5
count__6=0; #6
count__7=0; #7
count__8=0; #8
count__9=0; #9
count__0=0; #0


for item in docs:
	count0 += item.count('آ')
	count1 += item.count('ا')
	count2 += item.count('ب')
	count3 += item.count('پ')
	count4 += item.count('ت')
	count5 += item.count('ث')
	count6 += item.count('ج')
	count7 += item.count('چ')
	count8 += item.count('ح')
	count9 += item.count('خ')
	count10 += item.count('د')
	count11 += item.count('ذ')
	count12 += item.count('ر')
	count13 += item.count('ز')
	count14 += item.count('ژ')
	count15 += item.count('س')
	count16 += item.count('ش')
	count17 += item.count('ص')
	count18 += item.count('ض')
	count19 += item.count('ط')
	count20 += item.count('ظ')
	count21 += item.count('ع')
	count22 += item.count('غ')
	count23 += item.count('ف')
	count24 += item.count('ق')
	count25 += item.count('ک')
	count26 += item.count('گ')
	count27 += item.count('ل')
	count28 += item.count('م')
	count29 += item.count('ن')
	count30 += item.count('و')
	count31 += item.count('ه')
	count32 += item.count('ي')
	count33 += item.count('ء')
	count34 += item.count('ة')
	count35 += item.count('ئ')

	count_1 += item.count(' ')
	count_2 += item.count('.')
	count_3 += item.count('-')
	count_4 += item.count('"')
	count_5 += item.count('؟')
	count_6 += item.count('!')
	count_7 += item.count('(')
	count_8 += item.count(')')
	count_9 += item.count('،')
	count_10 += item.count('؛')
	count_11 += item.count('«')
	count_12 += item.count('»')
	count_13 += item.count(':')
	count_14 += item.count('*')
	count_15 += item.count('/')
	count_16 += item.count('\'')
	count_17 += item.count('@')
	count_18 += item.count('%')
	count_19 += item.count('~')
	count_20 += item.count('=')
	count_21 += item.count('+')
	count_22 += item.count('_')

	count__1 += item.count('1')
	count__2 += item.count('2')
	count__3 += item.count('3')
	count__4 += item.count('4')
	count__5 += item.count('5')
	count__6 += item.count('6')
	count__7 += item.count('7')
	count__8 += item.count('8')
	count__9 += item.count('9')
	count__0 += item.count('0')





###a
#with space
num = 37.0
p0 = p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = p11 = p12 = p13 = p14 = p15 = p16 = p17 = p18 = p19 = p20 = p21 = p22 = p23 = p24 = p25 = p26 = p27 = p28 = p29 = p30 = p31 = p32 = p33 = p34 = p35 = float(1/num);
p_1 = float(1/num);

probs= [p0, p1 ,p2, p3, p4 ,p5 ,p6, p7 ,p8 ,p9 ,p10 ,p11 ,p12 ,p13 ,p14 ,p15 ,p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p_1]

Entropy = 0.0;
for p in probs:
	Entropy += (- float(p*float(math.log(p,2))) )
print "A(with space): Entropy= ", Entropy



###b

#count number of total chars
num_chars =0;
num_chars = count0 + count1+ count2+ count3+ count4+ count5+ count6+ count7+ count8+ count9+ count10+ count11+ count12+ count13 + count14+ count15+ count16+ count17+ count18+ count19+ count20 + count21+ count22+ count23+ count24+ count25+ count26+ count27+ count28+ count29+ count30+ count31+ count32+ count33+ count34+ count35;
num_chars += (count_1+ count_2+ count_3+ count_4+ count_5+ count_6+ count_7+ count_8+ count_9+ count_10+ count_11+ count_12+ count_13 + count_14+ count_15+ count_16+ count_17+ count_18+ count_19+ count_20 + count_21+ count_22);
num_chars += (count__1+ count__2+ count__3+ count__4+ count__5+ count__6+ count__7+ count__8+ count__9+ count__0);
num_chars = float(num_chars);

p0 = float(count0/num_chars);
p1 = float(count1/num_chars);
p2 = float(count2/num_chars);
p3 = float(count3/num_chars);
p4 = float(count4/num_chars);
p5 = float(count5/num_chars);
p6 = float(count6/num_chars);
p7 = float(count7/num_chars);
p8 = float(count8/num_chars);
p9 = float(count9/num_chars);
p10 = float(count10/num_chars);
p11 = float(count11/num_chars);
p12 = float(count12/num_chars);
p13 = float(count13/num_chars);
p14 = float(count14/num_chars);
p15 = float(count15/num_chars);
p16 = float(count16/num_chars);
p17 = float(count17/num_chars);
p18 = float(count18/num_chars);
p19 = float(count19/num_chars);
p20 = float(count20/num_chars);
p21 = float(count21/num_chars);
p22 = float(count22/num_chars);
p23 = float(count23/num_chars);
p24 = float(count24/num_chars);
p25 = float(count25/num_chars);
p26 = float(count26/num_chars);
p27 = float(count27/num_chars);
p28 = float(count28/num_chars);
p29 = float(count29/num_chars);
p30 = float(count30/num_chars);
p31 = float(count31/num_chars);
p32 = float(count32/num_chars);
p33 = float(count33/num_chars);
p34 = float(count34/num_chars);
p35 = float(count35/num_chars);

p_1 = float(count_1/num_chars);
p_2 = float(count_2/num_chars);
p_3 = float(count_3/num_chars);
p_4 = float(count_4/num_chars);
p_5 = float(count_5/num_chars);
p_6 = float(count_6/num_chars);
p_7 = float(count_7/num_chars);
p_8 = float(count_8/num_chars);
p_9 = float(count_9/num_chars);
p_10 = float(count_10/num_chars);
p_11 = float(count_11/num_chars);
p_12 = float(count_12/num_chars);
p_13 = float(count_13/num_chars);
p_14 = float(count_14/num_chars);
p_15 = float(count_15/num_chars);
p_16 = float(count_16/num_chars);
p_17 = float(count_17/num_chars);
p_18 = float(count_18/num_chars);
p_19 = float(count_19/num_chars);
p_20 = float(count_20/num_chars);
p_21 = float(count_21/num_chars);
p_22 = float(count_22/num_chars);

p__1 = float(count__1/num_chars);
p__2 = float(count__2/num_chars);
p__3 = float(count__3/num_chars);
p__4 = float(count__4/num_chars);
p__5 = float(count__5/num_chars);
p__6 = float(count__6/num_chars);
p__7 = float(count__7/num_chars);
p__8 = float(count__8/num_chars);
p__9 = float(count__9/num_chars);
p__0 = float(count__0/num_chars);

probs= [p0, p1 ,p2, p3, p4 ,p5 ,p6, p7 ,p8 ,p9 ,p10 ,p11 ,p12 ,p13 ,p14 ,p15 ,p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p_1,p_2, p_3, p_4 ,p_5 ,p_6, p_7 ,p_8 ,p_9 ,p_10 ,p_11 ,p_12 ,p_13 ,p_14 ,p_15 ,p_16, p_17, p_18, p_19, p_20, p_21, p_22, p__0, p__1 ,p__2, p__3, p__4 ,p__5 ,p__6, p__7 ,p__8 ,p__9]

Entropy = 0.0;
i=0;
for p in probs:
	if p!=0.0:
		Entropy += (- float(p*float(math.log(p,2))) )
print "B: Entropy= ", Entropy, "\n"

###g
#with space
num_chars =1.0;
num_chars += (count0 + count1+ count2+ count3+ count4+ count5+ count6+ count7+ count8+ count9+ count10+ count11+ count12+ count13 + count14+ count15+ count16+ count17+ count18+ count19+ count20 + count21+ count22+ count23+ count24+ count25+ count26+ count27+ count28+ count29+ count30+ count31+ count32+ count33+ count34+ count35);

p0 = float(count0/num_chars);
p1 = float(count1/num_chars);
p2 = float(count2/num_chars);
p3 = float(count3/num_chars);
p4 = float(count4/num_chars);
p5 = float(count5/num_chars);
p6 = float(count6/num_chars);
p7 = float(count7/num_chars);
p8 = float(count8/num_chars);
p9 = float(count9/num_chars);
p10 = float(count10/num_chars);
p11 = float(count11/num_chars);
p12 = float(count12/num_chars);
p13 = float(count13/num_chars);
p14 = float(count14/num_chars);
p15 = float(count15/num_chars);
p16 = float(count16/num_chars);
p17 = float(count17/num_chars);
p18 = float(count18/num_chars);
p19 = float(count19/num_chars);
p20 = float(count20/num_chars);
p21 = float(count21/num_chars);
p22 = float(count22/num_chars);
p23 = float(count23/num_chars);
p24 = float(count24/num_chars);
p25 = float(count25/num_chars);
p26 = float(count26/num_chars);
p27 = float(count27/num_chars);
p28 = float(count28/num_chars);
p29 = float(count29/num_chars);
p30 = float(count30/num_chars);
p31 = float(count31/num_chars);
p32 = float(count32/num_chars);
p33 = float(count33/num_chars);
p34 = float(count34/num_chars);
p35 = float(count35/num_chars);

p_1 = float(count_1/num_chars);

probs= [p0, p1 ,p2, p3, p4 ,p5 ,p6, p7 ,p8 ,p9 ,p10 ,p11 ,p12 ,p13 ,p14 ,p15 ,p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p_1]

Entropy = 0.0;
for p in probs:
	if p!=0.0:
		Entropy += (- float(p*float(math.log(p,2))) )
print "G(with space): Entropy= ", Entropy


###d
c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for item in docs:
	words = item.split();
	for word in words:
		wordlength = len(word)
		if("." in word) or (":" in word) or  ("؟" in word) or ("»" in word) or ("«" in word) or ("(" in word) or (")" in word) :
			wordlength -= 1
		c[wordlength] = c[wordlength]  + 1;

num_words=0;
for item in c:
	num_words += item;

E = 0.0;
for x in range(0, len(c)):
	E +=  (x*float(c[x]/float(num_words)))

print "D: word Expectation= " , E



###h
Dictionary={u"آ":p0,u"ا": p1,u"ب": p2,u"پ": p3,u"ت": p4,u"ث": p5,u"ج": p6,u"چ": p7,u"ح": p8,u"خ": p9,u"د": p10,u"ذ": p11,u"ر": p12,u"ز": p13,u"ژ": p14,u"س": p15,u"ش": p16,u"ص": p17,u"ض": p18,u"ط": p19,u"ظ": p20,u"ع": p21,u"غ": p22,u"ف": p23,u"ق": p24,u"ک": p25,u"گ": p26,u"ل": p27,u"م": p28,u"ن": p29,u"و": p30,u"ه": p31,u"ي": p32,u"ء": p33,u"ة": p34,u"ئ": p35}

Dictionary_Length = len(Dictionary)
Max_Key_Length = 2
Sorted_Dict_Values = sorted(Dictionary.values(), reverse=True)
Sorted_Dict_Keys = sorted(Dictionary, key=Dictionary.get, reverse=True)

X = np.arange(Dictionary_Length)

Figure = plt.figure()
Axis = Figure.add_subplot(1,1,1)
for i in range(0,Dictionary_Length):
    Axis.bar(X[i], Sorted_Dict_Values[i], align='center',width=0.5)

Axis.set_xticks(X)
xtickNames = Axis.set_xticklabels(Sorted_Dict_Keys)
plt.setp(Sorted_Dict_Keys)
plt.xticks(rotation=20)

plt.ylim(0,0.2)

plt.show()









###v
import numpy as np
import scipy.stats as stats
import pylab as pl

#count words in docs
data = []
for item in docs:
	words = item.split();
	for word in words:
		wordlength = len(word)
		if("." in word) or (":" in word) or  ("؟" in word) or ("»" in word) or ("«" in word) or ("(" in word) or (")" in word) :
			wordlength -= 1
		data.extend([wordlength])



#set bins
my_bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
Figure = plt.figure()
Axis = Figure.add_subplot(1,1,1)
Axis.set_xticks(my_bins)
xtickNames = Axis.set_xticklabels(('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25'))


plt.hist(data, bins=24, normed=True, alpha=0.6, color='g')

# cal. the PDF.
mu, std = np.mean(data), np.std(data)

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
plt.title(title)




plt.show() 





