# ssh_log_parser.py
"""
A module of functions and classes that help parse gzipped SSH log file.
"""
from typing import *
from pathlib import Path
import gzip
import re
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime


OPENED_RE = re.compile(
    "(\w+ \d+ \S+) \w+ sshd\[(\d+)\]: \S+ session opened for user (\S+)")
FAILED_RE = re.compile(
    "Failed password for invalid user (\S+) from (\S+)"
)


@dataclass
class Session:
    pid: int
    user: str
    opened: datetime


def get_user_logins(gz_logfile: Path) -> Iterable[str]:
    """Return all users who opened sessions from `gz_logfile`."""
    users: set[str] = set()
    with gzip.open(gz_logfile, 'rt') as g:
        for line in g:
            if match := OPENED_RE.search(line):
                user = match.group(3)
                if user not in users:
                    users.add(user)
    return users


def get_failed_logins(gz_logfile: Path) -> dict[str, Iterable[str]]:
    """
    Get a mapping of IP addresses and list of associated usernamess
    that failed to login from `gz_logfile`.
    """
    ip_user_mapping: dict[str, Iterable[str]] = defaultdict(list)
    with gzip.open(gz_logfile, 'rt') as g:
        for line in g:
            if match := FAILED_RE.search(line):
                username, ip = match.groups()
                ip_user_mapping[ip].append(username)
    return ip_user_mapping


def get_sessions(gz_logfile: Path, year: int = 2017) -> Iterable[Session]:
    """Return an iterable of all opened sessions found in `gz_logfile`."""
    with gzip.open(gz_logfile, 'rt') as g:
        for line in g:
            if match := OPENED_RE.match(line):
                timestamp, pid, user = match.groups()
                yield Session(
                    int(pid),
                    user,
                    datetime.strptime(
                        timestamp, '%b %d %H:%M:%S'
                    ).replace(year=year)
                )


# base problem, test `get_user_logins()`
users = get_user_logins('sshd.log.gz')
assert users == {'virgil', 'taylor', 'nancy', 'wanda', 'juan', 'vickie'}

# bonus 1, test `get_failed_logins()`
attempts = get_failed_logins('sshd.log.gz')
assert len(attempts) == 232

# bonus 2, test `Session` class and `get_sessions()` function
sessions = list(get_sessions('sshd.log.gz'))
assert len(sessions) == 25