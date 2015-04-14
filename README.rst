****************************
Mopidy-EvtDev
****************************

.. image:: https://pypip.in/version/Mopidy-EvtDev/badge.png?latest
    :target: https://pypi.python.org/pypi/Mopidy-EvtDev/
    :alt: Latest PyPI version

.. image:: https://pypip.in/download/Mopidy-EvtDev/badge.png
    :target: https://pypi.python.org/pypi/Mopidy-EvtDev/
    :alt: Number of PyPI downloads

.. image:: https://travis-ci.org/liamw9534/mopidy-evtdev.png?branch=master
    :target: https://travis-ci.org/liamw9534/mopidy-evtdev
    :alt: Travis CI build status

.. image:: https://coveralls.io/repos/liamw9534/mopidy-evtdev/badge.png?branch=master
   :target: https://coveralls.io/r/liamw9534/mopidy-evtdev?branch=master
   :alt: Test coverage

`Mopidy <http://www.mopidy.com/>`_ extension for controlling music playback from virtual input device

Installation
============

Install by running::

    pip install Mopidy-EvtDev

Or, if available, install the Debian/Ubuntu package from `apt.mopidy.com
<http://apt.mopidy.com/>`_.


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-EvtDev to your Mopidy configuration file::

    [evtdev]
    # Location of virtual input devices
    dev_dir = /dev/input
    # List of virtual devices to open which can be either their path, name or physical address
    # Leave blank to listen to all devices
    devices = 00:11:67:D2:AB:EE, AT Translated Set 2 keyboard, isa0060/serio0/input0
    # Refresh period in seconds to check for new input devices
    refresh = 10

To permit mopidy to read virtual input devices without root permissions, you need to add
the following into /etc/udev/rules.d/99-input.rules:

	KERNEL=="event*", NAME="input/%k", MODE="660", GROUP="audio"

If you are concerned by security, then create a separate group name and add mopidy as a member
to that group.  E.g.,

	KERNEL=="event*", NAME="input/%k", MODE="660", GROUP="input"

Otherwise, just run mopidy as root to avoid any additional configuration requirements.


You can define your own key using following options in configuration file::


    [evtdev]
    #same configuration as before
    ...
    #define the play/pause button on key A
    play_pause_btn = KEY_A
    #define the stop button on key space
    stop_btn = KEY_SPACE
    #define mute button on key F12
    mute_btn = KEY_F12
    #define next track button on key '-' from the keypad
    next_track_btn = KEY_KPPLUS
    #define next track button on key '+' from the keypad
    prev_track_btn = KEY_KPMINUS
    #define volume up button on the page up key
    volume_up_btn = KEY_PAGEUP
    #define volume up button on the page down key
    volume_down_btn = KEY_PAGEDOWN

the list of available keys is defined in linux/input.h

Project resources
=================

- `Source code <https://github.com/liamw9534/mopidy-evtdev>`_
- `Issue tracker <https://github.com/liamw9534/mopidy-evtdev/issues>`_
- `Download development snapshot <https://github.com/liamw9534/mopidy-evtdev/archive/master.tar.gz#egg=mopidy-evtdev-dev>`_


Changelog
=========

v0.1.1
----------------------------------------

- Fixes issue #7: Race hazard - closing and re-opening already devices causes events to be missed.
- Improved unit test coverage.

v0.1.0
----------------------------------------

- Initial release.
