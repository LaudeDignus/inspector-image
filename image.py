import argparse
import model.image_info as image_info
import model.map_info as map_info
import model.gui_map
from style import GREEN,RESET
import model.steg_info as steg_info

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-map", help="Extract GPS from image")
    parser.add_argument("-steg", help="Reveal PGP key")
    parser.add_argument("--info", help="See the image")
    parser.add_argument("--gui", action="store_true", help="Run Graphic Interface Tkinter")

    args = parser.parse_args()

    if (args.map):
        print(f"{GREEN}📡 Analyse de l'image en cours :{RESET} {args.map}")
        map_info.extract_map(args.map)
    elif args.gui:
         model.gui_map.launch_gui()
    elif (args.steg):
        steg_info.stegano(args.steg)
    elif (args.info):
            image_info.info(args.info)

if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print("\n🛑 Interruption innatendu.")
