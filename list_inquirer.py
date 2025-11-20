import inquirer

def inquirer_login():
    login = [
        inquirer.List("list_login",
                    message="Pilih menu...",
                    choices=[
                        "Login",
                        "Registrasi",
                        "Keluar"
                        ]
                    )
                        
    ]
    jawab = inquirer.prompt(login)
    return jawab
    
    

