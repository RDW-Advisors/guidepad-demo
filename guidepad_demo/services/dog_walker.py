import time
from datetime import datetime

from guidepad.service.base_service import Service
from guidepad.types import registry


class DogWalker(Service):

    def start(self, done_signal):
        while True:
            Dog = registry.TypeRegistry.t('Dog')
            for d in Dog.list({}):
                d.times_walked += 1
                d.last_walked = datetime.utcnow()
                d.save()

            time.sleep(10)
