from random import randint
from getpass import getpass


# TODO:  Arreglar passwords
class AtmOperate:
    """
    This class allows you to perform several tasks in a fictitious AMT
    """

    ACCOUNTLIST = {}

    @staticmethod
    def credentials() -> tuple[bool, str, str]:
        user = input("Enter your user id: ")
        try:
            password = getpass("Introduce tu contraseña: ")
        except ValueError:
            raise ValueError("Password must be an integer")

        if user + '_' + str(password) in AtmOperate.ACCOUNTLIST:
            log_status = True
            return log_status, user, password

    @staticmethod
    def openAccount() -> None:
        """
        This method creates an account and add it to the general database of accounts
        :return: None
        """
        newAccount = {}
        name_surname = input("Insert name and surname: ")
        accNumber = randint(1000000, 9999999)
        user_name = input("Insert you user id: ")
        try:
            password = int(getpass("Introduce tu contraseña: "))  # TODO: Arreglar esto
        except ValueError:
            raise ValueError("Please enter a number")
        id_user = user_name + '_' + str(password)
        newAccount["id"] = id_user
        newAccount["user_id"] = user_name
        newAccount["password"] = password
        newAccount["user_name"] = name_surname
        newAccount["account_number"] = accNumber
        newAccount["balance"] = 0
        print(f"Felicidades, su cuenta con numero {accNumber} a nombre de {name_surname} ha sido abierta\n")
        # Añadimos la cuenta al conjunto de cuentas
        AtmOperate.ACCOUNTLIST[newAccount['id']] = newAccount

    @staticmethod
    def topUp(user: str, password: int) -> None:
        """
        This Method allows you to top up on your account
        :return: None
        """
        id_user = user + "_" + str(password)

        try:
            topUp = int(input("Introduce la cantidad deseada: "))
        except ValueError:
            raise ValueError("Introduce una cantidad correcta")

        if topUp <= 0:
            raise Exception("Introduce una cantidad correcta")

        print("Cuenta localizada. Realizando el ingreso")
        AtmOperate.ACCOUNTLIST[id_user]["balance"] += topUp
        print("La operación se realizó con éxito")

    @staticmethod
    def withdraw(user: str, password: int) -> None:
        """
        This method allow you to withdraw money from your account
        :return: None
        """
        user_id = user + "_" + str(password)
        try:
            withdraw = int(input("Indique la cantidad a retirar: "))
        except ValueError:
            raise ValueError("Introduce una cantidad correcta")

        if withdraw <= 0:
            raise ValueError("Introduce una cantidad correcta")

        if AtmOperate.ACCOUNTLIST[user_id]['balance'] - withdraw < 0:
            raise Exception("La cantidad solicitada es mayor que la disponible")
        else:
            print(f"Procediendo a retirar {withdraw} de la cuenta")
            AtmOperate.ACCOUNTLIST[user_id]['balance'] -= withdraw
            print("La operación se realizó con éxito")

    @staticmethod
    def balance(user: str, password: int) -> None:
        """
        This method allows you to check your balance
        :return: None
        """
        user_id = user + '_' + str(password)
        print(f"Su saldo es de: {AtmOperate.ACCOUNTLIST[user_id]['balance']}")

    def operate(self) -> None:
        """
        This method creates the interaction with the ATM
        :return:
        """
        while True:
            try:
                action_initial = int(input("Introduzca 1 crear cuenta nueva o 2 para acceder a su cuenta o 3 para "
                                           "salir: "))
            except ValueError:
                raise ValueError("Por favor, introduzca una opción correcta")

            if action_initial == 1:
                self.openAccount()
            elif action_initial == 2:
                logging_result, user, password = self.credentials()
                if logging_result:
                    while True:
                        try:
                            action = int(input(
                                "Elige la accion a realizar:\n 1.Depositar dinero\n 2.Retirar dinero\n 3.Consultar "
                                "saldo\n"
                                "4.Salir\n"))
                        except ValueError:
                            raise ValueError("Por favor introduce uno de los números indicados")

                        if action == 1:
                            self.topUp(user, password)
                        elif action == 2:
                            self.withdraw(user, password)
                        elif action == 3:
                            self.balance(user, password)
                        elif action == 4:
                            print("Muchas gracias por su tiempo")
                            break
                        else:
                            raise Exception("Operacion incorrecta")
                else:
                    raise Exception("Incorrect user or password")
            elif action_initial == 3:
                print("Muchas gracias por su tiempo")
                break
            else:
                raise Exception("Por favor, introduzca una opción correcta")
