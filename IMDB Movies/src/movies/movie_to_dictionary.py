from abc import ABC, abstractmethod
import csv
import json
#from movie_fetcher import list
# Storing the movie information
# in a csv file

# Uso del principio de Single Responsibility al hacer otro módulo dedicado a la conversión de los datos
def store_csv_movie_data(list):
    fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    with open("movie_results.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for movie in list:
            writer.writerow({**movie})
    
class Exporter(ABC):
    @abstractmethod
    def save(list):
        pass
    
class csvExporter(Exporter):
    def save(list):
        fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
        with open("movie_results.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for movie in list:
                writer.writerow({**movie})
                
class jsonExporter(Exporter):
    def save(list):
        json_object = json.dumps(list, indent = 8)
        with open("movie_results.json", "w") as file:
            file.write(json_object)
            
class SimpleExporterFactory:
    
    def createExporter(exporterType: str) -> Exporter:
        exporter: Exporter = None
        
        if exporterType == "csv":
            exporter = csvExporter()
        elif exporterType == "json":
            exporter = jsonExporter()
        else:
            raise Exception("Exporter type not supported")
        
        return exporter
    
