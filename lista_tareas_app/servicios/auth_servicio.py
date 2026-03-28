class AuthServicio:
    
    # Servicio de autenticación (login)
    

    def validar(self, user, password):
        # Validación simple (puede cambiar a base de datos)
        return user == "admin" and password == "1234"