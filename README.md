# SimpleAsyncQueue
# ================

## Description
Simple Async Task Queue.  Use this queue to concurrently execute functions in a threaded environment.  This a 
bare-metal library, which means it does not have dependencies on high-level multiprocessing or threading tools.

## Usage
See main.py for an example script.  Basically, add `Functions` via the `add_task` function; register callback 
functions to be executed after all the tasks finish via the `add_callback` function.

Created by: Juan Carlos Coto Ulate, 2014.
 
Contact: jc (at) jccoto (dot) com.
