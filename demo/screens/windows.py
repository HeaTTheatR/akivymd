from kivy.lang.builder import Builder

from kivymd.uix.screen import MDScreen

Builder.load_string(
    """
<MyWindow@AKFloatingWindow>
    size_hint: None, None
    size: dp(300), dp(300)
    orientation: "vertical"


<Windows>
    name: "Windows"

    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            id: toolbar
            title: root.name
            left_action_items: [["arrow-left", lambda x: app.show_screen("Home", "back")]]

        MDBoxLayout:
            spacing: dp(10)
            MDRaisedButton:
                text: "open_window 1"
                on_release: window1.open()

            MDRaisedButton:
                text: "open_window 2"
                on_release: window2.open()

    AKFloatingWindowLayout:

        MyWindow:
            id: window2
            window_title: "Window 2"
            top_widget: toolbar

            MDLabel:
                text: "MyLabel"
                halign: "center"
                valign: "center"

        MyWindow:
            id: window1
            window_title: "Window 1"

            MDRaisedButton:
                text: "Button"
                pos_hint: {"center_x": .5, "center_y": .5}
"""
)


class Windows(MDScreen):
    pass
