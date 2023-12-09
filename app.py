from litestar import Litestar, get
from pathlib import Path
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig
from litestar.response import Template
from controllers.user import UserController
from litestar.static_files.config import StaticFilesConfig

@get(path="/", sync_to_thread=False)
def index(name: str = "Chris") -> Template:
    data_object = { 
        "title": "Cedar Rapids",
        "rating": "R",
        "image": "https://www.searchlightpictures.com/media/original_images/poster-d7c5c294-7732-4dd9-8356-e15b22b3e87c.jpg",
        "trailer": "https://www.youtube.com/embed/d7LkZwnfwfc?si=MgsK2HkX_JROqona"
        }
    return Template(template_name="hello.html.jinja2", context={"name": name, "data_object": data_object})


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}

app = Litestar(
    route_handlers=[index, UserController],
    template_config=TemplateConfig(
        directory=Path("templates"),
        engine=JinjaTemplateEngine,
        ),
        static_files_config=[
            StaticFilesConfig(directories=["static"], path="/static"),
            StaticFilesConfig(directories=["html"], path="/html", html_mode=True),
        ],
    )

# app = Litestar([index, get_book])