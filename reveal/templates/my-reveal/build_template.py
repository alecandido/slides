import pathlib

from jinja2 import Environment, FileSystemLoader
import frontmatter


def main(here):
    # prepare environment
    # -------------------

    env = Environment(loader=FileSystemLoader(str(here)))

    # load data
    # ---------

    data = {}

    class Slide:
        def __init__(self, metadata, content):
            self.metadata = metadata
            self.content = content

    slides_dir = here / "src" / "slides"
    slides = []
    slides_paths = sorted(list(slides_dir.glob("*")))
    for slide_path in slides_paths:
        with open(slide_path) as f:
            metadata, content = frontmatter.parse(f.read())

        slide = Slide(metadata, content)
        slides.append(slide)

    data["slides"] = slides

    # dump the result
    # ---------------

    template = env.get_template("template.html")
    stream = template.stream(data)
    stream.dump(str(here / "index.html"))


if __name__ == "__main__":
    here = pathlib.Path(__file__).resolve().parent

    main(here)
