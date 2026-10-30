# Contenido de la demo Apartamentos Don Víctor (Salamanca) (es/en/fr/de). Hechos de donvictor.es leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones de clientes.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran los apartamentos reales.','en':' Images are illustrations and do not show the actual apartments.','fr':' Les images sont des illustrations et ne montrent pas les appartements réels.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Apartments.'}
H={'es':['Apartamentos #1, #2 y #3','Apartamentos #4 y #5'],'en':['Apartments #1, #2 and #3','Apartments #4 and #5'],'fr':['Appartements n°1, n°2 et n°3','Appartements n°4 et n°5'],'de':['Apartments Nr. 1, 2 und 3','Apartments Nr. 4 und 5']}
RD={
'es':['De una sola estancia, de 42 a 45 m², con ventana a la calle, cama de matrimonio de 150 x 190 cm, cocina integrada completa, baño privado con cabina de hidromasaje y wifi gratis.','De 50 y 52 m², con ventana a la calle, cocina con encimera de piedra, vitrocerámica y frigorífico combi, iluminación LED dual regulable y ventanas Climalit Silence.'],
'en':['Studio apartments of 42 to 45 m², with a window onto the street, 150 x 190 cm double bed, full integrated kitchen, private bathroom with hydromassage shower and free wifi.','50 and 52 m², with a window onto the street, kitchen with stone worktop, ceramic hob and fridge-freezer, dual adjustable LED lighting and Climalit Silence windows.'],
'fr':['Studios de 42 à 45 m², fenêtre sur rue, lit double 150 x 190 cm, cuisine intégrée complète, salle de bain privée avec cabine d’hydromassage et wifi gratuit.','De 50 et 52 m², fenêtre sur rue, cuisine avec plan en pierre, plaque vitrocéramique et réfrigérateur combiné, éclairage LED double réglable et fenêtres Climalit Silence.'],
'de':['Einraum-Apartments mit 42 bis 45 m², Fenster zur Straße, Doppelbett 150 x 190 cm, voll integrierter Küche, eigenem Bad mit Hydromassage-Dusche und kostenlosem WLAN.','50 und 52 m², Fenster zur Straße, Küche mit Steinarbeitsplatte, Glaskeramikkochfeld und Kühl-Gefrier-Kombination, dimmbarer Doppel-LED-Beleuchtung und Climalit-Silence-Fenstern.']}
ART={
'hero':('columns',9701,['#3b2a1c','#d9a35f','#f2d29b','#7a5a3a','#5c4329','#2d2014']),
'intro':('arches',9702,['#f1e9db','#faf4ea','#b07a3e','#7a5a3a','#3b2a1c']),
'r1':('columns',9711,['#efe6d6','#d39b57','#7a5a3a','#3b2a1c','#1f160e']),
'r2':('arches',9712,['#ece4d4','#c88d4c','#f0cf98','#5c4329','#3b2a1c','#21170e']),
'g1':('skyline',9721,['#2c2118','#e0aa64','#f4d7a6','#6a4e33','#523c27','#2a1e13']),
'g2':('columns',9722,['#f0e8da','#f9f3e9','#8a6440','#6a4c30','#3a2918']),
'g3':('hills',9723,['#ece7da','#f1e2c3','#d6a160','#a8a07e','#7c7458','#55503c']),
'g4':('arches',9724,['#3b2a1c','#dba660','#f3d49e','#4f3c52','#3d2f41','#221b27'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Apartamentos Don Víctor · Apartamentos en el centro de Salamanca',see_rooms='Ver los apartamentos',hero_k='Salamanca · Calle Hovohambre 11',hero_t='Siente el confort en el centro histórico de Salamanca',hero_s='5 apartamentos en la calle Hovohambre, a solo 170 m de la Plaza Mayor.',
 intro_t='Un oasis de tranquilidad en el centro',intro_p1='La calle Hovohambre es una de las pocas calles apacibles en el mismo centro de Salamanca. Cada apartamento se concibió desde cero, con especial atención a los detalles.',
 intro_p2='Sales por la puerta y tienes monumentos, tiendas, supermercados y vida nocturna. La entrada es con códigos que recibes antes de llegar, sin esperas de check-in.',
 stats=['5 apartamentos','170 m de la Plaza Mayor','Entrada con código','Wifi gratis'],nav_rooms='Apartamentos',rooms_t='Nuestros 5 apartamentos',rooms_s='De una sola estancia, de 42 a 52 m².',
 svcs=['Entrada con códigos antes de llegar','Wifi de alta velocidad sin límite','Cocina integrada completa','Cabina de hidromasaje','Calefacción','Ventanas Climalit Silence'],
 around_s='En pleno casco histórico, cerca de la Plaza Mayor, la Universidad y las catedrales.',
 loc_p='Calle Hovohambre 11 · 37001 Salamanca. Entrada y salida a las 12:00.',
 chips=['¿Qué apartamentos tenéis?','¿Cómo se entra al apartamento?','¿Cuánto cuesta la noche?','¿Cómo reservo?']),
'en':dict(title='Apartamentos Don Víctor · Apartments in central Salamanca',see_rooms='See the apartments',hero_k='Salamanca · Calle Hovohambre 11',hero_t='Feel the comfort of Salamanca’s old town',hero_s='5 apartments on Calle Hovohambre, just 170 m from the Plaza Mayor.',
 intro_t='An oasis of calm in the centre',intro_p1='Calle Hovohambre is one of the few quiet streets right in the centre of Salamanca. Each apartment was designed from scratch, with special attention to detail.',
 intro_p2='Step out of the door and you have monuments, shops, supermarkets and nightlife. Entry is with codes sent before you arrive, so there is no check-in wait.',
 stats=['5 apartments','170 m from Plaza Mayor','Code entry','Free wifi'],nav_rooms='Apartments',rooms_t='Our 5 apartments',rooms_s='Studio apartments from 42 to 52 m².',
 svcs=['Entry codes sent before arrival','Unlimited high-speed wifi','Full integrated kitchen','Hydromassage shower','Heating','Climalit Silence windows'],
 around_s='Right in the old town, close to the Plaza Mayor, the University and the cathedrals.',
 loc_p='Calle Hovohambre 11 · 37001 Salamanca. Check-in and check-out at 12:00.',
 chips=['Which apartments do you have?','How do I get into the apartment?','How much is a night?','How do I book?']),
'fr':dict(title='Apartamentos Don Víctor · Appartements au centre de Salamanque',see_rooms='Voir les appartements',hero_k='Salamanque · Calle Hovohambre 11',hero_t='Le confort au cœur du centre historique de Salamanque',hero_s='5 appartements rue Hovohambre, à seulement 170 m de la Plaza Mayor.',
 intro_t='Une oasis de calme au centre',intro_p1='La rue Hovohambre est l’une des rares rues paisibles en plein centre de Salamanque. Chaque appartement a été conçu de zéro, avec une attention particulière aux détails.',
 intro_p2='En sortant, vous avez monuments, boutiques, supermarchés et vie nocturne. L’entrée se fait avec des codes envoyés avant l’arrivée, sans attente au check-in.',
 stats=['5 appartements','170 m de la Plaza Mayor','Entrée par code','Wifi gratuit'],nav_rooms='Appartements',rooms_t='Nos 5 appartements',rooms_s='Studios de 42 à 52 m².',
 svcs=['Codes d’entrée envoyés avant l’arrivée','Wifi haut débit illimité','Cuisine intégrée complète','Cabine d’hydromassage','Chauffage','Fenêtres Climalit Silence'],
 around_s='En plein centre historique, près de la Plaza Mayor, de l’Université et des cathédrales.',
 loc_p='Calle Hovohambre 11 · 37001 Salamanque. Arrivée et départ à 12:00.',
 chips=['Quels appartements avez-vous ?',"Comment entre-t-on dans l'appartement ?",'Combien coûte la nuit ?','Comment réserver ?']),
'de':dict(title='Apartamentos Don Víctor · Apartments im Zentrum von Salamanca',see_rooms='Apartments ansehen',hero_k='Salamanca · Calle Hovohambre 11',hero_t='Komfort in der Altstadt von Salamanca',hero_s='5 Apartments in der Calle Hovohambre, nur 170 m von der Plaza Mayor.',
 intro_t='Eine Oase der Ruhe im Zentrum',intro_p1='Die Calle Hovohambre ist eine der wenigen ruhigen Straßen mitten im Zentrum von Salamanca. Jedes Apartment wurde von Grund auf und mit viel Liebe zum Detail gestaltet.',
 intro_p2='Vor der Tür liegen Sehenswürdigkeiten, Geschäfte, Supermärkte und Nachtleben. Der Zugang erfolgt mit Codes, die Sie vor der Anreise erhalten – ohne Wartezeit beim Check-in.',
 stats=['5 Apartments','170 m zur Plaza Mayor','Zugang per Code','Kostenloses WLAN'],nav_rooms='Apartments',rooms_t='Unsere 5 Apartments',rooms_s='Einraum-Apartments mit 42 bis 52 m².',
 svcs=['Zugangscodes vor der Anreise','Unbegrenztes Highspeed-WLAN','Voll integrierte Küche','Hydromassage-Dusche','Heizung','Climalit-Silence-Fenster'],
 around_s='Mitten in der Altstadt, nahe der Plaza Mayor, der Universität und den Kathedralen.',
 loc_p='Calle Hovohambre 11 · 37001 Salamanca. Check-in und Check-out um 12:00 Uhr.',
 chips=['Welche Apartments gibt es?','Wie komme ich ins Apartment?','Was kostet eine Nacht?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://www.donvictor.es/search-results/'
BOOK=dict(mode='engine',url={l:RB for l in ('es','en','fr','de')})
D=dict(name='Apartamentos Don Víctor',ac='#3b2a1c',ac2='#7a5a3a',ac2_a11y='#5c4329',book=BOOK,around=['Plaza Mayor de Salamanca','Universidad de Salamanca'],foot=FOOT,
 address='Calle Hovohambre 11 · 37001 Salamanca',phones=['+34 672 51 82 28'],emails=['reservas@donvictor.es'],maps='Apartamentos Don Víctor, Calle Hovohambre 11, 37001 Salamanca',t=T)
META=dict(repo='demo-apartamentos-don-victor-salamanca',name='Apartamentos Don Víctor',legal_name='Don Victor (titular persona física, autónomo, según el aviso legal de su web)',registry_ids=['NIF de persona física publicado en el aviso legal de su web (no se copia en la demo)'],
 url='https://www.donvictor.es/',domain='donvictor.es',municipality='Salamanca',province='Salamanca',sector='5 apartamentos turísticos en el centro de Salamanca',
 read_at='2026-10-30T09:22:00+01:00',created_at='2026-10-30T09:21:00+01:00',built_at='2026-10-30T09:35:00+01:00',audit_date='2026-10-30T09:08:00+01:00',
 rating=dict(value=4.5,coincide=['web'],date='2026-10-29',url='https://www.google.com/maps/place/Apartamentos+Don+V%C3%ADctor+Salamanca/@40.9644068,-5.6621099,17z/data=!3m1!4b1!4m6!3m5!1s0xd3f27005e10b4af:0x63cba54c45fa5062!8m2!3d40.9644068!4d-5.6621099!16s%2Fg%2F11vqdrxwgh'),
 book=dict(mode='engine',url=RB,note='motor de reservas real de su web (buscador MotoPress Hotel Booking del formulario «Reserva ya», action /search-results/), HTTP 200 comprobado el 30/10/2026; su web solo está en español, mismo enlace en los 4 idiomas.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué apartamentos tenéis?','K01'),('¿Cómo se entra al apartamento?','K02'),('¿A qué hora es la entrada y la salida?','K03'),('¿Hay wifi?','K04'),('¿Tienen cocina?','K05'),('¿Admitís mascotas?','K06'),('¿Cuánto cuesta la noche?','K07'),('¿Dónde están los apartamentos?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Cuál es la política de cancelación?','K10'),('¿Qué incluye la estancia?','K11'),('¿Tenéis piscina?',None),('¿Hay gimnasio?',None)],
'en':[('Which apartments do you have?','K01'),('How do I get into the apartment?','K02'),('What are the check-in and check-out times?','K03'),('Is there wifi?','K04'),('Is there a kitchen?','K05'),('Do you accept pets?','K06'),('How much is a night?','K07'),('Where are the apartments?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('What is the cancellation policy?','K10'),('What is included in the stay?','K11'),('Do you have a swimming pool?',None),('Is there a gym?',None)],
'fr':[('Quels appartements avez-vous ?','K01'),("Comment entre-t-on dans l'appartement ?",'K02'),('Quels sont les horaires d’arrivée et de départ ?','K03'),('Y a-t-il le wifi ?','K04'),('Y a-t-il une cuisine ?','K05'),('Acceptez-vous les animaux ?','K06'),('Combien coûte la nuit ?','K07'),('Où se trouvent les appartements ?','K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),("Quelle est la politique d'annulation ?",'K10'),('Qu’est-ce qui est inclus dans le séjour ?','K11'),('Avez-vous une piscine ?',None),('Y a-t-il une salle de sport ?',None)],
'de':[('Welche Apartments gibt es?','K01'),('Wie komme ich ins Apartment?','K02'),('Wann sind Check-in und Check-out?','K03'),('Gibt es WLAN?','K04'),('Gibt es eine Küche?','K05'),('Sind Haustiere erlaubt?','K06'),('Was kostet eine Nacht?','K07'),('Wo befinden sich die Apartments?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Wie sind die Stornobedingungen?','K10'),('Was ist im Aufenthalt inbegriffen?','K11'),('Haben Sie ein Schwimmbad?',None),('Gibt es ein Fitnessstudio?',None)]}
