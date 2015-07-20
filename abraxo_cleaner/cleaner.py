# -*- coding: utf-8 -*-

from .settings import ABRAXO_INSPECTED_MODELS
from django.utils.module_loading import import_string


class AbraxoCleaner(object):
    def __init__(self, inspected_models=ABRAXO_INSPECTED_MODELS):
        self.inspected_models = inspected_models
        self.models = []

    def load_models(self):
        for model in self.inspected_models:
            self.models.append(import_string(model))

    def clean(self):
        scour()
