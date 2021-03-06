from kivy.lang.builder import Builder

from kivymd.uix.screen import MDScreen

from akivymd.uix.imageview import AKImageViewer, AKImageViewerItem

Builder.load_string(
    """
<ImageViewer>
    name: "ImageViewer"

    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: root.name
            left_action_items: [["arrow-left", lambda x: app.show_screen("Home", "back")]]

        MDFloatLayout:

            MDRaisedButton:
                text:"Open Viewer"
                on_release: root.open()
                pos_hint: {"center_x": .5, "center_y": .5}
"""
)


class ImageViewer(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.viewer = AKImageViewer()
        images = ["assets/google.jpg", "assets/logo.png", "assets/fly.jpg"]

        for image in images:
            self.viewer.add_widget(AKImageViewerItem(source=image))

    def open(self):
        self.viewer.open()
