import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('./App/data.csv')

    # En esta seccion hay distintos filtros para que la informacion que se muestre sea facil de ver, aplica solo para graficos tipo torta

    data = list(filter(lambda index: index['Continent'] == 'North America',data))

    data = list(sorted(data, key=lambda index:index['World Population Percentage'], reverse=True))

    data = data[:10]

    # En esta seccion se ejecuta el codigo para grafico de torta para la poblacion mundial

    print(data)

    allpopulation = {index['Country/Territory']:index['World Population Percentage'] for index in data}
    names = allpopulation.keys()
    percen = allpopulation.values()

    charts.generate_pie_chart(names,percen)

    '''
    # En esta seccion se ejecuta el codigo para grafico de barras de la poblacion historica por pais

    country = input("Ingresa el nombre del país: ")

    result = utils.population_by_country(data,country)

    if len(result)>0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels,values)
    '''

if __name__ == '__main__':
    run()