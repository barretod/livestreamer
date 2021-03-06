class PluginError(Exception):
    """ Plugin related errors. """


class NoStreamsError(PluginError):
    def __init__(self, url):
        PluginError.__init__(self, ("No streams found on this URL: {0}").format(url))


class NoPluginError(PluginError):
    """
        This exception is triggered when no plugin can found when
        calling :meth:`Livestreamer.resolve_url`.

        Inherits :exc:`PluginError`.
    """


class StreamError(Exception):
    """ Stream related errors. """


__all__ = ["PluginError", "NoPluginError", "NoStreamsError", "StreamError"]
