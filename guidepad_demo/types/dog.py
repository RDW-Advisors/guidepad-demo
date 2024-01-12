import random
import time

from guidepad.messaging.event import Event
from guidepad.service.base_service import Service
from guidepad.types import attributes, base_type


class Dog(Service):

    class TypeConfig:
        instancestore_name = 'service'

    bladder_level = attributes.Int(default=0, maximum=100)
    service_type = attributes.String(default='guidepad_demo.dog')

    def start(self, done_signal):
        while True:
            new_level = self.bladder_level + random.randint(0, 10)
            if new_level > 100:
                new_level = 100

            self.bladder_level = new_level

            self.save()

            if self.bladder_level == 100:
                Event.create(
                    name=f'{self.name} bladder is full!',
                    event_type='dog_bladder_full'
                )

            time.sleep(self.monitor_interval)

