import tkinter as tk
import secrets
import string

def lancer():
    def generate_key():
        from cryptography.fernet import Fernet
        key = Fernet.generate_key()
        with open('unlock.key', 'wb') as unlock:
            unlock.write(key)


    def neto():
        with open("vosmotsdepasse.txt", "w") as file:
            file.truncate()

    def premier_demarrage():

        '''
        f =open("mdp_archive.txt", "x")
        f.close
        '''

        f =open("vosmotsdepasse.txt", "x")
        f.close

        f =open("vmpd_crypté.txt", "x")
        f.close
 

    def initialisation_service():
        generate_key()
        premier_demarrage()
        label_result.config(text="Service initialisé avec succès")

    def fermer_programme():
        root.destroy()

    def information():
        label_result.config(text="Consultez la page Web 'Information et utilisation de GenCode'")

    root = tk.Tk()
    root.title("GenCode")

    frame = tk.Frame(root)
    frame.pack()

    label = tk.Label(frame, text="Bonjour, pour utilisé le service GenCode vous devez passer par cette étape")
    label.pack()

    frame_buttons = tk.Frame(frame)
    frame_buttons.pack()

    button_initialisation = tk.Button(frame_buttons, text="Initialiser le service", command=initialisation_service)
    button_initialisation.grid(row=0, column=0)


    button_quitter = tk.Button(frame_buttons, text="Quitter", command=fermer_programme)
    button_quitter.grid(row=0, column=1)

    button_info = tk.Button(frame_buttons, text="Informations", command=information)
    button_info.grid(row=0, column=2)

    frame_result = tk.Frame(frame)
    frame_result.pack()

    label_result = tk.Label(frame_result)
    label_result.pack()

    root.mainloop()
