#!/usr/bin/env python
#
# $Id$
#
"""Compute the due date for a task.
"""

import time
import datetime

##
## TIME ZONES
##
## (Adapted from http://docs.python.org/lib/datetime-tzinfo.html)
##

ZERO = datetime.timedelta(0)

class UTC(datetime.tzinfo):
    """UTC"""
    def utcoffset(self, dt):
        return ZERO
    def tzname(self, dt):
        return "UTC"
    def dst(self, dt):
        return ZERO
utc = UTC()    

STDOFFSET = datetime.timedelta(seconds = -time.timezone)
if time.daylight:
    DSTOFFSET = datetime.timedelta(seconds = -time.altzone)
else:
    DSTOFFSET = STDOFFSET

DSTDIFF = DSTOFFSET - STDOFFSET

class LocalTimezone(datetime.tzinfo):
    """Determine the local time zone.

    """
    def utcoffset(self, dt):
        if self._isdst(dt):
            return DSTOFFSET
        else:
            return STDOFFSET

    def dst(self, dt):
        if self._isdst(dt):
            return DSTDIFF
        else:
            return ZERO

    def tzname(self, dt):
        return time.tzname[self._isdst(dt)]

    def _isdst(self, dt):
        tt = (dt.year, dt.month, dt.day,
              dt.hour, dt.minute, dt.second,
              dt.weekday(), 0, -1)
        stamp = time.mktime(tt)
        tt = time.localtime(stamp)
        return tt.tm_isdst > 0

local_tz = LocalTimezone()

if __name__ == '__main__':
    import optparse
    import sys

    option_parser = optparse.OptionParser(
        usage='usage: %prog [options] CLAIMED_TIME'
        )
    option_parser.add_option('-v',
                             dest='verbose', 
                             default=False, 
                             action='store_true',
                             help='Enable verbose output')
    option_parser.add_option('-d', '--days',
                             dest='days_to_complete',
                             default=5,
                             help='How many days to complete the task',
                             action='store',
                             type='int',
                             )
    option_parser.add_option('-f', '--format',
                             dest='time_format',
                             default='%B %d, %Y %I:%M:%S %p %Z',
                             help='How time strings are formatted',
                             action='store',
                             )

    (options, args) = option_parser.parse_args()

    # Require a claimed time value
    if not args:
        print >>sys.stderr, '\nERROR: No CLAIMED_TIME specified\n'
        option_parser.print_help(sys.stderr)
        sys.exit(1)
    claimed_str = ' '.join(args)

    # Parse the claimed time and force it into our local time zone
    parsed_time = time.strptime(claimed_str, options.time_format)
    dt_args = parsed_time[0:6] + (0, local_tz)
    claimed = datetime.datetime(*dt_args)
    if options.verbose:
        print 'CLAIMED  :', claimed.strftime(options.time_format)

    # Calculate the due date
    due = claimed + datetime.timedelta(options.days_to_complete)
    due = due.replace(second=0, minute=((due.minute/5)+1)*5)
    if options.verbose:
        print 'DUE      :', due.strftime(options.time_format)

    # Calculate the due date in UTC
    due_utc = due.astimezone(utc)
    if options.verbose:
        print 'DUE (UTC):', due_utc.strftime(options.time_format)
    else:
        print 'This task is due', due_utc.strftime(options.time_format)
        print 'Due-%s' % due_utc.strftime('%Y%m%d.%H%M')
