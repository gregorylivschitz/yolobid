__author__ = 'Greg'


class ConvertMixin:

    def _convert_predictors_to_prev_csum(self, predictors):
        prev_predictors = [predictor.replace('csum_min_', 'csum_prev_min_') for predictor in predictors]
        return prev_predictors

