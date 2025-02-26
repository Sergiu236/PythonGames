from domain import Land
from service import Service
from ui import UI

def main():
    service = Service(Land)
    ui = UI(service)
    ui.ui()

main()
