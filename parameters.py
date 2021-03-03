fields_to_pop = ['TIPOBITO', 'IDADEMAE', 'ESCMAE', 'ESCMAE2010', 'SERIESCMAE', 'OCUPMAE', 'QTDFILVIVO',
                     'QTDFILMORT', 'CONTADOR', 'TPMORTEOCO', 'OBITOGRAV', 'OBITOPUERP', 'LINHAA', 'LINHAB', 'LINHAC',
                     'LINHAD', 'LINHAII', 'CB_PRE', 'COMUNSVOIM', 'NUMEROLOTE', 'DTINVESTIG', 'DTCADASTRO',
                     'ATESTANTE', 'STCODIFICA', 'CODIFICADO', 'VERSAOSIST', 'VERSAOSCB', 'FONTEINV', 'DTRECEBIM',
                     'ATESTADO', 'DTRECORIGA', 'OPOR_DO', 'STDOEPIDEM', 'STDONOVA', 'DIFDATA', 'NUDIASOBCO',
                     'DTCADINV', 'TPOBITOCOR', 'DTCONINV', 'FONTES', 'TPRESGINFO', 'TPNIVELINV', 'DTCADINF',
                     'TP_ALTERA', 'CB_ALT', 'ESC', 'SERIESCFAL', 'CODESTAB', 'GRAVIDEZ', 'SEMAGESTAC', 'GESTACAO',
                     'PARTO', 'OBITOPARTO', 'PESO', 'EXAME', 'DTATESTADO', 'CAUSAMAT', 'ESCMAEAGR1', 'ESCFALAGR1',
                     'MORTEPARTO', 'DTCONCASO', 'ALTCAUSA']

fields_to_format_date = ['DTOBITO', 'DTNASC']

fields_to_int = ['IDADE']

fields_to_rename = [{'old': 'DTOBITO', 'new': 'death_date'}, {'old': 'HORAOBITO', 'new': 'death_time'},
                        {'old': 'NATURAL_', 'new': 'country_of_origin'},
                        {'old': 'CODMUNNATU', 'new': 'city_code'},
                        {'old': 'DTNASC', 'new': 'birth_date'}, {'old': 'RACACOR', 'new': 'ethnicity'},
                        {'old': 'ESTCIV', 'new': 'marital_status'}, {'old': 'ESC2010', 'new': 'education_level'},
                        {'old': 'OCUP', 'new': 'occupation'}, {'old': 'CODMUNRES', 'new': 'city_of_residence'},
                        {'old': 'LOCOCOR', 'new': 'place_of_death'}, {'old': 'CODMUNOCOR', 'new': 'city_of_death'},
                        {'old': 'ASSISTMED', 'new': 'was_medically_assisted'},
                        {'old': 'CIRURGIA', 'new': 'had_surgery'},
                        {'old': 'NECROPSIA', 'new': 'is_confirmed_by_autopsy'},
                        {'old': 'CAUSABAS', 'new': 'cause_of_death'}, {'old': 'CIRCOBITO', 'new': 'death_condition'},
                        {'old': 'ACIDTRAB', 'new': 'was_work_related'},
                        {'old': 'FONTE', 'new': 'info_source'},
                        {'old': 'CAUSABAS_O', 'new': 'original_cause_of_death'},
                        {'old': 'TPPOS', 'new': 'was_investigated'}, {'old': 'IDADE', 'new': 'age'},
                        {'old': 'SEXO', 'new': 'gender'}]

fields_to_rename_pt_br = [{'old': 'DTOBITO', 'new': 'data_obito'}, {'old': 'HORAOBITO', 'new': 'hora_obito'},
                          {'old': 'CODMUNNATU', 'new': 'naturalidade_municipio'},
                          {'old': 'DTNASC', 'new': 'data_nascimento'}, {'old': 'RACACOR', 'new': 'etnia'},
                          {'old': 'ESTCIV', 'new': 'estado_cvil'}, {'old': 'ESC2010', 'new': 'escolaridade'},
                          {'old': 'OCUP', 'new': 'profissao'}, {'old': 'CODMUNRES', 'new': 'municipio_residencia'},
                          {'old': 'LOCOCOR', 'new': 'local_obito'}, {'old': 'CODMUNOCOR', 'new': 'municipio_obito'},
                          {'old': 'ASSISTMED', 'new': 'houve_assistencia_medica'},
                          {'old': 'CIRURGIA', 'new': 'houve_cirurgia'},
                          {'old': 'NECROPSIA', 'new': 'confirmado_por_necropsia'},
                          {'old': 'CAUSABAS', 'new': 'causa_basica'}, {'old': 'CIRCOBITO', 'new': 'circustancia_obito'},
                          {'old': 'ACIDTRAB', 'new': 'acidente_dae_trabalho'},
                          {'old': 'FONTE', 'new': 'fonte_informadora'},
                          {'old': 'CAUSABAS_O', 'new': 'causa_basica_original'},
                          {'old': 'TPPOS', 'new': 'foi_investigado'}, {'old': 'IDADE', 'new': 'idade'},
                          {'old': 'SEXO', 'new': 'sexo'}]

state_mappings = [{'source': '43', 'target': 'RS'}, {'source': '35', 'target': 'SP'}, {'source': '27', 'target': 'AL'},
                  {'source': '12', 'target': 'AC'}, {'source': '13', 'target': 'AM'}, {'source': '16', 'target': 'AP'},
                  {'source': '29', 'target': 'BA'}]
