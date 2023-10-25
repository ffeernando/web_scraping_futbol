# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class CSVPipeline:
    def open_spider(self, spider):
        self.file = open('resultados.csv', 'w', newline='')
        self.filenames = ['equipo_local', 
            'equipo_visitante', 
            'gol_local', 
            'gol_visitante', 
            'posesion_local', 
            'posesion_visitante',
            'porcentaje_pases_local', 
            'porcentaje_pases_visitante', 
            'porcentaje_disparos_local', 
            'porcentaje_disparos_visitante', 
            'porcentaje_salvadas_local', 
            'porcentaje_salvadas_visitante',
            'faltas_cometidas_local',
            'faltas_cometidas_visitante',
            'corners_local',
            'corners_visitante',
            'pases_cruzados_local',
            'pases_cruzados_visitante',
            'toques_local',
            'toques_visitante',
            'derribos_local',
            'derribos_visitante',
            'intercepciones_local',
            'intercepciones_visitante',
            'duelos_aereos_local',
            'duelos_aereos_visitante',
            'despejes_local',
            'despejes_visitante',
            'offsides_local',
            'offsides_visitante',
            'saques_de_meta_local',
            'saques_de_meta_visitante',
            'saques_de_banda_local',
            'saques_de_banda_visitante',
            'pelotazos_local',
            'pelotazos_visitante']
        self.writer = csv.DictWriter(self.file, fieldnames=self.filenames)

        self.writer.writeheader()
    
    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        fila = {
            'equipo_local': item.get('equipo_local'),
            'equipo_visitante': item.get('equipo_visitante'),
            'gol_local': item.get('gol_local'),
            'gol_visitante': item.get('gol_visitante'),
            'posesion_local': item.get('posesion_local'),
            'posesion_visitante': item.get('posesion_visitante'),
            'porcentaje_pases_local': item.get('porcentaje_pases_local'),
            'porcentaje_pases_visitante': item.get('porcentaje_pases_visitante'),
            'porcentaje_disparos_local': item.get('porcentaje_disparos_local'),
            'porcentaje_disparos_visitante': item.get('porcentaje_disparos_visitante'),
            'porcentaje_salvadas_local': item.get('porcentaje_salvadas_local'),
            'porcentaje_salvadas_visitante': item.get('porcentaje_salvadas_visitante'),
            'faltas_cometidas_local': item.get('faltas_cometidas_local'),
            'faltas_cometidas_visitante': item.get('faltas_cometidas_visitante'),
            'corners_local': item.get('corners_local'),
            'corners_visitante': item.get('corners_visitante'),
            'pases_cruzados_local': item.get('pases_cruzados_local'),
            'pases_cruzados_visitante': item.get('pases_cruzados_visitante'),
            'toques_local': item.get('toques_local'),
            'toques_visitante': item.get('toques_visitante'),
            'derribos_local': item.get('derribos_local'),
            'derribos_visitante': item.get('derribos_visitante'),
            'intercepciones_local': item.get('intercepciones_local'),
            'intercepciones_visitante': item.get('intercepciones_visitante'),
            'duelos_aereos_local': item.get('duelos_aereos_local'),
            'duelos_aereos_visitante': item.get('duelos_aereos_visitante'),
            'despejes_local': item.get('despejes_local'),
            'despejes_visitante': item.get('despejes_visitante'),
            'offsides_local': item.get('offsides_local'),
            'offsides_visitante': item.get('offsides_visitante'),
            'saques_de_meta_local': item.get('saques_de_meta_local'),
            'saques_de_meta_visitante': item.get('saques_de_meta_visitante'),
            'saques_de_banda_local': item.get('saques_de_banda_local'),
            'saques_de_banda_visitante': item.get('saques_de_banda_visitante'),
            'pelotazos_local': item.get('pelotazos_local'),
            'pelotazos_visitante': item.get('pelotazos_visitante')
        }
        self.writer.writerow(fila)

        return item
