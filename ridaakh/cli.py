import click
import pathlib
import pkgutil
from jinja2 import Template
import os
import shutil

LIB_REPO= "https://github.com/ridaakh/ridaakhfw"
DOCS= "https://ridaakh.com"

def _get_template(name: str) -> Template:
    path = str(pathlib.Path("templates", name))
    content: bytes = pkgutil.get_data("ridaakh_cli", path)
    if content is None:
        raise ValueError(f"Template not found: {name}")
    return Template(content.decode("utf-8"))


class Writer:
    CREATE = click.style("CREATE", fg="green")

    def __init__(self, dry: bool):
        self.dry = dry

    def mkdir(self, path: pathlib.Path, **kwargs):
        if not self.dry:
            try:
                path.mkdir(**kwargs)
            except FileExistsError as exc:
                if path == pathlib.Path.cwd():
                    return
                raise exc from None

        click.echo(f"{self.CREATE} {path}")

    def writerfile(self, path: pathlib.Path, content: str):
        if path.exists():
            return
        if not self.dry:
            with open(str(path), "w", encoding="utf-8") as f:
                f.write(content)
                f.write("\n")

        nbytes = len(content.encode())
        click.echo(f"{self.CREATE} {path} ({nbytes} bytes)")

class Project:
    def __init__(
            self, location: pathlib.Path, name: str, package: str, 
            writer: Writer
        ):
        self.location = location.absolute()
        self.name = name
        self.package = package
        self.package_root = (self.location / self.package).absolute()
        self._writer = writer

    def _get_template_context(self) -> dict:
        return {
                "name": self.name,
                "package": self.package,
                "version": '1.0.0',
                }
    def _apply_templates(self, names, root: pathlib.Path):
        context = self._get_template_context()
        for name in names:
            template_name = f"{name}.jinja"
            content = _get_template(template_name).render(context)
            path = pathlib.Path(root, name)
            self._writer.writefile(path, content)

    def _create_dirs(self):
        self._writer.mkdir(self.location)
        self._writer.mkdir(self.package_root)

    def _create_meta(self):
        self._apply_templates(
            [ "templates"], root=self.location
        )
    
    def _create_package(self):
        self._apply_templates(
            [
                "__init__.py",
                "app.py",
                "asgi.py",
                "settings.py",
                "providerconf.py",
            ],
            root=self.package_root,
        )

    def _after_success(self):
        click.echo("\n ---- \n")
        click.echo(f"Success !!  ✨🌟✨ Created {self.name} at {self.location}")
        click.echo()
        click.echo("To get help about ridaakh, visit the docs: ")
        click.echo(DOCS)
    
        
        click.echo()
        click.echo("If you like it, give it a star" )
        click.echo(LIB_REPO)

        click.echo()
        click.echo("Happy coding! 🥪")


    def create(self):
        self._create_dirs()
        self._create_meta()
        self._create_package()
        self._after_success()

@click.group()
@click.version_option(
        prog_name = "ridaakh",
        message=  f"sss"
        )
def cli():
    print("This is main function of cli")

def add_package_param(ctx: click.Context, param: str, value: str) -> str:
    package = value.replace("-", "_")

    if not package.isidentifier():
        raise click.BadParameter(
            f"{package} is not a valid Python identifier. "
            "Please use another project name."
        )

    ctx.params["package"] = package

    return value


@cli.command()
@click.argument("name", callback= add_package_param)
@click.option(
        "-d",
        "--directory",
        type= click.Path(file_okay= False),
        help = (
            "Directory where the project should be created."
            "Created if doesnot exist"
            "Defauts to name"
            ),
        )
@click.option(
        "--dry",
        is_flag = True,
        default = False,
        help= "Dry mode: doesnot write anything",
        )

def create(name: str, package: str, directory: str, dry: bool):
    """Initialize a Bocadillo project."""
    if directory is None:
        directory= name


    if dry:
        click.secho(
                "Warning: running in dry mode. Nofiles will be written",
                fg= "yellow",
                )
        project = Project(
                location= pathlib.Path(directory),
                name= name,
                package = package,
                writer = Writer(dry= dry),
                )
        project.create()




@cli.command()
def do():
    def copytree(src="environment", dst="../", symlinks= False, ignore=None):
        for item in os.listdir(src):
            s= os.path.join(src, item)
            d= os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)
    copytree()
if __name__ == '__main__':
    cli()

