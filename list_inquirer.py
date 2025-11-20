import inquirer

def inquirer_login():
    login = [
        inquirer.List("list_login",
                    message="Pilih Menu Ynag Tersedia...",
                    choices=[
                        "Login",
                        "Registrasi",
                        "Keluar"
                        ]
                    )
                        
    ]
    jawab = inquirer.prompt(login)
    return jawab
    
    

