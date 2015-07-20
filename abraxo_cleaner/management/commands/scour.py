# -*- coding: utf-8 -*-

"""This command is used to deploy this django setup with ease"""

from __future__ import unicode_literals

import sys

from django.core.management.base import BaseCommand

from abraxo_cleaner import AbraxoCleaner


class NotRunningInTTYException(Exception):
    pass


class Command(BaseCommand):
    help = """Cleans models using abraxo_cleaner."""

    def handle(self, *args, **options):
        sys.stdout.write(
            "Sit back ... Relax ! Abraxo Cleaner does the work for you !\n"
            "The scouring of models will begin.\n"
        )
        
        cleaned = AbraxoCleaner.clean()

        sys.stdout.write("{0} models have been thoroughly scoured thanks"
                         " to Abraxo Cleaner !\n".format(cleaned))
