from PySide.QtGui import *

class GraphWidget(QGraphicsView):
    def __init__(self):
        QGraphicsView.__init__(self)
        scene = QGraphicsScene(self)
        self.setScene(scene)

        imageLabel = QLabel()
        self.image = QImage("centroid_rmsd_vs_phi.png")
        imageLabel.setPixmap(QPixmap.fromImage(self.image))

        scene.addWidget(imageLabel)
        self.show()



if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    frame = GraphWidget()
    sys.exit(app.exec_())


    '''
    have a look at:

    http://stackoverflow.com/questions/35508711/how-to-enable-pan-and-zoom-in-a-qgraphicsview
    '''
