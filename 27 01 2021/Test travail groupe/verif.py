def password(psd='null'):
    if psd != 'null':
        if len(psd) >= 10 and len(psd) <= 20:
            if '?' in psd or '@' in psd or '&' in psd or '$' in psd or '%' in psd or '#' in psd:
                if any(x.isupper() for x in psd) and any(x.islower() for x in psd):
                    if any(x.isdigit() for x in psd):
                        print("Votre mdp correspond à tous les critères")
                    else:
                        print("Veuillez rentrer au moins un chiffre")
                else:
                    print("Veuillez rentrer au moins une majuscule et une minuscule")
            else:
                print("veuillez rentrer au moins un caractère spécial")
        else:
            print("rentrez un mot de passe entre 10 et 20 caractères")
    else:
        print("rentrez un mot de passe svp")

def main():
    user_password = input("Saisissez un mot de passe:")
    if user_password is not None:
        password(user_password)



if __name__ == '__main__':
    main()