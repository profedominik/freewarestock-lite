"""Vocabulary source of truth.

Format per line:  word | category | es | fr | de | extra search tags (comma separated)

Levels:
  A0  - absolute beginner: the first concrete, picturable nouns
  A1  - beginner (CEFR A1)
  A2  - elementary (CEFR A2)
  B1  - intermediate (CEFR B1)
  B2  - upper intermediate (planned, not yet illustrated)
"""

A0 = """
boy|people|el niño|le garçon|der Junge|child,kid,son
girl|people|la niña|la fille|das Mädchen|child,kid,daughter
man|people|el hombre|l'homme|der Mann|adult,father,dad,person
woman|people|la mujer|la femme|die Frau|adult,mother,mum,mom,person
baby|people|el bebé|le bébé|das Baby|infant,child
house|home|la casa|la maison|das Haus|home,building
door|home|la puerta|la porte|die Tür|entrance
window|home|la ventana|la fenêtre|das Fenster|glass
bed|home|la cama|le lit|das Bett|sleep,bedroom
chair|home|la silla|la chaise|der Stuhl|seat,furniture
table|home|la mesa|la table|der Tisch|furniture,desk
lamp|home|la lámpara|la lampe|die Lampe|light
car|transport|el coche|la voiture|das Auto|vehicle,automobile
bus|transport|el autobús|le bus|der Bus|vehicle,public transport
bike|transport|la bicicleta|le vélo|das Fahrrad|bicycle,cycle
boat|transport|el barco|le bateau|das Boot|sailboat,ship,sea
train|transport|el tren|le train|der Zug|railway,locomotive
plane|transport|el avión|l'avion|das Flugzeug|airplane,aeroplane,aircraft,fly
dog|animals|el perro|le chien|der Hund|pet,puppy
cat|animals|el gato|le chat|die Katze|pet,kitten
bird|animals|el pájaro|l'oiseau|der Vogel|fly
fish|animals|el pez|le poisson|der Fisch|sea,water
horse|animals|el caballo|le cheval|das Pferd|farm,pony
cow|animals|la vaca|la vache|die Kuh|farm,milk
apple|food|la manzana|la pomme|der Apfel|fruit
banana|food|el plátano|la banane|die Banane|fruit
bread|food|el pan|le pain|das Brot|loaf,bakery
egg|food|el huevo|l'œuf|das Ei|breakfast
milk|food|la leche|le lait|die Milch|drink
water|food|el agua|l'eau|das Wasser|drink,glass
cake|food|el pastel|le gâteau|der Kuchen|birthday,dessert
sun|nature|el sol|le soleil|die Sonne|sky,weather,day
moon|nature|la luna|la lune|der Mond|night,sky
star|nature|la estrella|l'étoile|der Stern|night,sky
tree|nature|el árbol|l'arbre|der Baum|plant,forest
flower|nature|la flor|la fleur|die Blume|plant,garden
cloud|nature|la nube|le nuage|die Wolke|sky,weather
ball|things|la pelota|le ballon|der Ball|toy,play,sport
book|school|el libro|le livre|das Buch|read,school
pen|school|el bolígrafo|le stylo|der Kuli|write,school,ballpoint
phone|things|el teléfono|le téléphone|das Handy|mobile,smartphone,cell
cup|things|la taza|la tasse|die Tasse|mug,coffee,tea
key|things|la llave|la clé|der Schlüssel|lock,door
bag|things|el bolso|le sac|die Tasche|handbag,purse
clock|things|el reloj|l'horloge|die Uhr|time
hat|clothes|el sombrero|le chapeau|der Hut|sun hat
shoe|clothes|el zapato|la chaussure|der Schuh|sneaker,trainer
shirt|clothes|la camiseta|le t-shirt|das T-Shirt|t-shirt,top,tee
hand|body|la mano|la main|die Hand|fingers
eye|body|el ojo|l'œil|das Auge|see,look
"""

A1 = """
pig|animals|el cerdo|le cochon|das Schwein|farm
sheep|animals|la oveja|le mouton|das Schaf|farm,wool,lamb
duck|animals|el pato|le canard|die Ente|bird,pond
rabbit|animals|el conejo|le lapin|das Kaninchen|bunny,pet
elephant|animals|el elefante|l'éléphant|der Elefant|zoo,africa
lion|animals|el león|le lion|der Löwe|zoo,cat,africa
frog|animals|la rana|la grenouille|der Frosch|pond,green
butterfly|animals|la mariposa|le papillon|der Schmetterling|insect,fly
orange|food|la naranja|l'orange|die Orange|fruit,citrus
carrot|food|la zanahoria|la carotte|die Karotte|vegetable
tomato|food|el tomate|la tomate|die Tomate|vegetable,fruit
cheese|food|el queso|le fromage|der Käse|dairy
pizza|food|la pizza|la pizza|die Pizza|italian,dinner
ice cream|food|el helado|la glace|das Eis|dessert,summer,cone
grapes|food|las uvas|le raisin|die Trauben|fruit,grape
strawberry|food|la fresa|la fraise|die Erdbeere|fruit,berry
sofa|home|el sofá|le canapé|das Sofa|couch,furniture
television|home|la televisión|la télévision|der Fernseher|tv,screen
computer|home|el ordenador|l'ordinateur|der Computer|laptop,pc
umbrella|things|el paraguas|le parapluie|der Regenschirm|rain
glasses|things|las gafas|les lunettes|die Brille|spectacles,see
plate|things|el plato|l'assiette|der Teller|dish,kitchen
spoon|things|la cuchara|la cuillère|der Löffel|cutlery,kitchen
fork|things|el tenedor|la fourchette|die Gabel|cutlery,kitchen
bottle|things|la botella|la bouteille|die Flasche|drink,glass
dress|clothes|el vestido|la robe|das Kleid|skirt
sock|clothes|el calcetín|la chaussette|die Socke|feet
trousers|clothes|los pantalones|le pantalon|die Hose|pants,jeans
scarf|clothes|la bufanda|l'écharpe|der Schal|winter
mountain|nature|la montaña|la montagne|der Berg|hill,snow
sea|nature|el mar|la mer|das Meer|ocean,waves,beach
rain|nature|la lluvia|la pluie|der Regen|weather,cloud
snow|nature|la nieve|la neige|der Schnee|weather,winter,snowflake
rainbow|nature|el arcoíris|l'arc-en-ciel|der Regenbogen|weather,colours,colors
leaf|nature|la hoja|la feuille|das Blatt|tree,plant,autumn
fire|nature|el fuego|le feu|das Feuer|campfire,hot,flame
truck|transport|el camión|le camion|der Lastwagen|lorry,vehicle
helicopter|transport|el helicóptero|l'hélicoptère|der Hubschrauber|fly,aircraft
motorbike|transport|la moto|la moto|das Motorrad|motorcycle,vehicle
nose|body|la nariz|le nez|die Nase|face,smell
mouth|body|la boca|la bouche|der Mund|face,lips,eat
ear|body|la oreja|l'oreille|das Ohr|face,hear,listen
foot|body|el pie|le pied|der Fuß|feet,toes
tooth|body|el diente|la dent|der Zahn|teeth,dentist
pencil|school|el lápiz|le crayon|der Bleistift|write,draw
scissors|school|las tijeras|les ciseaux|die Schere|cut
guitar|things|la guitarra|la guitare|die Gitarre|music,instrument
kite|things|la cometa|le cerf-volant|der Drachen|toy,wind
gift|things|el regalo|le cadeau|das Geschenk|present,birthday
balloon|things|el globo|le ballon de baudruche|der Luftballon|party,birthday
"""

A2 = """
giraffe|animals|la jirafa|la girafe|die Giraffe|zoo,africa,tall
zebra|animals|la cebra|le zèbre|das Zebra|zoo,africa,stripes
monkey|animals|el mono|le singe|der Affe|zoo,jungle
penguin|animals|el pingüino|le manchot|der Pinguin|bird,ice,cold
snake|animals|la serpiente|le serpent|die Schlange|reptile
turtle|animals|la tortuga|la tortue|die Schildkröte|tortoise,reptile
whale|animals|la ballena|la baleine|der Wal|sea,ocean
shark|animals|el tiburón|le requin|der Hai|sea,ocean,fish
owl|animals|el búho|le hibou|die Eule|bird,night
bee|animals|la abeja|l'abeille|die Biene|insect,honey
spider|animals|la araña|l'araignée|die Spinne|web,insect
camel|animals|el camello|le chameau|das Kamel|desert
bridge|places|el puente|le pont|die Brücke|river
castle|places|el castillo|le château|die Burg|king,queen,palace
forest|places|el bosque|la forêt|der Wald|trees,woods
desert|places|el desierto|le désert|die Wüste|sand,cactus,hot
island|places|la isla|l'île|die Insel|sea,palm,beach
volcano|places|el volcán|le volcan|der Vulkan|mountain,lava
lighthouse|places|el faro|le phare|der Leuchtturm|sea,coast
farm|places|la granja|la ferme|der Bauernhof|barn,countryside
tent|places|la tienda de campaña|la tente|das Zelt|camping
beach|places|la playa|la plage|der Strand|sand,sea,holiday
airport|transport|el aeropuerto|l'aéroport|der Flughafen|plane,travel
ambulance|transport|la ambulancia|l'ambulance|der Krankenwagen|hospital,emergency
tractor|transport|el tractor|le tracteur|der Traktor|farm
submarine|transport|el submarino|le sous-marin|das U-Boot|sea,underwater
taxi|transport|el taxi|le taxi|das Taxi|cab,car
rocket|transport|el cohete|la fusée|die Rakete|space
ship|transport|el buque|le navire|das Schiff|ocean liner,cruise
anchor|transport|el ancla|l'ancre|der Anker|ship,sea
doctor|jobs|el médico|le médecin|der Arzt|hospital,health
teacher|jobs|la profesora|la professeure|die Lehrerin|school,class
police officer|jobs|el policía|le policier|der Polizist|police,cop
firefighter|jobs|el bombero|le pompier|der Feuerwehrmann|fire,fireman
chef|jobs|el cocinero|le cuisinier|der Koch|cook,kitchen,restaurant
farmer|jobs|el granjero|l'agriculteur|der Bauer|farm
nurse|jobs|la enfermera|l'infirmière|die Krankenschwester|hospital,health
camera|things|la cámara|l'appareil photo|die Kamera|photo,picture
wallet|things|la cartera|le portefeuille|die Geldbörse|money,purse
passport|things|el pasaporte|le passeport|der Reisepass|travel
ticket|things|el billete|le billet|die Fahrkarte|travel,cinema
map|things|el mapa|la carte|die Landkarte|travel,treasure
compass|things|la brújula|la boussole|der Kompass|north,direction
backpack|things|la mochila|le sac à dos|der Rucksack|bag,rucksack,school
suitcase|things|la maleta|la valise|der Koffer|luggage,travel
hammer|things|el martillo|le marteau|der Hammer|tool
ladder|things|la escalera de mano|l'échelle|die Leiter|climb
bucket|things|el cubo|le seau|der Eimer|pail,water
brush|things|el pincel|le pinceau|der Pinsel|paintbrush,paint
mirror|home|el espejo|le miroir|der Spiegel|reflection
pillow|home|la almohada|l'oreiller|das Kissen|cushion,bed,sleep
blanket|home|la manta|la couverture|die Decke|bed,warm
towel|home|la toalla|la serviette|das Handtuch|bathroom
soap|home|el jabón|le savon|die Seife|wash,bathroom
oven|home|el horno|le four|der Ofen|cooker,stove,kitchen
kettle|home|el hervidor|la bouilloire|der Wasserkocher|tea,kitchen
teapot|home|la tetera|la théière|die Teekanne|tea
fridge|home|la nevera|le frigo|der Kühlschrank|refrigerator,kitchen
microwave|home|el microondas|le micro-ondes|die Mikrowelle|kitchen
sandwich|food|el sándwich|le sandwich|das Sandwich|lunch,bread
soup|food|la sopa|la soupe|die Suppe|bowl,lunch
salad|food|la ensalada|la salade|der Salat|vegetables
rice|food|el arroz|le riz|der Reis|bowl,grain
noodles|food|los fideos|les nouilles|die Nudeln|pasta,bowl
chocolate|food|el chocolate|le chocolat|die Schokolade|sweet,dessert
honey|food|la miel|le miel|der Honig|bee,sweet
lemon|food|el limón|le citron|die Zitrone|fruit,sour,citrus
potato|food|la patata|la pomme de terre|die Kartoffel|vegetable
onion|food|la cebolla|l'oignon|die Zwiebel|vegetable
mushroom|food|la seta|le champignon|der Pilz|vegetable,forest
watermelon|food|la sandía|la pastèque|die Wassermelone|fruit,summer
pineapple|food|la piña|l'ananas|die Ananas|fruit,tropical
piano|music|el piano|le piano|das Klavier|instrument,keys
violin|music|el violín|le violon|die Geige|instrument
drum|music|el tambor|le tambour|die Trommel|instrument
microphone|music|el micrófono|le micro|das Mikrofon|sing,mic
headphones|music|los auriculares|le casque|die Kopfhörer|listen,music
lightbulb|things|la bombilla|l'ampoule|die Glühbirne|light,idea
battery|things|la pila|la pile|die Batterie|power,energy
magnet|school|el imán|l'aimant|der Magnet|science
globe|school|el globo terráqueo|le globe|der Globus|world,earth,geography
calendar|things|el calendario|le calendrier|der Kalender|date,month
envelope|things|el sobre|l'enveloppe|der Briefumschlag|letter,mail,post
newspaper|things|el periódico|le journal|die Zeitung|news,read
candle|things|la vela|la bougie|die Kerze|light,birthday
trophy|things|el trofeo|le trophée|die Trophäe|cup,prize,winner
"""


B1 = """
skyscraper|places|el rascacielos|le gratte-ciel|der Wolkenkratzer|building,city,tall
tunnel|places|el túnel|le tunnel|der Tunnel|road,mountain
harbour|places|el puerto|le port|der Hafen|harbor,port,boats
factory|places|la fábrica|l'usine|die Fabrik|industry,work
museum|places|el museo|le musée|das Museum|art,history
library|places|la biblioteca|la bibliothèque|die Bibliothek|books,read,bookshelf
stadium|places|el estadio|le stade|das Stadion|sport,football
hospital|places|el hospital|l'hôpital|das Krankenhaus|doctor,health
pharmacy|places|la farmacia|la pharmacie|die Apotheke|chemist,medicine
bakery|places|la panadería|la boulangerie|die Bäckerei|bread,shop
supermarket|places|el supermercado|le supermarché|der Supermarkt|shop,shopping
restaurant|places|el restaurante|le restaurant|das Restaurant|eat,food
post office|places|la oficina de correos|la poste|die Post|mail,letter
police station|places|la comisaría|le commissariat|die Polizeiwache|police
fire station|places|el parque de bomberos|la caserne de pompiers|die Feuerwache|fire,firefighter
laboratory|science|el laboratorio|le laboratoire|das Labor|lab,science,chemistry,flask
microscope|science|el microscopio|le microscope|das Mikroskop|science,biology
telescope|science|el telescopio|le télescope|das Teleskop|stars,space
satellite|science|el satélite|le satellite|der Satellit|space,orbit
robot|science|el robot|le robot|der Roboter|machine,technology
solar panel|science|el panel solar|le panneau solaire|die Solaranlage|energy,sun
wind turbine|science|el aerogenerador|l'éolienne|das Windrad|energy,wind
recycling bin|things|el contenedor de reciclaje|la poubelle de recyclage|die Recyclingtonne|recycle,environment
wheelchair|health|la silla de ruedas|le fauteuil roulant|der Rollstuhl|disability,mobility
crutches|health|las muletas|les béquilles|die Krücken|injury,leg
bandage|health|la tirita|le pansement|das Pflaster|plaster,band-aid,first aid
thermometer|health|el termómetro|le thermomètre|das Thermometer|temperature,fever
stethoscope|health|el estetoscopio|le stéthoscope|das Stethoskop|doctor
syringe|health|la jeringa|la seringue|die Spritze|injection,vaccine
pills|health|las pastillas|les comprimés|die Tabletten|medicine,tablets
jewellery|clothes|las joyas|les bijoux|der Schmuck|jewelry,jewellery box
necklace|clothes|el collar|le collier|die Halskette|jewellery,jewelry,pearls
ring|clothes|el anillo|la bague|der Ring|jewellery,wedding,diamond
bracelet|clothes|la pulsera|le bracelet|das Armband|jewellery
perfume|things|el perfume|le parfum|das Parfüm|smell,scent
pyjamas|clothes|el pijama|le pyjama|der Schlafanzug|pajamas,sleep
raincoat|clothes|el impermeable|l'imperméable|der Regenmantel|rain,coat
boots|clothes|las botas|les bottes|die Stiefel|rain boots,wellies
sandals|clothes|las sandalias|les sandales|die Sandalen|summer,shoes
belt|clothes|el cinturón|la ceinture|der Gürtel|trousers
tie|clothes|la corbata|la cravate|die Krawatte|necktie,suit
parachute|transport|el paracaídas|le parachute|der Fallschirm|sky,jump
hot-air balloon|transport|el globo aerostático|la montgolfière|der Heißluftballon|fly,sky
sailboard|transport|la tabla de windsurf|la planche à voile|das Windsurfbrett|windsurf,sea
earthquake|nature|el terremoto|le tremblement de terre|das Erdbeben|disaster
tornado|nature|el tornado|la tornade|der Tornado|wind,storm,twister
lightning|nature|el relámpago|l'éclair|der Blitz|storm,thunder
storm|nature|la tormenta|l'orage|der Sturm|weather,wind,thunder
fog|nature|la niebla|le brouillard|der Nebel|weather,mist
kangaroo|animals|el canguro|le kangourou|das Känguru|australia
koala|animals|el koala|le koala|der Koala|australia
parrot|animals|el loro|le perroquet|der Papagei|bird
dolphin|animals|el delfín|le dauphin|der Delfin|sea
octopus|animals|el pulpo|la pieuvre|der Oktopus|sea
crab|animals|el cangrejo|le crabe|die Krabbe|sea,beach
jellyfish|animals|la medusa|la méduse|die Qualle|sea
squirrel|animals|la ardilla|l'écureuil|das Eichhörnchen|tree,nuts
fox|animals|el zorro|le renard|der Fuchs|forest
wolf|animals|el lobo|le loup|der Wolf|forest,night
bear|animals|el oso|l'ours|der Bär|forest
deer|animals|el ciervo|le cerf|der Hirsch|forest,antlers
screwdriver|tools|el destornillador|le tournevis|der Schraubenzieher|tool,screw
drill|tools|el taladro|la perceuse|die Bohrmaschine|tool
saw|tools|la sierra|la scie|die Säge|tool,wood
wrench|tools|la llave inglesa|la clé à molette|der Schraubenschlüssel|spanner,tool
vacuum cleaner|home|la aspiradora|l'aspirateur|der Staubsauger|hoover,clean
washing machine|home|la lavadora|la machine à laver|die Waschmaschine|laundry
iron|home|la plancha|le fer à repasser|das Bügeleisen|clothes,ironing
hairdryer|home|el secador|le sèche-cheveux|der Föhn|hair
"""

# Planned levels: listed so the roadmap is visible in the browser.
B2_PLANNED = """
astronaut scientist mechanic plumber electrician pilot dentist judge architect photographer waiter cashier
cathedral pyramid windmill dam waterfall glacier cave cliff valley swamp canal
binoculars hourglass lantern padlock chain rope magnifying-glass wheelbarrow shovel rake watering-can
escalator elevator traffic-light crossroads petrol-station parking-meter
hedgehog bat beaver peacock flamingo swan seal walrus hippo rhino crocodile gorilla
skeleton brain lungs muscle
"""


def parse(block, level):
    out = []
    for line in block.strip().splitlines():
        word, cat, es, fr, de, tags = [p.strip() for p in line.split("|")]
        out.append({
            "word": word,
            "slug": word.replace(" ", "-"),
            "level": level,
            "category": cat,
            "translations": {"es": es, "fr": fr, "de": de},
            "tags": [t.strip() for t in tags.split(",") if t.strip()],
        })
    return out


def planned(block, level):
    return [{"word": w.replace("-", " "), "slug": w, "level": level, "status": "planned"}
            for w in block.split()]


WORDS = parse(A0, "A0") + parse(A1, "A1") + parse(A2, "A2") + parse(B1, "B1")
PLANNED = planned(B2_PLANNED, "B2")
