"""
Importa las bibliotecas necesarias, como cv2 (OpenCV) y numpy
Define una función llamada display_text que devuelve un texto (Izquierda o Derecha) según el color detectado.
Inicializa la cámara y establece su tamaño de captura.
Define valores iniciales para los límites de color en formato HSV (matiz, saturación y valor) para los colores rojo y verde. También se define un umbral de área para los contornos detectados.
Crea una ventana llamada Trackbars para ajustar los valores de detección de color utilizando barras deslizadoras.
Entra en un bucle infinito que realiza las siguientes acciones:
a. Lee un fotograma de la cámara.
b. Convierte el fotograma de BGR a HSV para facilitar la detección de colores.
c. Obtiene los valores actuales de las barras deslizadoras.
d. Define rangos de color para el rojo y el verde en función de los valores de las barras deslizadoras.
e. Crea máscaras para los colores rojo y verde utilizando los rangos definidos.
f. Aplica operaciones morfológicas para eliminar el ruido de las máscaras.
g. Encuentra los contornos de objetos rojos y verdes en las máscaras.
h. Calcula la distancia de cada contorno al centro de la imagen.
i. Determina el objeto más cercano y su color.
j. Dibuja un rectángulo alrededor del objeto más cercano con su color correspondiente en el fotograma.
k. Muestra el fotograma en una ventana llamada Detected Colors.
l. Sale del bucle si se presiona la tecla 'q'.
Finalmente, libera la cámara y cierra todas las ventanas abiertas cuando se sale del bucle."""


import cv2
import numpy as np

def display_text(color):
    if color == "red":
        return "Izquierda"
    elif color == "green":
        return "Derecha"
    else:
        return ""

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Establecer el tamaño de la ventana de captura
cap.set(3, 640) # Ancho
cap.set(4, 480) # Altura

# Definir los valores iniciales para los barras deslizadoras
red_hue_lower1 = 0
red_hue_upper1 = 5
red_hue_lower2 = 175
red_hue_upper2 = 180
red_saturation_lower = 100
red_saturation_upper = 255
red_value_lower = 100
red_value_upper = 255
green_hue_lower = 40
green_hue_upper = 80
green_saturation_lower = 100
green_saturation_upper = 255
green_value_lower = 100
green_value_upper = 255
area_threshold = 800

# Función para actualizar los valores de las barras deslizadoras
def update_values(x):
    pass

# Crear una ventana para ajustar los valores de detección de color
cv2.namedWindow("Trackbars")
cv2.createTrackbar("Red - Hue Lower 1", "Trackbars", red_hue_lower1, 180, update_values)
cv2.createTrackbar("Red - Hue Upper 1", "Trackbars", red_hue_upper1, 180, update_values)
cv2.createTrackbar("Red - Hue Lower 2", "Trackbars", red_hue_lower2, 180, update_values)
cv2.createTrackbar("Red - Hue Upper 2", "Trackbars", red_hue_upper2, 180, update_values)
cv2.createTrackbar("Red - Saturation Lower", "Trackbars", red_saturation_lower, 255, update_values)
cv2.createTrackbar("Red - Saturation Upper", "Trackbars", red_saturation_upper, 255, update_values)
cv2.createTrackbar("Red - Value Lower", "Trackbars", red_value_lower, 255, update_values)
cv2.createTrackbar("Red - Value Upper", "Trackbars", red_value_upper, 255, update_values)
cv2.createTrackbar("Green - Hue Lower", "Trackbars", green_hue_lower, 180, update_values)
cv2.createTrackbar("Green - Hue Upper", "Trackbars", green_hue_upper, 180, update_values)
cv2.createTrackbar("Green - Saturation Lower", "Trackbars", green_saturation_lower, 255, update_values)
cv2.createTrackbar("Green - Saturation Upper", "Trackbars", green_saturation_upper, 255, update_values)
cv2.createTrackbar("Green - Value Lower", "Trackbars", green_value_lower, 255, update_values)
cv2.createTrackbar("Green - Value Upper", "Trackbars", green_value_upper, 255, update_values)

while True:
    # Leer el fotograma de la cámara
    ret, frame = cap.read()

    if not ret:
        break

    # Convertir el fotograma de BGR a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Obtener los valores actuales de las barras deslizadoras
    red_hue_lower1 = cv2.getTrackbarPos("Red - Hue Lower 1", "Trackbars")
    red_hue_upper1 = cv2.getTrackbarPos("Red - Hue Upper 1", "Trackbars")
    red_hue_lower2 = cv2.getTrackbarPos("Red - Hue Lower 2", "Trackbars")
    red_hue_upper2 = cv2.getTrackbarPos("Red - Hue Upper 2", "Trackbars")
    red_saturation_lower = cv2.getTrackbarPos("Red - Saturation Lower", "Trackbars")
    red_saturation_upper = cv2.getTrackbarPos("Red - Saturation Upper", "Trackbars")
    red_value_lower = cv2.getTrackbarPos("Red - Value Lower", "Trackbars")
    red_value_upper = cv2.getTrackbarPos("Red - Value Upper", "Trackbars")
    green_hue_lower = cv2.getTrackbarPos("Green - Hue Lower", "Trackbars")
    green_hue_upper = cv2.getTrackbarPos("Green - Hue Upper", "Trackbars")
    green_saturation_lower = cv2.getTrackbarPos("Green - Saturation Lower", "Trackbars")
    green_saturation_upper = cv2.getTrackbarPos("Green - Saturation Upper", "Trackbars")
    green_value_lower = cv2.getTrackbarPos("Green - Value Lower", "Trackbars")
    green_value_upper = cv2.getTrackbarPos("Green - Value Upper", "Trackbars")

    # Definir rangos de color para el rojo
    lower_red1 = np.array([red_hue_lower1, red_saturation_lower, red_value_lower])
    upper_red1 = np.array([red_hue_upper1, red_saturation_upper, red_value_upper])
    lower_red2 = np.array([red_hue_lower2, red_saturation_lower, red_value_lower])
    upper_red2 = np.array([red_hue_upper2, red_saturation_upper, red_value_upper])

    # Definir rangos de color para el verde
    lower_green = np.array([green_hue_lower, green_saturation_lower, green_value_lower])
    upper_green = np.array([green_hue_upper, green_saturation_upper, green_value_upper])

    # Crear las máscaras para el rojo y el verde
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Realizar operaciones morfológicas para eliminar ruido
    kernel = np.ones((5, 5), np.uint8)
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_CLOSE, kernel)
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_CLOSE, kernel)

    # Encontrar contornos de objetos verdes y rojos
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Encontrar centro de la imagen
    center_x, center_y = frame.shape[1] // 2, frame.shape[0] // 2

    # Calcular distancia de cada contorno al centro de la imagen
    def calculate_distance(contour):
        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        return np.sqrt((center_x - cX)*2 + (center_y - cY)*2)

    # Encontrar el objeto más cercano y su color
    min_distance = float('inf')
    closest_color = None

    for contour in contours_red:
        area = cv2.contourArea(contour)
        if area > area_threshold:
            distance = calculate_distance(contour)
            if distance < min_distance:
                min_distance = distance
                closest_color = "red"

    for contour in contours_green:
        area = cv2.contourArea(contour)
        if area > area_threshold:
            distance = calculate_distance(contour)
            if distance < min_distance:
                min_distance = distance
                closest_color = "green"

    # Dibujar contorno del objeto más cercano con su color correspondiente
    if closest_color == "red":
        for contour in contours_red:
            area = cv2.contourArea(contour)
            if area > area_threshold:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                text = display_text("red")
                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    elif closest_color == "green":
        for contour in contours_green:
            area = cv2.contourArea(contour)
            if area > area_threshold:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = display_text("green")
                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Mostrar la imagen en la ventana
    cv2.imshow("Detected Colors", frame)

    # Salir del bucle al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas abiertas
cap.release()
cv2.destroyAllWindows()
