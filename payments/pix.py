import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self):
        #criar o pagamento na instituição financeira
        banck_payment_id = str(uuid.uuid4())

        # copia e cola o código do qr code
        hash_payment = f'hash_payment_{banck_payment_id}'

        # qr code
        img = qrcode.make(hash_payment)

        # salvar a imagem como png
        img.save(f'static/img/qr_code_payment_{banck_payment_id}.png')
        
        return{"banck_payment_id": banck_payment_id,
               "qr_code_path": f"qr_code_payment_{banck_payment_id}"}