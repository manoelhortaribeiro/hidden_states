import Tests.hsparallel_alt as hs
import aux

__author__ = 'Manoel Ribeiro'

tests = [10, 12, 14, 16, 18, 20, 30, 40, 50, 60, 70, 80, 90]
description = "cad120_7i50s_t10-90"
svmiter = 7
seed = 50
n_jobs = 1
detailed = "Full random init, seed 50, jobs 3, svmiter 7"

n_labels, folds, path, data, label, train, test, name, fold, date, project_folder, out = aux.cad120()

opt_tests_avg_std, opt_trains_avg_std, sopt_tests_avg_std, sopt_trains_avg_std = \
    hs.eval_data_set(tests, n_labels, folds, path, data, label, train, test, name, fold, kind="Equal",
                     svmiter=svmiter, seed=seed, n_jobs=n_jobs)

aux.write_file(project_folder, out, description, date, svmiter, tests, opt_tests_avg_std,
               opt_trains_avg_std, sopt_tests_avg_std, sopt_trains_avg_std, detailed)

description = "cad120_7i60s_t10-90"
svmiter = 7
seed = 60
n_jobs = 1
detailed = "Full random init, seed 60, jobs 3, svmiter 7"

n_labels, folds, path, data, label, train, test, name, fold, date, project_folder, out = aux.cad120()

opt_tests_avg_std, opt_trains_avg_std, sopt_tests_avg_std, sopt_trains_avg_std = \
    hs.eval_data_set(tests, n_labels, folds, path, data, label, train, test, name, fold, kind="Equal",
                     svmiter=svmiter, seed=seed, n_jobs=n_jobs)

aux.write_file(project_folder, out, description, date, svmiter, tests, opt_tests_avg_std,
               opt_trains_avg_std, sopt_tests_avg_std, sopt_trains_avg_std, detailed)