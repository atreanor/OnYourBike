from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('OnYourBike', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


template = env.get_template('mytemplate.html')

print (template.render(the='variables', go='here'))