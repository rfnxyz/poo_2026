from Continente import Continente
from Pais import Pais
from Provincia import Provincia


class Seeder:
    """Clase encargada de inicializar los datos del mapa del mundo (América y Europa)."""

    def __init__(self):
        self.__continentes = []

    def getContinentes(self):
        return self.__continentes

    def inicializarDatos(self):
        """Instancia todos los países de América y Europa con sus provincias y limítrofes."""

        # ============================
        # CONTINENTES
        # ============================
        america = Continente("América")
        europa = Continente("Europa")

        self.__continentes.append(america)
        self.__continentes.append(europa)

        # ============================
        # PAÍSES DE AMÉRICA
        # ============================

        # --- América del Norte ---
        canada = Pais("Canadá", "Ottawa", 9984670)
        estadosUnidos = Pais("Estados Unidos", "Washington D.C.", 9833520)
        mexico = Pais("México", "Ciudad de México", 1964375)

        # --- América Central ---
        guatemala = Pais("Guatemala", "Ciudad de Guatemala", 108889)
        belice = Pais("Belice", "Belmopán", 22966)
        honduras = Pais("Honduras", "Tegucigalpa", 112492)
        elSalvador = Pais("El Salvador", "San Salvador", 21041)
        nicaragua = Pais("Nicaragua", "Managua", 130373)
        costaRica = Pais("Costa Rica", "San José", 51100)
        panama = Pais("Panamá", "Ciudad de Panamá", 75417)

        # --- Caribe (países insulares principales) ---
        cuba = Pais("Cuba", "La Habana", 109884)
        haiti = Pais("Haití", "Puerto Príncipe", 27750)
        republicaDominicana = Pais("República Dominicana", "Santo Domingo", 48671)
        jamaica = Pais("Jamaica", "Kingston", 10991)
        trinidadYTobago = Pais("Trinidad y Tobago", "Puerto España", 5130)

        # --- América del Sur ---
        colombia = Pais("Colombia", "Bogotá", 1141748)
        venezuela = Pais("Venezuela", "Caracas", 916445)
        guyana = Pais("Guyana", "Georgetown", 214969)
        surinam = Pais("Surinam", "Paramaribo", 163820)
        brasil = Pais("Brasil", "Brasilia", 8515767)
        ecuador = Pais("Ecuador", "Quito", 256370)
        peru = Pais("Perú", "Lima", 1285216)
        bolivia = Pais("Bolivia", "Sucre", 1098581)
        paraguay = Pais("Paraguay", "Asunción", 406752)
        chile = Pais("Chile", "Santiago", 756102)
        argentina = Pais("Argentina", "Buenos Aires", 2780400)
        uruguay = Pais("Uruguay", "Montevideo", 176215)

        # ============================
        # PROVINCIAS / ESTADOS DE AMÉRICA
        # ============================

        # --- Canadá (provincias principales) ---
        for nombre in ["Ontario", "Quebec", "Columbia Británica", "Alberta",
                        "Manitoba", "Saskatchewan", "Nueva Escocia",
                        "Nuevo Brunswick", "Terranova y Labrador",
                        "Isla del Príncipe Eduardo"]:
            canada.agregarProvincia(Provincia(nombre))

        # --- Estados Unidos (estados principales) ---
        for nombre in ["California", "Texas", "Florida", "Nueva York",
                        "Pensilvania", "Illinois", "Ohio", "Georgia",
                        "Carolina del Norte", "Michigan"]:
            estadosUnidos.agregarProvincia(Provincia(nombre))

        # --- México (estados principales) ---
        for nombre in ["Jalisco", "Ciudad de México", "Nuevo León",
                        "Veracruz", "Puebla", "Guanajuato", "Chiapas",
                        "Oaxaca", "Michoacán", "Sonora"]:
            mexico.agregarProvincia(Provincia(nombre))

        # --- Guatemala ---
        for nombre in ["Guatemala", "Quetzaltenango", "Escuintla",
                        "Alta Verapaz", "Petén"]:
            guatemala.agregarProvincia(Provincia(nombre))

        # --- Belice ---
        for nombre in ["Belice", "Cayo", "Orange Walk", "Corozal",
                        "Stann Creek", "Toledo"]:
            belice.agregarProvincia(Provincia(nombre))

        # --- Honduras ---
        for nombre in ["Francisco Morazán", "Cortés", "Atlántida",
                        "Olancho", "Comayagua"]:
            honduras.agregarProvincia(Provincia(nombre))

        # --- El Salvador ---
        for nombre in ["San Salvador", "Santa Ana", "La Libertad",
                        "San Miguel", "Sonsonate"]:
            elSalvador.agregarProvincia(Provincia(nombre))

        # --- Nicaragua ---
        for nombre in ["Managua", "León", "Matagalpa", "Chinandega",
                        "Masaya"]:
            nicaragua.agregarProvincia(Provincia(nombre))

        # --- Costa Rica ---
        for nombre in ["San José", "Alajuela", "Cartago", "Heredia",
                        "Guanacaste", "Puntarenas", "Limón"]:
            costaRica.agregarProvincia(Provincia(nombre))

        # --- Panamá ---
        for nombre in ["Panamá", "Colón", "Chiriquí", "Veraguas",
                        "Coclé"]:
            panama.agregarProvincia(Provincia(nombre))

        # --- Cuba ---
        for nombre in ["La Habana", "Santiago de Cuba", "Camagüey",
                        "Holguín", "Villa Clara"]:
            cuba.agregarProvincia(Provincia(nombre))

        # --- Haití ---
        for nombre in ["Oeste", "Norte", "Sur", "Artibonito",
                        "Centro"]:
            haiti.agregarProvincia(Provincia(nombre))

        # --- República Dominicana ---
        for nombre in ["Distrito Nacional", "Santiago", "Santo Domingo",
                        "La Vega", "San Cristóbal"]:
            republicaDominicana.agregarProvincia(Provincia(nombre))

        # --- Jamaica ---
        for nombre in ["Kingston", "Saint Andrew", "Saint Catherine",
                        "Clarendon", "Manchester"]:
            jamaica.agregarProvincia(Provincia(nombre))

        # --- Trinidad y Tobago ---
        for nombre in ["Puerto España", "San Fernando", "Chaguanas",
                        "Arima", "Tobago"]:
            trinidadYTobago.agregarProvincia(Provincia(nombre))

        # --- Colombia (departamentos principales) ---
        for nombre in ["Bogotá D.C.", "Antioquia", "Valle del Cauca",
                        "Cundinamarca", "Atlántico", "Santander",
                        "Bolívar", "Nariño", "Tolima", "Boyacá"]:
            colombia.agregarProvincia(Provincia(nombre))

        # --- Venezuela (estados principales) ---
        for nombre in ["Distrito Capital", "Zulia", "Miranda",
                        "Carabobo", "Lara", "Aragua", "Bolívar",
                        "Anzoátegui", "Táchira", "Mérida"]:
            venezuela.agregarProvincia(Provincia(nombre))

        # --- Guyana ---
        for nombre in ["Demerara-Mahaica", "Essequibo Islands-West Demerara",
                        "Berbice Oriental-Corentyne", "Pomeroon-Supenaam"]:
            guyana.agregarProvincia(Provincia(nombre))

        # --- Surinam ---
        for nombre in ["Paramaribo", "Wanica", "Nickerie", "Sipaliwini"]:
            surinam.agregarProvincia(Provincia(nombre))

        # --- Brasil (estados principales) ---
        for nombre in ["São Paulo", "Río de Janeiro", "Minas Gerais",
                        "Bahía", "Paraná", "Rio Grande do Sul",
                        "Pernambuco", "Ceará", "Amazonas", "Santa Catarina"]:
            brasil.agregarProvincia(Provincia(nombre))

        # --- Ecuador ---
        for nombre in ["Pichincha", "Guayas", "Azuay", "Manabí",
                        "Tungurahua", "El Oro", "Loja"]:
            ecuador.agregarProvincia(Provincia(nombre))

        # --- Perú (departamentos principales) ---
        for nombre in ["Lima", "Arequipa", "Cusco", "La Libertad",
                        "Piura", "Junín", "Lambayeque", "Loreto",
                        "Cajamarca", "Puno"]:
            peru.agregarProvincia(Provincia(nombre))

        # --- Bolivia (departamentos) ---
        for nombre in ["La Paz", "Santa Cruz", "Cochabamba", "Potosí",
                        "Chuquisaca", "Oruro", "Tarija", "Beni",
                        "Pando"]:
            bolivia.agregarProvincia(Provincia(nombre))

        # --- Paraguay ---
        for nombre in ["Asunción", "Central", "Alto Paraná",
                        "Itapúa", "Caaguazú", "San Pedro"]:
            paraguay.agregarProvincia(Provincia(nombre))

        # --- Chile (regiones principales) ---
        for nombre in ["Región Metropolitana", "Valparaíso", "Biobío",
                        "Maule", "La Araucanía", "Los Lagos",
                        "O'Higgins", "Coquimbo", "Antofagasta",
                        "Atacama"]:
            chile.agregarProvincia(Provincia(nombre))

        # --- Argentina (provincias) ---
        for nombre in ["Buenos Aires", "Córdoba", "Santa Fe",
                        "Mendoza", "Tucumán", "Entre Ríos",
                        "Salta", "Misiones", "Chaco", "Corrientes",
                        "Santiago del Estero", "San Juan", "Jujuy",
                        "Río Negro", "Neuquén", "Formosa",
                        "Chubut", "San Luis", "Catamarca",
                        "La Rioja", "La Pampa", "Santa Cruz",
                        "Tierra del Fuego"]:
            argentina.agregarProvincia(Provincia(nombre))

        # --- Uruguay (departamentos principales) ---
        for nombre in ["Montevideo", "Canelones", "Maldonado",
                        "Salto", "Paysandú", "Colonia",
                        "Rivera", "Cerro Largo", "Rocha"]:
            uruguay.agregarProvincia(Provincia(nombre))

        # ============================
        # LIMÍTROFES DE AMÉRICA
        # ============================

        # Canadá - Estados Unidos
        canada.agregarLimitrofe(estadosUnidos)
        estadosUnidos.agregarLimitrofe(canada)

        # Estados Unidos - México
        estadosUnidos.agregarLimitrofe(mexico)
        mexico.agregarLimitrofe(estadosUnidos)

        # México - Guatemala, Belice
        mexico.agregarLimitrofe(guatemala)
        mexico.agregarLimitrofe(belice)
        guatemala.agregarLimitrofe(mexico)
        belice.agregarLimitrofe(mexico)

        # Guatemala - Belice, Honduras, El Salvador
        guatemala.agregarLimitrofe(belice)
        guatemala.agregarLimitrofe(honduras)
        guatemala.agregarLimitrofe(elSalvador)
        belice.agregarLimitrofe(guatemala)
        honduras.agregarLimitrofe(guatemala)
        elSalvador.agregarLimitrofe(guatemala)

        # Honduras - El Salvador, Nicaragua
        honduras.agregarLimitrofe(elSalvador)
        honduras.agregarLimitrofe(nicaragua)
        elSalvador.agregarLimitrofe(honduras)
        nicaragua.agregarLimitrofe(honduras)

        # Nicaragua - Costa Rica
        nicaragua.agregarLimitrofe(costaRica)
        costaRica.agregarLimitrofe(nicaragua)

        # Costa Rica - Panamá
        costaRica.agregarLimitrofe(panama)
        panama.agregarLimitrofe(costaRica)

        # Panamá - Colombia
        panama.agregarLimitrofe(colombia)
        colombia.agregarLimitrofe(panama)

        # Haití - República Dominicana (comparten isla)
        haiti.agregarLimitrofe(republicaDominicana)
        republicaDominicana.agregarLimitrofe(haiti)

        # Colombia - Venezuela, Brasil, Perú, Ecuador
        colombia.agregarLimitrofe(venezuela)
        colombia.agregarLimitrofe(brasil)
        colombia.agregarLimitrofe(peru)
        colombia.agregarLimitrofe(ecuador)
        venezuela.agregarLimitrofe(colombia)
        brasil.agregarLimitrofe(colombia)
        peru.agregarLimitrofe(colombia)
        ecuador.agregarLimitrofe(colombia)

        # Venezuela - Brasil, Guyana
        venezuela.agregarLimitrofe(brasil)
        venezuela.agregarLimitrofe(guyana)
        brasil.agregarLimitrofe(venezuela)
        guyana.agregarLimitrofe(venezuela)

        # Guyana - Surinam, Brasil
        guyana.agregarLimitrofe(surinam)
        guyana.agregarLimitrofe(brasil)
        surinam.agregarLimitrofe(guyana)
        brasil.agregarLimitrofe(guyana)

        # Surinam - Brasil
        surinam.agregarLimitrofe(brasil)
        brasil.agregarLimitrofe(surinam)

        # Brasil - Perú, Bolivia, Paraguay, Argentina, Uruguay
        brasil.agregarLimitrofe(peru)
        brasil.agregarLimitrofe(bolivia)
        brasil.agregarLimitrofe(paraguay)
        brasil.agregarLimitrofe(argentina)
        brasil.agregarLimitrofe(uruguay)
        peru.agregarLimitrofe(brasil)
        bolivia.agregarLimitrofe(brasil)
        paraguay.agregarLimitrofe(brasil)
        argentina.agregarLimitrofe(brasil)
        uruguay.agregarLimitrofe(brasil)

        # Ecuador - Perú
        ecuador.agregarLimitrofe(peru)
        peru.agregarLimitrofe(ecuador)

        # Perú - Bolivia, Chile
        peru.agregarLimitrofe(bolivia)
        peru.agregarLimitrofe(chile)
        bolivia.agregarLimitrofe(peru)
        chile.agregarLimitrofe(peru)

        # Bolivia - Paraguay, Argentina, Chile
        bolivia.agregarLimitrofe(paraguay)
        bolivia.agregarLimitrofe(argentina)
        bolivia.agregarLimitrofe(chile)
        paraguay.agregarLimitrofe(bolivia)
        argentina.agregarLimitrofe(bolivia)
        chile.agregarLimitrofe(bolivia)

        # Paraguay - Argentina
        paraguay.agregarLimitrofe(argentina)
        argentina.agregarLimitrofe(paraguay)

        # Chile - Argentina
        chile.agregarLimitrofe(argentina)
        argentina.agregarLimitrofe(chile)

        # Argentina - Uruguay
        argentina.agregarLimitrofe(uruguay)
        uruguay.agregarLimitrofe(argentina)

        # --- Vincular países a América ---
        america.agregarPais(canada)
        america.agregarPais(estadosUnidos)
        america.agregarPais(mexico)
        america.agregarPais(guatemala)
        america.agregarPais(belice)
        america.agregarPais(honduras)
        america.agregarPais(elSalvador)
        america.agregarPais(nicaragua)
        america.agregarPais(costaRica)
        america.agregarPais(panama)
        america.agregarPais(cuba)
        america.agregarPais(haiti)
        america.agregarPais(republicaDominicana)
        america.agregarPais(jamaica)
        america.agregarPais(trinidadYTobago)
        america.agregarPais(colombia)
        america.agregarPais(venezuela)
        america.agregarPais(guyana)
        america.agregarPais(surinam)
        america.agregarPais(brasil)
        america.agregarPais(ecuador)
        america.agregarPais(peru)
        america.agregarPais(bolivia)
        america.agregarPais(paraguay)
        america.agregarPais(chile)
        america.agregarPais(argentina)
        america.agregarPais(uruguay)

        # ============================
        # PAÍSES DE EUROPA
        # ============================

        espana = Pais("España", "Madrid", 505990)
        portugal = Pais("Portugal", "Lisboa", 92212)
        francia = Pais("Francia", "París", 643801)
        reinoUnido = Pais("Reino Unido", "Londres", 243610)
        irlanda = Pais("Irlanda", "Dublín", 70273)
        belgica = Pais("Bélgica", "Bruselas", 30528)
        paisesbajos = Pais("Países Bajos", "Ámsterdam", 41543)
        luxemburgo = Pais("Luxemburgo", "Luxemburgo", 2586)
        alemania = Pais("Alemania", "Berlín", 357022)
        suiza = Pais("Suiza", "Berna", 41285)
        austria = Pais("Austria", "Viena", 83879)
        italia = Pais("Italia", "Roma", 301340)
        noruega = Pais("Noruega", "Oslo", 323802)
        suecia = Pais("Suecia", "Estocolmo", 450295)
        finlandia = Pais("Finlandia", "Helsinki", 338424)
        dinamarca = Pais("Dinamarca", "Copenhague", 42924)
        islandia = Pais("Islandia", "Reikiavik", 103000)
        polonia = Pais("Polonia", "Varsovia", 312696)
        chequia = Pais("Chequia", "Praga", 78867)
        eslovaquia = Pais("Eslovaquia", "Bratislava", 49035)
        hungria = Pais("Hungría", "Budapest", 93028)
        rumania = Pais("Rumanía", "Bucarest", 238391)
        bulgaria = Pais("Bulgaria", "Sofía", 110879)
        grecia = Pais("Grecia", "Atenas", 131957)
        croacia = Pais("Croacia", "Zagreb", 56594)
        serbia = Pais("Serbia", "Belgrado", 88361)
        ucrania = Pais("Ucrania", "Kiev", 603500)
        bielorrusia = Pais("Bielorrusia", "Minsk", 207600)
        lituania = Pais("Lituania", "Vilna", 65300)
        letonia = Pais("Letonia", "Riga", 64559)
        estonia = Pais("Estonia", "Tallin", 45228)
        rusia = Pais("Rusia", "Moscú", 17098242)
        albania = Pais("Albania", "Tirana", 28748)
        macedoniaNorte = Pais("Macedonia del Norte", "Skopie", 25713)
        montenegro = Pais("Montenegro", "Podgorica", 13812)
        bosniaHerzegovina = Pais("Bosnia y Herzegovina", "Sarajevo", 51197)
        eslovenia = Pais("Eslovenia", "Liubliana", 20273)
        moldavia = Pais("Moldavia", "Chisináu", 33846)

        # ============================
        # PROVINCIAS / REGIONES DE EUROPA
        # ============================

        # --- España (comunidades autónomas principales) ---
        for nombre in ["Madrid", "Cataluña", "Andalucía", "Valencia",
                        "Galicia", "Castilla y León", "País Vasco",
                        "Castilla-La Mancha", "Canarias", "Aragón"]:
            espana.agregarProvincia(Provincia(nombre))

        # --- Portugal (distritos principales) ---
        for nombre in ["Lisboa", "Oporto", "Braga", "Setúbal",
                        "Aveiro", "Faro", "Coímbra"]:
            portugal.agregarProvincia(Provincia(nombre))

        # --- Francia (regiones principales) ---
        for nombre in ["Isla de Francia", "Provenza-Alpes-Costa Azul",
                        "Auvernia-Ródano-Alpes", "Occitania",
                        "Nueva Aquitania", "Hauts-de-France",
                        "Gran Este", "Bretaña", "Normandía",
                        "Países del Loira"]:
            francia.agregarProvincia(Provincia(nombre))

        # --- Reino Unido ---
        for nombre in ["Inglaterra", "Escocia", "Gales",
                        "Irlanda del Norte"]:
            reinoUnido.agregarProvincia(Provincia(nombre))

        # --- Irlanda ---
        for nombre in ["Leinster", "Munster", "Connacht", "Ulster"]:
            irlanda.agregarProvincia(Provincia(nombre))

        # --- Bélgica ---
        for nombre in ["Flandes", "Valonia", "Bruselas-Capital"]:
            belgica.agregarProvincia(Provincia(nombre))

        # --- Países Bajos (provincias principales) ---
        for nombre in ["Holanda Meridional", "Holanda Septentrional",
                        "Utrecht", "Brabante Septentrional",
                        "Güeldres", "Limburgo"]:
            paisesbajos.agregarProvincia(Provincia(nombre))

        # --- Luxemburgo ---
        for nombre in ["Luxemburgo", "Diekirch", "Grevenmacher"]:
            luxemburgo.agregarProvincia(Provincia(nombre))

        # --- Alemania (estados federados principales) ---
        for nombre in ["Baviera", "Renania del Norte-Westfalia",
                        "Baden-Wurtemberg", "Baja Sajonia", "Hesse",
                        "Sajonia", "Berlín", "Hamburgo",
                        "Renania-Palatinado", "Brandeburgo"]:
            alemania.agregarProvincia(Provincia(nombre))

        # --- Suiza (cantones principales) ---
        for nombre in ["Zúrich", "Berna", "Ginebra", "Vaud",
                        "Lucerna", "San Galo"]:
            suiza.agregarProvincia(Provincia(nombre))

        # --- Austria (estados federados) ---
        for nombre in ["Viena", "Baja Austria", "Alta Austria",
                        "Estiria", "Tirol", "Carintia",
                        "Salzburgo", "Vorarlberg", "Burgenland"]:
            austria.agregarProvincia(Provincia(nombre))

        # --- Italia (regiones principales) ---
        for nombre in ["Lombardía", "Lacio", "Campania", "Sicilia",
                        "Véneto", "Emilia-Romaña", "Piamonte",
                        "Toscana", "Cerdeña", "Calabria"]:
            italia.agregarProvincia(Provincia(nombre))

        # --- Noruega ---
        for nombre in ["Oslo", "Viken", "Vestland", "Rogaland",
                        "Trøndelag", "Nordland"]:
            noruega.agregarProvincia(Provincia(nombre))

        # --- Suecia ---
        for nombre in ["Estocolmo", "Västra Götaland", "Escania",
                        "Östergötland", "Uppsala", "Jönköping"]:
            suecia.agregarProvincia(Provincia(nombre))

        # --- Finlandia ---
        for nombre in ["Uusimaa", "Pirkanmaa", "Ostrobotnia del Norte",
                        "Finlandia Suroccidental", "Laponia"]:
            finlandia.agregarProvincia(Provincia(nombre))

        # --- Dinamarca ---
        for nombre in ["Capital", "Jutlandia Central", "Dinamarca Meridional",
                        "Jutlandia Septentrional", "Selandia"]:
            dinamarca.agregarProvincia(Provincia(nombre))

        # --- Islandia ---
        for nombre in ["Reikiavik", "Sur", "Noreste", "Noroeste",
                        "Este", "Vestfjörður"]:
            islandia.agregarProvincia(Provincia(nombre))

        # --- Polonia (voivodatos principales) ---
        for nombre in ["Mazovia", "Pequeña Polonia", "Gran Polonia",
                        "Baja Silesia", "Silesia", "Pomerania",
                        "Łódź", "Lublin"]:
            polonia.agregarProvincia(Provincia(nombre))

        # --- Chequia ---
        for nombre in ["Praga", "Moravia Meridional", "Bohemia Central",
                        "Moravia-Silesia", "Ústí nad Labem"]:
            chequia.agregarProvincia(Provincia(nombre))

        # --- Eslovaquia ---
        for nombre in ["Bratislava", "Košice", "Prešov", "Žilina",
                        "Banská Bystrica", "Nitra", "Trnava",
                        "Trenčín"]:
            eslovaquia.agregarProvincia(Provincia(nombre))

        # --- Hungría ---
        for nombre in ["Budapest", "Pest", "Borsod-Abaúj-Zemplén",
                        "Hajdú-Bihar", "Győr-Moson-Sopron", "Baranya"]:
            hungria.agregarProvincia(Provincia(nombre))

        # --- Rumanía ---
        for nombre in ["Bucarest", "Cluj", "Timiș", "Iași",
                        "Constanța", "Brașov", "Dolj"]:
            rumania.agregarProvincia(Provincia(nombre))

        # --- Bulgaria ---
        for nombre in ["Sofía", "Plovdiv", "Varna", "Burgas",
                        "Stara Zagora"]:
            bulgaria.agregarProvincia(Provincia(nombre))

        # --- Grecia ---
        for nombre in ["Ática", "Macedonia Central", "Tesalia",
                        "Creta", "Macedonia Occidental",
                        "Grecia Occidental"]:
            grecia.agregarProvincia(Provincia(nombre))

        # --- Croacia ---
        for nombre in ["Zagreb", "Split-Dalmacia", "Primorje-Gorski Kotar",
                        "Osijek-Baranja", "Istria"]:
            croacia.agregarProvincia(Provincia(nombre))

        # --- Serbia ---
        for nombre in ["Belgrado", "Vojvodina", "Šumadija",
                        "Nišava", "Podunavlje"]:
            serbia.agregarProvincia(Provincia(nombre))

        # --- Ucrania ---
        for nombre in ["Kiev", "Járkov", "Odesa", "Dnipropetrovsk",
                        "Donetsk", "Leópolis", "Zaporizhia"]:
            ucrania.agregarProvincia(Provincia(nombre))

        # --- Bielorrusia ---
        for nombre in ["Minsk", "Gómel", "Moguiliov", "Vítebsk",
                        "Grodno", "Brest"]:
            bielorrusia.agregarProvincia(Provincia(nombre))

        # --- Lituania ---
        for nombre in ["Vilna", "Kaunas", "Klaipėda", "Šiauliai",
                        "Panevėžys"]:
            lituania.agregarProvincia(Provincia(nombre))

        # --- Letonia ---
        for nombre in ["Riga", "Daugavpils", "Liepāja", "Jelgava",
                        "Jūrmala"]:
            letonia.agregarProvincia(Provincia(nombre))

        # --- Estonia ---
        for nombre in ["Harju", "Tartu", "Ida-Viru", "Pärnu",
                        "Lääne-Viru"]:
            estonia.agregarProvincia(Provincia(nombre))

        # --- Rusia (distritos/sujetos federales principales) ---
        for nombre in ["Moscú", "San Petersburgo", "Novosibirsk",
                        "Ekaterimburgo", "Kazán", "Rostov del Don",
                        "Krasnodar", "Samara", "Omsk", "Cheliábinsk"]:
            rusia.agregarProvincia(Provincia(nombre))

        # --- Albania ---
        for nombre in ["Tirana", "Durrës", "Vlorë", "Elbasan",
                        "Shkodër"]:
            albania.agregarProvincia(Provincia(nombre))

        # --- Macedonia del Norte ---
        for nombre in ["Skopie", "Bitola", "Kumanovo", "Prilep",
                        "Tetovo"]:
            macedoniaNorte.agregarProvincia(Provincia(nombre))

        # --- Montenegro ---
        for nombre in ["Podgorica", "Nikšić", "Herceg Novi",
                        "Bijelo Polje", "Bar"]:
            montenegro.agregarProvincia(Provincia(nombre))

        # --- Bosnia y Herzegovina ---
        for nombre in ["Federación de Bosnia y Herzegovina",
                        "República Srpska", "Distrito de Brčko"]:
            bosniaHerzegovina.agregarProvincia(Provincia(nombre))

        # --- Eslovenia ---
        for nombre in ["Liubliana", "Maribor", "Celje", "Kranj",
                        "Koper"]:
            eslovenia.agregarProvincia(Provincia(nombre))

        # --- Moldavia ---
        for nombre in ["Chisináu", "Bălți", "Gagauzia", "Transnistria",
                        "Cahul"]:
            moldavia.agregarProvincia(Provincia(nombre))

        # ============================
        # LIMÍTROFES DE EUROPA
        # ============================

        # España - Portugal, Francia
        espana.agregarLimitrofe(portugal)
        espana.agregarLimitrofe(francia)
        portugal.agregarLimitrofe(espana)
        francia.agregarLimitrofe(espana)

        # Francia - Bélgica, Luxemburgo, Alemania, Suiza, Italia
        francia.agregarLimitrofe(belgica)
        francia.agregarLimitrofe(luxemburgo)
        francia.agregarLimitrofe(alemania)
        francia.agregarLimitrofe(suiza)
        francia.agregarLimitrofe(italia)
        belgica.agregarLimitrofe(francia)
        luxemburgo.agregarLimitrofe(francia)
        alemania.agregarLimitrofe(francia)
        suiza.agregarLimitrofe(francia)
        italia.agregarLimitrofe(francia)

        # Bélgica - Países Bajos, Luxemburgo, Alemania
        belgica.agregarLimitrofe(paisesbajos)
        belgica.agregarLimitrofe(luxemburgo)
        belgica.agregarLimitrofe(alemania)
        paisesbajos.agregarLimitrofe(belgica)
        luxemburgo.agregarLimitrofe(belgica)
        alemania.agregarLimitrofe(belgica)

        # Países Bajos - Alemania
        paisesbajos.agregarLimitrofe(alemania)
        alemania.agregarLimitrofe(paisesbajos)

        # Luxemburgo - Alemania
        luxemburgo.agregarLimitrofe(alemania)
        alemania.agregarLimitrofe(luxemburgo)

        # Alemania - Suiza, Austria, Chequia, Polonia, Dinamarca
        alemania.agregarLimitrofe(suiza)
        alemania.agregarLimitrofe(austria)
        alemania.agregarLimitrofe(chequia)
        alemania.agregarLimitrofe(polonia)
        alemania.agregarLimitrofe(dinamarca)
        suiza.agregarLimitrofe(alemania)
        austria.agregarLimitrofe(alemania)
        chequia.agregarLimitrofe(alemania)
        polonia.agregarLimitrofe(alemania)
        dinamarca.agregarLimitrofe(alemania)

        # Suiza - Italia, Austria
        suiza.agregarLimitrofe(italia)
        suiza.agregarLimitrofe(austria)
        italia.agregarLimitrofe(suiza)
        austria.agregarLimitrofe(suiza)

        # Austria - Italia, Eslovenia, Hungría, Eslovaquia, Chequia
        austria.agregarLimitrofe(italia)
        austria.agregarLimitrofe(eslovenia)
        austria.agregarLimitrofe(hungria)
        austria.agregarLimitrofe(eslovaquia)
        austria.agregarLimitrofe(chequia)
        italia.agregarLimitrofe(austria)
        eslovenia.agregarLimitrofe(austria)
        hungria.agregarLimitrofe(austria)
        eslovaquia.agregarLimitrofe(austria)
        chequia.agregarLimitrofe(austria)

        # Italia - Eslovenia
        italia.agregarLimitrofe(eslovenia)
        eslovenia.agregarLimitrofe(italia)

        # Eslovenia - Hungría, Croacia
        eslovenia.agregarLimitrofe(hungria)
        eslovenia.agregarLimitrofe(croacia)
        hungria.agregarLimitrofe(eslovenia)
        croacia.agregarLimitrofe(eslovenia)

        # Hungría - Croacia, Serbia, Rumanía, Ucrania, Eslovaquia
        hungria.agregarLimitrofe(croacia)
        hungria.agregarLimitrofe(serbia)
        hungria.agregarLimitrofe(rumania)
        hungria.agregarLimitrofe(ucrania)
        hungria.agregarLimitrofe(eslovaquia)
        croacia.agregarLimitrofe(hungria)
        serbia.agregarLimitrofe(hungria)
        rumania.agregarLimitrofe(hungria)
        ucrania.agregarLimitrofe(hungria)
        eslovaquia.agregarLimitrofe(hungria)

        # Croacia - Bosnia y Herzegovina, Serbia, Montenegro
        croacia.agregarLimitrofe(bosniaHerzegovina)
        croacia.agregarLimitrofe(serbia)
        croacia.agregarLimitrofe(montenegro)
        bosniaHerzegovina.agregarLimitrofe(croacia)
        serbia.agregarLimitrofe(croacia)
        montenegro.agregarLimitrofe(croacia)

        # Bosnia y Herzegovina - Serbia, Montenegro
        bosniaHerzegovina.agregarLimitrofe(serbia)
        bosniaHerzegovina.agregarLimitrofe(montenegro)
        serbia.agregarLimitrofe(bosniaHerzegovina)
        montenegro.agregarLimitrofe(bosniaHerzegovina)

        # Serbia - Montenegro, Albania, Macedonia del Norte, Bulgaria, Rumanía, Kosovo (omitido)
        serbia.agregarLimitrofe(montenegro)
        serbia.agregarLimitrofe(albania)
        serbia.agregarLimitrofe(macedoniaNorte)
        serbia.agregarLimitrofe(bulgaria)
        serbia.agregarLimitrofe(rumania)
        montenegro.agregarLimitrofe(serbia)
        albania.agregarLimitrofe(serbia)
        macedoniaNorte.agregarLimitrofe(serbia)
        bulgaria.agregarLimitrofe(serbia)
        rumania.agregarLimitrofe(serbia)

        # Montenegro - Albania
        montenegro.agregarLimitrofe(albania)
        albania.agregarLimitrofe(montenegro)

        # Albania - Macedonia del Norte, Grecia
        albania.agregarLimitrofe(macedoniaNorte)
        albania.agregarLimitrofe(grecia)
        macedoniaNorte.agregarLimitrofe(albania)
        grecia.agregarLimitrofe(albania)

        # Macedonia del Norte - Grecia, Bulgaria
        macedoniaNorte.agregarLimitrofe(grecia)
        macedoniaNorte.agregarLimitrofe(bulgaria)
        grecia.agregarLimitrofe(macedoniaNorte)
        bulgaria.agregarLimitrofe(macedoniaNorte)

        # Grecia - Bulgaria
        grecia.agregarLimitrofe(bulgaria)
        bulgaria.agregarLimitrofe(grecia)

        # Bulgaria - Rumanía
        bulgaria.agregarLimitrofe(rumania)
        rumania.agregarLimitrofe(bulgaria)

        # Rumanía - Moldavia, Ucrania
        rumania.agregarLimitrofe(moldavia)
        rumania.agregarLimitrofe(ucrania)
        moldavia.agregarLimitrofe(rumania)
        ucrania.agregarLimitrofe(rumania)

        # Moldavia - Ucrania
        moldavia.agregarLimitrofe(ucrania)
        ucrania.agregarLimitrofe(moldavia)

        # Ucrania - Bielorrusia, Polonia, Eslovaquia, Rusia
        ucrania.agregarLimitrofe(bielorrusia)
        ucrania.agregarLimitrofe(polonia)
        ucrania.agregarLimitrofe(eslovaquia)
        ucrania.agregarLimitrofe(rusia)
        bielorrusia.agregarLimitrofe(ucrania)
        polonia.agregarLimitrofe(ucrania)
        eslovaquia.agregarLimitrofe(ucrania)
        rusia.agregarLimitrofe(ucrania)

        # Polonia - Chequia, Eslovaquia, Lituania, Bielorrusia, Rusia
        polonia.agregarLimitrofe(chequia)
        polonia.agregarLimitrofe(eslovaquia)
        polonia.agregarLimitrofe(lituania)
        polonia.agregarLimitrofe(bielorrusia)
        polonia.agregarLimitrofe(rusia)
        chequia.agregarLimitrofe(polonia)
        eslovaquia.agregarLimitrofe(polonia)
        lituania.agregarLimitrofe(polonia)
        bielorrusia.agregarLimitrofe(polonia)
        rusia.agregarLimitrofe(polonia)

        # Chequia - Eslovaquia
        chequia.agregarLimitrofe(eslovaquia)
        eslovaquia.agregarLimitrofe(chequia)

        # Bielorrusia - Lituania, Letonia, Rusia
        bielorrusia.agregarLimitrofe(lituania)
        bielorrusia.agregarLimitrofe(letonia)
        bielorrusia.agregarLimitrofe(rusia)
        lituania.agregarLimitrofe(bielorrusia)
        letonia.agregarLimitrofe(bielorrusia)
        rusia.agregarLimitrofe(bielorrusia)

        # Lituania - Letonia
        lituania.agregarLimitrofe(letonia)
        letonia.agregarLimitrofe(lituania)

        # Letonia - Estonia, Rusia
        letonia.agregarLimitrofe(estonia)
        letonia.agregarLimitrofe(rusia)
        estonia.agregarLimitrofe(letonia)
        rusia.agregarLimitrofe(letonia)

        # Estonia - Rusia
        estonia.agregarLimitrofe(rusia)
        rusia.agregarLimitrofe(estonia)

        # Finlandia - Suecia, Noruega, Rusia
        finlandia.agregarLimitrofe(suecia)
        finlandia.agregarLimitrofe(noruega)
        finlandia.agregarLimitrofe(rusia)
        suecia.agregarLimitrofe(finlandia)
        noruega.agregarLimitrofe(finlandia)
        rusia.agregarLimitrofe(finlandia)

        # Noruega - Suecia, Rusia
        noruega.agregarLimitrofe(suecia)
        noruega.agregarLimitrofe(rusia)
        suecia.agregarLimitrofe(noruega)
        rusia.agregarLimitrofe(noruega)

        # --- Vincular países a Europa ---
        europa.agregarPais(espana)
        europa.agregarPais(portugal)
        europa.agregarPais(francia)
        europa.agregarPais(reinoUnido)
        europa.agregarPais(irlanda)
        europa.agregarPais(belgica)
        europa.agregarPais(paisesbajos)
        europa.agregarPais(luxemburgo)
        europa.agregarPais(alemania)
        europa.agregarPais(suiza)
        europa.agregarPais(austria)
        europa.agregarPais(italia)
        europa.agregarPais(noruega)
        europa.agregarPais(suecia)
        europa.agregarPais(finlandia)
        europa.agregarPais(dinamarca)
        europa.agregarPais(islandia)
        europa.agregarPais(polonia)
        europa.agregarPais(chequia)
        europa.agregarPais(eslovaquia)
        europa.agregarPais(hungria)
        europa.agregarPais(rumania)
        europa.agregarPais(bulgaria)
        europa.agregarPais(grecia)
        europa.agregarPais(croacia)
        europa.agregarPais(serbia)
        europa.agregarPais(ucrania)
        europa.agregarPais(bielorrusia)
        europa.agregarPais(lituania)
        europa.agregarPais(letonia)
        europa.agregarPais(estonia)
        europa.agregarPais(rusia)
        europa.agregarPais(albania)
        europa.agregarPais(macedoniaNorte)
        europa.agregarPais(montenegro)
        europa.agregarPais(bosniaHerzegovina)
        europa.agregarPais(eslovenia)
        europa.agregarPais(moldavia)
