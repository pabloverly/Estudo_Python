from logging import DEBUG
from kivymd.tools.hotreload.app import MDApp
from kivy.lang import Builder
 

class HotReload(MDApp):
    KV_FILES = ["app/pomodoro.kv"]
    DEBUG = True
    def build_app(self):
        return Builder.load_file('app/pomodoro.kv')

HotReload().run()