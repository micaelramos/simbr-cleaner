# simbr-cleaner
Data Cleaner for Brazilian SIM System

SIM (Sistema de Informação sobre Mortalidade) is the brazilian public information system that contains country-wide 
mortality information since 1979.

This project aims to clean data sets into a friendly JSON format, enabling further data mining and research with 
current technologies.

Datasets for SIM can be found at:

https://opendatasus.saude.gov.br/dataset/sistema-de-informacao-sobre-mortalidade-sim-1979-a-2019

## Usage
```python sim_cleaner.py -i <input_file_path> -o <output_file_path>```

## Data Formats

Datasets available for SIM are Comma-separated records (actually Semicolon-separated) which gets translated and mapped
to a JSON dataset. Fields get translated to human-readable field names and values are also formatted to friendly 
data formats.

Sample Input:
```
"CONTADOR","TIPOBITO","DTOBITO","HORAOBITO","NATURAL_","CODMUNNATU","DTNASC","IDADE","SEXO","RACACOR","ESTCIV","ESC","ESC2010","SERIESCFAL","OCUP","CODMUNRES","LOCOCOR","CODESTAB","CODMUNOCOR","IDADEMAE","ESCMAE","ESCMAE2010","SERIESCMAE","OCUPMAE","QTDFILVIVO","QTDFILMORT","GRAVIDEZ","SEMAGESTAC","GESTACAO","PARTO","OBITOPARTO","PESO","TPMORTEOCO","OBITOGRAV","OBITOPUERP","ASSISTMED","EXAME","CIRURGIA","NECROPSIA","LINHAA","LINHAB","LINHAC","LINHAD","LINHAII","CAUSABAS","CB_PRE","COMUNSVOIM","DTATESTADO","CIRCOBITO","ACIDTRAB","FONTE","NUMEROLOTE","DTINVESTIG","DTCADASTRO","ATESTANTE","STCODIFICA","CODIFICADO","VERSAOSIST","VERSAOSCB","FONTEINV","DTRECEBIM","ATESTADO","DTRECORIGA","OPOR_DO","CAUSAMAT","ESCMAEAGR1","ESCFALAGR1","STDOEPIDEM","STDONOVA","DIFDATA","NUDIASOBCO","DTCADINV","TPOBITOCOR","DTCONINV","FONTES","TPRESGINFO","TPNIVELINV","DTCADINF","MORTEPARTO","DTCONCASO","ALTCAUSA","CAUSABAS_O","TPPOS","TP_ALTERA","CB_ALT"
"1","2","09122019","2210","829","290280","11051930","489","1","4","3","2","1","1","999993","290280","1","2799855","290280",,,,,,,,,,,,,,,,,,,,,"*R092","*I219",,,,"I219",,,"10122019",,,,"20190012",,"16122019","1","S","S","3.2.02","3.2",,"17122019","R092/I219","17122019","8",,,"01","0","1","008",,,,,,,,,,,,"I219",,,
```

Sample output:
```json
[{"death_date": "2019-12-09T00:00:00", "death_time": "2210", "country_of_origin": "829", "city_code": "290280", "birth_date": "1930-05-11T00:00:00", "ethnicity": "4", "marital_status": "3", "education_level": "1", "occupation": "999993", "city_of_residence": "290280", "place_of_death": "1", "city_of_death": "290280", "was_medically_assisted": "", "had_surgery": "", "is_confirmed_by_autopsy": "", "cause_of_death": "I219", "death_condition": "", "was_work_related": "", "info_source": "", "original_cause_of_death": "I219", "was_investigated": "", "age": 489, "gender": "1"}]
```

## Data Dictionaries and Other Info

The SIM specific data dictionaries are also included on folder "SIM_data_dicts", original files for the dictionaries
and further dataset information can be found at Fiocruz website:

https://bigdata-metadados.icict.fiocruz.br/dataset/sistema-de-informacoes-de-mortalidade-sim


## Parameters
The 

## Why this project exists?

The increasing public interest on mortality data due to the global COVID-19 pandemic was a motivation to enable
research in this matter. Considering that government system's data is not friendly to be directly mined, 
this project aims to make life easier for everyone who might want to work with SIM datasets.
