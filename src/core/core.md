# Core

## Usage
The scripts in this file represent the 'heart' of a deployment.
These utilities are responsible for parsing a deployment.json file, launching the appropriate utilities in order to fulfill the deplyoment, and monitor the utilities for any problems.  

## Development:
**Current:** Scripts for safely launching child processes and monitoring their health are complete.

**In-Progress:** The `core.py` file is intended to be the main interface by which the scripts of the core collection are called.
It should be an idiomatic representation of the appropriate workflow for this collection.
The `setup_pgrms.py` file is intended to house the internals of the parsing (and possibly any default-actions, although it is important for the current design philosophy that any scripts at this level do not hide state).


**Future:** Additional functions to be performed by the *core* collection are still indeterminate.
There is currently an open question of wether to merge scheduling functions into this collection, or keep them as separate.
For simplicity's sake, a smaller number of script groups is desireable, but the categorization of functions should also be exceedingly clear s.t. those with an interest in modifying any component can do so with minimal effort and little-to-no side-effects.
Ideally, each collection should be black-box esque in its interchangeability with any other set of scripts that achieve the same goals.
