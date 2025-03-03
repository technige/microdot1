from microdot import Microdot

sub_app = Microdot()


@sub_app.get("/<uuid:my_uuid>")
async def show_my_uuid(request, my_uuid):
    return f"Your UUID is {my_uuid}"
