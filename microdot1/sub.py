from microdot import Microdot

sub_app = Microdot()


@sub_app.get("/<uuid:my_uuid>")
async def show_my_uuid(request, my_uuid):
    return f"Your {my_uuid.__class__.__name__} is {my_uuid}"
