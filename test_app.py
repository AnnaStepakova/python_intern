#!/usr/bin/python3
from app import is_alive_host


def test_is_alive_host_true1():
    assert is_alive_host("vk.com") == True


def test_is_alive_host_true2():
    assert is_alive_host("semrush.com") == True


def test_is_alive_host_false1():
    assert is_alive_host("ssssemrush.com") == False


def test_is_alive_host_false2():
    assert is_alive_host("klpuytri.com") == False