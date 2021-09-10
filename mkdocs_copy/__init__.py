import os
import logging
from mkdocs.exceptions import PluginError
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
from mkdocs import utils


LOGLEVEL = os.getenv('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)


try:
    ModuleNotFoundError
except NameError:  # pragma: no cover
    ModuleNotFoundError = ImportError


# https://www.mkdocs.org/dev-guide/plugins/#developing-plugins
class CopyPlugin(BasePlugin):
    """ A MkDocs plugin to copy arbitrary files to the output build."""

    config_scheme = (
        ('add_per_path', config_options.Type((str, list), default=None)),
    )

    def on_page_content(self, content, page, config, files):
        """ Hooks into MkDocs' default page (== http paths) list. Runs multiple times (once per output path). """
        logging.debug("--- on_pre_page ---")
        logging.debug(self.config)
        logging.debug(page.__repr__())

        source_dir = os.path.dirname(page.file.abs_src_path)
        logging.debug('source dir: ' + source_dir)

        dest_dir = os.path.dirname(page.file.abs_dest_path)
        os.makedirs(dest_dir, exist_ok=True)
        exists_dest_dir = os.path.isdir(dest_dir)
        logging.debug('dest dir: ' + dest_dir +
                      ' (exists: ' + str(exists_dest_dir) + ')')

        source_file = os.path.join(source_dir, '.htaccess')
        exists_dest_file = os.path.isfile(source_file)
        logging.debug('source file: ' + source_file +
                      ' (exists: ' + str(exists_dest_file) + ')')

        exists_dest_file and utils.copy_file(source_file, dest_dir)
        logging.debug("--- /on_pre_page ---")

        return content
