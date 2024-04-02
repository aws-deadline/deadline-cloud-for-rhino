# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
from PySide2.QtCore import QSize, Qt  # type: ignore
from PySide2.QtWidgets import (  # type: ignore
    QCheckBox,
    QComboBox,
    QFileDialog,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QWidget,
)
from deadline.client.ui import block_signals

"""
UI widgets for the Scene Settings tab.
"""


class FileSearchLineEdit(QWidget):
    """
    Widget used to contain a line edit and a button which opens a file search box.
    """

    def __init__(self, file_format=None, directory_only=False, parent=None):
        super().__init__(parent=parent)

        if directory_only and file_format is not None:
            raise ValueError("")

        self.file_format = file_format
        self.directory_only = directory_only

        lyt = QHBoxLayout(self)
        lyt.setContentsMargins(0, 0, 0, 0)
        lyt.setMargin(0)

        self.edit = QLineEdit(self)
        self.btn = QPushButton("...", parent=self)
        self.btn.setMaximumSize(QSize(100, 40))
        self.btn.clicked.connect(self.get_file)

        lyt.addWidget(self.edit)
        lyt.addWidget(self.btn)

    def get_file(self):
        """
        Open a file picker to allow users to choose a file.
        """
        if self.directory_only:
            new_txt = QFileDialog.getExistingDirectory(
                self,
                "Open Directory",
                self.edit.text(),
                QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
            )
        else:
            new_txt = QFileDialog.getOpenFileName(self, "Select File", self.edit.text())

        if new_txt:
            self.edit.setText(new_txt)

    def setText(self, txt: str) -> None:  # pylint: disable=invalid-name
        """
        Sets the text of the internal line edit
        """
        self.edit.setText(str(txt))

    def text(self) -> str:
        """
        Retrieves the text from the internal line edit.
        """
        return self.edit.text()


class SceneSettingsWidget(QWidget):
    """
    Widget containing all top level scene settings.
    """

    def __init__(self, initial_settings, parent=None):
        super().__init__(parent=parent)
        self.all_views = initial_settings.all_views
        self._build_ui(initial_settings)
        self._configure_settings(initial_settings)

    def _build_ui(self, settings):
        lyt = QGridLayout(self)
        self.op_path_txt = FileSearchLineEdit(directory_only=True)
        lyt.addWidget(QLabel("Output Path"), 1, 0)
        lyt.addWidget(self.op_path_txt, 1, 1)
        self.views_box = QComboBox(self)
        lyt.addWidget(QLabel("Views"), 2, 0)
        lyt.addWidget(self.views_box, 2, 1)

        self.frame_override_chck = QCheckBox("Override Frame Range", self)
        self.frame_override_txt = QLineEdit(self)
        lyt.addWidget(self.frame_override_chck, 3, 0)
        lyt.addWidget(self.frame_override_txt, 3, 1)
        self.frame_override_chck.stateChanged.connect(self.activate_frame_override_changed)
        self.bongo_chk = QCheckBox("Bongo", self)
        lyt.addWidget(self.bongo_chk, 4, 0)
        lyt.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding), 12, 0)
        self._fill_views_box(0)

    def _fill_views_box(self, _):
        with block_signals(self.views_box):
            saved_view = self.views_box.currentData()
            self.views_box.clear()
            for n in self.all_views:
                self.views_box.addItem(n, n)
            index = self.views_box.findData(saved_view)
            if index >= 0:
                self.views_box.setCurrentIndex(index)

    def _configure_settings(self, settings):
        self.op_path_txt.setText(settings.output_file_path)
        self.frame_override_chck.setChecked(settings.override_frame_range)
        self.frame_override_txt.setEnabled(settings.override_frame_range)
        self.frame_override_txt.setText(settings.frame_list)
        index = self.views_box.findData(settings.view_selection)
        if index >= 0:
            self.views_box.setCurrentIndex(index)

    def update_settings(self, settings):
        """
        Update a scene settings object with the latest values.
        """
        settings.output_file_path = self.op_path_txt.text()
        settings.override_frame_range = self.frame_override_chck.isChecked()
        settings.frame_list = self.frame_override_txt.text()

    def activate_frame_override_changed(self, state):
        """
        Set the activated/deactivated status of the Frame override text box
        """
        self.frame_override_txt.setEnabled(state == Qt.Checked)
