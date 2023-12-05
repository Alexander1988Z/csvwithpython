import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        # vamos a leer la primera fila del archivo csv y a imprimirla en consola
        header = next(reader)
        # vamos a crear una lista para guartar los futuros diccionarios de datos
        data=[]

        # vamos a crear un for para leer e imprimir fila a fila el archivo csv
        for row in reader:
            iterable = zip(header, row)                     
            country_dict = {key: value for key, value in iterable }
            data.append(country_dict)
        return data
 
if __name__ == '__main__':
    data = read_csv('./App/data.csv')
    #print(data)