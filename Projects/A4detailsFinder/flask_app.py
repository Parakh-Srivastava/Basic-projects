from flask import Flask,render_template,url_for,request

app = Flask(__name__)

students = {
    145120171: ("POOJITH B", "poojithb440@gmail.com", 8610838256, "5/47, Prarthana salai, Pasumpon nagar, Perumbakkam, Chennai.", (24, 5, 2008)),
    145120173: ("PAVITHRAN V", "pavithran9107@gmail.com", 9787708137, "155,SINGARAVELAR STREET, THARANGAMBADI.", (9, 10, 2007)),
    145120174: ("PRAVEEN R", "pk5931113@gmail.com", 7538820307, "No 24, Mudichur road, Bharathi Nagar, Old Perungalathur, West Tambaram.", (3, 12, 2007)),
    145120175: ("PARAKH SRIVASTAVA", "parakhsriv01@gmail.com", 9142000371, "C/o Pankaj Srivastava, Indira Nagar, Laliyahi.", (1, 2, 2006)),
    145120176: ("NIXON VETHAKANI SAMUEL B", "bennybenjamin200176@gmail.com", 9841326373, "21'A' kullakarai street, Muduchur road, West Tambaram.", (6, 6, 2008)),
    145120179: ("NITIN P", "nitin252007@gmail.com", 9944027095, "1903 Tiana, Hiranandani Egattur, Chennai.", (25, 7, 2007)),
    145120180: ("PARTHA SARATHY R", "rameshparthasarathy46@gmail.com", 9380969651, "NO 80A, SVN PILLAI ST, KANCHIPURAM.", (21, 3, 2008)),
    145120181: ("SURYA S", "ayrus101010@gmail.com", 8056722088, "12/27, Ramalingam street, Gopalasamudram .", (11, 5, 2007)),
    145120182: ("SURYAKUMAR M", "suryakumarmaniveeran@gmail.com", 9360987212, "1/55 WEST STREET, IRUPPUKURCHI, KUPPANTHAM PO, VRIDHACHALAM TK, CUDDALORE DT.", (22, 11, 2007)),
    145120183: ("SUYAMBU RATHISH S", "rathishsuyambu338@gmail.com", 9942678499, "Keela pallivasal street, Tisaiyanvilai, Tirunelveli district.", (26, 7, 2007)),
    145120185: ("TARASVIN SRINIVAAS M", "tarasvinsrinivas2007@gmail.com", 9176181090, "32/38B RAJAJI NAGAR, 2ND STREET, VILLIVAKKAM, Villivakkam, Villivakkam, Tiruvallur.", (12, 5, 2007)),
    145120187: ("THARUN G", "thxrun012907@gmail.com", 9952951983, "No. 21/472, AYOTHIYA NAGAR, TRIPLICANE.", (29, 11, 2007)),
    145120188: ("VALLARASU B", "vallarasuvasu8@gmail.com", 9655012138, "Mig 222, 12th Cross New A.S.T.C Hudco , Hosur - 635 109.", (8, 8, 2007)),
    145120190: ("VENKATMARAN P", "venkatmaran03@gmail.com", 9486386781, "1/171a, Amman Kovil Street, Manakadu, Melapattu, PO:Kilapattu, DIST: Kallakurichi.", (26, 9, 2007)),
    145120191: ("VETRIVEL P", "VMPVETRI07@GMAIL.COM", 9843199101, "11A, BHARATHIYAR ROAD, 2ND MAIN ROAD, JAIHINDPURAM, MADURAI.", (11, 9, 2007)),
    145120192: ("VISHAL A", "vishal1988viji@gmail.com", 9342122660, "53b,KURIJI NAGAR 13, THIRUMANGULAM,PO:THIRUMANGALAM,DIST;MADURAI, TAMIL NADU-625706.", (20, 12, 2007)),
    145120193: ("YABIN S", "yabinswagger@gmail.com", 9345783521, "SURANDAI ,SHALOM COTTAGE , PARANGUNDRAPURAM , 627859", (2, 9, 2007)),
    145120194: ("THRISH KUMAR M", "marakutty16041986@gmail.com", 9042588690, "No:20, Om sakthi nagar, manjakuppam, cuddalore-607001", (20, 8, 2007)),
    145120195: ("SURYA S", "suryaofficial19.03.2008@gmail.com", 9751805648, "1/206, North Street, Sittilarai, Musiri.", (19, 3, 2008)),
    145120197: ("SUJITH P", "sujith58prabhakaran@gmail.com", 7845530232, "Charles nagar, 3rd street No:12/21 Thiruvottiyur chennai.", (5, 8, 2007)),
    145120199: ("SRISHANTH S", "srishanth1716@gmail.com", 7418343346, "No.31, Durgalaya road, Thiruvarur.", (17, 1, 2008)),
    145120200: ("SRIMAN M", "sriman99902@gmail.com", 6382925275, "1/11, 16th Cross street, Indra nagar, Adyar, Chennai.", (9, 1, 2008)),
    145120202: ("SRIHARESH S", "sriharesh008@gmail.com", 8608411488, "NO 3/149-18A KAKKAN STREET, PONNI NAGAR, SRINIVASAPURAM, MAYILADUTHURAI", (2, 5, 2007)),
    145120203: ("SRI SHAKTHIVEL K", "srishakthivel07@gmail.com", 9600000875, "No:428th street, Poompuhar nagar, Kolathur, Chennai. ", (3, 8, 2007)),
    145120204: ("SRI SANJAY K", "srisanjay.official00@gmail.com", 6374197352, "No.8,RMV GARDEN LOGAMBIKAI ST,T.V.PURAM, PONNERI 601204.", (5, 7, 2007)),
    145120208: ("RITHIKAA K", "rithikaakarthik007@gmail.com", 9500447269, "10, VISALAKSHIPURAM MAIN ROAD NEAR TO MADURAI PUBLIC SCHOOL.", (28, 5, 2007)),
    145120209: ("RITHANYA A R", "arrithanya6@gmail.com", 9384016477, "601, BLOCK 1, ALLIANCE ORCHID SPRINGS, WATER CANAL ROAD, KORATTUR, CHENNAI.", (6, 12, 2007)),
    145120210: ("YOGITHA R", "rajendranj1979@gmail.com", 9444922831, "Anna Street, Thiruvanmiyur, Chennai.", (22, 5, 2007)),
    145120211: ("SUPRIYA R", "supriyamugilan2612@gmail.com", 9500514962, "2F/1056, P&T COLONY, 6TH STREET WEST 3RD MILE.", (26, 1, 2008)),
    145120212: ("YOSHITHA S", "yoshithas854@gmail.com", 9500116170, "19/G1, Ruby Residency, Narmatha street, Irumbuliyur, East Tambaram, Chennai.", (19, 6, 2008)),
    145120213: ("ALEXANDER S V", "alexanderalexander40054@gmail.com", 9843738127, "No 616, Raghavendra Nagar 3rd Street, Vettavalam Road , Tiruvannamalai.", (19, 6, 2008)),
    145120214: ("ASHWANTH A", "ashwanthayyappan1258@gmail.com", 9080060339, "Kalladikkollai, jambuvanodai, Thiruvarur, Tamil nadu-614738.", (12, 5, 2008)),
    145120215: ("ASWIN R J", "aswinrj1560@gmail.com", 8248671962, "G13, Malligai appartment, vijayalakshmi, Ambattur.", (28, 6, 2008)),
    145120216: ("BHARATH KUMAR S", "bharathrevathi.s22@gmail.com", 9003122548, "91, Muthamman nagar, Chennai.", (22, 6, 2007)),
    145120217: ("DEIVANAI S", "svldeivanai2008@gmail.com", 9865346819, "113C/5 Sankar colony 3rd Street, 3rd mile Thoothukudi.", (12, 5, 2008)),
    145120218: ("DHUSHYANTH V", "dhushvmj@gmail.com", 9600844826, "B/2 Mount batten street, Chennai.", (20, 8, 2007)),
    145120219: ("GODLIN K L", "klgodlin2008@gmail.com", 9487438374, "Nadaikkavu, Chathencode p.o, Kanniyakumari.", (10, 3, 2008)),
    145120220: ("HARI NIVVAS SANTHANAM", "hariniwas708@gmail.com", 7200587434, "3/505 Vembuli amman kovil street 1 ECR palavakkam, Chennnai 41", (31, 7, 2008)),
    145120221: ("JAGHADEESH R", "rjjagadeesh12@gmail.com", 9443953213, "7,South Ramalingam street, Mayiladuthrai. ", (4, 9, 2007)),
    145120222: ("JAYANTHIRAN S", "vvishal05116@gmail.com", 6381220682, "NO 29, MUTHUPILLAI STREET, VOC NAGAR, CHINNA SANKARANPALAYAM.", (20, 10, 2007)),
    145120223: ("JEYA SURYA R", "suryarajr360@gmailm.com", 9342914143, "206/30 rajmanikandan .c malai mettu street, Gandhi Salai, Chengalpattu.", (27, 8, 2008)),
    145120224: ("KISHORE KUMAR J", "god1912008@gmail.com", 9600221698, "62A, Srm avenue, kelakalkandar kottai, Trichy.", (19, 1, 2008)),
    145120225: ("KUMARAN K", "kumaranvdm2007@gmail.com", 9498802640, "32/A, NANDAVANKULA STREET, VEDARANYAM.", (30, 5, 2007)),
    145120226: ("NANCY METILDA D", "nancymetilda977@gmail.com", 9444914766, "NO 166, RK MUTT ROAD, MANDAVELI, CHENNAI.", (10, 11, 2007)),
    145120227: ("PRITHIVIRAJ D", "prithiviraj.d13@gmail.com", 9344247521, "No. 7 Muthulinga reddy street, West Tambaram, Chennai.", (13, 11, 2007)),
    145120228: ("RUVANTHIKA S", "ruvanthika8a@gmail.com", 9382676414, "No.112/3, MGR 5th Street MMDA colony, Arumbakkam.", (7, 1, 2008)),
    145120229: ("SANJAY M", "sanjaymurari82@gmail.com", 9566383763, "78A, Ganesh Garden, Chennivakam Ponneri.", (7, 7, 2007)),
    145120230: ("SARA V", "vasanthakumarsara77@gmail.com", 9003940462, "98/4303, OTTAKARA STREET, EAST GATE, THANJAVUR.", (29, 6, 2008)),
    145120231: ("SHANA MIRACLIN GIFTA S", "shanagifta2008@gmail.com", 9941227337, "10/1/G1 - THIRUKUNDRAM FLATS, SRINIVASA STREET, PERAMBUR", (20, 6, 2008)),
    145120232: ("SOUNDHARRAJ P", "danialsoundharraj@gmail.com", 9626605363, "Baba kovil back side, Ashok nagar, Thiruvathigai, Panruti.", (29, 1, 2008)),
    145120233: ("SURIYA N", "surixa1411@gmail.com", 7305804882, "121/64, Perumal Kovil 5th cross street, Madhavaram, Chennai.", (11, 3, 2008)),
    145120234: ("THEJASWINYI V", "thejuv08@gmail.com", 7904181972, "NO.19/4 RI FLATS VENKATESA NAGAR 2ND STREET 2ND EXTENSION SALIGRAMAM CHENNAI 600093", (10, 1, 2008)),
    145120235: ("VIJAY PRASANNA S", "vijay8610145@gmail.com", 8778177006, "1/495, SETHURAJAPURAM, PANDALGUDI POST, ARUPPUKOTTAI TALUKA, VIRUDHUNAGAR.", (18, 5, 2007)),
    145120236: ("YUVA RAJ M B", "yuvaraj272007@gmail.com", 6382550097, "152, MARIYAMMAN KOIL STREET, PANAMPATTU, VILLUPURAM.", (27, 9, 2007)),
    145120238: ("AL JESIRA J", "aljesira2007@gmail.com", 7305895460, "No,474B, Sulochana Nillayam, Scared Heart Street, Rajiv Gandhi Nagar, Pattabiram-600072", (17, 10, 2007)),
    145120241: ("HARITHA SREE R", "harithasree53690@gmail.com", 8438363886, "D712, D block, Urbanrise revolution one, padur, Kelambakkam.", (1, 11, 2007)),
    145120242: ("JAYASRIHARINI S", "jayasriharinis2007@gmail.com", 8012314447, "2/24, North street, Arasavanangadu, Thiruvarur.", (16, 8, 2007)),
    145120247: ("PAVITHRA T", "pavithratm21@gmail.com", 9150490683, "105, kalpataru royale, A block Vignarajapuram 6th extension Vengaivasal, Medavakkam.", (19, 7, 2007)),
    145120250: ("RUNEY JESLY R T", "runeyjesly@gmail.com", 9345179101, "12/17 Periyar Salai Main road, Kovilambakkam.", (25, 5, 2008)),
    145120255: ("OGGISETTY SRUJANA", "oggisettysrujana@gmail.com", 6300785949, "1-58, 1st ward, Near water tank , Near venugopala swamy temple Street, Parchur (PO)(Md), Bapatla district.", (6, 6, 2008))
}

@app.route('/', methods = ["GET", "POST"])
def index():
    css_ = url_for('static', filename='styles.css')
    result = ()
    submitted = False

    if request.method == "POST":
        submitted = True

        try:
            registerNumber = int(request.form.get("registerNum"))
            # Return a default 'not found' tuple when missing so template logic works
            result = students.get(registerNumber)
        except (ValueError,TypeError):
            result = None
    
    return render_template('index.html', css_path=css_, result=result, submitted=submitted)

if __name__ == "__main__":
    app.run(debug=True)