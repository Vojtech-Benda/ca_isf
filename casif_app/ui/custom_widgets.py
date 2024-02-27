from math import sqrt
import PySide6.QtCore as qtc
import PySide6.QtWidgets as qtw
import PySide6.QtGui as qtg


class GraphicsView(qtw.QGraphicsView):
    def __init__(self, *args, **kwargs):
        super(GraphicsView, self).__init__(*args, **kwargs)
        self.start_point = None
        self.end_point = None
        self._line = None
        self.graphics_line = None
        self.length_text = None
        self.labm_x_pos = None
        self.labm_y_pos = None
        self.pixel_spacing = None
        self.painting_flag = False
        self.points = []

        self.setMouseTracking(True)
        self.setScene(GraphicsScene())
        self.setSceneRect(0, 0, self.width(), self.height())
        self.setRenderHint(qtg.QPainter.RenderHint.Antialiasing)

    def set_pos_label(self, labm_x_pos: qtw.QLabel, labm_y_pos: qtw.QLabel):
        self.labm_x_pos = labm_x_pos
        self.labm_y_pos = labm_y_pos

    def set_painting_flag(self, flag: bool):
        if flag:
            self.painting_flag = flag
            self.setCursor(qtc.Qt.CursorShape.CrossCursor)
"""
    def mouseMoveEvent(self, event: qtg.QMouseEvent) -> None:
        super().mouseMoveEvent(event)

        cursor_pos = self.mapToScene(event.position().toPoint())
        self.labm_x_pos.setText(f"{int(cursor_pos.x())}")
        self.labm_y_pos.setText(f"{int(cursor_pos.y())}")

        if self.painting_flag:
            if event.buttons() == qtc.Qt.MouseButton.LeftButton:
                mouse_pos = self.mapToScene(event.position().toPoint())
                self.end_point = mouse_pos
                self.scene().addItem(self.length_text.update_text(self._line))
                self.length_text.update_pos(self._line)

                self.update_line()

    def mousePressEvent(self, event: qtg.QMouseEvent) -> None:
        super().mousePressEvent(event)

        if len(self.points) == 2:
            self.points.clear()

        if self.painting_flag:
            if event.button() == qtc.Qt.MouseButton.LeftButton:
                mouse_pos = self.mapToScene(event.position().toPoint())
                self.start_point = mouse_pos
                self.end_point = self.start_point

                self._line = qtc.QLineF(self.start_point, self.end_point)
                self.graphics_line = Connection(self._line)
                self.length_text = LengthText(self.pixel_spacing)
                self.update_line()

                point = Point(mouse_pos.x(), mouse_pos.y())
                self.scene().addItem(point)
                self.points.append(mouse_pos)

                self.points.append(mouse_pos)

    def mouseReleaseEvent(self, event: qtg.QMouseEvent) -> None:
        super().mouseReleaseEvent(event)

        if self.painting_flag:
            mouse_pos = self.mapToScene(event.position().toPoint())
            self.end_point = mouse_pos
            self.update_line()

            point = Point(mouse_pos.x(), mouse_pos.y())
            self.scene().addItem(point)

        if len(self.points) == 2:
            self.setCursor(qtc.Qt.CursorShape.ArrowCursor)
            self.painting_flag = False

    def update_line(self):
        if self.painting_flag:
            if not self.start_point.isNull() and not self.end_point.isNull():
                self._line.setP2(self.end_point)
                self.graphics_line.setLine(self._line)
                self.scene().addItem(self.graphics_line)

    def get_point_list(self):
        return self.points

    def set_image_metadata(self, metadata):
        self.pixel_spacing = metadata["pixel_spacing"]
"""

class GraphicsScene(qtw.QGraphicsScene):
    def __init__(self):
        super(GraphicsScene, self).__init__()


class Point(qtw.QGraphicsEllipseItem):
    def __init__(self, x=None, y=None):
        super().__init__()

        self.setRect(0, 0, 6, 6)
        self.setPos(x - 3, y - 3)
        self.setPen(Pens().point_edge_pen)
        self.setBrush(Pens().point_fill_pen)
        # FIXME: scale points and lines (lines temporarily fixed) to graphics view


class Connection(qtw.QGraphicsLineItem):
    def __init__(self, line: qtc.QLineF):
        super().__init__(line)

        self.start_pos = line.p1().toPoint()
        self.end_pos = line.p2().toPoint()
        self.setPen(Pens().point_edge_pen)


class LengthText(qtw.QGraphicsTextItem):
    def __init__(self, px_spacing):
        super().__init__()
        self.px_spacing = px_spacing

        self.setDefaultTextColor(qtg.QColor("red"))
        self._font = qtg.QFont(self.font().family(), 12)
        self._font.setWeight(qtg.QFont.Weight.DemiBold)
        self.setFont(self._font)
        self.setFlags(self.GraphicsItemFlag.ItemIgnoresTransformations)

    def update_text(self, line: qtc.QLineF):
        # FIXME: length text position
        length_x = (int(line.p2().x() - line.p1().x())) * self.px_spacing[0]
        length_y = (int(line.p2().y() - line.p1().y())) * self.px_spacing[1]
        length = sqrt((length_x ** 2) + (length_y ** 2))
        self.setPlainText(f"{length:.2f} mm")

        self.setTransformOriginPoint(self.boundingRect().center())
        return self

    def update_pos(self, line: qtc.QLineF):
        line_angle = line.angle()

        # position the text
        if 0.0 <= line_angle <= 90.0:  # upper left corner
            self.setPos(line.center())

        elif 90.0 < line_angle <= 180.0:  # lower left corner
            self.setPos(line.center().x(),
                        line.center().y() - self.boundingRect().height() - 100)

        elif 180.0 < line_angle <= 270.0:  # lower right corner
            self.setPos(line.center().x() - self.boundingRect().width() - 300,
                        line.center().y() - self.boundingRect().height() - 100)

        elif 270.0 < line_angle <= 360.0:  # lower left corner
            self.setPos(line.center().x(),
                        line.center().y() - self.boundingRect().height() - 100)


class Pens:
    def __init__(self):
        self.point_edge_pen = qtg.QPen(qtg.QColor("red"))
        self.point_fill_pen = qtg.QBrush(qtg.QColor("red"))
        self.point_edge_pen.setWidthF(1.5)
        self.point_edge_pen.setCosmetic(True)  # scales lines relative to graphics view
