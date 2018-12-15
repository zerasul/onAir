
class Renderer:
    templatepath = None

    def __init__(self, path="."):
        self.templatepath=path

    def render_template(self, template_name=None, args={}):
        f = open(self.templatepath+"/"+template_name)
        tempcontent = f.readlines()
        strcom = ''
        for line in tempcontent:
            strcom = strcom + line
        for key in args.keys():
            strcom.replace("${"+key+"}", args[key])
        return strcom
