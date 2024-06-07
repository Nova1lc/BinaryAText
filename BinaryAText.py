def binario_a_texto(texto_binario):
    try:
        segmentos = texto_binario.split()
        caracteres = [chr(int(segmento, 2)) for segmento in segmentos]
        texto = ''.join(caracteres)
        return texto
    except ValueError:
        raise FormatException("La entrada no es un texto binario válido")

class FormatException(Exception):
    pass

def main():
    continuar = '1'
    while continuar == '1':
        texto_binario = input("Introduce el texto binario a convertir a texto: ")
        try:
            texto = binario_a_texto(texto_binario)
            print(f"El texto es: {texto}")
        except FormatException as e:
            print(f"Error: {e}")
        continuar = input("Si deseas introducir otro texto binario, introduce el numero 1: ")
        print()  # Para agregar un salto de línea después de la lectura de la tecla

if __name__ == "__main__":
    main()
