choko_len = int(input("Введите длину шоколадки : "))
choko_wid = int(input("Введите ширину шоколадки : "))
piece_count = int(input("Введите количество кусочнов : "))

if piece_count < choko_len * choko_wid and ((piece_count % choko_len == 0) or (piece_count % choko_wid == 0)):
    print('Можно отломить')
else:
    print('Отломить нельзя')
