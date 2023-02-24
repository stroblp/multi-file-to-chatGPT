import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QFileDialog, QVBoxLayout, QHBoxLayout, QWidget

class FolderSelectionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # set up window
        self.setWindowTitle("Folder Selection App")
        self.setGeometry(100, 100, 600, 100)

        # create button to open folder selection dialog
        self.select_folder_btn = QPushButton("Select Folder", self)
        self.select_folder_btn.clicked.connect(self.select_folder)

        # create entry widget to show selected folder path
        self.folder_entry = QLineEdit()

        # create start button
        self.start_btn = QPushButton("Start", self)
        self.start_btn.clicked.connect(self.start_processing)

        # create layout for widgets
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.folder_entry)
        hbox.addWidget(self.select_folder_btn)
        hbox.addWidget(self.start_btn)
        vbox.addLayout(hbox)

        # create main widget and set layout
        main_widget = QWidget(self)
        main_widget.setLayout(vbox)
        self.setCentralWidget(main_widget)

    def select_folder(self):
        # open folder selection dialog
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")

        # update folder path in entry widget
        self.folder_entry.setText(folder_path)

    def scan_files(self,work_dir, file_extensions):
        file_list = []
        for dirpath, dirnames, filenames in os.walk(work_dir):
            for filename in filenames:
                if filename.endswith(tuple(file_extensions)):
                    filepath = os.path.join(dirpath, filename)
                    relative_path = os.path.relpath(filepath, work_dir)
                    try:
                        with open(filepath, 'r') as file:
                            content = file.read()
                            file_list.append([relative_path, content])
                    except Exception as e:
                        file_list.append((relative_path, "error"))
                        # print(f"Error opening file {filepath}: {e}")

        return file_list        

    def start_processing(self):

        # get folder path from entry widget
        folder_path = self.folder_entry.text()
        file_data_list = self.scan_files(folder_path,["py","html","css","js","svelte"])

        # create layout for buttons
        hbox = QHBoxLayout()

        # add init button to layout
        button = QPushButton("init chat GPT", self)
        text_init = """
        I want you to act as a Senior software developer.
        I will paste multiple files to your promt. 
        I will write END to to your promt when I am ready with all files.
        Do not ask or epxlain anything until END.
        """ 
        button.clicked.connect(lambda checked, text=text_init: QApplication.clipboard().setText(text))
        hbox.addWidget(button)

        # create and add buttons to layout
        for index,file_data in enumerate(file_data_list):
            button = QPushButton(file_data[0], self)
            text_out = "This is the next file. Do not explaine.\nfile name:\n"+file_data[0]+"\nfile data:\n"+file_data[1]
            button.clicked.connect(lambda checked, text=text_out: QApplication.clipboard().setText(text))
            hbox.addWidget(button)


        # set layout for buttons
        buttons_widget = QWidget(self)
        buttons_widget.setLayout(hbox)

        # add buttons widget to main layout
        main_layout = self.centralWidget().layout()
        main_layout.addWidget(buttons_widget)



# create Qt application
app = QApplication([])

# create instance of FolderSelectionApp
window = FolderSelectionApp()
window.show()

# start Qt event loop
app.exec_()

