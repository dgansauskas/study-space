import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from extracao_anuncios.app.timer_tasks import elapsed_time_process


#definir variáveis
_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
_REPORT_DATE = datetime.today().strftime('%Y%m%d')
_OLX_CAR_LIST = []
_ML_CAR_LIST = []
_GEN_MAX_PRICE='52000'
_GEN_MIN_PRICE='38000'
_GEN_MAX_KM='70000'
_GEN_MIN_YEAR ='2014'
_OLX_PAGES = 4
_ML_PAGES = 12
_SAVEPATH = f'path\\to_needed_folder\\resumo_anuncios_{_REPORT_DATE}.csv'
_ENCODING = 'utf-8-sig'

@elapsed_time_process
def buscar_dados_olx(pages=_OLX_PAGES) -> pd.DataFrame:
    """Função para extrair dados da OLX"""

    prefix='https://www.olx.com.br'
    search='/autos-e-pecas/carros-vans-e-utilitarios'
    brand = {
        'spacefox':'/vw-volkswagen/spacefox',
        'voyage':'/vw-volkswagen/voyage',
        'hb20s':'/hyundai/hb20s',
        'honda_fit':'/honda/fit',
        'cobalt':'/gm-chevrolet/cobalt',
        'prisma':'/gm-chevrolet/prisma',
        'onix':'/gm-chevrolet/onix/seda'
        }
    search_region = {
        'CG':'/estado-ms/mato-grosso-do-sul/campo-grande',
        'SP':'/estado-sp/sao-paulo-e-regiao'
        }
    max_km=f'?me={_GEN_MAX_KM}'
    max_price=f'&pe={_GEN_MAX_PRICE}'
    min_price=f'&ps={_GEN_MIN_PRICE}'

    print("Extraindo dados da OLX")

    for car, car_brand in brand.items():

        for region, region_link in search_region.items():    

            for x in range(0, pages):
                if x == 0:
                    url = prefix+search+car_brand+region_link+max_km+min_price+max_price
                else:
                    url = prefix+search+car_brand+region_link+max_km+min_price+max_price+'&o='+str(x+1)
                print(url)
                page = requests.get(url=url, headers=_HEADERS)
                soup = BeautifulSoup(page.content, "lxml")
                itens_search = soup.find_all("div", {"class":"sc-3888b54f-0 dPstMh renderIfVisible"})

                for a in itens_search:
                    try:
                        classified_ads= a.find_all("h2")[0].contents[0]
                        car_price= a.find_all("h3")[0].contents[0]
                        car_price= car_price.split("R$")[1]
                        car_price= int(car_price.replace(".",""))
                        ads_date = a.find_all("p", "olx-text olx-text--caption olx-text--block olx-text--regular olx-ad-card__date--horizontal")[0].contents[0]
                        car_url = a.find_all("a", "olx-ad-card__title-link")[0]["href"]
                        car_km = a.find_all("li","olx-ad-card__labels-item")[0].contents[0].text
                        car_km = car_km.split()[0].replace('.','')
                        car_year = a.find_all("li","olx-ad-card__labels-item")[1].contents[0].text
                        combustivel = a.find_all("li","olx-ad-card__labels-item")[2].contents[0].text
                        car_local = a.find_all("p", "olx-text olx-text--caption olx-text--block olx-text--regular")[0].contents[0]
                        car_city = car_local.split(', ')[0]
                        car_neighbor = car_local.split(', ')[1].rstrip()
                    except:
                        print('Link não encontrado')

                    json_record = {
                        "regiao": region.upper(),
                        "cidade": car_city.upper(),
                        "bairro": car_neighbor.upper(),
                        "anuncio": classified_ads.upper(),
                        "preco_veiculo": car_price,
                        "kilometragem": car_km,
                        "ano_veiculo": car_year,
                        "combustivel": combustivel,
                        "dia_postagem": ads_date,
                        "fonte": "OLX",
                        "url_anuncio": car_url
                    }

                    _OLX_CAR_LIST.append(json_record)
        
    df = pd.DataFrame(_OLX_CAR_LIST)

    return df
                    
@elapsed_time_process
def buscar_dados_mercado_livre(pages=_ML_PAGES) -> pd.DataFrame:
    """Função para extrair dados do Mercado Livre"""

    prefix='https://lista.mercadolivre.com.br'
    search_region = {
        "CG":f"/veiculos/ate-{_GEN_MAX_KM}-km-em-mato-grosso-do-sul",
        'SP':f"/veiculos/ate-{_GEN_MAX_KM}-km-em-sao_paulo"
        }
    max_price=f'-{_GEN_MAX_PRICE}'
    min_price=f'/_PriceRange_{_GEN_MIN_PRICE}'

    print("Extraindo dados do Mercado Livre")

    for region, region_link in search_region.items():   

        for x in range(0, pages): 
            if x == 0:
                url = prefix+region_link+min_price+max_price+'_NoIndex_True?'
            else:
                url = prefix+region_link+"_Desde_"+str((x*48)+1)+min_price+max_price+'_NoIndex_True?'
            
            print(url)

            page = requests.get(url=url, headers=_HEADERS)
            soup = BeautifulSoup(page.content, "lxml")
            itens_search = soup.find_all("div", {"class":"ui-search-result__content"})

            for a in itens_search:
                try:
                    classified_ads= a.find_all("h2")[0].contents[0]
                    car_price= a.find_all("span", "andes-money-amount__fraction")[0].contents[0]
                    car_price= int(car_price.replace(".",""))
                    car_url = a.find_all("a", "ui-search-item__group__element ui-search-link")[0]["href"]
                    car_km = a.find_all("li","ui-search-card-attributes__attribute")[1].contents[0].text
                    car_km = car_km.split()[0].replace('.','')
                    car_year = a.find_all("li","ui-search-card-attributes__attribute")[0].contents[0].text
                    car_local = a.find_all("span", "ui-search-item__group__element ui-search-item__location")[0].contents[0]
                    car_city = car_local.split(' - ')[0]
                    # estado_veiculo = car_local.split(' - ')[1]
                except:
                    print('Link não encontrado')

                json_record = {
                    "regiao": region.upper(),
                    "cidade": car_city.upper(),
                    "bairro": None,
                    "anuncio": classified_ads.upper(),
                    "preco_veiculo": car_price,
                    "kilometragem": car_km,
                    "ano_veiculo": car_year,
                    "combustivel": None,
                    "dia_postagem": None,
                    "fonte": "Mercado Livre",
                    "url_anuncio": car_url
                }

                _ML_CAR_LIST.append(json_record)

    df = pd.DataFrame(_ML_CAR_LIST)

    return df


def run():
    olx_df = buscar_dados_olx()
    ml_df = buscar_dados_mercado_livre()

    print()
    subset_columns = ['regiao','cidade','bairro','anuncio','preco_veiculo','kilometragem','ano_veiculo','combustivel','fonte']

    print("Agrupar searchs e excluir recordes duplicados baseado em colunas determinadas")
    full_df = pd.concat([olx_df,ml_df], axis=0).drop_duplicates(subset=subset_columns, keep='first')

    print("Garantir que os campos `kilometragem` e `ano_veiculo` estão tipados como integer")
    full_df['kilometragem'] = full_df['kilometragem'].astype('int64')
    full_df['ano_veiculo'] = full_df['ano_veiculo'].astype('int64')

    print("Excluir carros indesejados pela nomenclatura")
    full_df = full_df[~full_df['anuncio'].str.contains('PRISMA 1.0 JOY|FORD KA 1.0|TIIDA|PEUGEOT 308|KWID| UNO | GOL |MOBI|SANDERO| MARCH |UP!|LOGAN|MONTANA|ARGO|HB20 |PEUGEOT 208|ETIOS|CAPTIVA| C3 1|UP CROSS|FUSION|SAVEIRO|KANGOO| AGILE |I-MOTION|DUALOGIC|KOMBI')]
    
    print("Excluir links de motos")
    full_df = full_df[~full_df['url_anuncio'].str.contains('https://moto.')]
    
    print(f"Excluir carros com quilometragem superior a {_GEN_MAX_KM}")
    full_df = full_df[full_df['kilometragem']<=int(_GEN_MAX_KM)]
    
    print(f"Excluir carros com ano de fabricação inferior a {_GEN_MAX_KM}")
    full_df = full_df[full_df['ano_veiculo']>=int(_GEN_MIN_YEAR)]
    
    print('Organizar anúncios por ano(DESC),kilometragem(ASC),preco(ASC)')
    full_df = full_df.sort_values(['ano_veiculo','kilometragem','preco_veiculo'], ascending=[False,True,True])

    print(f"Salvar relatório!")
    full_df.to_csv(path_or_buf=_SAVEPATH, sep=',', header=True, index=False, encoding=_ENCODING)

    print("Fim do processo!!!")

if __name__ =='__main__':
    run()
