# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapingFutbolItem(scrapy.Item):
    equipo_local = scrapy.Field()
    equipo_visitante = scrapy.Field()
    gol_local = scrapy.Field()
    gol_visitante = scrapy.Field()
    posesion_local = scrapy.Field()
    posesion_visitante = scrapy.Field()

    porcentaje_pases_local = scrapy.Field()
    porcentaje_pases_visitante = scrapy.Field()

    porcentaje_disparos_local = scrapy.Field()
    porcentaje_disparos_visitante = scrapy.Field()

    porcentaje_salvadas_local = scrapy.Field()
    porcentaje_salvadas_visitante = scrapy.Field()

    tarjetas_amarillas_local = scrapy.Field()
    tarjetas_amarillas_visitante = scrapy.Field()
    tarjetas_rojas_local = scrapy.Field()
    tarjetas_rojas_visitante = scrapy.Field()

    faltas_cometidas_local = scrapy.Field()
    faltas_cometidas_visitante = scrapy.Field()
    corners_local = scrapy.Field()
    corners_visitante = scrapy.Field()
    pases_cruzados_local = scrapy.Field()
    pases_cruzados_visitante = scrapy.Field()
    toques_local = scrapy.Field()
    toques_visitante = scrapy.Field()
    derribos_local = scrapy.Field()
    derribos_visitante = scrapy.Field()
    intercepciones_local = scrapy.Field()
    intercepciones_visitante = scrapy.Field()
    duelos_aereos_local = scrapy.Field()
    duelos_aereos_visitante = scrapy.Field()
    despejes_local = scrapy.Field()
    despejes_visitante = scrapy.Field()
    offsides_local = scrapy.Field()
    offsides_visitante = scrapy.Field()
    saques_de_meta_local = scrapy.Field()
    saques_de_meta_visitante = scrapy.Field()
    saques_de_banda_local = scrapy.Field()
    saques_de_banda_visitante = scrapy.Field()
    pelotazos_local = scrapy.Field()
    pelotazos_visitante = scrapy.Field()

    

