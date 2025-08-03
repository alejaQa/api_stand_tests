import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


def post_products_kits(body):
    respuestaSolicitudKit = requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                                          json=body,
                                          headers=data.headers)
    return respuestaSolicitudKit


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# print("\n USUARIOS ---------------------")
# response = post_new_user(data.user_body)
# print(response.status_code)
# print(response.json())
#
#
# print("\n KITS ---------------------")
# # Metodo para consultar los kits
# respuestaKits = post_products_kits(data.product_ids)
# print(respuestaKits.status_code)
# print(respuestaKits.json())
