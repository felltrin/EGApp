from ProcessGameState import ProcessGameState


def main():
    pgs = ProcessGameState()
    pgs.process_coord_boundary()
    pgs.process_inventory_classes()
    print("this is awesome")


if __name__ == '__main__':
    main()
