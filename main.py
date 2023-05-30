"""
Important resources:
https://pandas.pydata.org/docs/index.html
https://numpy.org/doc/stable/index.html
"""
from ProcessGameState import ProcessGameState


def main():
    pgs = ProcessGameState()
    pgs.process_coord_boundary()
    print("this is awesome")
    pgs.process_inventory_classes()


if __name__ == '__main__':
    main()
