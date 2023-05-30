from ProcessGameState import ProcessGameState


def main():
    pgs = ProcessGameState()
    pgs.process_coord_boundary()
    pgs.process_inventory_classes()


if __name__ == '__main__':
    main()
