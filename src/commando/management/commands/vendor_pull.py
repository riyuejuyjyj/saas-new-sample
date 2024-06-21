from django.core.management.base import BaseCommand
import helpers
from django.conf import settings

import helpers.downloader
VENDOR_STATICFILES = {
    "flowbite.min.css":"https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js":"https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js"
}


STATICFILES_VENDOR_DIR = getattr(
    settings,
    'STATICFILES_VENDOR_DIR'
)

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Downloading vendor static files")
        completed_urls = []
        for name,url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.downloader.download_to_local(url, out_path)
            print(f"Downloading {name} from {url} ot {out_path}")
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {name} from {url}")
                )
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS("All vendor static files downloaded")
            )
        else:
            self.stdout.write(
                self.style.WARNING("Some vendor static files failed to download")
            )    