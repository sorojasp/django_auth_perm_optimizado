import bcrypt


class EncriptadorBcrypt():
    """clase que usa el paquete bcrypt para encriptar mensajes y compararlos con el original,
    pero no hace nongún tipo de desencriptación"""

    """podría aplicarse el patrón Singleton"""

    __salt:str="$2b$12$9sJCU11NAKqf3WcfXlLQmu"

    def __init__(self):
        pass

    def encriptar(self, password:str)->str:
        try:
            encriptado=bcrypt.hashpw(password.encode(), self.__salt.encode())
            return encriptado.decode("utf-8")
        except Exception as error:
            print(f'error en la encriptación: {error}')
            False

    def chequear_bcrypt(self, password:str, encriptado:str)->bool:
        """Si se presenta algún problema en entre los datos encriptadoss y los originales, 
        envía un diccionario con los datos del resultado del chequeo
        
        * encriptado= password encriptado que se quiere comparar
        * password= password ingresado por el usuario y que se quiere validar
        
        """
        try:
            return bcrypt.checkpw(password.encode(), encriptado.encode())
        except Exception as error:
            print(f'error en el chequeo: {error}')
            return {
                "resultado":"Error"
            }
