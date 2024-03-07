def load_pir_data(wb_list):
    import pandas as pd, sqlite3, os, re, janitor
    from pir_pipeline import config as conf

    config = conf.config

    # Establish db connection
    pir_logs_db = os.path.join(config["root"], "pir_logs.db")
    try:
        log_conn = sqlite3.connect(pir_logs_db)
        log_cursor = log_conn.cursor()
    except:
        raise(f"Could not open database: {pir_logs_db}")
    
    section_re = re.compile("^Section")
    for workbook in wb_list:
        for sheet in workbook.sheet_names:
            # Special logic for sections
            if re.match(section_re, sheet):

                # Naive approach to reshape, needs refactoring
                df = pd.read_excel(workbook, sheet_name=sheet)
                df.columns = df.iloc[0]
                df = df.iloc[1:]
                df = df.melt(id_vars=list(df.columns[0:10]), var_name = 'question_name', value_name = 'answer')
                continue
            # Reference and program can be loaded directly
            else:
                try:
                    df = pd.read_excel(workbook, sheet_name=sheet)
                    df = janitor.clean_names(df)
                    if sheet == 'Reference':
                        group_vars = ['question_number', 'question_name']
                        # Ensure that data is unique by question_number and question_name
                        try:
                            assert df.set_index(group_vars).index.is_unique
                        except:
                            df = df.drop_duplicates(group_vars)
                        finally:
                            assert df.set_index(group_vars).index.is_unique
                    print(df)
                except Exception as e:
                    raise(e)
