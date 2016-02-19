__author__ = 'Greg'


class ConvertMixin:

    def _convert_predictors_to_prev_csum(self, predictos):
        for predictor in predictos:
            if 'csum_min_' in predictor:
                predictor.replace('csum_min_, csum_orev_min_')
        return predictos

