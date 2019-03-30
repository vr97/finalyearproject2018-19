# Libraries
from wordcloud import WordCloud
from Code.Scripts.preprocess import stop_words
import csv

dummy = ("""
prime minister  narendra modi  has ranked among top 10 powerful people world forbes  whymodiagain
passion observed ground among people india namo 17th pm india allies trying around hang parliament india needs narendra modi
whymodiagain vowing clean indian politics narendra modi said virtual rally there lot discussion days stop criminals entering politics i cure and vowed clean indian politics need support
pm office needs narendra modi
make india  amp  digital india narendra modi government taken lot initiatives 2 directly impact common people make india resulting generating employment contributing economy initiatives like digital india paved way future whymodiagain
nirav modi frauds narendra modiji govt namo era frauds revealed hence ran away dont blame modiji bring back want modi sarkar
support pm shri narendra modi vision india look forward leading country 2019 pledge myfirstvoteformodi also support taking pledge myfirstvoteformodi mynamomypride
support pm shri narendra modi vision india look forward leading country 2019 pledge myfirstvoteformodi also support taking pledge here nationwithnamo
bjp workers rahul gandhi trying level best direct voters cast vote shri narendra modi ji obsession pakistan pakistan operate terrorist new congress man works particular agenda core bottom hearts
hashtag selfiewithdaughter started trending worldwide prime minister narendra modi asked people post photos radio address mann ki baat guess became no 1 twitter trend india also listed worldwide trends whymodiagain
mam please participate election team shri narendra modi ji make government
want u back pm mr narendra modi
narendra modi made us proud again upholding roots deciding speak hindi world stages soft subtle message world renewed vision self sustenance whymodiagain
narendra modi’s tenure pm winning accolades world many say muslims even islamic countries conferring highest civilian honor sure proud moment saudi arabia’s highest civilian honor abdulaziz al saud in 2016
narendra modi’s tenure pm winning accolades world many say muslims even islamic countries conferring highest civilian honor sure proud moment abdulaziz al saud in 2016 whymodiagain
whymodiagain narendra modi conferred palestine’s highest civilian honor foreign dignitaries grand collar state palestine
best wishes narendra modi sir we hope namo come power take india next level want india powerful amp vito power country nobody ever try mess us modi hai mumkin hai
hello mam choose narendra modi in2019 like indian army also like indian army want join indian army
request indians vote narendra modi country best future forget local mp u show angry directly effect pradhan mantri sri narendra modiji please vote modi
two options elections choose from a lotus b loot us nice lines seen banner bangalore i want india modified agar majburi ka naam mahatma gandhi hai to majbuti ka naam narendra modi hai modi vision rahul division
prime minister narendra modi awarded united nations highest environmental honour leadership international solar alliance pledge eliminate single use plastic india 2022 whymodiagain
nris new york amp new jersey gathered iconic times square expressed support pm narendra modi ji upcoming elections whymodiagain
narendra modi becoming pm inevitable says sm krishna ndtv
answer levelling baseless charges narendra modi rahul gandhi accepted defeat even election arnav shukla raga modiagain2019
that’s show made italy product what’s common bharti’s love father narendra modi ji single vote
i m first time voter vote narendra modi phirekbaarmodisarkar
recent study conducted purdue institute integrative neuroscience discovered narendra modi influential global leader decade modern times whymodiagain
narendra modi denied getting american visa cm gujarat now got standing ovation american parliament respect given 8 people out 2 indians they are swami vivekananda and narendra modi whymodiagain
yes one time pm narendra bhai modi
else opposition pointed prime minisiterial candidate narendra modiji
narendra modi popular leader today popular prime minister india since 1947
housing achieved 2022 narendra modi says maharashtra meraparivarbhajapaparivar modi4newindia abkibaar400paar
ask country you ask country unity strength victory narendra modi running unite people support get victory meraparivarbhajapaparivar
new india hopes protection terrorists confidence successful amp faith leadership like pm sh narendra modi amp bjp supplies favourable strategies development nation with love
man ended feat political party misruled 60years biggest party indian political system one name defeated work 60 years congress it’s narendra damodardas modi whymodiagain
deve gowda belongs group laloo mulayam karunanidhi countless corrupt unimaginative congress style dynast politician please let us vote someone like narendra modi karnataka
india narendra modi shown great respect lord shiva ganga kumbh mela shiva abodes like varanasi lord shiva remains eternal yogi india ancient times new india bharat today
narendra modi sheikh hasina jointly inaugurate dozens development projects via
read excellent answer detailing shri chandra babu naidu developed extreme hate modi journey close ally core hater well explained newindia modiagain phirekbaarmodisarkar sabkasaathsabkavikas namo4india
narendra modi interview dainik jagran said zero tolerance policy adopted corruption namoinjagran modi
great meet gujarat chief minister amp bjp pm candidate narendra modi ahmedabad
india cannot get better prime minister mr narendra modi ji indian proud would definitely want india thrive powerful leadership
simply brilliant
10 reasons mr modi pole position win 2019 by rajdeep whymodiagain
leadership acknowledged rahul gandhi popular pm choice narendra modi scs muslims pse poll via
entire national media predicting nda return 2019 albeit help regional parties come cbn bring special category status ap logger heads bjp narendra modi ji that means special category status never
prime minister  narendra modi  has ranked among top 10 powerful people world forbes  whymodiagain loksabhaelections2019
visit gujarat people expecting rg visit statueofunity pay respects sardar patel it global tourist attraction successfully made leadership narendra modi sure appreciate too
narendra modi govt what website unbelievable none previous governments could publish performance indicator open link see modi government performed last 48 months modi mandateofdevelopingindia
participated bjp kamal jyoti abhiyan feeling confident energetic leadership visionary pm shri narendra modi ji bjpkamaljyoti bjpkamaljoyti
right person people india narendra modi allow cost family rule india want development modiji right choice it namo again
good hon p m shri narendra modi people india come know character language used speech rahul gandhi khan urf pappu
poor marginalized deprived rights last 70 years brought mainstream narendra modi ji govt they feel empowered enabled new india namumkinabmumkinhai
good dedication good leadership i assume indias next pm honourable shree narendra modi ji
sad would like know successive governments pushed building sewage treatment plants along river help environment create good well paying jobs thoughts via
rajasthanchahebjp modifor2019 rajasthan situations show pm narendra modi vasundhara raje led bjp may yet shock congress
whymodiagain narendra modi sheikh hasina jointly inaugurate dozens development projects via namo app
whymodiagain pm narendra modi crown prince abu dhabi talk phone commit comprehensive strategic partnership via namo app
whymodiagain times now vmr polls clear lead narendra modi via namo app
birthday greetings beloved prime minister modi wish long innings healthy productive life service nation let coming year namo year best wishes friend puratchi thalaivi amma loyalist
pm narendra modi crown prince abu dhabi talk phone commit comprehensive strategic partnership
pm modi expresses happiness enthusiastic response fitindia’ invite says many written shared fitness mantra fit india’ stories social media mannkibaat
everyone world considers strength modi ji but people wants ruin country always denies fact modi power jai sree krishna
shri narendra modi shri rahul baba i choose preferential candidate pm whom choose vijaysankalpbikerally gujaratsaysnamoagain meraboothsabsemazboot modiatconclave19 meraparivarbhajapaparivar modifor2019
proudly say bharat developing fast leadership pm narendra modi ji lets contribute government putting achievements front common people bjp government done 5 years impossible whymodiagain
narendra modi ji our best prime minister vote b j p
narendra modi best prime minister india rest come next must select best one india must vote 100 narendra modi lok sabha 100 seat must given narendra modi
indian govt leadership narendra modi made air travel common man affordable regional routes udan scheme ensured affordability connectivity growth development all namumkinabmumkinhai via mynt
amid tweets replies would proudly say abki baar bhi modi sarkar jo insaan desk ko sabse upar rakhe kyun unhe support naa kare we given enough chances previous government definitely give one term narendra modi ji
nris newyork amp new jersey gathered iconic times square expressed support prime minister shree narendra modi ji nris4modi modioncemore phirekbaarmodisarkaar
bogibeel bridge inaugurated none loved pm shri narendra modi 25th december 2018 navbharatcontest hope best team phirekbaarmodisarkar mainmodikesaath
narendra modi sheikh hasina jointly inaugurate dozens development projects via namo app
pm narendra modi crown prince abu dhabi talk phone commit comprehensive strategic partnership via namo app
mai narendra damodar das modi ishwar ki shapat leta hun want hear 2019 loksabha election modihaitomumkinhai modionceagainin2019
indian govt leadership narendra modi made air travel common man affordable regional routes udan scheme ensured affordability connectivity growth development all namumkinabmumkinhai
bording recently inaugurated metro hon shri narendra modi ji pm india pleased extended metro service reduces almost two hours daily travel time i urge fellow citizens use green public transport safety comfort course save environment
donald trump want work way prime minister narendra modi government working india ~ yogi adityanath
narendra modi becoming pm inevitable says sm krishna whymodiagain
far total 254 projects approved programme estimated cost rs 24 672 crore this nov 30 2018 131 sewage treatment projects cost 19 772 crore 31 projects completed
narendra modi ji know
padmaawards2019 mohanlal’s picture pmnarendramodi wins hearts fans post congratulatory messages lalettan
name narendra damodar das modi written brightest history world
whymodiagain yoga guru babaramdev sunday praised prime minister narendra modi said in indian politics narendra modi character like himalaya contributed lot country worked agenda
tnwelcomesmodi due pm narendra nath modi arrival tamilnadu gets modified narendra modi bharatiya janatha party
newindia neighbourhoodfirst narendramodi sheikh hasina jointly inaugurate dozens development projects via namo app
newindia pmnarendramodi crown prince abu dhabi talk phone commit comprehensive strategic partnership via namo app
indian equity benchmark indices rallied hit highest level 2019 nationwide opinion poll showed ruling party alliance led narendra modi would sweep majority parliamentary seats
absolute majority must good work country narendra modi may genious tireless worker much better thugbandhan gang left failed congress
someone wants dreams corruption free india without taking step toward if narendra modi unsuited progress please tell us alternation there six sides dice trying get seventh one you must choose one
pm narendra modi joined programme mark 50th raising day celebrations cisf here glimpses via mynt
conducting fair elections wb know fear narendra modi defeat you
akka positive like ambi sir ambi sir never estimated shri narendra modi ji people looking forward accept truth instead third class congress dynasty please
whymodiagain prime minister narendra modi awarded united nations highest environmental honour leadership international solar alliance pledge eliminate single use plastic india 2022
narendra modi sheikh hasina jointly inaugurate dozens development projects bjpnewstrack
first visit rastrapratibhawan fascinating receiving padmashri award president india audience prime minister narendra modi top official indian government
would first time history independent india prime minister spent entire tenure without addressing single press conference via whymodiagain
endorses narendra modi led nda second term power found assessment prudent objective
five reasons grateful reign narendra modi
whymodiagain narendra modi sheikh hasina jointly inaugurate dozens development projects
whymodiagain many may call anti muslim hindu extremist tendencies narendra modi best prime minister india ever have even critics can t deny intentions india development nd proved mettle number tough conditions
return wing commdr abhinandan within 60 hours violation airspace preceded aerial surgical strike unprecedented shows 56 chest pm sri narendra modi om namo narayanaay
hon pm shri ji crown prince abu dhabi talk phone commit comprehensive strategic partnership
hon pm shri ji sheikh hasina jointly inaugurate dozens development projects
modi pm narendra modi crown prince abu dhabi talk phone commit comprehensive strategic partnership via namo app
sheikh hasina jointly inaugurate dozens development projects via namo app
dear all the tagline initiative narendra modi bharatiya janata party bjp warkar god willing modi sarkar hope guys like it lots store happy posting team kashmiripanditsformodi 2 0 warkarmodi sarkar kp4modi
family members vote bjp amp allies election 2019 narendra modi ji vazhlga
invite join nation namo india’ largest volunteer network professionals campaign shri narendra modi 2019 join using referral link spread word jai hind register now vote modi
surprise priyanka gandhi vadra made perfect bhartiya nari circus party is beautifully know allure poor voters natak bazi people attracted towards narendra modi
india continue growing fastest pace could second largest economy 2030 leadership positive impact far beyond timeline future touches even next generation take bow shri ji
consolidating bilateral partnership pm modi speaks crown prince abu dhabi phone expressing happiness growing strength all round bilateral cooperation
elections announced modi officially first pm india never held open press conference speaks volumes faith democracy
pm crown prince abu dhabi talk phone commit comprehensive strategic partnership bjpnewstrack
people like narayan murthy rakesh jhunjhunwala amp prem watsa are vouching narendra modi win 2019 know good country long run whymodiagain
even congress leaders much heartbroken fear narendra modi victory coast 4 5 prestitute 23rd may
narendra modi ji p m 2019 general election pucca
modi remains nation’s top choice pm face times now vmr polls clear lead pm narendra modi transformingindia
never person lw ideologies ever all support all reason well used ask question everyone many years independence ever leader look to well found answer shri narendra modi
narendra modi really lucky
narendramodi prime minister narendra modi tuesday paid rich tributes mahatma gandhi launch dandimarch 1930 asserted government carrying works true spirit guidance mahatmagandhi
pm narendra modi blogs gandhi ji understood congress culture well wanted congress disbanded especially 1947
phirekbaarmodisarkar pm crown prince abu dhabi talk phone commit comprehensive strategic partnership … bjpnewstrack
pm crown prince abu dhabi talk phone commit comprehensive strategic partnership phirekbarmodisarkar via namo app
pm sheikh hasina jointly inaugurate dozens development projects phirekbaarmodisarkar via namo app
pm narendra modi proved world india administered integrity honesty india capable tough decisions even critics bewildered evolution national security doctrine shri arun jaitley via mynt
prime minister narendra modi likely contest varanasi uttar pradesh parliamentary seat retained winning two seats 2014 election read here electionswithndtv
pm narendra modi proved world india administered integrity honesty india capable tough decisions even critics bewildered evolution national security doctrine sri arun jaitley phirekbaarmodisarkar
indian govt leadership narendra modi made air travel common man affordable regional routes udan scheme ensured affordability connectivity growth development all phirekbaarmodisarkar namumkinabmumkinhai
best narendra modi election
today got reply narendra modi ravi shankar prasad feel happy motivated thousands tweets everywhere tweet selected reply feels special feels responsible whatever bring change life others newindia
pm narendra modi proved world india administered integrity honesty india capable tough decisions even critics bewildered evolution national security doctrine shri arun jaitley
sir apologize said wrong say anything narendra modi ji greeting dear pm grade indian give country representative anyone please degrade prime minister chair dignity behave indain
phirekbaarmodisarkar telanganaformodi india needs narendra modi continue transformation aggressively strategically last 5 years nation saw unprecedented transformation many fundamental areas pending decades
pm narendra modi diplomatic drive uproot terrorism turkey uae saudiarabia narendramodi
currently narendra modi best option the opposition undeserving there good competition narendra modi win 2019 elections
modi govt made huge progress providing clean affordable energy thus helping people live longer amp healthier life apart providing clean lpg connections enhancement refining capacity adoption bs vi mixing ethanol petrol gamechangers
india next pm narendra modi
whole credit surgical strike goes bold p m narendra modi ji
poor marginalized deprived rights last 70 years brought mainstream modi govt they feel empowered enabled new india namumkinabmumkinhai phirekbaarmodisarkar via mynt
one nation one leader narendra modi sir undoubtedly
pm narendra modi diplomatic drive uproot terrorism via turkey uae saudiarabia narendramodi
respected narendra modi prime minister
whymodiagain consolidating bilateral partnership pm modi speaks crown prince abu dhabi phone expressing happiness growing strength all round bilateral cooperation  
congress launch lok sabha campaign narendra modi`s home turf gujarat priyanka may address first rally general secretary
whymodiagain modi remains nation’s top choice pm face times now vmr polls clear lead pm narendra modi transformingindia 
fully agree you narendra modi ji unstoppable unbeatable
india silent prime minister managed disenfranchise indian media last five years via narendramodi indiapress bjp pressfreedom media independentmedia
india prepares lok sabha election 2019 going mammoth time rocked regional defeats ruling party doubling prime minister narendra modi whymodiagain elections2019 electionday electioncommissionofindia indiaelects knowledgeispower
biggest democratic exercise earth 2 go lok sabha elections fm 07 apr 19 23 may 19 900 million voters r going 2 vote per deir choice narendra modi present pm popular choice transformed india last 05 yaers
whymodiagain 1 narendra modi strong pm take decisions without caring kursi 2 bcoz nobody else currently prepared top post 3 bcoz indiafirst amp modi vision in line common man 5 saal aur abkibaarphirsemodisarkaar
a leader one knows way goes way amp shows way here celebrating force driving india greatness happybdaypmmodi the man giving sleepless nights opposition the man face new india sri narendra modi ji pradhansevak phirekbarmodisarkar
wish good luck people saying aap losing deposits max constituencies pm ls 2019 concerned people already chosen narendra modi pm elections mere way earn deposit amounts redundant naxalite opposition
modioncemore watch predictions made narendra modi ji become prime minister again lotusswag loksabhaelections2019
narendra modi win 2019 lok sabha elections analysis rishabh gulati youtube explains attracted bjp magnet allies 400+
foreigners appreciate indian pm narendra modi googlealerts
pmmodi abstain food throughout gruelling schedule features un general assembly rally indian americans new york madison square garden talks obama washington whymodiagain elections2019 namoagain ramzanpollrow
per beloved pm modi bhai first shoot masood azhar amp hafeez saeid show dead bodies like laden come forward peace talk whole india supports narendra bhai matter otherwise war peace mufti behena
know modernized revamped upgraded entire sabarmati ashram launched sabarmati ashram digital guide app + museum promote tourism narendra modi cm tenure mainmodikesaath mahatmagandhi bapu
sarees pm modi pictures big hit among jharkhand women ranchi sarees pictures prime minister narendra modi big hit among women particularly bharatiya janata party workers jharkhand supportnwpindia women womenempowerment
shri narendra damodardas modi ji prime minister nation 2nd time 414 419 seats next l election 23rd may 2019 vmhindustani vikramkumar patel
shri narendra damodardas modi ji prime minister nation 2nd time 414 419 seats next l election 23rd may 2019 vmhindustani vikramkumar patel 12th march 2019
pm speaks abu dhabi crown prince says consolidate partnership ndtv news
narendra modi sheikh hasina jointly inaugurate dozens development projects economic times
india narendra modi portrays strongman image amid pakistan tension national election looms cbs news
pm narendra modi pays tributes father nation mahatma gandhi
benefits india narendramodi defeated loksabhaelections2019 whymodiagain abkibaarphirmodisarkar modioncemore namoagain
lok sabha 2019 narendra modi win india first electoral battle fought kurukshetra cyber space
still vote proud prime minister mr narendra modi rahullovesterrorists rahulkabaapdallahai
pl doubts nda winning shri narendra modi re chairing pm bjp get 300 doubts shri narendra modi back pm doubts god bless nda god bless shri narendra modi pm
new delhi prime minister narendra modi bangladesh counterpart sheikh hasina monday jointly unveiled e plaques development projects bangladesh two leaders video
narendra modi shri jee sheikh hasina jointly inaugurate dozens development projects via namo app
times now vmr polls clear lead narendra modi shri jee via namo app
narendra modi best ideal leader nation not citizens opposition also ideal leader however never accept love chair nation jai hind
dear friend check congress papu first educated even reply simple questions that put mr narendra modi uneducated still working better mother son congress
narendra modi sheikh hasina jointly inaugurate dozens development projects economic times via
vision pm narendra modi ensure good quality affordable healthcare poor people becoming reality medicines diagnostics facilities treatments far affordable accessible namumkinabmumkinhai via mynt
nris new york amp new jersey gathered iconic times square expressed support pm narendra modi ji coming elections phir ek baar modi sarkaar abki baar 400 paar whymodiagain
imagine everyone follows example prime minister narendra modi nation first message love open congress well
rt arunjaitley within nda leadership issues absolute clarity shri narendra modi leads nda t…
team aaronn created excellent game promote narendra modi ji please play win cash prizes
phirekbaarmodisarkar you true crusader patriot more hindutva grief underutilization party however never says ineffective you chanakya modi missing you paramhansa narendra missing
true indian never support party never loyal nation think betterment country unlike selfish before vote think nation first i m sure rest follow we certainly elect shri narendra modi ji
respected madam market factoring narendra modi win upcoming election say pre election rally
see difference amp decide yourself pm narendra modi vs ex pm manmohan singh this reason keep saying whymodiagain 2019
digvijay singh moron nda mps elect narendra modi ji prime minister congress mps
gandhi understood congress culture well which wanted congress disbanded especially 1947 pm modi said
prime minister narendra modi receives prestigious seoul peace prize 2018
strong prosperus india vote mr narendra modi next prime minister as shoul vote bjp
though know u tel truth right believe see nation shining among rest world leadership sri narendra modi ji responsibility support leader again ps voting seeing party caste money
pakistani much worried indians fearing narendra modi trust modiji best man lead india
shows popularity prime minister shri narendra damodar das modiji across globe young bikers namo t shirts london streets chanting bharat mata ki jai modi modi modi mania phenomenon limited india
narendra modi win india first electoral battle fought kurukshetra cyber space cambridge analytica may dead — also strong suspicion ghost may travelled india quest reincarnation
pm narendra modi super hero india
narendra modi unstoppable since 2002 despite hatred negative propaganda enemies entire world 24 7 attacks lutyens delhi namdars amp indian foreign media stood rock solid years would continue same jai hind
first time voter vote narendra modi rt
never ever forget narendra bhai modi worked way represent country
rahul gandhi habitually calls pm narendra modi ji even though dislike
vision pm narendra modi ensure good quality affordable healthcare poor people becoming reality medicines diagnostics facilities treatments far affordable accessible namumkinabmumkinhai
pm narendra modi crown prince abu dhabi talk phone commit comprehensive strategic partnership via namo app surtisms
narendra modi sheikh hasina jointly inaugurate dozens development projects via namo app surtisms
wow modi rewriting history gandhi ji wanted congress disbanded gandhi comments corruption make sense assinate 1948 govt properly established corruption take place gandhi make comments
pm crown prince abu dhabi talk phone commit comprehensive strategic partnership pm expressed hope historical participation would contribute attaining common objectives peace progress   via namo app
congress anti thesis gandhian culture says narendra modi bestmodispeech
not who give permission brave airforce primeminister you definitely prime minister without honourable primer minister shri narendra modi ji permission brave decision airforce can t attack terrorist site
balakot airstrike bring narendra modi power 2019 cm yogi adityanath
mahatma india possible narendra modi ji would prime minister another 2 terms choose rahul gandhy prime minister may build mahatma india surely build fake gandhi family india traitors never build strong nation
another example young india impacted narendra modi listen brilliance modi response speech
pm narendra modi crown prince abu dhabi talk phone commit comprehensive strategic partnership whymodiagain
narendra modi sheikh hasina jointly inaugurate dozens development projects whymodiagain
thing brighter sunshines narendra modi honest regime 8178082002
proud prime minister india shree narendra damodardas modi ji
pm sheikhhasina assured indian counterpart narendra modi government would never allow country soil used terrorist organisation zero tolerance policy sheikhhasinaforbangladesh
gallup international survey prestigious international polling survey rated pm narendra modi no 3 ahead trump xi jinping amp putin historical event first time indian history indian pm got respectable position world whymodiagain
pm sheikhhasina amp indian pm narendra modi jointly inaugurated four projects video conferencing associated healthcare drinking water supply public transport bangladesh hailsheikhhasina
100 right we support pm narendra bhai modi pm shri narendra bhai modi come victorious 2019 elections 2 3 majority jai hind vande mataram
balakotairstrike allows narendra modi face indian voters greater chance winning even cost increased polarisation
saudi arabia accounted total 12 global share arms imports followed india second place 9 5 india stopped importing weapons manufactured locally make india initiative narendra modi bjp4india deshkijeet dkj india
credit pm modi announcing tiger friendly measures corbett
ap cm chandrababu naidu says narendra modi best pm country since independence
phirekbaarmodisarkar upa hiked reliance gas price from2 3 to4 2 2007 amp 4 2 to8 4 in2014 with dubious formula4loot laks crores modi rejected price of8 4 in2014 5 6 15 4 6 16 3 8 17 2 89 18 3 upa corruption modi honesty
i m first time voter i ll vote shri narendra modi ji inspired everyday power work nation i ll make sure 10 people around vote only jai hind
shri narendra modi ji hope young india tenure went building base better tomorrow make better definitely deserves next tenure country deserves next tenure narendramodi whymodiagain
z schemes modi government abkibaarphirmodisarkar bjp bharatkemannkibaat narendra modi government
great pm narendra modi sir india piople u like self sanjay kumar say
think know first thing honorable prime minister narendra modi done things like since 2014 always aim development whether election time time
today nris newyork amp new jersey gathered iconic times square expressed support sh narendra modi ji nris4modi phirekbaarmodisarkaar abkibaar400paar
seen 2 greatest pm india span 20 years atal bihari vajpayee amp narendra modi being responsible citizen duty vote best whymodiagain
india’s election season bombing interrupts modi’s slump new york times new delhi — one month ago narendra modi india’s unstoppable
namoagainwhen king becomes stronger amp controls nation petty thied terrorist traitors feel heat amp complain intolerance society this said 2300 years back great chanayka guess king today one amp only narendra damodardas modi namoagain
hon ble prime minister shri narendra modi radio address mann ki baat appreciating noble efforts chief guest zarurat celebrating innocence padma shri d prakash rao zarurat
top story lok sabha 2019 narendra modi win india first electoral battle fought kurukshetra cyber space see
prime minister narendra modi attended 50th raising day central industrial security force cisf delhi ncr ghaziabad india indialove indian indianfood india everyday indiana india gram
spineless congress inc attitude main reason terror elements ruthlessness j amp k state india the ruthless terrorist masood azhar commiting sin sins under pm shri narendra modi ji india stands international community war terrorism
lets listen padma bhusan b hegde message 2014 particularly says pm narendra modi thinks india india needs people lead country lets vote team modi 2 0 stronger better india ekcalldeshkenaam
next prime minister india narendra modi valuable man india popularity person india
india2020 apj vision2020 my dream year congratulations nation we re great pm narendra damodardaas modi 2020 very satisfied poll i m
much improvement national security modi sarkar jai bharath jai narendra modi jai modi sarkar
pm narendra modi waives 3 50 lakh crore debt 15 industrialists waive loans farmers
jay ho bjp jay ho modi ji narendra damodardas modi
narendra modi sustainable development clear vision going benefit next generation
shrimati sushma ji multilingual communicative skills impressive best our pm shri narendra modi ji extempore exorbitant effective communication skills amp leaders team unparalleled delight india
vision pm narendra modi ensure good quality affordable healthcare poor people becoming reality medicines diagnostics facilities treatments far affordable accessible namumkinabmumkinhai namo
narendra modi raised india image world narendra modi showed courage demolish corruption terrorism pakistan dying talk india india showing interest modi influence that whymodiagain
shri narendra modi twitter comments glad note prasar bharati brought 11 state dd channels satellite footprint india dd free dish includes five channels for
gallup international survey pm narendra modi no 3 ahead trump xi jinping putin via
well said shrimati sushma ji our pm shri narendra modi ji team people people in highly competent amp competing modern world india needs decisive versatile innovative leadership shri narendra modi ji get developed so india bjp
vision pm narendra modi ensure good quality affordable healthcare poor people becoming reality medicines diagnostics facilities treatments far affordable accessible namumkinabmumkinhai phirekbaarmodisarkaar
sheikh hasina assured narendra modi government would never allow country soil used terrorist organisation
power unity narendra modi
whymodiagain 300 years islamic rule 300 years christian rule and 70 years islamo christian i e secular congress rule has destroyed bharat enough son soil narendra modi capacity 2do viskas + dharma together amp restore glory bharat 670 years slavery
modi remains nation’s top choice pm face times now vmr polls clear lead pm narendra modi transformingindia nationwithnamo
we applaud hon’ble pm shri narendra modi 7cs vision india futuremobility common connected convenient congestion free charged clean cutting edge chandrajit banerjee dg futuremobilityshow fms2019
narendra modi great pm
said app kiska chunne ja rahe ho ans prime minister better narendra modi vote bjp self make full majority namoagain2019
whymodiagain bcoz india one leader stronger narendra modi that whymodiagain
seems narendra modi governance reached people throughout india electricity too
trust narendra modi bjp battleof2019
hearty birthday wishes indian captain r shri amarinder ji our pm shri narendra modi ji politics highly nourished matured mannerism amp perfectionism salute pm shri narendra modi ji delight
support narendra modi ji growth country
another tmc mp joins bharatiya janata party bjp support bjp narendra modi growing day abkibaarfirmodisarkar namumkinabmumkinhai
trust nda government led narendra modi know leader india wanted create change indian politics phirekbaarmodisarkar
indian railways reached remotest corner north east inauguration broad gauge railway line reached belonia south tripura phirekbaarmodisarkaar
congress governance healthcare riches more specifically dangerous diseases shri narendra modi ji team bjp governance generic medical stores amp ayushman bharat pmjay boons poor amp middle class cancer medicines cheaper
chart clearly represent indians support leadership narendra modi it schemes commitment bring change life people bring india decades problems facing today india saying phirekbaarmodisarkar
proud leader honble prime minister narendra modi ji bjp president amit saha ji decision bjp mp candidate like professional non political background new comer youngster professor dr subash aspirant mp bjp dhenkanal
kannada beautiful language india narendra modi beautiful person world
modi remains nation’s top choice pm face times now vmr polls clear lead pm narendra modi transformingindia via mynt
may god bless souls ethiopia air crash fatal victims rest peace under pm shri narendra modi ji india stands international communities pain amp pleasure
people favourate leader strengthening defended narendra modi ji congratulations jai bjp 2019 new india best bharat matha ki jai
glimpse honorable prime minister sh narendra modi 50th raising day central industrial security force cisf camp he also praised cisf personnel contributions national emergencies disasters namoagain
upward surge ind sensex hints narendra modi resounding comeback win pm india on3rd may 2019
loksabha election starting 11th april amp result 23th may phirekbaarmodisarkaar those could vote narendra modi last time offer extended again it free vote4modi2019
prem watsa popularly known canada’s warren buffett rates narendra modi’s 5 year tenure highly saying economic reforms undertaken indian prime minister helped economy grow
people favourate leader strengthening defended narendra modi ji congratulations continue india jai bjp 2019 new india best bharat matha ki jai
pm shri narendra modi ji ayushman bharat pmjay boon poor amp middle class people suffering dangerous diseases only pm shri narendra modi ji india gets generic medical store saves thousands rupees common man salute delight ji
without doubt sir honourable pm shri narendra modi re elected second time
well said shri yogi ji under versatile decisive pm shri narendra modi ji india befittingly stands international community wat terrorism the ruthless j e m perish
narendra modi blog tribute great unifier sardar vallabhbhai patel justly regarded maker modern india
people wise so choose bjp shri narendra modi ji works year realize dreams bapu shri mahatma gandhi ji but people never choose congress inc thinks bapu shri mahatma gandhi ji 2nd oct only
narendra modi ji what’s take this
om namo the nation chants 2019 om more namo narendra modi
india safe pm modi leadership says arun jaitley
whymodiagain forget 2019 narendra modi may remain pm till 2029 know long top world leaders last
narendra modi face pm 23may 2019
coming digital india 1 narendra modi government introduced rupay cards created india we using cards everywhere eliminating use visa mastercard 2 upi nowadays send money bank bank without charge still hating modi
pm modi meets nari shakti award winners says work inspiration ndtv
country safe prime minister narendra modi arun jaitley
common citizen india want see narendra modi pm india next five years least time would like journalists like keep questions gov different front loksabhaelections2019
pm narendra modi explains relevance communication national youth parliament festival awards 2019
prime minister narendra modi ambitious scheme national health protection scheme 10 crore poor families given cover rs 5 lakh per family annually bjpvijaysankalpbikerally
darr accha hai 7 fears pm narendra modi thinks good india via namo app
modihaintomumkinhai welcome bihar modi ji best wishes coming future us narendra modi ji
ashutosh ji need confirmation respect proper passport money pocket go around world move pan india realise respect power associated narendra modi
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
prime minister narendra modi launches khelo india app promote sports fitness via namo app
tiger back thank narendra modi ji
dharma yudh fight right n evil bhishma advices pm protect people would general bhishma tell prime minister narendra modi today via
pm narendra modi two day visit gujarat today inaugurate first phase ahmedabad metro service via namo app
first indian tipical pakistani concerned country prime minister indian much proud prime minister mr narendra modi enough matured decide whome vote
prime minister narendra modi launches several development projects amethi amethirally
bjp relentlessly take credit political power displayed surgicalstrike airstrike downing f16 fighter plane getting abhinandanvarthaman back 48 hrs flat yes armed forces belong india narendra modi prime minister
india narendra modi shown great respect lord shiva ganga kumbh mela shiva abodes like varanasi lord shiva remains eternal yogi india ancient times new india bharat today mahashivaratri
ratan tata votes narendra modi says prime minister capable delivering new india
prime minister narendra modi asked ministers bjp governed states bjp mps attend last rites jawans lost lives pulwamaattack respective states constituencies pulwamarevenge
pm modi asks seven aaj tak questions india today conclave via namo app
pm modi asks seven aaj tak questions india today conclave via namo app
pm narendra modi transforming india
pm narendra modi visit andhra pradesh tamil nadu karnataka tomorrow indiablooms first portal digital news management tnwelcomemodi
thankyou narendra modi calm metro ride advertisement app twitter pak released wc abhinandan chhakke chhuda diye wah masterstroke
glimpse shri amit shah ji listening video conference delhi party members conference prime minister shri narendra modi ji interacted nearly 1 crore people 15 00 places
thanks great leader narendra modi
bharatbadalgayahai wing commander abhinandan vartharaj return india today options pakistan nothing pakistan compelled return wing commander india else pakistan would shiver fear narendra modi indian side
pmo full event prime minister narendra modi inaugurates construction technology india 2019
prime minister narendra modi bhumipujan vishv umiyadham ahmedabad gujarat believe maa umiya never support female foeticide appeal let us create society discrimination based gender
namo decries vandalism statues warns action
admire narendra modi core donald trump asked de escalate narendra modi gave heed words evident rebuffing invitation talk imran free hand forces stern statement today strikes practice
prime minister narendra modi launches khelo india app promote sports fitness via namo app
indian army powerful disciplined force draws operative strenth political leadership day failing imagine pak would released iaf pilot manmohan singh still pm proud indian govt led pm narendra modi
russia president vladimir v putin called prime minister narendra modi phone today conveyed solidarity india fight terrorism follow special coverage ndtv 24x7
washing workers feet political gimmick sanskar narendra modi
india keen reach top 25 position global innovation index soon innovation globalinnovationindex
previous govt failed get bulletproof jackets armed forces got 2 lakh says pm modi via namo app
ending india pakistan crisis requires courageous narendra modi look past coming election say nothing domestic media favor compromise
main deshnahimitnedunga take pledge motherland never allow nation perish pm modi recites poem churu meraboothsabsemazboot
let know narendra modi gujarat cm ahmedabad clean time
pm narendra modi lays foundation stone vishwa umiya dham temple complex jaspur gujarat
strength country defined n narendra modi strong govt air army naval foces mutual cooperation international friends one vision zero tolerance anti national activities bharat truly leader international front jai hind
starting today onwards please join hon ble pm movement meraparivarbhajapaparivar hoisting bjp flag home bringing bjp back power 2019 bjp4india narendra modi amit shah chandupatlakeerthireddy
great indian prime minister narendra modi international support incress india indian prime minister take second second decision health indian features
take name name narendra modi say
pic 1 tweet pic 2 bio honoured followed narendra modi
mr narendra modi actions speak words words speak action even sitting somewhere india heart somewhere else probably pakistan gharmegaddar
india keen reach top 25 position global innovation index soon narendra modi via namo app
pm narendra modi chairs high level meeting security amid india pakistan tensions via
top story narendra modi speaking india today conclave wide range issues watch see
pakistani media anchor praising pm narendra modi work nation b via
sister sushma sowaraj welcome oic conference people balochistan proud narendra modi presence political arena
siddhu respect sentiments country think good country know people dont speak like voters interpreat thought anti national politician congress think rather makings foolish cmnts shri narendra modi ji
telephonic conversation president russia mr vladimir putin invited indian prime minister narendra modi take part eastern economic forum vladivostok september 2019 main main guest 2019elections
pm candidate shri narendra modi indian army kargil
pmnarendramodi inaugurates kalashnikov factory rahul gandhi lok sabha constituency amethi thanks dear friend russian president vladimir putin modiinamethi ak203
would reaction liberals abhinandan press confrense says thank shree narendra modi ji safety arrival happy pm leadership go kill enemies nation
banda apna sahi hai twitter thanks narendra modi surgical strike 2 0 bjp rap song via namo app
advantageindia foreignpolicystrategyrevealed prime minister narendra modi foreign policies strategic diplomacy various international official visits put india position sustainable advantage pakistan china indiastrikespakistan
dear narendra modi 14 year old girl live chhattisgarh middle class mother suffering bone marrow cancer still mother happy inspire lot father never smiles feel bad plzz help us
wow wonderfully written
prime minister narendra modi hindu symbolism behind air strikes pakistan excellent piece k bhattacharjee
india pakistan conflict live wing commander abhinandan varthaman tried swallow documents capture pak troops abhinandanmyhero indiastrikespakistan abhinandan
vote respected pm mr narendra modi hinduism nowadays terrorists generated madressas states
nda 2 tenure 2014 2019 mark best average growth rate 7 4 lowest average inflation 4 5 government india since liberalisation pm narendra modi
pm narendra modi says 1 1 crore farmers got kisan scheme payout pmkisan via namo app
ncdc new scheme yuva sahakar giving wings young entrepreneurs cooperatives entrepreneure narendra modi
time clapping respectable primeminister shri narendra damodardas modi every time criticising near 5 years completing never said pm modi ji great
sir abhinandan returned hero welcome bcos outstanding diplomacy narendra modi indians urge start hunger strike even pakistan wishes
pm narendra modi says 1 1 crore farmers got kisan scheme payout
pm attend two temple functions patidars march 4 5
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
salute hero
way gandhi maidan patna new delhi attend possibly pm narendra modi biggest sankalp rally 2019 phirekbaarmodisarkar sankalprally sankalprallypatna
pm narendra modi attend two temple functions patidars march 4 5
bharat forever pm modiatconclave19 letsconclave19 full coverage
prime minister shri narendra modi dedicate nation lay foundation stones for…
pm shri ji takes delhi metro khan market station reach gita aradhana event iskcon glory india cultural centre meraboothsabsemazboot
india buckle pressure prime minister narendra modi held day long back back meetings national security advisor ajit doval defence minister nirmala sitharaman …
new delhi pti prime minister narendra modi amethi parliamentary constituency congress leader sonia gandhi sunday launch kalashnikov rifles manufacturing
opposition leaders afraid future due honesty braveness beloved leader mr narendra damodar das modi one ready believe rumours spread opposition leaders modi ji
liberals always bark women empowerment india think forgot nupur ji india also many women like days voice leader like narendra modi ji big admirer way speak fearlessly power
meraboothsabsemajboot prime minister shri narendra modi mega interaction party workers people sections society volunteers around 15 00 locations 28 02 2019 11
correct see difference response narendra modi imran khan modi remain calm composed created fear pakistan imran khan speaks much face saving also possible
shri narendra modi unveiled bhagwad gita 2 8 meters high weighs 800 kg pic credit delhi tentaran bhagwadgita narendramodi
pm narendra modi explains relevance communication national youth parliament festival awards 2019 via namo app
pm narendra modi pulls child ear delhi metro young boy reaction make day via namo app
heartening thing narendra modi shown come us pressure chabahar buying oil iran 400 russia everytime ignored us threats drastically different kargil 2008 mumbai attack
always proud feeling hear narendra damodar das modi dynamic pm india
pm narendra modi transforming india
jai jawan jai kisan pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
modihaitomumkinhai sankanprally support mr narendra modi 2019
offcourse narendra modi nobody visionary modi india lead world next 10 years modi remains prime minister
pm modi chairs high level meeting security
jay shri radhe prabhu g swachh bharat swasthya bharat samradha bharat atal bharat jay hind ki sena india stop cost fight win grow one prime minister narendra modi via namo app
unfortunate many fail recognize greatness man treta yug lord ram take birth become leader kaliyug mortal man rise deeds man narendra modi godsent karmayogi
pm narendra modi addressing indiatodayconclave2019 new delhi
tnwelcomesmodi budget 2016 17 speech suresh prabhu growth amit shah narendra modi infographics speeches documents rail budget 2016 17       railway 
u r indirectly wanted sympathy innocent voters entire nation united far terrorism concerned wot ever prime minister narendra modi interest nation political politicians like u n arvind kejriwal cant mislead
indian certitudes namo fumbles proud pm like narendra modi traitors plotters anti nationalists performing games trustworthy honest pm modiji
welcome narendra modi sir andhra pradesh
portal launched prime minister narendra modi become country largest online lending platform sanctioning loans worth rs 35 00 crore
pm narendra modi says 1 1 crore farmers got kisan scheme payout
narendra modi world powerful leader agree=retweet disagree =like
india let sacrifice jawans go vain says pm modi sankalp rally happened elections news
pm narendra modi attend two temple functions patidars march 4 5
pmjdy become world largest financial inclusion initiative empowering poor people india narendra modi govt 27 44 crore rupay cards issued beneficiaries
thanks modi
invite join nation namo india largest volunteer network professionals campaign shri narendra modi 2019 join using referral link spread word jai hind
many kudos prime minister narendra modi exemplary strategic planning implementation foreign policies proud born 1950 matured great leader upa youwantcredit takefullcredit
empower women prosperous india says narendra modi gujarat pregnant muslim women raped foetus es burned india
india keen reach top 25 position global innovation index soon narendra modi via namo app
pm narendra modi transforming india
believe narendra modi whole nation decision
support pm shri narendra modi vision india look forward leading country 2019 pledge myfirstvoteformodi also support taking pledge
needed abhinandan coming back one one reason narendra modi proud pm narendra modi
prime minister narendra modi friday declared country longer helpless face terror saying new india pay back terrorists interest
recorded p narendra modi today dedicated joint venture indo russian rifles nation also laid foundation stone dedicated 538 crore various development projects amethi u p gsvjresearch centre kanpur india
dear honourable president korea sir love exo anything life please bring coming india else send return gift mr narendra modi ji thank sir
congratulations narendra modi bringing worst us nationfirst bringbackabhinandan
successful shri narendra modi prime minister 2019 leader narendra modi thanku
narendramodi speaking public rally gujarat jamnagar inaugurated various developmental infrastructure projects including guru gobind singh hospital
dear prime minister narendra modi jee tnwelcomesmodi tnwelcomesmodi tnwelcomesmodi tnwelcomesmodi tnwelcomesmodi tnwelcomesmodi tnwelcomesmodi tnwelcomesmodi tnwelcomesmodi tnwelcomesmodi tnwelcomesmodi tnwelcomesmodi tnwelcomesmodi tnwelcomesmodi
india keen reach top 25 position global innovation index soon narendra modi via namo app
leadership prime minister iaf put strong display country valour uttar pradesh chief minister addresses rally amethi watch live ndtv 24x7 follow updates
like narendra modi
say imran khan want peace first say pm kick terrorist country pm narendra modi sir think war
prime minister narendra modi launches various scheme benefiting gujarat narendramodi gujarat ahmedabad ahmedabadmetro news newsupdate dailynews politics
like bande dum hai proud pm narendra modi
narendra modi struggle india soul orange evolution
pm narendra modi transforming india financial express
banda apna sahi hai twitter thanks narendra modi surgical strike 2 0 bjp rap song via namo app
india placed 18th spot highest among brics nations good ranking prime minister narendra modi visionary leadership policies towards achieving sdg building smart cities many inclusive growth initiatives
sir become possible respected prime minister shri narendra modi indeed care nation people please give vote narendra modi thank
according mood nation survey india today best prime minister india   atal bihari vajpayee indira gandhi people country incumbent prime minister narendra modi who holds pride place hearts modiniti
narendra damodar das modi back
washing workers feet political gimmick sanskar pm narendra modi via namo app
narendra modi ji best prime minister india ever best stateman world
pm shri narendra modi dedicate nation 2 lane kollam bypass nh 66 kerala today
words prime minister shri narendra modi really super powerful pm world sulate
pm narendra modi launches various sauni projects guru gobind singh hospital jamnagar gujarat
modihaintomumkinhai sankalprally support narendra modi g 2019
pmo shrimp narendra damodardas modi saying piolet abhinandan project want say modi project us pride pls politics kind matters pmoindia narendramodi abhinandancomingback incp
bcoz wonderful diplomacy safe apna pm kaisa ho narendra modi jaisa ho
sir make india succeed proud part journey thanx narendra modi pappu tere bas ka nhi h baba
go pakistan teach u many things like jihad n one thing u learn pm narendra modi u take revenge every drop blood like congress 26 11
support ironic leadership narendra modi
prime minister modi turned attention towards raging issue strikes pakistan following pulwamaattack new india changed india said adding blood every soldier valuable one threaten us
happy welcome pm shri narendra modi tn laying foundation stone aims maduraithanksmodi tnwelcomesmodi
namoagain2019 vote prestigious bharat hindutva vote namo prime minister narendra modi launches khelo india app promote sports fitness via namo app
meraparivarbhajapaparivar see support especially see love prime minister narendra modi ji varanasi modiinvaranasi
tempers cool alarming confrontation india pakistan analysts say leaders emerged stronger — narendra modi burnishing nationalist
previous govt failed get bulletproof jackets armed forces got 2 lakh says pm transformingindia
narendra modi sir best
narendra modi exercised unique ability make isi puppet look like statesman naya india remember
pm narendra modi transforming india
9 2018 sunjuwan attack 11 killed 2018 sukma attack 9 killed 2019 pulwama attack 46 killed war monger pm narendra modi shown 56 4 major strikes took revenge martyrdom jawans manipur ambush myanmar killed 158+ terrorists
country always many gaddars fortunately dear narendra bhai modi ji rule exposing dejection frustration perversion
narendra modi continues get strength committed haters haters want miss chance show hatred modi without understanding issue implications often end committing self goal
pm narendra modi inaugurates national war memorial previous govts putting family first via namo app
underestimating narendra modi imran khan forced released abhinandan due fear modi would congress govt released hi
tnwelcomesmodi press release union mukhtar abbas naqvi palghar maharashtra 8 2016 government india narendra modi 7 central budget empowerment india new development infrastructure nda press release union minister state parliamentary affairs
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
washing workers feet political gimmick sanskar pm narendra modi via namo app
pmjdy become world largest financial inclusion initiative empowering poor people india narendra modi govt 27 44 crore rupay card issued beneficiaries
laid foundation stone inaugurated several infrastructure projects odisha presence ji leadership hon ble pm sri narendra modi eastern india developing faster ever odisha soon become engine growth india newindia
dear fellow indians really want anything country armed forces please excercise power vote vote present government pm narendra modi sir give bigger mandate last time progress
vizag railway station developed narendra modi cental government state govt need know minimu common sense railway jobs employees rwcruitment happened central government
modihaitomumkinhai sankalprally support narendra modi g 2019
washing workers feet political gimmick sanskar pm narendra modi via namo app
good morning opinion need election direct selection narendra modi prime minister political party required
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
banda apna sahi hai twitter thanks narendra modi surgical strike 2 0 bjp rap song via namo app
washing workers feet political gimmick sanskar pm narendra modi via namo app
pm narendra modi rally kanyakumari 26 11 happened india expected action terrorists nothing happened uri pulwama happened saw brave soldiers salute serving nation
fact matter pm narendra modi redefined india strategic doctrine ordering air strikes nuke powered state 1st world tt baba like dhume upset
popular leader like narendra modi ji see world proud indian prime minister narendra modi ji congratulations continue indian prime minister jai bjp 2019 new india best bharath matha ki jai
right time think nations request politicians political party practical support respected pm shri narendra modi
far away backpackers yoga retreats call centres modern india famous another india – ready conflict
pm narendra modi cut shorts function rushes review security situation
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
dalits muslims buy like aadhaar big brother narendra modi pm modi launch one nation one card modes travel today india news times india
request crown prince saudi arabia increased india quota haj pilgrims prime minister patna highlights
banda apna sahi hai twitter thanks narendra modi surgical strike 2 0 bjp rap song via namo app
invite join nation namo india largest volunteer network professionals campaign shri narendra modi 2019 join using referral link spread word jai hind
pm narendra modi says 1 1 crore farmers got kisan scheme payout welcomehomeabhinandan abhinandan
tum mujhe kab tak rokoge beautiful rendition amitabh bacchan pleasantly surprised know poem written none pm narendra modi
pm narendra modi pulls child ear delhi metro young boy reaction make day via namo app
pm narendra modi confers shanti swarup bhatnagar prize excellence science technology
contrary political detractors say regarding public engagements exactly circumstances giving clearances armed forces standing behind time crisis offering guidance
iron man india sardar vallabh bhai patel presenting second iron man india shree narendra damodardas modi
narendra modi best fittest matured popularity prime minister india wants see coming election modiji jindabad jay hind
imran khan patch narendra modi time pulwama happened nm conducted duties admirably
something big happened brave wingcommandarabhinandan comeback pretty sure primeminister sh narendra modi address award ceremony scientists mr modi man words narendramodi abhinandan jaihind
darr accha hai 7 fears pm narendra modi thinks good india india news indiatodayconclave2019
0 tax people earning rs 9 75 lakh one biggest relief done people country modi government simple illustration namoagain sanjay tandon narendra modi
worry sir next pm mr narendra modi
prime minister narendra modi interacts participants smart india hackathon 2019 video conference
salute indian air force bravery honourable prime minister india shri narendra modi daring decision need country abolish article 370 root terrorist activities jammu nd kashmir namoagain
proud narendra modi
new india decisive fearless pm narendra modi
condemned told chor thief right talk anything shri narendra modi
imran khan hero want see hero heard name narendra modi thats sufficient
acceptable indianairforces indianarmy pmo please something pakistan esa sabak sikhao ki kabhi bhi pakistan kuch bhi karne se pehle 100 bar soche proud indian army air force pmo shri narendra modi
coming due course nobel narendra modi nothing
iaf pilot released wagah attari border sources welcome back abhinandan
indians standing like rock counter enemy evil designs live grow fight win one pm narendra modi said
lapse centuries fortunately strong regime lead competent man narendra modi coming years prove
washing workers feet political gimmick sanskar pm narendra modi via namo app
please read extraordinarily insightful article narendra modi must use balakot consolidate india rajasic transformation
thanks million beloved prime minister bringing back pm like mr narendra modi world saluting sir dr shobha vardhamanji entire jain community pride returning tom celebrate tom
beloved comrade narendra modi
true government narendra modi much concerned time gonna leave pakistan without paying dividends proxy war india
time come stand united india protest pakistan heinous crime killing nationals near pok loc kashmir salute iaf pm narendra modi decision crucial moment
soilder die die true indians pm narendra modi
prime minister narendra modi saturday said time come total transformation fruits development must reach every citizen economic times
india pm shri narendra modi inaugurated world biggest bhagavad gita iskcon delhi 26th february 2019 hh gopal krishna goswami maharaj hg madhudwisha prabhu hg yudhister govind prabhu
mamta member tukde tukde gang disappointed see success pm india 130 crores rallying round narendra bha modi best competent fulfill cherished desires whole india
india rajasic retribution hard cold decisive great pc india needs look back look ahead
rare pic pm imran khan giving autograph narendra modi
tweet narendra modi narendra modi tweeted new india fully capable protecting nation giving befitting reply disturb atmosphere peace
previous govt failed get bulletproof jackets armed forces got 2 lakh says pm modiatconclave19 via namo app
banda apnasahihai twitter thanks pm narendramodi surgical strike 2 0 bjp rap song meraboothsabsemazboot
india stop cost fight win grow one prime minister narendra modi via namo app
great work narendra modi ji farmers really going vote runfornamoagain
doubt abhinandan great hero would like thank primeminister mr narendra modi whose leadership able bring back great solder jaihind
modihaitohmumkinhai darr accha hai 7 fears pm ji thinks good india
set beloved prime minister sri narendra modi ji meeting tomorrow railway grounds
looking forward interacting karyakartas evening watch interaction narendra modi mobile app
pm modi asks seven aaj tak questions india today conclave india news
india aims among world top 3 economies next 15 years pm narendra modi via namo app
pleasure announce prime minister shri narendra modi address participants smart india hackathon 2019 grand finale via video conferencing today 10 00 pm ist sih2019grandfinale
well narendra modi ji ample time remove intended seriously
28th february 2019 prime minister shri narendra modi mega interaction watch live meraboothsabsemazboot
really great heard things ever happening last 30 years terrorists attacking various places routed completely traces sri narendra modi capable
improved ties israel gulf states well decline palestinian issue india foreign policy narendra modi accelerated indo israeli cooperation argues
26 11 happened india expected action terrorists nothing happened uri pulwama happened saw brave soldiers salute serving nation pm follow live updates
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
gujarat prime minister narendra modi flagged humsafar express train jamnagar bandra terminus via video conference inaugurated various development projects earlier today jamnagar
tntrustsmodi central government arun jaitley india narendra modi speech photo rural healthcare first 9 11 budget two successful initiatives central government
pm modi home turf gujarat today addresses rally highlights
pm modi launch pradhanmantrikisansammannidhi scheme gorakhpur today pradhanmantrikisansammannidhi pm kisan financeminsitry
india must reach top 25 global innovation index soon pm modi ndtv
india keen reach top 25 position global innovation index soon pm sh
mr naidu count days modis graph vertically going upwards next pm narendra modi cent percent correct hero shivaji also crossing limits ramoji rao news paper full party ads ntr hated joined hands congress shamelessly ntr biopicflop
expressexplained pm narendra modi bihar cm nitish kumar shared stage today rally patna first time decade picture two leaders tells story changing political relationship
well presented analysis need narendra modi political party guts mindset implement
pm narendra modi explains relevance communication national youth parliament festival awards 2019 via namo app
narendra modi must use balakot consolidate india rajasic transformation
honorable pm sri narendra modi cabinet indian armed forces know well enthusiast warmonger civilians demanding strict action
prime minister narendra modi launches khelo india app promote sports fitness via namo app
well written
namo400plus please use hashtag bring narendra modi government back 2019 huge majority county needs brave intelligent leaders take care poorest poor daring teach lesson pakistan great international relationships deserve back
well said mr shri narendra modi ji nda leaders people progress nation growth wider wisdomed shri narendra modi ji may god bless hale healthiness bihar cm shri nitish kumar ji
strong reason believe narendra modi led government way indian government able corner pakistan world stand unite behind india surge forward decisive battle terrorism
pm india tum people see kaun person great country blessed bhagvan wonderful amazing leader pm narendra damodardas mulchand modi ji haa
researching historical evolution international economics interplay environment firm belief india game changer create high growth large scale employment sustainable green economy
india indians look forward future renewed sense optimism gloom upa 2 era saw huge corruption massive economic underperformance nda pm narendra modi indeed transformed india excellent read
abhinandan wc abhinandan home coming proud also proud narendra modi thanks diplomacy abhinandan released within 56 hours without condition
hon ble prime minister india narendra modi presently taking part opening adyar cancer center diamond festival tnwelcomemodi narendramodi
r proud shri narendra modi like
narendra modi get piece noble prize future yes
india prime minister pm narendra modi touts govt achievement rising india summit
want masood azhar hafiz sayeed dawood ibrahim brave pilot nothing less else start counting graves dear pm narendra modi india
shree narendra modi want next pm
pm formulates 2019 mantra bjp workers mera booth sabse mazboot bjpnewstrack
political exploitation combat operations electoral gains well truly underway hoarding seen picture featuring prime minister narendra modi uttar pradesh dy chief minister keshav maurya put near circuit house allahabad
primer minister india shri narendra modi ji interacting participants 6 selected nodal centres sih2019 grand finale software edition 10 00 pm march 2 2019
pm narendra modi need say empty words proves actions addresses people fact abhinandan returning home safely clear solid proof wish waste breath giving gaalis person like
vote everybody supports narendra modi meraboothsabsemazbooth
bjp rally pm narendra modi launch govt schemes kanyakumari
meraparivarbhajapaparivar prime minister narendra modi
pm narendra modi explains relevance communication national youth parliament festival awards 2019 via namo app
rt timesofindia prime minister narendra modi addresses winners shanti swarup bhatnagar prizes delhi vigyan bhavan
previous govt failed get bulletproof jackets armed forces got 2 lakh says pm modi via namo app
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
narendra modi ji best pm today shown india namo
pm narendra modi leadership skills never doubt many countries praising one tallest leaders world new story
28th february 2019 prime minister shri narendra modi mega interaction watch live meraboothsabsemazboot
talking mms govt 2014 new india dear narendra damodardas modi pm misadventure pak fcuked hard
glory days india world thank sushma swaraj ji thank narendra modi ji
prime minister narendra modi confer national youth parliament festival 2019 awards winners via namo app
pm narendra modi visit gujarat today inaugurate ahmedabad metro project gujaratsaysnamoagain
uri attack pulwama attack 26 11 many attack keep calm believe army narendra modi sayyestowar
banda apna sahi hai twitter thanks narendra modi surgical strike 2 0 bjp rap song via namo app
india keen reach top 25 position global innovation index soon innovation globalinnovationindex
surgicalstrike2 pakistan anupamkher tells rahulgandhi start saluting pm narendramodi
let us also acknowledge role india powerful women narendra modi stronger skillful engagement pakistan sushma swaraj minister external affairs nirmala sitharaman minister defense bharat shakti living fact
prime minister narendra modi blessing country worked awesome modi ji great runfornamoagain
well said shri narendra modi ji shame congress co
pm narendra modi inauguration foundation stone laying ceremony various development projects kanyakumari
pm narendra modi two day visit gujarat today inaugurate first phase ahmedabad metro service via namo app
want kohinoor already kohinoor narendra modi ji congress
excellent pm shri narendra modi ji determination made india proud sent loud clear message pakistan new india shri narendra modi ji prime ministry never hesitate enforce legitimate rights punish terrorists even beyond india boundary
pm two day visit gujarat today inaugurate first phase ahmedabadmetro service gujarat
india gate memorial 70k soldiers british indian army part work imperial war graves commission dec 1917 politicians last 70 years built memorials soldiers independent india shri narendra modi regarded soldiers
dont remember congress done mumbai atrack oh sorry congress coward busy destroying india fight terrorism narendra modi shown determination
washing workers feet political gimmick sanskar pm narendra modi sanskar modi workers bjp politicstoday
pm narendra modi amethi today unveil string projects
love indian army narendra modi ji
pm narendra modi two day visit gujarat today inaugurate first phase ahmedabad metro service via namo app
sir politicians self centered except namo independence political leaders failed make indians feel proud ever pappu family kept looting national treasury narendra modi man india needs another decade
shri narendra modi honorable pm salute giving army free hand thank sir
proud world number one leader narendra modi ji real lion india congratulations best bharat matha ki jai proud india
morningnews prime minister narendra modi launch various development projects tamil nadu today
let us also acknowledge role india powerful women narendra modi stronger skillful engagement pakistan sushma swaraj minister external affairs nirmala sitharaman minister defense bharat shakti living fact
pm narendra modi pulls child ear delhi metro young boy reaction make day via namo app
thanks primeminister shree narendra modi ji
previous govt failed get bulletproof jackets armed forces got 2 lakh says pm modi via namo app
pm narendra modi transforming india financial express
e inauguration pmkk center honorable mp general retd vijay kumar singh honorable prime minister sri narendra modi
happens shri narendra modi ji
wonderful bjp shri narendra modi ji team nda sure win 2019 ls election huge majority votes seats people witnessing wonder capability pm shri narendra modi ji team tireless selfless hardworking culture india glory
previous govt failed get bulletproof jackets armed forces got 2 lakh says pm modi via namo app
welcome shri narendra modi ji
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
congrts uncle pm narendra modi
pm launches khelo india app promote sports fitness transformingindia
bengal wants modi narendra modi needed develope india
undoubtedly shri narendra modi done lot good work india runfornamoagain
balakotairstrike proves narendra modi accept congress approach kashmir
pm narendra modi visit gujarat today inaugurate ahmedabad metro project gujaratsaysnamoagain
ie abhinandan used mean congratulation meaning change pm narendra modi h changing stripes conservation toi abhinandan used mean welcome meaning would change pm
delete tweet later cause results favor beloved pm narendra modi
l salute armed force took revenge also salute pm narendra modi
bjp confident well 2019 lok sabha elections narendra modi via namo app
bjp govt narendra modi shy like upa take pakistan given bold…
india strong ruler called narendra damodardhas modi rebellion admit r call sangi proud gladly
magnanimity appreciating nda govt decisive patriotic leader narendra modi nation
skill development air warriors e learning software software house development iaf massive potential awarded honourable pm narendra modi
tnwelcomesmodi tntrustsmodi strong leadership pm narendra modi hastened fight corruption every citizen must contribute
pm narendra modi ji liked
previous govt failed get bulletproof jackets armed forces got 2 lakh says pm modi via namo app
big diplomatic victory seen today 1 sushmaji speach oicsummit 2 safe return brave wing commander abhinandanvartaman hats ji foreign policy thank narendra modi ji namoagain2019
occassion student anjanakshi receiving 2nd prize national youth parliament festival 2019 awards hon ble pm shri narendra modi celebration moment blessings poojya gurudev
pm narendra modi explains relevance communication national youth parliament festival awards 2019 via namo app
narendra modi really great created laddhak separate divisionseperste valleynow reservation poor residents state good action towards welfare poor members sc st
please praise father pm praised indian people one thing many days months father hold pm post reality country never ever seen pm like narendra modi super star father compared namo jai hind
name narendra damodardas modi proud
salute brave prime minister shri narendra modi ji fight pakistan
washing workers feet political gimmick sanskar pm narendra modi
okay proud prime minister narendra modi ji see country pm ji modifor2019
pm sh ji address smart india hackathon 2019 iit roorkee
thanks mr pm narendra modi
much flatterry good man atleast think saying narendra modi proved leader raga acieved mention 5 achievement apart son grandson gandhi
india keen reach top 25 position global innovation index soon modiinamethi via namo app
india believes namo india stop cost fight win grow one prime minister narendra modi via namo app
prime minister narendra modi confer national youth parliament festival 2019 awards winners via namo app
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
prime minister narendra modi amethi might lost election hearts last 5 years smriti ji worked hard development region never made feel whether made win lose worked person
made first video narendra modi come
pm narendra modi pulls child ear delhi metro young boy reaction make day via namo app
remaking india hindu pure land
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
hon ble pm shri ji transformingindia via namo app
pm narendra modi leader last 70 years allocated close 6 lakh crore andhra pradesh andhra ready welcome hon ble pm narendra modi ji come join large numbers andhrathanksmodi
see sagarika pm narendra modi although busy election campaign unlike many political leaders also thinks people india despite busy schedule
prime minister narendra modi nominated nobel peace prize 2019 launching world largest healthcare scheme saynotowar
gujarat 2 day visit pm narendra modi inaugurate several projects gujaratsaysnamoagain
pm narendra modi visit gujarat today inaugurate ahmedabad metro project gujaratsaysnamoagain
previous govt failed get bulletproof jackets armed forces got 2 lakh says pm modi via namo app
pm narendra modi transforming india five year term bjp led nda india gdp estimated grow `76 lakh crore relatively lower inflation fiscal deficit cad
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
banda apna sahi hai twitter thanks narendra modi surgical strike 2 0 bjp rap song bjpnewstrack
download app get detailed information pradhan mantri ujjwala yojana declared prime minister narendra modi
deplometic winning shree narendra modi welcomebackabhinandan
washing workers feet political gimmick sanskar pm narendra modi via namo app
opinion government done government recent past tackle india biggest challenge—ensuring every indian access bare necessities life
fruitful meeting shri senior leaders aiadmk nda leadership pm narendra modi ji committed development tamil nadu
student ms anjanakshi 2nd prize national youth parliament speaking award ceremony front hon ble prime minister bharat sri narendra modi ji proud moment us
pm narendra modi says 1 1 crore farmers got kisan scheme payout
india keen reach top 25 position global innovation index soon narendra modi
tune hear pm shri narendra modi mannkibaat 11 today may also listen namo app
washing workers feet political gimmick sanskar pm narendra modi via namo app
washing workers feet political gimmick sanskar pm narendra modi times india
meraparivarbhajapaparivar good wishes campaign committed success party making narendra modi pm india 2019 election
washing workers feet political gimmick sanskar pm narendra modi via namo app
congrats pm narendra modi architect new india getting back wing commander abhinandan
narendra modi busted pakistan myth shown india glorious tradition boldly fighting back via
previous govt failed get bulletproof jackets armed forces got 2 lakh says pm modi via namo app
pm narendra modi pulls child ear delhi metro young boy reaction make day via namo app
previous govt failed get bulletproof jackets armed forces got 2 lakh says pm modi via namo app
india keen reach top 25 position global innovation index soon narendra modi via namo app
indians need narendra modi pm till 2029 see india super power
country became super rich narendra modi ji government need money hence let go enough extradition although money farmers soldiers education employment development basic amenities
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
pm narendra modi pulls child ear delhi metro young boy reaction make day via namo app
many kudos prime minister narendra modi face india resistance enemy aggression great poise confidence face adversity proud born 1950 jawaharlal nehru prime minister india tweetlikesalmankhurshid
spreading propaganda pm narendra modi cuts short function rushes review security situation
previous govt failed get bulletproof jackets armed forces got 2 lakh says pm modi via namo app
live pm shri narendra modi public meeting visakhapatnam andhra pradesh andhrathanksmodi
great interaction large numbers beneficiaries benefited various schemes initiatives hon pm shri narendra modi ji ward 64 versova vidhansabha gathered together participated kamaljyotisankalp lighted lamps kamaljyoti versova
got relief enough hindus deshbhakts believes pm narendra modi iaf
washing workers feet political gimmick sanskar pm narendra modi via namo app
indira gandhi atal bihari vajpayi narendra modi strength power pm must country
india must reach top 25 global innovation index soon pm modi
sir apj abdul kalam narendra modi person whose personality attracts sane lady politician india enough words awesome perosn india needs forever ever
modihaitomumkinhai president called prime minister narendra modi phone today expressed deep condolences pulwama terrorist attack also conveyed solidarity people russian federation people india fight terrorism
prime minister narendra modi launches khelo india app promote sports fitness
pm launch rs 75 00 crore kisan income scheme farmers gorakhpur
congratulations shri narendra modi pm india establish national war memorial first india bangladesh india took many years political party opposition demanded
pm narendra modi transforming india
credit goes narendra modi
shri nitin gadkari said ganga important us 48 population lives ganga basin working fulfill pm shri narendra modi ji promise make ganga nirmal aviral
pm narendra modi announces special package rs 1 25 00 crore rs 40 00 crore bihar get via
woman child superspeciality hospital civil hospital ahmedabad ingurated primeminister shri narendra modi
india keen reach top 25 position global innovation index soon narendra modi via namo app
previous govt failed get bulletproof jackets armed forces got 2 lakh says pm modi via namo app
crown prince vice president council ministers defence kingdom saudi arabia prince mohammed bin salman bin abdulaziz al saud received prime minister shri narendra modi arrival new delhi february 19 2019
pm narendra modi explains relevance communication national youth parliament festival awards 2019 via namo app
support pm shri narendra modi vision india look forward leading country 2019 pledge myfirstvoteformodi also support taking pledge
support pm shri narendra modi vision india look forward leading country 2019 pledge myfirstvoteformodi also support taking pledge
prime minister narendra modi launch various development projects tamilnadu today
pm narendra modi says 1 1 crore farmers got kisan scheme payout
nitish kumar shares political stage narendra modi 9 years
previous govt failed get bulletproof jackets armed forces got 2 lakh says pm modi via namo app
south india stands firmly bjp popularity pm narendra modi south india huge regional party done good states bjp provide inclusive round fast paced development andhrathanksmodi
vast difference witnessing strong leader like shri narendra modi pm welcome back brave heart wg cdr abhinandan jai hind
prime minister bjp led nda govt completes deployed many unique development governance models significantly different past governments transformingindia
proud narendra modi pm leader work according fixed target clear vision well modi ji shows best politician world defeat pakistan diplomacy
prime minister shri narendra modi inauguration foundation stone laying ceremony various development projects kanyakumari march 01 2019
understand politics one question people want sir narendra modi become esteemed pm eyes think eligible candidate would really like know
india narendra modi develops greater sense national identity purpose strength opposition tries increase divisions within country encourage sympathy india adversaries
gujarat 2 day visit pm narendra modi inaugurate several projects gujaratsaysnamoagain
pm narendra modi explains relevance communication national youth parliament festival awards 2019 via namo app
official response moved sending dossiers revenge strikes kudos narendra modi govt waiting moves preemptive strikes
open view news desk prime minister shri narendra modi dedicate nation lay
bharat ratna must awarded honurable pm shri narendra modi ji dedication towards nation people busy playing cheap politics modiji working sleepless nation bharatratna namumkinabmumkinhai modiunstoppable bjp modi india
karnataka bjp chief b yeddyurappa wednesday said india pre emptive strikes terror camps pakistan created wave favour prime minister narendra modi enthused youths help us winning 22 lok sabha seats karnataka
india keen reach top 25 position global innovation index soon narendra modi
modi modi ji thank much bringing wing commander abhimanyu back proved skills management bharat got glory desired since centuries
pm narendra modi pulls child ear delhi metro young boy reaction make day via namo app
past today hon pm shree narendra modi ji good bond american country also would like tell frndshp telling wht trump said modi frnd ivanka friend well grt respect 4 him
prime minister narendra modi grand finale smart india hackathon 57th rank global innovation index 2014 81 means made jump 24 ranks 4 years reach top 25 soon connectgujarat beyondjustnews
india keen reach top 25 position global innovation index soon narendra modi via namo app
please forward hounarable prime minister sri narendra modi
salute indianairforce fearless operation testimony iaf defence forces unparalleled strike capabilities pm narendra modi led bjp government believes forces makes compromise terrorism national security jai hind
race pm post nation stands firmly behind narendra modi nitin gadkari
hon pm sri narendra modi ji visionary initiative amrut facilitating robust sewage clean water supply across country foundation stone ambitious project worth rs 213 cr amrut formally laid recently nagaon nagaonischanging
pm narendra modi addressing construction technology india event 2019 new delhi pm emphasized commitment government towards ensuring every family dream home becomes reality
new india governed strong leader shri narendra modi ji modihaitomumkinhai
baby afraid shri narendra modi pappu
public trust narendra modi except disgruntled politicians phir ek bar modi sarkar
gujarat prime minister narendra modi flagged humsafar express train jamnagar bandra terminus via video conference inaugurated various development projects earlier today jamnagar
navbharatcontest place required 1947 1971 govt give time start construction us big gift named war memorial delhi always near heart every indian thanks narendra modi ji namoagain
gujarat prime minister narendra modi flagged humsafar express train jamnagar bandra terminus via video conference inaugurated various development projects earlier today jamnagar
perfect india needs narendra modi rather nincompoop slave corrupt dynasty
pm narendra modi pulls child ear delhi metro young boy reaction make day via namo app
let us forget thank narendra damodar modi bharat today truly showed us political accomplish
fan mr narendra modi
yes people amethi waiting welcome beloved prime minister shree narendra modi ji
new india decisive fearless pm narendra modi
would day take narendra modi premiership countenance praise statesmanship puppet military evil enemy
prime minister narendra modi launches khelo india app promote sports fitness via namo app
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
historic rally bihari shree narendra modi thanks
prime minister shri narendra modi address students participating smart india hackathon 2019 2nd march 10 pm night video conference
pm shri narendra modi launches various sauni projects jamnagar gujarat gujaratsaysnamoagain
runfornamoagain namo coz way prime minister narendra modi handles situation
mr narendra modi real super hero want see pm 2019
difference nationalist pm dalal family rule narendra modi got owr pilot released 48 hours someone family would power would taken year jai hind
respectworthy pm appreciates assam rickshaw puller mannkibaat setting 9 schools meraboothsabsemazboot
new india decisive fearless pm narendra modi
washing workers feet political gimmick sanskar pm narendra modi via namo app
bjp president amit shah rally umaria madhya pradesh today pakistan isolated internationally nobody ready support kind diplomatic victory brought bjp narendra modi government
god bless brave heart happy return big thank hon ble prime minister mr narendra modi skillfully handling delicate usuues
pls coordinate narendra modi ji wife son want welcome iaf pilot abhinandan wagha border
warm welcome hero wing commander abhinandan true national hero dear narendra modi ji hats sir lucky prime minister vande mataram
sometime talk favourite religion islam feel insecure every non islamic country targeting hinduism even know hindu kings fought islamic ruler people like making support narendra modi
endorsing pm narendra modi solve kashmir issue
gujarat 2 day visit pm narendra modi inaugurate several projects gujaratsaysnamoagain
think pm position india mr narendra modi continue 2029 country stronge devolpe
pm narendra modi explains relevance communication national youth parliament festival awards 2019 via nmapp
modihaitomumkinhai pmjdy become world largest financial inclusion initiative empowering poor people india narendra modi govt 27 44 crore rupay card issued beneficiaries via mynt
india buckle pressure forces given free hand take action pakistan proud hon ble prime minister mr narendra modi salute indian air force wing commander mr abhinandan jai hind
india listened narendra modi must shy away applauding forces public indiawithforces
pm narendra modi transforming india
world recognizes leader inner enemies wont personal gains
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
india keen reach top 25 position global innovation index soon narendra modi via namo app
common muslim india always nation narendra modi govt know holistic development done modi govt party plays vote bank politics win elections defeat modi
pm shri ji addresses mega video conference bjp workers meraboothsabsemazboot
pm narendra modi received gujarat cm vijay rupani deputy cm nitinbhai patel arrival jamnagar gujarat gujaratsaysnamoagain gujarat
ji ji ji requesting narendra modi sir kindly get iaf soldier abhinandan pakistani custody indians would highly obliged hit pakistan hard
tum mujhe kab tak rokoge beautiful rendition amitabh bacchan pleasantly surprised know poem written none pm narendra modi
pm narendra modi transforming india financial express
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
fishermen trained also enable incomes rise says pm addressing rally visakhapatnam follow live updates
shri narendra damodardas modi none far claim position
kheloapp pm narendra modi wednesday launched sports authority india sai first kind mobile application khelo india app order create awareness sports
aam junta goes narrative today narendra modi way ahead among 240 minimum bjp alone today 2019elections
wholehearted welcome beloved prime minister shri narendra modi ji visit today inauguration series development projects kanyakumari goddess district
india keen reach top 25 position global innovation index soon narendra modi via namo app
main desh nahi mitne dunga pm narendra modi recites poem praising indian air force crowd goes gaga
pm narendra modi night monitoring iaf air strike jaish e mohammed terror camp sources times
narendra modi busted pakistan myth shown india glorious tradition boldly fighting back via
true nationalist vote narendra modi pm fake one oppose election
new india decisive fearless pm narendra modi via
god hand gonna unstoppable welcome new india newindia pm narendra modi transforming india via namo app
narendramodi busted pakistan myth shown india glorious tradition boldly fighting back
never seen irresponsible prime minister like modiji atalji rajivji indira gandhi lived nation hand narendra modi working elections 24x7 election mode
watching samvad mera booth sabse majboot honourable pm narendra modi ji plz get connected dd namo app watch namoagain bjpm southdelhi
pm narendra modi pulls child ear delhi metro young boy reaction make day via namo app
namoagain2019 u better ditch prepare 2029 instead learn best pm new india decisive fearless pm narendra modi
golden era india chandragupt mourya loved nation like pious narendra modi ji loves never miss make modi hand string upcoming elections
narendra modi must use balakot consolidate india rajasic transformation via hallabol
pm narendra modi says 1 1 crore farmers got kisan scheme payout via namo app
join pm shri narendra modi mega interaction bjp karyakartas volunteers 15 00 locations across country 28th february 2019 12 30pm share questions ideas using meraboothsabsemazboot
pm narendra modi transforming india via
india keen reach top 25 position global innovation index soon narendra modi via namo app
narendra modi political retaliate take strict actions enemies country congress nothing support terrorism country time country
pm narendra modi opposition parties weaken country sake politics
pm narendra modi night monitoring iaf air strike jaish e mohammed terror camp  sources
modi opinion saudi prince kashmir issue see beautifully expressed opinion
washing workers feet political gimmick sanskar pm narendra modi via namo app
pm narendra modi transforming india five year term bjp led nda india gdp estimated grow `76 lakh crore relatively lower inflation fiscal deficit cad
congress president rahul gandhi asked state congress units forward list probable candidates third week february kick starting seen early congress preparations lok sabha elections
minimum income guarantee would brahmastra finish poverty hunger it give helping hand farmers job losers besides massive wealth distribution programme reduce gap crorepatis amp aam aadmi chehud
heartfelt gratitude hon ble cp shri rahul gandhi giving opportunity serve party will give 100 percent discharge assignment honour receive order
tamil nadu congress committee minority department state chairman dr j aslam basha districts visit tour schedule following krishinigiri dharampuri thiruvannamalai villupuram strengthen honable congress president shri rahul gandhi ji rgmission2019
youó cp aicc general secretary tell crpf trooperõs family lost life pulwama attack
modi time up rahul time now you can t see him time now it franchise gandhi shining now you can t see time now whymodi fridaythoughts
congress president shri rahul gandhi ji greets students who ve come interact jawaharlal nehru indoor auditorium delhi youngindiarising
breaking congress trying arjun khotkar jalna loksabha he may join congress presence rahul gandhi 1st march also if happens easy raosaheb danve prez bjp maharashtra
northeastwelcomesrahulgandhi during trip assam congress president rahul gandhi visits apollo hospital guwahati meet injured protestors arunachal pradesh agitation
ready congress co ordination committee meeting rahul gandhi ji guwahati
today aicc president ji visited aicc scy ailing father sri bogiram borah health city hospital guwahati thanks rahul gandhi jii
watched republictv 5 minutes arnab goswami barking opp politicising airstrikes amp called rahul gandhi ô50 yr old overgrown childõ oxford thesaurus include ôarnabõ list synonyms ôshamelessnessõ
rahul gandhi significantly gained alot seen recent state poll results anyways peace sakhshi
thanks shri rahul gandhi ji opposition parties bring back wing commander abhinandan ji requisting government
tommorrow public meeting mumbai organised mrcc particular professionals public tolk president indian national congress rahul gandhi ji request professionals part meeting rahul paswan sc dept patna
rahul gandhi pls answer idiots
rahul gandhi media shows
defend rahul gandhi party want say saynotowar
congratulations another promise fulfilled per direction cp rahul gandhi ji
please advice rahul gandhi friend program mumbai tomorrow
rahul gandhi indian would praise paf
breaking congress leader rahul gandhi becomes no 1 choice become prime minister india 2019 lok sabha elections claims survey pakistan
thank rahul gandhi breathing time
credit goes candle march rahul gandhi
margaret alvaõs congress comeback shows rahul gandhiõs mission election room
know difference true patriot rahul gandhi fake patriot narendra modi
like moral victory rahul gandhi elections
next p m rahul gandhi sir
thank much didnt expect anything less you thank securing release airforce personal cannot wait rahul gandhi sit toghther take south asia new direction
biggest scumbag ever saw politics iota sense even rahul gandhi looks matured front him
rahul gandhi promise india come power give martyrs status paramilitaries force
see tomorrow sir india congress party president rahul gandhi ji
congress president shri maharashtra today rahulgandhiinmaharashtra rginmumbai we welcome shri rahul gandhi maharashtrawithrg regards team
morning motivation leader move rahul gandhi went village campaign asked villagers mention two main problems village informed one problems lack qualified medical doctors
statement release came 6 01 pm would rahul gandhi candle march persona pressure put imran khan release commander modi ji spoken anything credit goes rahul ji
terrorists militants martyrs dead gov supporters bhakts rss hinduterrorist org terrorism religion rahul gandhi visionary pm modi working without rest hasnõt achieved anything imrankhan peacemaker independent media group
rahul gandhi next pm
live congress president rahul gandhi addresses public meeting dhule maharashtra aaplarahulgandhi
aaplarahulgandhi cp rahul gandhi maharashtra today adressing two public meetings one dhule one mumbai farmer suicides corruption amp unemployment time high
congress president rahul gandhi maharastra today looking forward hearing him aaplarahulgandhi
deciding prioritize sensitivity politics shown once again that heart right place this diff true patriotic nationalist rahul gandhi fake nationalist modi aaplarahulgandhi
rahul gandhi thinks billion indians think aaplarahulgandhi
great job rahul gandhi india salutes you tweet possible abhinandan back india
live congress president rahul gandhi addresses public meeting mumbai maharashtra mumbaicharahulgandhi
mumbaicharahulgandhi live congress president rahul gandhi addresses public meeting mumbai maharashtra mumbaicharahulgandhi
people mumbai happily welcome hoardings proclaiming rahul gandhi future prime minister greeted roads outside mumbai airport supporters too
people mumbai north central constituency welcomed mr rahul gandhi leader that mr gandhi scheduled meeting party municipal corporators
rahul gandhi promise upa come power give martyrs status paramilitary forces modi government doesnõt give martyrs status crpf menõs deaths fighting terrorists
vote support everything rahul gandhi
happy faces welcome rahul gandhi mumbai
i m quite sure visit rahul gandhi deep impact voters
taking moment ones make it ok waiting mr rahul gandhi make happen wish best
ok everything set visit rahul gandhi
rahul ji must thankful god saves wants peace gandhi ji always wanted peaceful solutions life must learn father nation sort things peace lots expectations next pm
true modi supportor says pm rahul gandhi banega
important rahul gandhi thinks its important billion indians think aaplarahulgandhi
mumbai promises housing slum dwellers
rahul gandhi promises 500 square feet homes mumbaiõs slum dwellers read more
rahul gandhi promises 500 sq ft houses slum dwellers mumbai mumbai hashmumbai
rahul gandhi promises 500 sq ft houses slum dwellers mumbai
rahul gandhi promises 500 sq ft houses slum dwellers mumbai money wealth stocks
rahul gandhi great leader
mumbai congress party president sanjay nirupam ji today bandra kurla complex welcome india congress party president rahul gandhi
state level lo cong tho alliance vunte loss national level lo congress tho alliance ki peddha opposition emi ledhu today rahul gandhi approval ratings ap far higher modi
shri rahul gandhi addressing public rally ranchi today discussing series issues including unemployment adivasi issues amp agri crisis
election season kicked off last evening rahul gandhi addressed rally mumbai apart attacking spoke providing minimum income poor people country party comes power 1 n
rahul gandhi ji pm india problem faced us
mr rahul gandhi ji please save annual festival threat youth congress post holder abhijeet pandey students iet davv indore
rahul gandhi assures 500 sq ft houses slum dwellers mumbai within ten days voted power
rahul gandhi next pm
congress president rahul gandhi said today party victory assembly bypolls bjp ruled madhya pradesh indicated winds change blowing
massive crowed rahul gandhi rally ranchi parivartanulgulanrally
congress chief rahul gandhi addressing public rally ranchi jharkhand live parivartanulgulanrally
rahul gandhi full attack mode parivartanulgulanrally loving it
congress give minimum guarantee income voted power money transferred directly account poor rahul gandhi
congress president shri rahul gandhi announced congress party would give 500 sq ft houses slum dwellers mumbai within 10 days voted power aaplarahulgandhi
parivartanulgulanrally state jharkhand suffering severely bjp rule congress president rahul gandhi address issues faced state address including issues unemployment tribal issues agricultural issues
congress president rahul gandhi arrives public rally thunderous applause amp tons love people jharkhand parivartanulgulanrally
congress president rahul gandhi arrives public rally thunderous applause amp tons love people jharkhand parivartanulgulanrally
rahul gandhi said five years back modi enjoyed good reputation today people see chor thief
welcome join team rahul gandhi
leader nation mr rahul gandhi ji
dear rahul gandhi plz lodge fir modi theft promise vote go congress
add this possible government rahul gandhi
dear rahul gandhi saying true please take court
coz difference modi rahul gandhi later favourite leader modi quality good kind human
first see facts speak have logic statements andh bhakt what rahul gandhi spoke today correct
hope star campaigner rahul gandhi many rallies tamil nadu
dear sir invite rahul gandhi india today conclave looking vision new india
rahulji plan slum dwellers bombay
pm modi launch projects worth rs 11 00 crore rahul gandhiõs bastion amethiêtoday
rahul gandhi next prime minister india
nice mr rahul gandhi such steps go long way winning people heart
pm modi solely responsible delay rafale jets arrival rahul gandhi
modi massive corruption rs 30 00 crore rafael fighter jets deal rahul gandhi
rahul gandhi speech mumbai outstanding amp people mumbai become happy amp encouraged rahul gandhi make counter attack modi shah regarding air strikes amp pulwama attack
amethi always deprived development since years rahul gandhi would have done smriti irani now
parivartanulgulanrally congress president rahul gandhi addresses parivartan ulgulan rally ranchi jharkhand
zero chance smriti irani able beat rahul gandhi amethi 2019 her best chance beat 2014 able so she can t beat amethi
next pm long live rahul gandhi
sure looks like intolerant india full hate amp division cong amp rahul gandhi keep talking about
missing point pm india can t ridicule even haters like that representing 1 25 billion people includes rahul gandhi well he respected post maintain discipline decorum
creditchorpracharak cp shri rahul gandhi opposition cancelled rallies post airstrikes amp wanted abhinandhan back but chowkidar busy trying make political mileage air strikes chowkidaarchorhai
honour meet leader true inspiration thank giving opportunity meet president mr rahul ji gandhi ji ji
watching vison rahul gandhi
rahul gandhi pm
rahul gandhi interacts tribal women ranchi via
never shared video rahul gandhi today sharing video rahul gandhi shows far far far far better modi human being modi would never done entire life
valuable advice congress rahul gandhi ji let sachin pilot jyotiraditya scindia cm odd days ashok gehlot kamal nath even days problem solved
former pm dr manmohan singh congress president sri rahul gandhi amp opposition leaders across country gather rajasthan swearing ceremony cm ashokgehlot amp deputy cm sachinpilot indiatrustscongress
recent airstrike balakot rahul gandhi mentioned people lost lives everyone understand right perspective
i’m priyanka ji next pm mr rahul gandhi ji
congress president rahul gandhi wrote visitors book gandhi ashram a inspiring place thank keeping flame leader alive
president rahul gandhi visitors book gandhi ashram a inspiring place thank keeping flame leader alive congress
hale hearty welcome beloved leader congress president shri rahul gandhi tamil nadu tamilnaduwelcomerahulgandhi
congress president rahul gandhi wrote visitors book gandhi ashram a inspiring place thank keeping flame leader alive rahulgandhi gandhimarcheson gandhiashram ahmedabad
jay ho congress jay ho rahul gandhi ji jay ho delhi congress jindabad vote congress party congress lao desh bachao ranjan sethy bargarh lokshaba odisha congress
anniversary dandimarch congress kicks campaign loksabhapolls the party leadership paid respect mahatma gandhi sabarmati ashram ahmedabad ahead launching campaign read
former pm dr manmohan singh upa chairperson smt sonia gandhi congress president rahul gandhi amp senior congress leaders visit gandhi ashram sabarmati gandhimarcheson dandimarch
upa chairperson sonia gandhi ji amp congress president rahul gandhi pay respects amp tribute sahid samarak ahmedabad ahead congress working committee meet gandhimarcheson
rahul gandhi ji wrote visitors book gandhi ashram sabarmati ahmedabad a inspiring place thank keeping flame leader alive
congress president shri rahul gandhi cpp chairperson smt sonia gandhi former pm dr manmohan singh paying homage martyrs shaheed smarak ahmedabad
rahul gandhi ji wrote visitors book gandhi ashram sabarmati ahmedabad a inspiring place thank keeping flame leader alive rgingujarat
congress president rahul gandhi upa chief mrs sonia gandhi former pm dr manmohan singh paid homage shaheed smarak ahmedabad
a inspiring place congress president rahul gandhi writes visitor book sabarmati gandhi ashram ahmedabad
congress president rahul gandhi upa chief mrs sonia gandhi former pm dr manmohan singh paid homage shaheed smarak ahmedabad gandhimarcheson
congress party kickstarts campaign prayer meeting anniversary dandi march rahul gandhi signed visitors book sabarmati ashram a inspiring place thank keeping flame leader alive gandhimarcheson
congress president rahul gandhi sonia gandhi manmohan singh priyanka gandhi vadra leaders attend prayer meet sabarmati ashram ahmedabad anniversary dandi march video credit ani
thiruvananthapuram   kerala congress screening committee finalise distribution seats discussing party chief rahul gandhi visits state thursday a committee meeting held monday delhi leadership …
sharad pawar contest loksabha elections 2019 maharashtra cong lop son joins bjp mlas telangana amp gujarat deserting congress indicator way wind blowing also rahul gandhi leadership inspiring s
rahul gandhi must got hard on seeing hardik patel
rahul gandhi wrote visitors book gandhi ashram sabarmati ahmedabad a inspiring place thank keeping flame leader alive welcometogujaratrahulji
good thinking great congress best rahul gandhi
rahul gandhi wrote visitors book gandhi ashram sabarmati ahmedabad a inspiring place thank keeping flame leader alive dandimarch
former pm dr manmohan singh ji upa chairperson smt sonia gandhi ji congress president shri rahul gandhi ji smt priyanka gandhi ji amp senior congress leaders visit gandhi ashram sabarmati today
""")

# path_to_tweets = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Operated tweets\\"
file_modi = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\word cloud data\\modi.csv"
file_rahul = "D:\\Users\\yashk\\Campaign-Assistant\\Data\word cloud data\\rahul.csv"


def getdataforcloud(file_path):
    fileobject = open(file_path,'r')
    file = csv.reader(fileobject)
    text = ""
    for row in file:
        text += row[0]
    return text


if __name__ == "__main__":
    # adding some words which are obvious
    for word in ["modi","rahul","narendra","gandhi"]:
        stop_words.add(word)
    # text = (getdataforcloud(file_path=file_modi))
    text = dummy
    word_cloud = WordCloud(max_words=100, width=1200,
                           height=700, margin=0,
                           background_color=None,
                           mode="RGBA",  # makes the background transparent with None in background_color
                           stopwords=stop_words
                           ).generate(text)
    word_cloud.to_file('D:\\Users\\yashk\\Campaign-Assistant\\Code\\Resources\\dummy_cloud.png')
    # word_cloud = WordCloud(max_words=100, width=1200,
    #                        height=700, margin=0,
    #                        background_color=None,
    #                        mode="RGBA",  # makes the background transparent with None in background_color
    #                        stopwords=stop_words
    #                        ).generate(text)
    # word_cloud.to_file('D:\\Users\\yashk\\Campaign-Assistant\\Code\\Resources\\modi_cloud.png')
    # text = (getdataforcloud(file_path=file_rahul))
    # word_cloud = WordCloud(max_words=100, width=1200,
    #                        height=700, margin=0,
    #                        background_color=None,
    #                        mode="RGBA",
    #                        stopwords=stop_words
    #                        ).generate(text)
    # word_cloud.to_file('D:\\Users\\yashk\\Campaign-Assistant\\Code\\Resources\\rahul_cloud.png')
    # Display the generated image:
    # print(word_cloud.words_)
    # plt.imshow(word_cloud, interpolation='bilinear')
    # plt.axis("off")
    # plt.margins(x=0, y=0)
    # plt.show()

# getdataforcloud(file_path=path_to_tweets+file_modi)