from __future__ import unicode_literals

import logging
import pykka
from agent import EvtDevAgent

logger = logging.getLogger(__name__)


class EvtDevFrontend(pykka.ThreadingActor):

    def __init__(self, config, core):
        super(EvtDevFrontend, self).__init__()
        dev_dir = config['evtdev']['dev_dir']
        devices = config['evtdev']['devices']
        vol_step_size = config['evtdev']['vol_step_size']
        refresh = config['evtdev']['refresh']

        btn = {}
        btn['play_pause_btn'] = config['evtdev']['play_pause_btn']
        btn['stop_btn'] = config['evtdev']['stop_btn']
        btn['next_track_btn'] = config['evtdev']['next_track_btn']
        btn['prev_track_btn'] = config['evtdev']['prev_track_btn']
        btn['volume_up_btn'] = config['evtdev']['volume_up_btn']
        btn['volume_down_btn'] = config['evtdev']['volume_down_btn']
        btn['mute_btn'] = config['evtdev']['mute_btn']

        # EvtDevAgent performs all the handling of device
        # key presses on our behalf
        self.agent = EvtDevAgent(core, dev_dir, devices,
                                 vol_step_size, refresh, btn)
        logger.info('EvtDevAgent started')

    def on_stop(self):
        """
        Hook for doing any cleanup that should be done *after* the actor has
        processed the last message, and *before* the actor stops.

        This hook is *not* called when the actor stops because of an unhandled
        exception. In that case, the :meth:`on_failure` hook is called instead.

        For :class:`ThreadingActor` this method is executed in the actor's own
        thread, immediately before the thread exits.

        If an exception is raised by this method the stack trace will be
        logged, and the actor will stop.
        """
        self.agent.stop()
        logger.info('EvtDevAgent stopped')
