from pyee import BaseEventEmitter


class RaceEventEmitter(BaseEventEmitter):
    """Event emitter for forcing the result of a race in once.

    Will automatically remove the listener right before calling the function.
    """
    def _call_handlers(self, event, args, kwargs):
        handled = False

        with self._lock:
            funcs = list(self._events[event].values())
        for f in funcs:
            self.remove_listner(event, f)
            self._emit_run(f, args, kwargs)
            handled = True

        return handled


