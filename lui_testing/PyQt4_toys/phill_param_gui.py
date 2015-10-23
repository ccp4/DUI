
from __future__ import division
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QTreeView
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QStandardItemModel
from PyQt4.QtGui import QSortFilterProxyModel
from PyQt4.QtGui import QStandardItem
from PyQt4.QtGui import QAbstractItemView
from PyQt4.QtGui import QHeaderView
from PyQt4.QtGui import QStyledItemDelegate
from PyQt4.QtGui import QSpinBox
from PyQt4.QtGui import QDoubleSpinBox
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QComboBox
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QSize
from PyQt4.QtCore import QString
from PyQt4.QtCore import QRegExp
from PyQt4.QtCore import QModelIndex


class StringEditor(QLineEdit):

  def __init__(self, parent=None):
    super(StringEditor, self).__init__(parent)

  def setEditorData(self, index):
    value = index.model().data(index, Qt.EditRole).toString()
    self.setText(value)

  def setModelData(self, model, index):
    value = self.text()
    model.setData(index, value, Qt.EditRole)


class IntEditor(QSpinBox):

  def __init__(self, parent=None, value_min=None, value_max=None):
    super(IntEditor, self).__init__(parent)
    if value_min is not None:
      self.setMinimum(value_min)
    else:
      self.setMinimum(-1e9)
    if value_max is not None:
      self.setMaximum(value_max)
    else:
      self.setMaximum(1e9)

  def setEditorData(self, index):
    value = index.model().data(index, Qt.EditRole).toInt()
    self.setValue(value[0])

  def setModelData(self, model, index):
    self.interpretText()
    value = self.value()
    model.setData(index, value, Qt.EditRole)


class FloatEditor(QDoubleSpinBox):

  def __init__(self, parent=None, value_min=None, value_max=None):
    super(FloatEditor, self).__init__(parent)
    if value_min is not None:
      self.setMinimum(value_min)
    else:
      self.setMinimum(-1e9)
    if value_max is not None:
      self.setMaximum(value_max)
    else:
      self.setMaximum(1e9)
    self.setDecimals(2)

  def setEditorData(self, index):
    value = index.model().data(index, Qt.EditRole).toFloat()
    self.setValue(value[0])

  def setModelData(self, model, index):
    self.interpretText()
    value = self.value()
    model.setData(index, value, Qt.EditRole)


class ChoiceEditor(QComboBox):

  def __init__(self, parent=None, choices=None):
    super(ChoiceEditor, self).__init__(parent)
    if choices is not None:
      for choice in choices:
        self.addItem(choice)

  def setEditorData(self, index):
    value = index.model().data(index, Qt.EditRole).toString()
    self.setCurrentIndex(self.findText(value))

  def setModelData(self, model, index):
    value = self.currentText()
    model.setData(index, value, Qt.EditRole)


class BoolEditor(QComboBox):

  def __init__(self, parent=None):
    super(BoolEditor, self).__init__(parent)
    self.addItem("False")
    self.addItem("True")

  def setEditorData(self, index):
    value = index.model().data(index, Qt.EditRole).toString()
    self.setCurrentIndex(self.findText(value))

  def setModelData(self, model, index):
    value = self.currentText()
    model.setData(index, value, Qt.EditRole)


class ParameterItemDelegate(QStyledItemDelegate):

  def __init__(self, parent=None):

    super(ParameterItemDelegate, self).__init__(parent)

  def createEditor(self, parent, option, index):
    parameter = index.model().data(index, Qt.UserRole+1).toPyObject()
    dtype = parameter.type
    ptype = dtype.phil_type
    if ptype == 'str':
      editor = StringEditor(parent)
    elif ptype == 'float':
      editor = FloatEditor(parent, dtype.value_min, dtype.value_max)
    elif ptype == 'int':
      editor = IntEditor(parent, dtype.value_min, dtype.value_max)
    elif ptype == 'choice':
      def strip(w):
        w = str(w)
        if w.startswith("*"):
          return w[1:]
        return w
      choices = [strip(w) for w in parameter.words]
      editor = ChoiceEditor(parent, choices)
    elif ptype == 'bool':
      editor = BoolEditor(parent)
    else:
      raise RuntimeError("Handle type %s" % dtype)
    return editor

  def setEditorData(self, editor, index):
    editor.setEditorData(index)

  def setModelData(self, editor, model, index):
    editor.setModelData(model, index)

  def updateEditorGeometry(self, editor, option, index):
    editor.setGeometry(option.rect)

  def sizeHint(self, option, index):
    size = super(ParameterItemDelegate, self).sizeHint(option, index)
    size.setWidth(size.width() * 1.5)
    size.setHeight(size.height() * 2)
    return size


class ParameterItemModel(QStandardItemModel):

  def __init__(self, parameters=None):
    super(ParameterItemModel, self).__init__()
    self.setParameters(parameters)

  def setParameters(self, parameters):

    # Save the parameters
    self.parameters = parameters

    # Clear the model
    self.clear()

    # Traverse the parameter tree and add to the tree view widget
    def add_parameters(root, parameter):
      if parameter.is_scope:
        name_node = QStandardItem(parameter.name)
        name_node.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        name_node.setData(parameter, Qt.UserRole + 1)
        for obj in parameter.objects:
          add_parameters(name_node, obj)
        root.appendRow(name_node)
      elif parameter.is_definition:
        name_node = QStandardItem(parameter.name)
        name_node.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        name_node.setData(parameter, Qt.UserRole + 1)
        value_node = QStandardItem(str(parameter.extract()))
        value_node.setData(parameter, Qt.UserRole + 1)
        root.appendRow([name_node, value_node])
      else:
        raise RuntimeError('Handle This!')

    # Populate the tree
    if parameters is not None:
      for obj in parameters.objects:
        add_parameters(self, obj)

  def getParameters(self):
    return self.parameters

  def data(self, index, role=Qt.DisplayRole):
    if role == Qt.ToolTipRole:
      parameter = index.model().data(index, Qt.UserRole+1).toPyObject()
      if parameter is None:
        return ""
      return str(parameter.help)
    return super(ParameterItemModel, self).data(index, role)


class ParameterSortFilterProxyModel(QSortFilterProxyModel):

  def __init__(self, parent=None):

    super(ParameterSortFilterProxyModel, self).__init__(parent)
    self.setFilterKeyColumn(0)

    self.expert_level = 0
    self.search_string = ''
    self.string_filter_cache = {}

  def setExpertLevel(self, level):
    self.expert_level = level
    self.invalidateFilter()

  def setSearchString(self, text):
    self.search_string = text
    self.invalidateFilter()

  def invalidateFilter(self):

    # Empty the string filter cache
    self.string_filter_cache = {}

    # Get the model
    model = self.sourceModel()

    # Recursive function to traverse the tree of nodes.
    # If a child matches the search string, keep the parent
    def update_string_filter_cache(model, parent):
      show_parent = False
      for row in range(model.rowCount(parent)):
        index = model.index(row, 0, parent)
        parameter = model.data(index, Qt.UserRole+1).toPyObject()
        name = parameter.full_path()
        if model.hasChildren(index):
          show = update_string_filter_cache(model, index)
        else:
          show = str(self.search_string) in name
        self.string_filter_cache[name] = show
        show_parent = show_parent or show
      return show_parent

    # Update the string filter cache
    update_string_filter_cache(model, QModelIndex())

    # Call the parent method
    super(ParameterSortFilterProxyModel, self).invalidateFilter()

  def filterAcceptsRow(self, row, parent):

    # Get the index
    index = self.sourceModel().index(row, 0, parent)

    # Get the parameter
    parameter = index.model().data(index, Qt.UserRole+1).toPyObject()

    # Get the expert level
    expert = parameter.expert_level
    if expert is None:
      expert = 0

    # Check the expert level
    if self.expert_level == 0 and expert > 0:
      return False

    # Check the string filter cache
    if self.string_filter_cache[parameter.full_path()] == False:
      return False

    # Otherwise OK
    return True


class ParameterTreeView(QTreeView):

  def __init__(self, parent=None):

    super(ParameterTreeView, self).__init__(parent)
    self.setItemDelegate(ParameterItemDelegate())
    self.setAlternatingRowColors(True)
    self.setSortingEnabled(False)
    self.setHeaderHidden(True)
    self.setAnimated(True)
    self.setSelectionBehavior(QAbstractItemView.SelectItems)
    self.setEditTriggers(QAbstractItemView.AllEditTriggers)
    self.setIndentation(30)


class ParameterTreeWidget(QWidget):

  def __init__(self, parent=None, parameters=None):

    # Init the parent
    super(ParameterTreeWidget, self).__init__(parent)

    # Create the model
    model = ParameterItemModel(parameters)

    # Create a parameter tree
    self.tree = ParameterTreeView()

    # Create the filter model
    filter_model = ParameterSortFilterProxyModel()
    filter_model.setSourceModel(model)
    filter_model.setExpertLevel(0)

    # Set the model in the tree
    self.tree.setModel(filter_model)

    # Set the header mode
    self.tree.header().setStretchLastSection(True)
    self.tree.header().setResizeMode(0, QHeaderView.ResizeToContents)

    # Start everything expanded
    self.tree.expandAll()

    # Create the layout
    layout = QVBoxLayout()
    layout.setMargin(0)
    layout.addWidget(self.tree)
    self.setLayout(layout)

  def setExpertLevel(self, level):
    self.tree.model().setExpertLevel(level)

  def setSearchString(self, text):
    self.tree.model().setSearchString(text)


class ParameterWidget(QWidget):

  def __init__(self, parent=None, parameters=None):

    super(ParameterWidget, self).__init__(parent)

    # Create the parameter window widget
    self.params = ParameterTreeWidget(None, parameters)

    # Create the search widget
    self.search = QLineEdit()
    self.search.setPlaceholderText("Search...")
    self.search.textChanged.connect(self.params.setSearchString)

    # Create the expert level widget
    self.expert = QComboBox()
    self.expert.addItem("Simple")
    self.expert.addItem("Advanced")
    self.expert.currentIndexChanged.connect(self.params.setExpertLevel)

    # Layout the controls
    control_layout = QHBoxLayout()
    control_layout.addWidget(self.expert)
    control_layout.addWidget(self.search)

    # Create the widget layout
    main_layout = QVBoxLayout()
    main_layout.addLayout(control_layout)
    main_layout.addWidget(self.params)
    self.setLayout(main_layout)

  def setParameters(self, parameters):
    self.params.setParameters(parameters)

  def setExpertLevel(self, level):
    self.params.setExpertLevel(level)


class IntegrateParameterWidget(ParameterWidget):

  def __init__(self, parent=None):
    from dials.command_line.integrate import phil_scope

    # Init parent
    super(IntegrateParameterWidget, self).__init__(parent, phil_scope)


class MainWindow(QMainWindow):

  def __init__(self, parent=None):

    # Call the parent constructor
    super(MainWindow, self).__init__(parent)

    # Create the parameter window widget
    params = IntegrateParameterWidget()

    # Create the window layout
    layout = QVBoxLayout()
    layout.addWidget(params)

    # Setup the window contents
    window = QWidget()
    window.setLayout(layout)
    self.setCentralWidget(window)


if __name__ == '__main__':
  import sys

  # Create the application
  app = QApplication(sys.argv)

  # Create the main window
  window = MainWindow()
  window.resize(800, 600)
  window.show()

  # Execute the application
  sys.exit(app.exec_())





'''

class ExportPage(QtGui.QWidget):

    def __init__(self, parent = None):
        super(ExportPage, self).__init__(parent)


        self.cmd_lin_default = "dials.export integrated.pickle integrated.h5"
        self.button_label = "Export"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/bird_dartlang_logo_small.png"

        startQueryButton = QtGui.QPushButton("Bttn tst")
        mainLayout = QtGui.QVBoxLayout()

        mainLayout.addWidget(startQueryButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)



if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    #ex = ImportPage()
    #ex = SpotFindPage()
    #ex = IndexPage()
    #ex = RefinePage()
    ex = IntegratePage()
    #ex = ExportPage()

    ex.show()
    sys.exit(app.exec_())




'''


