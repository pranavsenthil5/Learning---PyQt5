from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from folium.plugins import Draw
import folium
import io
import sys
import json

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    m = folium.Map(location=[55.8527, 37.5689], zoom_start=13)
    m.get_root().script.add_child(Element(my_js))
    draw = Draw(
        draw_options={
            'polyline': False,
            'rectangle': True,
            'polygon': True,
            'circle': False,
            'marker': True,
            'circlemarker': False},
        edit_options={'edit': False})
    m.add_child(draw)

    data = io.BytesIO()
    m.save(data, close_file=False)

    class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
        def javaScriptConsoleMessage(self, level, msg, line, sourceID):
            coords_dict = json.loads(msg)
            coords = coords_dict['geometry']['coordinates'][0]
            print(coords_dict)
            # print(coords)

    view = QtWebEngineWidgets.QWebEngineView()
    page = WebEnginePage(view)
    view.setPage(page)
    view.setHtml(data.getvalue().decode())
    view.show()
    sys.exit(app.exec_())
