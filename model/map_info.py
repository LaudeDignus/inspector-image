
import exifread
from style import GREEN, RESET,BLUE 

def dms_to_decimal(dms, ref):
    deg = dms[0].num / dms[0].den
    min = dms[1].num / dms[1].den
    sec = dms[2].num / dms[2].den

    result = deg + (min / 60.0) + (sec / 3600.0)

    if ref in ['S', 'W']:
        result = -result

    return [round(result, 6),deg,min,sec]

def extract_map(image_path):
    with open(image_path, "rb") as f:
        tags = exifread.process_file(f)
    
    lat = tags.get("GPS GPSLatitude")
    lat_ref = tags.get("GPS GPSLatitudeRef")
    lon = tags.get("GPS GPSLongitude")
    lon_ref = tags.get("GPS GPSLongitudeRef")

    if lat and lon and lat_ref and lon_ref:
        latitude = dms_to_decimal(lat.values, lat_ref.printable)
        longitude = dms_to_decimal(lon.values, lon_ref.printable)

        print(f"Lat/Lon: ({latitude[0]} / {longitude[0]}) \n")

        gps_lat=f"{round(latitude[1])}° {round(latitude[2])}' {round(latitude[3],2)}\" {lat_ref}"
        gps_long=f"{round(longitude[1])}° {round(longitude[2])}' {round(longitude[3],2)}\" {lon_ref}"
        print(f"📍 GPS Latitude :{GREEN} {gps_lat} {RESET}")

        print(f"📍 GPS Latitude :{GREEN} {gps_long} {RESET}")

        open_map(latitude[0],longitude[0])

    else:
        print("❌ Aucune donnée GPS trouvée.")

def open_map(lat, lon):
    url = f"https://www.google.com/maps?q={lat},{lon}"
    print(f"🔗 Ouvre ce lien dans ton navigateur : {BLUE} {url} {RESET}")
