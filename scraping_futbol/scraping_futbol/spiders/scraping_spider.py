import scrapy
from scraping_futbol.items import ScrapingFutbolItem
from scrapy.selector import Selector

class FutbolSpider(scrapy.Spider):

    name = 'liga'

    download_delay = 10

    start_urls = [
        'url_liga'
    ]

    
    def parse(self, response):
        
        td_elements = response.xpath("//td[@data-stat='match_report']//a[contains(@href, '/es/partidos/')]")
        for td in td_elements:
            hrefs = td.xpath('@href').getall()
            for href in hrefs:
                yield response.follow(href, self.parse_information)
    
    def parse_information(self, response):
        partido = ScrapingFutbolItem()

        teams = response.xpath("//div[@class='scorebox']//a[contains(@href, '/es/equipos/')]").extract()
        team_condition = ['equipo_local', 'equipo_visitante']

        for i in range(0, len(teams)):
            sel = Selector(text=teams[i])
            partido[team_condition[i]] = sel.xpath("//a/text()").get()

        goals = response.xpath("//div[@class='scorebox']//div[@class='score']").extract()
        goal_condition = ['gol_local', 'gol_visitante']
        
        for i in range(0, len(goals)):
            sel = Selector(text=goals[i])
            partido[goal_condition[i]] = sel.xpath("//div/text()").get()

        first_stats = response.xpath("//div[@id='team_stats']//strong").extract()
        stats_1 = ['posesion_local', 
                    'posesion_visitante', 
                    'porcentaje_pases_local', 
                    'porcentaje_pases_visitante', 
                    'porcentaje_disparos_local', 
                    'porcentaje_disparos_visitante', 
                    'porcentaje_salvadas_local', 
                    'porcentaje_salvadas_visitante']

        for i in range(0,len(first_stats)):
            sel = Selector(text=first_stats[i])
            partido[stats_1[i]] = sel.xpath("//strong/text()").get().replace('%','')

        partido['tarjetas_amarillas_local'] = len(response.xpath("(//div[@class='cards'])[1]/span[@class='yellow_card']"))

        partido['tarjetas_amarillas_visitante'] = len(response.xpath("(//div[@class='cards'])[2]/span[@class='yellow_card']"))

        partido['tarjetas_rojas_local'] = len(response.xpath("(//div[@class='cards'])[1]/span[@class='red_card']"))

        partido['tarjetas_rojas_visitante'] = len(response.xpath("(//div[@class='cards'])[2]/span[@class='red_card']"))

        second_stats = response.xpath("//div[@id='team_stats_extra']//div//div").extract()
        stats_2 = ['faltas_cometidas_local',
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

        for i in range(0,3):
            for j in range(1,5):
                sel = Selector(text=second_stats[3*(j+5*i)])
                partido[stats_2[2*(j-1)+(8*i)]] = sel.xpath("//div/text()").get() #stats_local

                sel = Selector(text=second_stats[(3*(j+5*i))+2])
                partido[stats_2[(2*(j-1)+(8*i))+1]] = sel.xpath("//div/text()").get() #stats_visitante
            
        yield partido
    