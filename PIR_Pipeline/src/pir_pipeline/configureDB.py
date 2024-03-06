def main():
    from . import config as conf
    from . import setupDB
    if conf.config['dbms'] != 'SQLite':
        import os, json
        import tkinter as tk
        from tkinter import ttk
        from tkinter.messagebox import showinfo

        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_py = os.path.join(current_dir, "config.py")

        root = tk.Tk()
        root.geometry("500x300")
        root.resizable(False, False)
        root.title("Configure Database Credentials")

        username = tk.StringVar()
        password = tk.StringVar()
        host = tk.StringVar(value='localhost')
        port = tk.IntVar(value=0)
        db_path = tk.StringVar()

        # Configuration Frame
        configure = ttk.Frame(root)
        configure.pack(padx=10, pady=10, fill='x', expand=True)

        # username
        username_label = ttk.Label(configure, text='Database Username:')
        username_label.pack(fill='x', expand=True)

        username_entry = ttk.Entry(configure, textvariable = username)
        username_entry.pack(fill="x", expand = True)
        username_entry.focus()

        # password
        password_label = ttk.Label(configure, text='Database Password:')
        password_label.pack(fill='x', expand=True)

        password_entry = ttk.Entry(configure, textvariable = password, show="*")
        password_entry.pack(fill="x", expand = True)

        # host
        host_label = ttk.Label(configure, text='Database Host:')
        host_label.pack(fill='x', expand=True)

        host_entry = ttk.Entry(configure, textvariable = host)
        host_entry.pack(fill="x", expand = True)

        # port
        port_label = ttk.Label(configure, text='Database Port:')
        port_label.pack(fill='x', expand=True)

        port_entry = ttk.Entry(configure, textvariable = port)
        port_entry.pack(fill="x", expand = True)

        # Database path
        db_path_label = ttk.Label(configure, text='Database Path:')
        db_path_label.pack(fill='x', expand=True)

        db_path_entry = ttk.Entry(configure, textvariable = db_path)
        db_path_entry.pack(fill="x", expand = True)

        # Finish button
        def finish_clicked():
            from . import config as conf
            dbusername = username.get()
            dbpassword = password.get()
            dbhost = host.get()
            dbport = port.get()
            dbpath = db_path.get()
            try:
                config = conf.config
            except:
                config = {}
            for c in ["dbusername", "dbpassword", "dbhost", "dbport", "dbpath"]:
                config[c] = locals()[c]
            with open(config_py, 'w') as f:
                f.write("config = ")
                json.dump(config, f, indent=4)
            root.destroy()
            setupDB.main()
            

        finish_button = ttk.Button(configure, text="Finish", command=finish_clicked)
        finish_button.pack(fill='x', expand=True, pady=10)

        root.mainloop()
    else:
        setupDB.main()
    
if __name__ == "__main__":
    main()