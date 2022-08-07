import sys
import io
import json

import folium
from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QTextEdit, QWidget
#from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

#url = "https://google.com"

app = QApplication(sys.argv)

geo_json_map = json.load(open('sample.geojson'))
# m = folium.Map(
#     # location=[45.5236, -122.6750], tiles="Stamen Toner", zoom_start=13
#     location=[38.8709, -77.0558],  zoom_start=25, geo_data=geo_json_map
# )

m = folium.Map(location=[24.2170111233401, 81.0791015625000],
               zoom_start=5)

folium.Rectangle(
    [(28.6471948, 76.9531796), (19.0821978, 72.7411)]).add_to(m)

data = io.BytesIO()
m.save(data, close_file=False)

w = QMainWindow()

browser = QWebEngineView()
browser.setHtml(data.getvalue().decode())
# browser.setHtml('''
# <iframe width="600" height="450" style="border:0" loading="lazy" allowfullscreen
#         referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps/embed/v1/place?key=AIzaSyC8mgtCvBNbSdgortZ3HfWF_G8KhpPfilI
#     &q=Space+Needle,Seattle+WA">
# </iframe>
# ''')


# browser.setHtml('''
# <style>
#   .google-maps {
#     position: relative;
#     padding-bottom: 75%; // This is the aspect ratio
#     height: 0;
#     overflow: hidden;
#   }
#   .google-maps iframe {
#     position: absolute;
#     top: 0;
#     left: 0;
#     width: 100% !important;
#     height: 100% !important;
#   }
# </style>

# <div class="google-maps">
#   <iframe
#     src="https://www.google.com/maps/embed/v1/place?key=AIzaSyC8mgtCvBNbSdgortZ3HfWF_G8KhpPfilI&q=Shenandoah+County,+VA"
#     width=100%
#     height=100%
#     style="border:0;"
#     allowfullscreen=""
#     loading="lazy"
#   ></iframe>
# </div>
# ''')
central_widget = QWidget()
w.setCentralWidget(central_widget)

lay = QGridLayout(central_widget)
lay.addWidget(browser, 0, 0, 2, 1)
lay.addWidget(QTextEdit(), 0, 1)
lay.addWidget(QTextEdit(), 1, 1)

lay.setColumnStretch(0, 1)
lay.setColumnStretch(1, 1)

lay.setRowStretch(0, 1)
lay.setRowStretch(1, 1)

w.show()

sys.exit(app.exec_())
