
# Taille des nombres premiers P et Q
PRIME_SIZE_P = 500
MIN_PRIME_SIZE_Q = 451
AMPL_PRIME_SIZE_Q = 20


# Valeurs de fonctionement de RSA
e = 65537
p = 1
q = 1
n_local = 1
n_distant = 1
d = 0


# Port de communication
PORT_NUMBER = 8790


# Affichage du ViteVite
VITEVITE = ["                     ______     ",
            "    .----.   @   @  / Vite `--. ",
            "   / .-\"-.`.  \\v/  <    Vite ! )",
            "   | | '\\ \\ \\_/ )   '---------' ",
            " ,-\\ `-.' /.'  /                ",
            "'---`----'----'                 "]
VITEVITE_DELAY = 0.09



ETX = ("" + chr(3)).encode('UTF-8') #End of Text
EOT = ("" + chr(4)).encode('UTF-8') #End of Transmission