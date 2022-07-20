from sqlite import BasePixhos

if __name__ == "__main__":
    bp = BasePixhos()
    # bp.insert_pixhos("Gilberto", "Santa Branca", "CPF", "463.380.088-40")
    # bp.delete_pixhos_by_id(1)
    # print(bp.pixhos)
    # print(bp.insert_config('Fax', 7, 4))
    print(bp.config)
    bp.update_config("ABC", 5,5)
    print(bp.config)