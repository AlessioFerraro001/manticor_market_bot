import Controller
import Model
import View

ui = View.UI()
configs = (Model.Config())
configs.setConfigs("config.txt")
ui.internalBot = Controller.Bot(Model.Data(configs))
ui.start()
