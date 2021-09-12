# SPDX-License-Identifier: CC0-1.0

from PyQt5.QtWidgets import QDialog


class TwentyBrushesDialog(QDialog):

    def __init__(self, uitwentybrushes, parent=None):
        super(TwentyBrushesDialog, self).__init__(parent)

        self.uitwentybrushes = uitwentybrushes

    def accept(self):
        self.uitwentybrushes.twentybrushes.writeSettings()

        super(TwentyBrushesDialog, self).accept()

    def closeEvent(self, event):
        event.accept()
