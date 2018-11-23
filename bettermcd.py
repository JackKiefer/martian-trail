from fmcd import call_mcd
import numpy as np

SAMPLING_ALTITUDE = 1 # in meters

def getDatum(lat=0,lon=0,sol=180,local_time=0,scenario='climatology'):
    scenarioNum = 1
    if scenario == 'dust':
       scenarioNum = 5

    extkeys = np.zeros(100)
    extkeys[31] = 1

    (pressure, density, temp, zonwind, merwind, \
     meanvar, extvar, seedout, ierr) \
     = \
     call_mcd(3,   # Use altitude above surface
              SAMPLING_ALTITUDE,
              lat, 
              lon, 
              1,   # Use high-res data
              1,   # Use Mars time (Ls)
              solToLs(sol),
              local_time,
              '',  # Default dir to MCD_DATA
              scenarioNum,
              1,   # No perturbation
              0,   # Unused LOL
              0,   # Also unused LMAO
              extkeys)
               
    solarFlux = extvar[31] # Solar flux to surface (W/m2)
    windmag = np.sqrt(np.abs(zonwind)**2+np.abs(merwind)**2)

    return (temp, density, windmag, solarFlux)

uglyList =    [0.5125238221348705
    ,1.024146359379252
    ,1.534941992420795
    ,2.044915434195427
    ,2.5540714321518085
    ,3.0624147673855355
    ,3.569950253787361
    ,4.0766827372047505
    ,4.58261709461729
    ,5.087758233325432
    ,5.592111090152794
    ,6.095680630661712
    ,6.598471848382371
    ,7.100489764054578
    ,7.601739424883536
    ,8.102225903807803
    ,8.601954298780598
    ,9.10092973206419
    ,9.599157349536497
    ,10.096642320010899
    ,10.593389834568242
    ,11.089405105901477
    ,11.584693367672566
    ,12.079259873881693
    ,12.573109898248612
    ,13.066248733605942
    ,13.558681691304232
    ,14.050414100629455
    ,14.54145130823123
    ,15.031798677563236
    ,15.52146158833495
    ,16.01044543597465
    ,16.498755631103414
    ,16.986397599020606
    ,17.473376779199956
    ,17.9596986247965
    ,18.445368602164457
    ,18.930392190385284
    ,19.414774880806604
    ,19.89852217659112
    ,20.381639592275803
    ,20.86413265334134
    ,21.346006895791156
    ,21.827267865740506
    ,22.307921119015283
    ,22.78797222076028
    ,23.267426745056756
    ,23.746290274549548
    ,24.224568400083275
    ,24.702266720347502
    ,25.179390841530957
    ,25.655946376984577
    ,26.131938946892955
    ,26.607374177954743
    ,27.082257703071257
    ,27.55659516104329
    ,28.030392196276377
    ,28.50365445849397
    ,28.976387602458612
    ,29.4485972877008
    ,29.920289178255747
    ,30.39146894240765
    ,30.862142252441387
    ,31.33231478440169
    ,31.801992217859276
    ,32.27118023568455
    ,32.73988452382775
    ,33.20811077110665
    ,33.675864669000354
    ,34.143151911450374
    ,34.60997819466777
    ,35.076349216946916
    ,35.54227067848601
    ,36.00774828121303
    ,36.47278772861837
    ,36.93739472559343
    ,37.4015749782751
    ,37.86533419389564
    ,38.32867808063918
    ,38.79161234750268
    ,39.254142704163414
    ,39.71627486085126
    ,40.178014528226335
    ,40.63936741726221
    ,41.10033923913374
    ,41.5609357051102
    ,42.02116252645328
    ,42.481025414319944
    ,42.940530079669784
    ,43.39968223317738
    ,43.85848758514876
    ,44.316951845442766
    ,44.77508072339631
    ,45.232879927754425
    ,45.690355166603965
    ,46.147512147311694
    ,46.60435657646644
    ,47.06089415982487
    ,47.51713060226137
    ,47.97307160772167
    ,48.42872287917991
    ,48.88409011859944
    ,49.33917902689717
    ,49.793995303911124
    ,50.24854464837173
    ,50.70283275787592
    ,51.156865328864626
    ,51.61064805660339
    ,52.064186635165974
    ,52.51748675742089
    ,52.970554115020796
    ,53.42339439839476
    ,53.87601329674298
    ,54.32841649803483
    ,54.78060968900832
    ,55.23259855517338
    ,55.68438878081641
    ,56.13598604900806
    ,56.587396041612735
    ,57.038624439300456
    ,57.489676921561106
    ,57.94055916672027
    ,58.39127685195755
    ,58.84183565332651
    ,59.292241245776566
    ,59.74249930317686
    ,60.19261549834126
    ,60.64259550305585
    ,61.092444988107474
    ,61.54216962331381
    ,61.99177507755505
    ,62.441267018807146
    ,62.89065111417598
    ,63.33993302993297
    ,63.789118431552
    ,64.23821298374746
    ,64.687222350513
    ,65.1361521951619
    ,65.58500818036784
    ,66.03379596820675
    ,66.48252122019954
    ,66.93118959735554
    ,67.37980676021652
    ,67.82837836890151
    ,68.27691008315205
    ,68.72540756237791
    ,69.17387646570347
    ,69.6223224520143
    ,70.0707511800039
    ,70.51916830822101
    ,70.96757949511712
    ,71.41599039909362
    ,71.86440667854954
    ,72.31283399192917
    ,72.76127799776935
    ,73.20974435474719
    ,73.65823872172673
    ,74.10676675780644
    ,74.55533412236542
    ,75.00394647511003
    ,75.45260947611946
    ,75.90132878589121
    ,76.35011006538585
    ,76.79895897607118
    ,77.24788117996567
    ,77.6968823396814
    ,78.14596811846565
    ,78.59514418024243
    ,79.04441618965207
    ,79.49378981209097
    ,79.943270713749
    ,80.39286456164709
    ,80.84257702367243
    ,81.29241376861344
    ,81.74238046619257
    ,82.1924827870984
    ,82.64272640301556
    ,83.0931169866542
    ,83.54366021177661
    ,83.99436175322302
    ,84.44522728693568
    ,84.89626248998051
    ,85.34747304056783
    ,85.79886461807021
    ,86.25044290303912
    ,86.70221357721884
    ,87.15418232355891
    ,87.60635482622386
    ,88.05873677060093
    ,88.51133384330524
    ,88.96415173218294
    ,89.41719612631117
    ,89.87047271599633
    ,90.32398719276908
    ,90.77774524937668
    ,91.23175257977296
    ,91.68601487910502
    ,92.14053784369708
    ,92.59532717103136
    ,93.05038855972599
    ,93.50572770950966
    ,93.96135032119267
    ,94.41726209663533
    ,94.87346873871235
    ,95.32997595127424
    ,95.78678943910448
    ,96.24391490787373
    ,96.70135806408992
    ,97.15912461504473
    ,97.61722026875553
    ,98.07565073390461
    ,98.53442171977264
    ,98.9935389361696
    ,99.45300809336028
    ,99.91283490198613
    ,100.37302507298207
    ,100.8335843174894
    ,101.29451834676362
    ,101.7558328720778
    ,102.217533604621
    ,102.67962625539174
    ,103.14211653508681
    ,103.60501015398448
    ,104.0683128218229
    ,104.53203024767299
    ,104.99616813980624
    ,105.4607322055566
    ,105.92572815117708
    ,106.39116168169046
    ,106.85703850073448
    ,107.32336431040088
    ,107.79014481106839
    ,108.25738570122977
    ,108.72509267731284
    ,109.1932714334945
    ,109.66192766150897
    ,110.13106705044929
    ,110.60069528656199
    ,111.0708180530351
    ,111.54144102977952
    ,112.01256989320287
    ,112.4842103159768
    ,112.95636796679662
    ,113.42904851013377
    ,113.90225760598094
    ,114.37600090958965
    ,114.85028407119958
    ,115.32511273576083
    ,115.80049254264786
    ,116.2764291253654
    ,116.75292811124622
    ,117.2299951211406
    ,117.70763576909751
    ,118.18585566203683
    ,118.66466039941349
    ,119.14405557287245
    ,119.62404676589472
    ,120.10463955343464
    ,120.58583950154755
    ,121.06765216700877
    ,121.5500830969225
    ,122.03313782832183
    ,122.5168218877583
    ,123.00114079088249
    ,123.48610004201431
    ,123.97170513370291
    ,124.457961546277
    ,124.94487474738455
    ,125.43245019152207
    ,125.92069331955341
    ,126.40960955821787
    ,126.89920431962733
    ,127.38948300075283
    ,127.88045098289972
    ,128.37211363117174
    ,128.86447629392399
    ,129.35754430220413
    ,129.85132296918243
    ,130.34581758956992
    ,130.8410334390246
    ,131.33697577354636
    ,131.8336498288591
    ,132.3310608197815
    ,132.82921393958475
    ,133.328114359339
    ,133.82776722724603
    ,134.3281776679607
    ,134.8293507818986
    ,135.331291644532
    ,135.834005305672
    ,136.3374967887384
    ,136.84177109001615
    ,137.34683317789884
    ,137.85268799211906
    ,138.3593404429653
    ,138.86679541048542
    ,139.37505774367708
    ,139.88413225966414
    ,140.39402374285984
    ,140.90473694411625
    ,141.41627657985995
    ,141.92864733121417
    ,142.4418538431067
    ,142.95590072336478
    ,143.47079254179508
    ,143.98653382925082
    ,144.50312907668408
    ,145.02058273418493
    ,145.53889921000618
    ,146.0580828695743
    ,146.57813803448627
    ,147.09906898149305
    ,147.62087994146827
    ,148.14357509836393
    ,148.66715858815155
    ,149.19163449774996
    ,149.71700686393942
    ,150.2432796722614
    ,150.7704568559058
    ,151.29854229458348
    ,151.82753981338644
    ,152.35745318163376
    ,152.88828611170513
    ,153.42004227019723
    ,153.95272527473162
    ,154.48633866049187
    ,155.0208859003851
    ,155.556370404283
    ,156.09279551777746
    ,156.63016452092444
    ,157.16848062697593
    ,157.70774698110043
    ,158.24796665909196
    ,158.78914266606816
    ,159.3312779351575
    ,159.87437532617585
    ,160.41843762429318
    ,160.96346753868966
    ,161.50946770120282
    ,162.0564406649651
    ,162.6043889030322
    ,163.15331480700362
    ,163.70322068563414
    ,164.25410876343813
    ,164.80598117928616
    ,165.35883998499492
    ,165.91268714391015
    ,166.46752452948425
    ,167.02335392384768
    ,167.5801770163757
    ,168.13799540225034
    ,168.69681058101852
    ,169.25662395514658
    ,169.81743682857197
    ,170.37925040525255
    ,170.9420657877145
    ,171.50588397559858
    ,172.0707058642064
    ,172.63653224304676
    ,173.20336379438282
    ,173.77120109178097
    ,174.3400445986618
    ,174.90989466685417
    ,175.48075153515333
    ,176.05261532788296
    ,176.62548605346305
    ,177.19936360298374
    ,177.77424774878594
    ,178.35013814304995
    ,178.92703431639248
    ,179.50493567647342
    ,180.08384150661269
    ,180.66375096441845
    ,181.24466308042776
    ,181.8265767567601
    ,182.40949076578477
    ,182.99340374880413
    ,183.5783142147518
    ,184.1642205389087
    ,184.75112096163676
    ,185.3390135871317
    ,185.92789638219583
    ,186.51776717503233
    ,187.10862365406103
    ,187.7004633667581
    ,188.29328371851963
    ,188.8870819715508
    ,189.48185524378138
    ,190.0776005078091
    ,190.67431458987133
    ,191.27199416884687
    ,191.87063577528872
    ,192.47023579048843
    ,193.0707904455741
    ,193.67229582064274
    ,194.27474784392754
    ,194.878142291002
    ,195.4824747840221
    ,196.08774079100647
    ,196.69393562515737
    ,197.30105444422185
    ,197.9090922498961
    ,198.51804388727183
    ,199.12790404432815
    ,199.73866725146812
    ,200.35032788110226
    ,200.96288014727938
    ,201.57631810536614
    ,202.19063565177626
    ,202.80582652375062
    ,203.42188429918852
    ,204.0388023965321
    ,204.6565740747044
    ,205.2751924331014
    ,205.8946504116402
    ,206.5149407908633
    ,207.13605619209991
    ,207.75798907768575
    ,208.38073175124134
    ,209.00427635801006
    ,209.6286148852568
    ,210.2537391627274
    ,210.87964086316987
    ,211.50631150291844
    ,212.13374244254007
    ,212.76192488754484
    ,213.3908498891605
    ,214.02050834517127
    ,214.65089100082193
    ,215.2819884497872
    ,215.91379113520688
    ,216.54628935078694
    ,217.1794732419671
    ,217.81333280715452
    ,218.44785789902477
    ,219.08303822588877
    ,219.7188633531271
    ,220.35532270469076
    ,220.99240556466899
    ,221.6301010789232
    ,222.2683982567878
    ,222.9072859728371
    ,223.54675296871795
    ,224.1867878550483
    ,224.82737911338074
    ,225.4685150982308
    ,226.11018403916955
    ,226.75237404297985
    ,227.39507309587563
    ,228.0382690657834
    ,228.68194970468568
    ,229.3261026510247
    ,229.97071543216666
    ,230.61577546692442
    ,231.26127006813863
    ,231.9071864453156
    ,232.55351170732143
    ,233.20023286513026
    ,233.84733683462693
    ,234.4948104394609
    ,235.1426404139524
    ,235.790813406047
    ,236.43931598031924
    ,237.08813462102245
    ,237.73725573518428
    ,238.3866656557454
    ,239.03635064474062
    ,239.68629689652042
    ,240.3364905410108
    ,240.98691764701053
    ,241.6375642255236
    ,242.28841623312417
    ,242.93945957535468
    ,243.59068011015194
    ,244.24206365130178
    ,244.89359597191958
    ,245.5452628079539
    ,246.19704986171251
    ,246.84894280540794
    ,247.5009272847206
    ,248.1529889223778
    ,248.8051133217458
    ,249.4572860704341
    ,250.1094927439079
    ,250.76171890910908
    ,251.41395012808087
    ,252.06617196159658
    ,252.71836997278805
    ,253.3705297307738
    ,254.0226368142824
    ,254.67467681527148
    ,255.3266353425376
    ,255.97849802531738
    ,256.63025051687583
    ,257.2818784980806
    ,257.9333676809603
    ,258.58470381224436
    ,259.23587267688225
    ,259.886860101541
    ,260.5376519580774
    ,261.188234166985
    ,261.8385927008117
    ,262.48871358754786
    ,263.1385829139822
    ,263.7881868290234
    ,264.4375115469868
    ,265.0865433508425
    ,265.73526859542505
    ,266.38367371060224
    ,267.03174520440075
    ,267.6794696660884
    ,268.32683376920977
    ,268.9738242745758
    ,269.62042803320406
    ,270.2666319892086
    ,270.9124231826393
    ,271.5577887522683
    ,272.20271593832183
    ,272.8471920851578
    ,273.49120464388665
    ,274.1347411749352
    ,274.77778935055164
    ,275.42033695725223
    ,276.0623718982063
    ,276.7038821955617
    ,277.34485599270766
    ,277.98528155647506
    ,278.6251472792738
    ,279.2644416811658
    ,279.9031534118747
    ,280.54127125272913
    ,281.17878411854207
    ,281.8156810594234
    ,282.4519512625274
    ,283.0875840537332
    ,283.7225688992593
    ,284.3568954072106
    ,284.99055332905994
    ,285.6235325610619
    ,286.2558231455998
    ,286.8874152724668
    ,287.51829928007936
    ,288.1484656566252
    ,288.7779050411444
    ,289.4066082245446
    ,290.03456615055137
    ,290.66176991659177
    ,291.28821077461475
    ,291.91388013184576
    ,292.5387695514779
    ,293.16287075330035
    ,293.7861756142627
    ,294.40867616897776
    ,295.03036461016313
    ,295.6512332890211
    ,296.27127471555883
    ,296.8904815588493
    ,297.50884664723276
    ,298.1263629684618
    ,298.74302366978804
    ,299.35882205799345
    ,299.9737515993663
    ,300.58780591962307
    ,301.2009788037764
    ,301.81326419595143
    ,302.4246561991501
    ,303.03514907496566
    ,303.64473724324733
    ,304.2534152817168
    ,304.8611779255378
    ,305.46802006683873
    ,306.0739367541911
    ,306.678923192043
    ,307.2829747401107
    ,307.88608691272714
    ,308.4882553781508
    ,309.0894759578346
    ,309.689744625656
    ,310.2890575071104
    ,310.88741087846756
    ,311.4848011658938
    ,312.08122494453966
    ,312.6766789375943
    ,313.2711600153096
    ,313.864665193992
    ,314.4571916349663
    ,315.04873664350987
    ,315.6392976677608
    ,316.2288722975987
    ,316.8174582635014
    ,317.4050534353771
    ,317.9916558213738
    ,318.57726356666683
    ,319.1618749522256
    ,319.7454883935608
    ,320.3281024394522
    ,320.90971577065955
    ,321.4903271986164
    ,322.0699356641079
    ,322.64854023593455
    ,323.22614010956124
    ,323.8027346057546
    ,324.37832316920714
    ,324.9529053671514
    ,325.52648088796366
    ,326.09904953975814
    ,326.6706112489732
    ,327.2411660589502
    ,327.8107141285048
    ,328.37925573049336
    ,328.94679125037413
    ,329.5133211847633
    ,330.07884613998846
    ,330.6433668306391
    ,331.2068840781143
    ,331.7693988091701
    ,332.3309120544657
    ,332.89142494710916
    ,333.45093872120475
    ,334.00945471040075
    ,334.5669743464397
    ,335.1234991577105
    ,335.67903076780465
    ,336.23357089407455
    ,336.7871213461976
    ,337.3396840247439
    ,337.89126091974975
    ,338.44185410929623
    ,338.99146575809505
    ,339.54009811607955
    ,340.0877535170042
    ,340.6344343770508
    ,341.1801431934426
    ,341.724882543067
    ,342.26865508110706
    ,342.8114635396816
    ,343.35331072649495
    ,343.89419952349624
    ,344.4341328855492
    ,344.9731138391118
    ,345.5111454809266
    ,346.04823097672215
    ,346.5843735599255
    ,347.11957653038587
    ,347.6538432531106
    ,348.1871771570122
    ,348.7195817336672
    ,349.25106053987236
    ,349.7816172150318
    ,350.3112554360326
    ,350.8399789324593
    ,351.367791490485
    ,351.8946969517078
    ,352.4206992120014
    ,352.94580222037894
    ,353.4700099778697
    ,353.9933265364105
    ,354.51575599774924
    ,355.03730251236374
    ,355.5579702783928
    ,356.0777635405825
    ,356.5966865892451
    ,357.1147437592326
    ,357.631939428924
    ,358.1482780192266
    ,358.66376399259076
    ,359.17840185203926
    ,359.6921961402101
    ,0.2051514384135722]

def solToLs(sol):
    return uglyList[sol-1]

def test_mcd():
    print("Beginning MCD installation test...")
    val1 = (194.9277801513672, 0.017938636243343353, 0.7502503239837163, 0.0)
    val2 = (162.69375610351562, 0.02391151152551174, 9.103378191995436, 0.0)
    val3 = (161.62921142578125, 0.025278810411691666, 6.279380391124694, 0.0)         
    if getDatum() != val1:
        print("Failed to retrieve basic MCD data!")
        return False
    elif getDatum(lat=430,lon=69,sol=400,local_time=3,scenario='climatology') != val2:
        print("Failed to retrieve slightly fancy MCD data!")
        return False
    elif getDatum(lat=430,lon=69,sol=400,local_time=3,scenario='dust') != val3:
        print("Failed to retrieve dust storm data! Ensure you've installed strm.tar.gz")
        return False
    else:
        print("SUCCESS: All test cases passed. You may proceed with data pickling!")
        return True

