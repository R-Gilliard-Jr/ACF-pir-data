
def main():
    import os, json, glob
    import tkinter as tk
    from tkinter import Tk, ttk
    from tkinter.filedialog import askdirectory, askopenfilename

    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_py = os.path.join(current_dir, "config.py")
    
    root = Tk()
    root.title("PIR Setup")
    root.geometry("400x250")


    pir_root = tk.StringVar(value = r"C:\Program Files\PIR")
    
    # Look for R and include as default if found
    suggested_path = glob.glob("C:/Program Files/R/*/bin/RScript.exe")
    if suggested_path:
        r_path = tk.StringVar(value=suggested_path[0])
    else:
        r_path = tk.StringVar()
    
    dbms = tk.StringVar()
    
    configure = ttk.Frame(root)
    configure.pack(padx=10, pady=10, fill='x', expand=True)
    
    # Interface
    def browseDir():
        path = askdirectory()
        dir_entry.delete(0, tk.END)
        dir_entry.insert(0, path)
    
    def browseFile():
        path = askopenfilename()
        r_entry.delete(0, tk.END)
        r_entry.insert(0, path)
    
    dir_label = ttk.Label(configure, text='PIR Root Directory:')
    dir_label.pack(fill='x', expand=True)
    dir_entry = ttk.Entry(configure, textvariable=pir_root)
    dir_entry.pack(fill='x', expand = True)
    dir_browse = ttk.Button(configure, text="Browse", command=browseDir)
    dir_browse.pack(fill='x', expand=True)
    
    r_label = ttk.Label(configure, text="Path to Rscript.exe:")
    r_label.pack(fill='x', expand=True)
    r_entry = ttk.Entry(configure, textvariable=r_path)
    r_entry.pack(fill='x', expand = True)
    r_browse = ttk.Button(configure, text="Browse", command=browseFile)
    r_browse.pack(fill='x', expand=True)

    dbms_options = ["MySQL", "SQLite"]
    dbms_label = ttk.Label(configure, text="Database:")
    dbms_label.pack(fill='x', expand=True)
    dbms_menu = ttk.OptionMenu(configure, dbms, *dbms_options)
    dbms_menu.pack(fill='x', expand=True)
    dbms.set(dbms_options[1])
    
    if dir_entry.get() == '':
        exit()

    # Setup directories and configuration
    def finish_clicked():
        try:
            from . import config as conf
            config = conf.config
        except:
            config = {}
        
        config['root'] = dir_entry.get()
        for dir in ["mySQL_Logs", "mySQL_General_Logs", "mySQL_Binary_Logs", "mySQL_Query_Logs", "Installation_Logs",
                    "Automated_Pipeline_Logs", "Listener_Logs", "PIR_data_repository", "Listener_bats",
                    "PIR_data_repository\\Raw", "PIR_data_repository\\Processed", "PIR_data_repository\\Unprocessed"]:
            path = os.path.join(dir_entry.get(), dir)
            try:
                os.makedirs(path)
            except Exception as e:
                if e.winerror == 183:
                    pass
                else:
                    raise(e)
            config[dir.replace("PIR_data_repository\\", "")] = path
            
        config["R_Path"] = r_entry.get()
        config["dbms"] = dbms.get()

        with open(config_py, "w") as f:
            f.write("config = ")
            json.dump(config, f, indent = 4)
        root.destroy()

    finish_button = ttk.Button(configure, text="Finish", command=finish_clicked)
    finish_button.pack(fill='x', expand=True, pady=10)
    
    root.mainloop()