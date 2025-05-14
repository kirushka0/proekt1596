import qrcode

data_list = ["Проект1", "Проект2", "Проект3", "ПРОЕКТ4"]
for idx, data in enumerate(data_list, start=1):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(f'static/qrcodes/qr_{idx}.png')