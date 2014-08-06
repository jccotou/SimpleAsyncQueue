from threading import Lock
from event_loop.EventLoop import EventLoop
from worker.Worker import Worker


class Queue(object):

    def __init__(self, parallelism, main_event_loop):
        self._callbacks = list()
        self._event_loop = main_event_loop
        self._lock = Lock()
        self._tasks = list()
        self._tasks_in_flight = 0
        self._workers = list()
        self._is_running = False

        for worker_num in xrange(0, parallelism):
            # TODO not sure about this event loop thing
            self._workers.append(Worker(self, self._event_loop))


    # Requested API #
    def size(self):
        with self._lock:
            return len(self._tasks)

    def is_running(self):
        with self._lock:
            return self._is_running

    def in_flight(self):
        with self._lock:
            return self._tasks_in_flight

    def add_task(self, task):
        with self._lock:
            self._tasks.append(task)

    def add_callback(self, callback):
        with self._lock:
            self._callbacks.append(callback)

    def start(self):
        self._is_running = True
        for worker in self._workers:
            worker.start()

    # Additional functions #

    def get_task(self):
        with self._lock:
            return self._tasks.pop()

    def task_started(self):
        with self._lock:
            self._tasks_in_flight += 1

    def task_finished(self):
        with self._lock:
            self._tasks_in_flight -= 1

    def get_should_finish(self):
        with self._lock:
            if self._is_running:
                self._is_running = False
                return True
            return False

    def finish(self):
        while True:
            try:
                self._event_loop.append(self._callbacks.pop())
            except IndexError:
                break
