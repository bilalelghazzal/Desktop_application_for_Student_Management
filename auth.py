import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, 
    QMessageBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QFormLayout, QDialog, QDialogButtonBox,QLabel
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sqlite3


class DataManager:
    def __init__(self, database="etudiants.db"):
        self.database = database  # SQLite database file
        self.db = None  # Database connection
        self.connection()  # Initialize the database connection

    def connection(self):
        try:
            self.conn = sqlite3.connect(self.database)
            print("Connexion réussie à la base de données.")
        except sqlite3.Error as e:
            print("Erreur de connexion à la base de données:", e)
            raise Exception("Failed to connect to the database.")

    def check_user(self, username, password):
        if not self.conn:
            print("Database is not connected.")
            return False

        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM users WHERE username = ? AND password = ?"
            
            print("Executing Query:", query)
            print("Bound Values: username =", username, ", password =", password)
            
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            
            if result:
                return True
            else:
                return False
                
        except sqlite3.Error as e:
            print("Erreur lors de l'exécution de la requête:", e)
            return False
    
        
        
    
    def GET_DATA(self):
        db=sqlite3.Connection("etudiants.db")
        cursor=db.cursor()
        command="SELECT * FROM etudiant"
        result=cursor.execute(command)
        return result.fetchall()
    
    def SEARCH_DATA(self,name): 
        db=sqlite3.Connection("etudiants.db")
        cursor=db.cursor()
        command="SELECT * FROM etudiant WHERE nom=?"
        result=cursor.execute(command,(name,))
        return result.fetchall()
    
    def DELETE_DATA(self,id):
        db=sqlite3.Connection("etudiants.db")# Create a connection to the database
        cursor=db.cursor() # Create a cursor object to execute SQL commands
        # Prepare the SQL command to delete the student with the given name
        command="DELETE FROM etudiant WHERE id=?"
        cursor.execute(command,(id)) # Execute the command with the provided name
        db.commit() # Commit the changes to the database

    def INSERT_DATA(self,nom,prenom,email,matiere,note):
        db=sqlite3.Connection("etudiants.db")
        cursor=db.cursor()
        command="INSERT INTO etudiant (nom,prenom,email,matiere,note) VALUES (?,?,?,?,?)"
        cursor.execute(command,(nom,prenom,email,matiere,note))
        db.commit()
        # update a row 
    def MODIFY_DATA(self,id,nom,prenom,email,matiere,note):
        db=sqlite3.Connection("etudiants.db")
        cursor=db.cursor()
        command="UPDATE etudiant set nom=?,prenom=?,email=?,matiere=?,note=? WHERE id=?"
        cursor.execute(command,(nom,prenom,email,matiere,note,id))
        db.commit()
    def STAT(self,matiere,note):
        db=sqlite3.Connection("etudiant.db")
        cursor=db.cursor()
        command="select matiere,note from etudiant "
        result=cursor.execute(command,(matiere,note))
        return result
    
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion des Étudiants")
        self.setGeometry(200, 110, 900, 600)
        self.setWindowIcon(QIcon("python.png"))

        self.setStyleSheet("background-color: #f0f0f0;")
        
        # Central widget
        central_widget = QWidget()
    
        self.setCentralWidget(central_widget)
   

        # Main layout (horizontal)
        main_layout = QHBoxLayout()

        # Table
        self.table = QTableWidget()
        self.table.setGeometry(20, 20, 760, 500)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['id', 'Nom', 'Prenom', 'Email', 'Matiere', 'Note'])
        self.table.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: green; color: white; font-weight: bold; }")
    
        main_layout.addWidget(self.table)

        # Buttons layout (vertical)
        buttons_layout = QVBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Rechercher par nom/ Supprimer etudiant")
        self.search_input.setFixedWidth(150) 
        buttons_layout.addWidget(self.search_input)


        # Add Button
        self.add_button = QPushButton("Ajouter")
        self.add_button.setFixedWidth(150)
        self.add_button.setFixedHeight(40)
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* Green background */
                color: white; /* White text */
                font-size: 16px; /* Font size */
                font-weight: bold; /* Bold text */
                border-radius: 10px; /* Rounded corners */
                padding: 10px; /* Padding inside the button */
                border: 2px solid #3e8e41; /* Green border */
            }
            QPushButton:hover {
                background-color: #45a049; /* Darker green on hover */
            }
            QPushButton:pressed {
                background-color: #3e8e41; /* Even darker green when pressed */
            }
        """)
        buttons_layout.addWidget(self.add_button)

        # Update Button
        self.update_button = QPushButton("Mettre à jour")
        self.update_button.setFixedWidth(150)
        self.update_button.setFixedHeight(40)
        self.update_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3; /* Blue background */
                color: white; /* White text */
                font-size: 16px; /* Font size */
                font-weight: bold; /* Bold text */
                border-radius: 10px; /* Rounded corners */
                padding: 10px; /* Padding inside the button */
                border: 2px solid #1976D2; /* Blue border */
            }
            QPushButton:hover {
                background-color: #1976D2; /* Darker blue on hover */
            }
            QPushButton:pressed {
                background-color: #1565C0; /* Even darker blue when pressed */
            }
        """)
        buttons_layout.addWidget(self.update_button)

        # Modify Button
        self.modify_button = QPushButton("Modifier")
        self.modify_button.setFixedWidth(150)
        self.modify_button.setFixedHeight(40)
        self.modify_button.setStyleSheet("""
            QPushButton {
                background-color: #FF9800; /* Orange background */
                color: white; /* White text */
                font-size: 16px; /* Font size */
                font-weight: bold; /* Bold text */
                border-radius: 10px; /* Rounded corners */
                padding: 10px; /* Padding inside the button */
                border: 2px solid #FB8C00; /* Orange border */
            }
            QPushButton:hover {
                background-color: #F57C00; /* Darker orange on hover */
            }
            QPushButton:pressed {
                background-color: #EF6C00; /* Even darker orange when pressed */
            }
        """)
        buttons_layout.addWidget(self.modify_button)

        # Delete Button
        self.delete_button = QPushButton("Supprimer")
        self.delete_button.setFixedWidth(150)
        self.delete_button.setFixedHeight(40)
        self.delete_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336; /* Red background */
                color: white; /* White text */
                font-size: 16px; /* Font size */
                font-weight: bold; /* Bold text */
                border-radius: 10px; /* Rounded corners */
                padding: 10px; /* Padding inside the button */
                border: 2px solid #d32f2f; /* Red border */
            }
            QPushButton:hover {
                background-color: #e53935; /* Darker red on hover */
            }
            QPushButton:pressed {
                background-color: #c62828; /* Even darker red when pressed */
            }
        """)
        buttons_layout.addWidget(self.delete_button)

        # Search Button
        self.search_button = QPushButton("Rechercher")
        self.search_button.setFixedWidth(150)
        self.search_button.setFixedHeight(40)
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #FFC107; /* Yellow background */
                color: black; /* Black text */
                font-size: 16px; /* Font size */
                font-weight: bold; /* Bold text */
                border-radius: 10px; /* Rounded corners */
                padding: 10px; /* Padding inside the button */
                border: 2px solid #FFA000; /* Yellow border */
            }
            QPushButton:hover {
                background-color: #FFB300; /* Darker yellow on hover */
            }
            QPushButton:pressed {
                background-color: #FF8F00; /* Even darker yellow when pressed */
            }
        """)
        buttons_layout.addWidget(self.search_button)

        # Stats Button
        self.stats_button = QPushButton("Statistiques")
        self.stats_button.setFixedWidth(150)
        self.stats_button.setFixedHeight(40)
        self.stats_button.setStyleSheet("""
            QPushButton {
                background-color: #673AB7; /* Purple background */
                color: white; /* White text */
                font-size: 16px; /* Font size */
                font-weight: bold; /* Bold text */
                border-radius: 10px; /* Rounded corners */
                padding: 10px; /* Padding inside the button */
                border: 2px solid #5E35B1; /* Purple border */
            }
            QPushButton:hover {
                background-color: #5E35B1; /* Darker purple on hover */
            }
            QPushButton:pressed {
                background-color: #512DA8; /* Even darker purple when pressed */
            }
        """)
        buttons_layout.addWidget(self.stats_button)

        main_layout.addLayout(buttons_layout)
        central_widget.setLayout(main_layout)
        self.show()

        self.add_button.clicked.connect(self.add_student)
        self.update_button.clicked.connect(self.get_data)
        self.modify_button.clicked.connect(self.update_student)
        self.delete_button.clicked.connect(self.delete_student)
        self.search_button.clicked.connect(self.search_student)
        self.stats_button.clicked.connect(self.shows_stats)
        
        #show window 
        self.show()

        self.get_data() 

        
    def get_data(self):
        data_manager = DataManager()
        result = data_manager.GET_DATA()
        self.table.setRowCount(0)  # Clear the table before adding new data
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def add_student(self):
        data_manager = DataManager()
        dialog = QDialog(self)
        dialog.setWindowTitle("Ajouter un étudiant")
        dialog.setGeometry(100, 100, 400, 300)
        dialog.setWindowIcon(QIcon("python.png"))
        layout = QFormLayout()
        self.nom_input = QLineEdit()
        self.prenom_input = QLineEdit()
        self.email_input = QLineEdit()
        self.matiere_input = QLineEdit()
        self.note_input = QLineEdit()
        layout.addRow("Nom:", self.nom_input)
        layout.addRow("Prenom:", self.prenom_input)
        layout.addRow("Email:", self.email_input)
        layout.addRow("Matiere:", self.matiere_input)
        layout.addRow("Note:", self.note_input)
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)# Create OK and Cancel buttons
        button_box.accepted.connect(dialog.accept)# Connect the OK button to accept the dialog
        button_box.rejected.connect(dialog.reject)# Connect the Cancel button to reject the dialog
        layout.addRow(button_box)# Add the button box to the layout
        dialog.setLayout(layout)# Set the layout for the dialog
        if dialog.exec_() == QDialog.Accepted:# Show the dialog and wait for user input
            nom = self.nom_input.text()# Get the input values
            prenom = self.prenom_input.text()
            email = self.email_input.text()
            matiere = self.matiere_input.text()
            note = self.note_input.text()
            try:
                data_manager.INSERT_DATA(nom,prenom,email,matiere,note)# Insert the data into the database
                self.get_data()
                QMessageBox.information(self, "Information", "Étudiant ajouté avec succès.")# Show success message
            except Exception as e:
                print("Erreur lors de l'ajout des données:", e)
                QMessageBox.critical(self, "Erreur", "Erreur lors de l'ajout de l'étudiant.")# Show error message


        

    def update_student(self):
        # Get the selected row
        selected_row = self.table.currentRow()

        # Check if a row is selected
        if (selected_row < 0):
            QMessageBox.warning(self, "Avertissement", "Veuillez sélectionner un étudiant à modifier.")
            return

        # Retrieve data from the selected row
        id_value = self.table.item(selected_row, 0).text()
        nom_value = self.table.item(selected_row, 1).text()
        prenom_value = self.table.item(selected_row, 2).text()
        email_value = self.table.item(selected_row, 3).text()
        matiere_value = self.table.item(selected_row, 4).text()
        note_value = self.table.item(selected_row, 5).text()

        # Create a dialog for editing the student
        dialog = QDialog(self)
        dialog.setWindowTitle("Modifier un étudiant")
        dialog.setGeometry(100, 100, 400, 300)
        dialog.setWindowIcon(QIcon("python.png"))
        layout = QFormLayout()

        # Input fields pre-filled with the current data
        self.nom_input = QLineEdit(nom_value)
        self.prenom_input = QLineEdit(prenom_value)
        self.email_input = QLineEdit(email_value)
        self.matiere_input = QLineEdit(matiere_value)
        self.note_input = QLineEdit(note_value)

        layout.addRow("Nom:", self.nom_input)
        layout.addRow("Prenom:", self.prenom_input)
        layout.addRow("Email:", self.email_input)
        layout.addRow("Matiere:", self.matiere_input)
        layout.addRow("Note:", self.note_input)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addRow(button_box)
        dialog.setLayout(layout)

        
        if dialog.exec_() == QDialog.Accepted:
            # Update the student in the database
            data_manager = DataManager()
            try:
                data_manager.MODIFY_DATA(
                    id_value,
                    self.nom_input.text(),
                    self.prenom_input.text(),
                    self.email_input.text(),
                    self.matiere_input.text(),
                    self.note_input.text()
                )
                self.get_data()  # Refresh the table
                QMessageBox.information(self, "Information", "Étudiant modifié avec succès.")
            except Exception as e:
                print("Erreur lors de la modification des données:", e)
                QMessageBox.critical(self, "Erreur", "Erreur lors de la modification de l'étudiant.")
        

    def delete_student(self):
        # Get the ID from the search input
        id = self.search_input.text()
        if not id:
            QMessageBox.warning(self, "Avertissement", "Veuillez entrer l'ID de l'étudiant à supprimer.")
            return

        # Create an instance of DataManager
        data_manager = DataManager()

        try:
            # Delete the student from the database
            result = data_manager.DELETE_DATA(id)
            if result:
                # Remove the row from the table
                for i in range(self.table.rowCount()):
                    if self.table.item(i, 0).text() == id:
                        self.table.removeRow(i)
                        QMessageBox.information(self, "Information", "Étudiant supprimé avec succès.")
                    
                QMessageBox.warning(self, "Avertissement", "Etudiant a été supprimé.")
            else:
                QMessageBox.critical(self, "Erreur", "Erreur lors de la suppression de l'étudiant.")
        except Exception as e:
            print("Erreur lors de la suppression des données:", e)
            QMessageBox.critical(self, "Erreur", "Erreur lors de la suppression des données.")


    def search_student(self):
        data_manager = DataManager()
        name = self.search_input.text()
        if name:
            try :
                result=data_manager.SEARCH_DATA(name)
                if result: # Check if result is not empty
                    self.table.setRowCount(0)   # Clear the table before adding new data
                    for row_number,row_data in enumerate(result): 
                        self.table.insertRow(row_number)
                        for column_number,data in enumerate(row_data):
                            self.table.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                else:
                    QMessageBox.information(self, "Information", "Aucun étudiant trouvé avec ce nom.")
            except Exception as e:
                print("Erreur lors de la recherche des données:", e)
    def shows_stats(self):
        # Create a dialog for displaying statistics
        dialog = QDialog(self)
        dialog.setGeometry(300, 300, 400, 300)
        dialog.setWindowTitle("Statistiques")
        dialog.setWindowIcon(QIcon("python.png"))
        layout = QVBoxLayout()

        # Create an instance of DataManager
        data_manager = DataManager()

        try:
            # Fetch data for statistics
            result = data_manager.GET_DATA()  # Get all data from the database

            if result:
                # Calculate statistics
                stats = {}
                for row in result:
                    matiere = row[4]  # Assuming 'matiere' is the 5th column (index 4)
                    try:
                        note = float(row[5])  # Assuming 'note' is the 6th column (index 5)
                    except ValueError:
                        continue  # Skip rows with invalid note values

                    if matiere not in stats:
                        stats[matiere] = []
                    stats[matiere].append(note)

                # Display statistics
                for matiere, notes in stats.items():
                    moyenne = sum(notes) / len(notes)  # Calculate average
                    label = QLabel(f"Matière: {matiere}, Moyenne: {moyenne:.2f}")
                    label.setStyleSheet(
                    "font-size: 14px; font-weight: bold; color: #333;"
                    "background-color: #e0e0e0; padding: 5px; border-radius: 5px;"
                )
                    layout.addWidget(label)
            else:
                layout.addWidget(QLabel("Aucune donnée disponible pour les statistiques."))

        except Exception as e:
            print("Erreur lors du calcul des statistiques:", e)
            layout.addWidget(QLabel("Erreur lors du calcul des statistiques."))

        dialog.setLayout(layout)
        dialog.exec_()

class authentifcation:
    def __init__(self):
        self.window = QWidget()
        self.window.setWindowTitle("Authentification")
        self.window.setWindowIcon(QIcon("python.png"))
        self.window.setGeometry(100, 100, 800, 400)

        # Set background image
        self.window.setStyleSheet(
            "background-image: url('background.png'); background-repeat: no-repeat; background-position: center;"
        )
        

        # Main layout
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.window.setLayout(self.layout)

         # Welcome label
        self.welcome_label = QLabel("Bienvenue...Veuillez entrer vos informations")
        self.welcome_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; color: #030303; margin-bottom: 20px; background-color :#F5EEDC"
        )
        self.layout.addWidget(self.welcome_label, alignment=Qt.AlignCenter)


        # Username input
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.username.setFixedWidth(300)
        self.username.setFixedHeight(40)
        self.username.setStyleSheet("""
    QLineEdit {
        font-size: 16px; /* Font size */
        font-weight: bold; /* Bold text */
        color: #333; /* Text color */
        background-color: #f9f9f9; /* Light gray background */
        border: 2px solid #007BFF; /* Blue border */
        border-radius: 10px; /* Rounded corners */
        padding: 5px; /* Padding inside the input */
    }
    QLineEdit:focus {
        border: 2px solid #0056b3; /* Darker blue border when focused */
        background-color: #ffffff; /* White background when focused */
    }
""")
        self.layout.addWidget(self.username, alignment=Qt.AlignCenter)

        # Password input
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFixedWidth(300)
        self.password.setFixedHeight(40)
        self.password.setStyleSheet("""
    QLineEdit {
        font-size: 16px; /* Font size */
        font-weight: bold; /* Bold text */
        color: #333; /* Text color */
        background-color: #f9f9f9; /* Light gray background */
        border: 2px solid #007BFF; /* Blue border */
        border-radius: 10px; /* Rounded corners */
        padding: 5px; /* Padding inside the input */
    }
    QLineEdit:focus {
        border: 2px solid #0056b3; /* Darker blue border when focused */
        background-color: #ffffff; /* White background when focused */
    }
""")
        self.layout.addWidget(self.password, alignment=Qt.AlignCenter)

        # Login button
        self.login = QPushButton("Login")
        self.login.setFixedWidth(150)
        self.login.setFixedHeight(40)
        self.login.setStyleSheet("""
            QPushButton {
                background-color: #007BFF; /* Blue background */
                color: black; /* Black text */
                font-size: 16px; /* Font size */
                font-weight: bold; /* Bold text */
                border-radius: 10px; /* Rounded corners */
                padding: 10px; /* Padding inside the button */
                border: 2px solid #0056b3; /* Blue border */
            }
            QPushButton:hover {
                background-color: #0056b3; /* Darker blue on hover */
                border: 2px solid #003f7f; /* Darker border on hover */
            }
            QPushButton:pressed {
                background-color: #003f7f; /* Even darker blue when pressed */
                border: 2px solid #001f3f; /* Even darker border when pressed */
            }
        """)
        self.login.clicked.connect(self.auth)
        self.layout.addWidget(self.login, alignment=Qt.AlignCenter)

        self.window.show()

    def auth(self):
        username = self.username.text()
        password = self.password.text()

        # Create an instance of DataManager
        data_manager = DataManager()
        print("Checking user credentials...")
        print("Username:", username)
        print("Password:", password)

        # Call the check_user method on the instance
        if data_manager.check_user(username, password):  
            print("Authentication successful!")
            self.window.close()
            self.main_window = Mainwindow()  # Ensure Mainwindow is correctly initialized
            self.main_window.show()  # Explicitly show the Mainwindow
        else:
            QMessageBox.critical(self.window, "Erreur", "Nom d'utilisateur ou mot de passe incorrect")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    auth_window = authentifcation()
    sys.exit(app.exec_())