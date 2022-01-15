def transponders(ident):
    crafts = len(ident)
    crafts = str(crafts)
    dspycraft = crafts + " aircraft(s) in sight."
    for idents in ident:
        msg = "Displayed \"" + idents + "\"."
        print(msg)
    print(dspycraft)
    if "CSN3456" not in ident:
        print("\"3456复飞了\"")
    else:
        print("\"速度大点没事\"")


ident = ['CSN8888', 'CSN3456', 'CSN7777']
transponders(ident)

built_models = ["A220", "A320", "A330"]
rendered_models = []


def rendering_models(built, rendered):
    while built:
        output_models = built_models.pop()

        print("Rendering: " + "\"" + output_models + "\"")
        rendered_models.append(output_models)


def show_rendered(rendered_models):
    for comp in rendered_models:
        print("Completed rendering model: " + "\"" + comp + "\"")


rendering_models(built_models, rendered_models)
show_rendered(rendered_models)
