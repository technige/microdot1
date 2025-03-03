from uuid import UUID

from microdot import Microdot
from microdot.microdot import URLPattern

from microdot1.sub import sub_app

app = Microdot()
URLPattern.register_type("uuid", pattern="[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}", parser=UUID)


@app.get("/")
async def get_home(request):
    return "Home page"


app.mount(sub_app, url_prefix="/sub")
