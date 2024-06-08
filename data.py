headers = {
    "Content-Type": "application/json"
}

new_user = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}


Kit = {
       "name": "Mi kit",
}


auth_token = {

    "Content-Type": "application/json",
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}

# Caso 1: El número permitido de caracteres es 1
kit_body_1 = {"name": "a"}

# Caso 2: El número permitido de caracteres es 511
kit_body_2 = {"name":"Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                     "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                     "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                     "abcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                     "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                     "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

# Caso 3: El número de caracteres es menor que la cantidad permitida (0)
kit_body_3 = {"name": ""}

# Caso 4: El número de caracteres es mayor que la cantidad permitida (512)
kit_body_4 = {"name":"Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
             # Generar más de 512 caracteres

# Caso 5: Se permiten caracteres especiales
kit_body_5 = {"name": "№%@"}

# Caso 6: Se permiten espacios
kit_body_6 = {"name": " A Aaa "}

# Caso 7: Se permiten números
kit_body_7 = {"name": "123"}

# Caso 8: El parámetro no se pasa en la solicitud
kit_body_8 = {}

# Caso 9: Se ha pasado un tipo de parámetro diferente (número)
kit_body_9 = {"name": 123}  # Pasando un número en lugar de una cadena



