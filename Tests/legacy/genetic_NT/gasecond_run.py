import Tests.genetic_alg as ga
import aux

__author__ = 'Manoel Ribeiro'


def run_it(seed, description):
    n_labels, folds, date, out = aux.armgesture()
    init = 42
    p_size = 20
    CXPB = 0.6
    MUTPB = 0.6
    NGEN = 10
    t_size = 2
    svm = 5
    elite_size = 1

    tests, logbook, best, arbitrary = ga.main(n_labels, folds, init=init, p_size=p_size, CXPB=CXPB,
                                              MUTPB=MUTPB, NGEN=NGEN, t_size=t_size, seed=seed,
                                              elite_size=elite_size, rd=True)

    aux.write_file(out, description, date, tests, logbook, best, svm, arbitrary)


desc = "RANDOM"
run_it(seed=1, description="GA1" + desc)
run_it(seed=2, description="GA2" + desc)
run_it(seed=3, description="GA3" + desc)
