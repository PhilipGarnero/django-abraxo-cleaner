# -*- coding: utf-8 -*-

from django.conf import settings

ABRAXO_INSPECTED_MODELS = getattr(settings, "ABRAXO_INSPECTED_MODELS", [])
