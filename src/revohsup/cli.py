import logging
import typer

from typing import Annotated

from .message import send_message

log = logging.getLogger(__name__)

app = typer.Typer()


@app.command("message")
def _message(
    message: Annotated[str, typer.Argument(help="The message to send")],
    image_path: Annotated[
        str,
        typer.Option(
            help="Path to an image to send with the message", show_default=False
        ),
    ] = None,
    title: Annotated[
        str, typer.Option(help="The title of the message", show_default=False)
    ] = None,
    url: Annotated[
        str, typer.Option(help="A URL to include with the message", show_default=False)
    ] = None,
    url_title: Annotated[
        str, typer.Option(help="The title of the URL", show_default=False)
    ] = None,
    priority: Annotated[
        int,
        typer.Option(
            help="The priority of the message (-2 to 2)",
            show_default=False,
            min=-2,
            max=2,
        ),
    ] = None,
    timestamp: Annotated[
        int,
        typer.Option(
            help="The timestamp of the message (Unix timestamp)", show_default=False
        ),
    ] = None,
    retry: Annotated[
        int,
        typer.Option(
            help="The retry interval for emergency priority messages (in seconds)",
            show_default=False,
        ),
    ] = None,
    expire: Annotated[
        int,
        typer.Option(
            help="The expiration time for emergency priority messages (in seconds)",
            show_default=False,
        ),
    ] = None,
    ttl: Annotated[
        int,
        typer.Option(
            help="Time for the message to live before being deleted automatically (in seconds)",
            show_default=False,
        ),
    ] = None,
    sound: Annotated[
        str,
        typer.Option(
            help="The sound to play when the message is received", show_default=False
        ),
    ] = None,
    html: Annotated[
        bool,
        typer.Option(help="Whether to parse the message as HTML", show_default=False),
    ] = False,
    markdown: Annotated[
        bool,
        typer.Option(
            help="Whether to parse the message as Markdown", show_default=False
        ),
    ] = False,
    token: Annotated[
        str,
        typer.Option(
            help="The Pushover API token to use for sending the message",
            show_default=False,
        ),
    ] = None,
    user: Annotated[
        str,
        typer.Option(
            help="The Pushover user key to send the message to", show_default=False
        ),
    ] = None,
    device: Annotated[
        str,
        typer.Option(
            help="The Pushover device name to send the message to", show_default=False
        ),
    ] = None,
):
    """
    Send a message using the Pushover message api.

    Parameters
    ----------
    token

    """
    send_message(
        message=message,
        image_path=image_path,
        title=title,
        url=url,
        url_title=url_title,
        priority=priority,
        timestamp=timestamp,
        retry=retry,
        expire=expire,
        ttl=ttl,
        sound=sound,
        html=html,
        markdown=markdown,
        token=token,
        user=user,
        device=device,
    )


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print("Welcome to revohsup. Use --help for more information.")
