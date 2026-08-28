import datetime as dt 
import zoneinfo as z

city_timezones = {
    # Middle East
    ("Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Ras Al Khaimah", "Fujairah", "Umm Al Quwain"): "Asia/Dubai",
    ("Riyadh", "Mecca", "Medina", "Jeddah"): "Asia/Riyadh",
    ("Doha", "Al Rayyan"): "Asia/Qatar",
    ("Kuwait City", "Kuwait"): "Asia/Kuwait",
    ("Manama", "Bahrain"): "Asia/Bahrain",
    ("Muscat", "Salalah"): "Asia/Muscat",
    ("Sana'a", "Aden"): "Asia/Aden",
    ("Amman", "Zarqa"): "Asia/Amman",
    ("Beirut", "Tripoli"): "Asia/Beirut",
    ("Damascus", "Aleppo"): "Asia/Damascus",
    ("Baghdad", "Basra", "Mosul"): "Asia/Baghdad",
    ("Tehran", "Mashhad", "Isfahan"): "Asia/Tehran",
    ("Jerusalem", "Tel Aviv", "Haifa"): "Asia/Jerusalem",

    # South Asia
    ("Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad",
     "Ahmedabad", "Pune", "Jaipur", "Surat"): "Asia/Kolkata",
    ("Islamabad", "Karachi", "Lahore", "Peshawar"): "Asia/Karachi",
    ("Dhaka", "Chittagong"): "Asia/Dhaka",
    ("Kathmandu", "Pokhara"): "Asia/Kathmandu",
    ("Colombo", "Sri Jayawardenepura Kotte"): "Asia/Colombo",
    ("Malé", "Male"): "Indian/Maldives",

    # East Asia
    ("Tokyo", "Osaka", "Kyoto", "Yokohama", "Nagoya"): "Asia/Tokyo",
    ("Seoul", "Busan", "Incheon"): "Asia/Seoul",
    ("Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu",
     "Chongqing", "Hong Kong", "Macau"): "Asia/Shanghai",
    ("Taipei", "Kaohsiung"): "Asia/Taipei",
    ("Singapore",): "Asia/Singapore",
    ("Kuala Lumpur", "George Town", "Kuching"): "Asia/Kuala_Lumpur",
    ("Jakarta",): "Asia/Jakarta",
    ("Manila", "Quezon City", "Davao"): "Asia/Manila",
    ("Bangkok", "Chiang Mai"): "Asia/Bangkok",
    ("Hanoi", "Ho Chi Minh City"): "Asia/Ho_Chi_Minh",

    # Europe
    ("London", "Birmingham", "Manchester", "Liverpool", "Edinburgh"): "Europe/London",
    ("Paris", "Lyon", "Marseille", "Toulouse"): "Europe/Paris",
    ("Berlin", "Hamburg", "Munich", "Frankfurt", "Cologne"): "Europe/Berlin",
    ("Madrid", "Barcelona", "Valencia", "Seville"): "Europe/Madrid",
    ("Rome", "Milan", "Naples", "Turin"): "Europe/Rome",
    ("Amsterdam", "Rotterdam", "The Hague"): "Europe/Amsterdam",
    ("Brussels", "Antwerp"): "Europe/Brussels",
    ("Vienna", "Salzburg", "Graz"): "Europe/Vienna",
    ("Zurich", "Geneva", "Bern"): "Europe/Zurich",
    ("Stockholm", "Gothenburg", "Malmö"): "Europe/Stockholm",
    ("Oslo", "Bergen", "Trondheim"): "Europe/Oslo",
    ("Copenhagen", "Aarhus"): "Europe/Copenhagen",
    ("Helsinki", "Tampere"): "Europe/Helsinki",
    ("Athens", "Thessaloniki"): "Europe/Athens",
    ("Lisbon", "Porto"): "Europe/Lisbon",
    ("Dublin", "Cork"): "Europe/Dublin",
    ("Warsaw", "Kraków"): "Europe/Warsaw",
    ("Prague", "Brno"): "Europe/Prague",
    ("Budapest", "Debrecen"): "Europe/Budapest",
    ("Bucharest", "Cluj-Napoca"): "Europe/Bucharest",
    ("Sofia", "Plovdiv"): "Europe/Sofia",
    ("Kyiv", "Lviv", "Odesa"): "Europe/Kyiv",
    ("Moscow", "Saint Petersburg", "Kazan"): "Europe/Moscow",
    ("Istanbul", "Ankara", "Izmir"): "Europe/Istanbul",

    # North America
    ("New York", "Boston", "Washington", "Philadelphia", "Miami",
     "Atlanta", "Detroit"): "America/New_York",
    ("Chicago", "Houston", "Dallas", "Austin", "New Orleans"): "America/Chicago",
    ("Denver", "Albuquerque", "Colorado Springs"): "America/Denver",
    ("Phoenix", "Tucson"): "America/Phoenix",
    ("Los Angeles", "San Francisco", "San Diego", "Las Vegas", "Seattle",
     "Portland"): "America/Los_Angeles",
    ("Anchorage", "Fairbanks"): "America/Anchorage",
    ("Toronto", "Ottawa", "Montreal", "Quebec City"): "America/Toronto",
    ("Vancouver", "Victoria"): "America/Vancouver",
    ("Mexico City", "Guadalajara", "Monterrey"): "America/Mexico_City",

    # South America
    ("São Paulo", "Rio de Janeiro", "Brasília", "Belo Horizonte"): "America/Sao_Paulo",
    ("Buenos Aires", "Córdoba", "Rosario"): "America/Argentina/Buenos_Aires",
    ("Santiago", "Valparaíso"): "America/Santiago",
    ("Lima", "Arequipa"): "America/Lima",
    ("Bogotá", "Medellín", "Cali"): "America/Bogota",
    ("Caracas", "Maracaibo"): "America/Caracas",
    ("Quito", "Guayaquil"): "America/Guayaquil",

    # Africa
    ("Cairo", "Alexandria", "Giza"): "Africa/Cairo",
    ("Johannesburg", "Cape Town", "Durban", "Pretoria"): "Africa/Johannesburg",
    ("Nairobi", "Mombasa"): "Africa/Nairobi",
    ("Lagos", "Abuja", "Kano"): "Africa/Lagos",
    ("Accra", "Kumasi"): "Africa/Accra",
    ("Casablanca", "Rabat", "Marrakesh"): "Africa/Casablanca",
    ("Algiers", "Oran"): "Africa/Algiers",
    ("Tunis", "Sfax"): "Africa/Tunis",
    ("Addis Ababa", "Dire Dawa"): "Africa/Addis_Ababa",
    ("Dar Es Salaam", "Dodoma"): "Africa/Dar_es_Salaam",
    ("Khartoum", "Omdurman"): "Africa/Khartoum",

    # Australia / Oceania
    ("Sydney", "Melbourne", "Canberra", "Hobart"): "Australia/Sydney",
    ("Brisbane", "Gold Coast", "Cairns"): "Australia/Brisbane",
    ("Adelaide",): "Australia/Adelaide",
    ("Perth",): "Australia/Perth",
    ("Darwin",): "Australia/Darwin",
    ("Auckland", "Wellington", "Hamilton"): "Pacific/Auckland",
    ("Honolulu",): "Pacific/Honolulu",
}

def info(city):
    key = None
    for cities in city_timezones.keys():
        if city in cities:
            key = cities
            break
    if not key: 
        return f"{city.capitalize()} does not exist"
    t = dt.datetime.now((z.ZoneInfo(f"{city_timezones[key]}")))
    return t.strftime("%I:%M:%S %p , %#d %B %Y")

while True:
    choice = int(input("1.Time\n"))
    if choice == 1:
        city = input("Enter City").strip().capitalize()
        print(info(city))
        break
