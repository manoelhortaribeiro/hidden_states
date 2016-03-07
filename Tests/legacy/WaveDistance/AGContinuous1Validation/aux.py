import datetime


def armgesturethreefold():
    n_labels = 6
    folds = [1, 2, 3]
    path = "/home/manoel/Projects/hidden_states_entropy/Dataset/Data/ArmGesture/Continuous1/"
    data = "data"
    label = "seqLabels"
    train = "Train"
    test = "Test"
    name = "ArmGestureContinuous"
    fold = "Fold1"
    date = datetime.datetime.utcnow().strftime("%d_%m_%y-%H:%M")
    project_folder = "/home/manoel/Projects/"
    out = "hidden_states_entropy/Dataset/Output/Results/"
    datapath = "/home/manoel/Projects/hidden_states_entropy/Dataset/Data/ArmGesture/Continuous3/" + "ArmGestureDiscrete3.mat"

    return datapath, n_labels, folds, path, data, label, train, test, name, fold, date, project_folder, out



def write_file(project_folder, out, description, date, svmiter, tests, opt_tests_avg_std,
              opt_trains_avg_std, sopt_tests_avg_std, sopt_trains_avg_std, detailed):
    f = open(project_folder + out + description + date, "a")

    f.write(detailed + "\n")

    f.write("Number of latent iterations in the SSVM: " + str(svmiter) + "\n")

    f.write("Number of states used in each test: " + str(tests) + "\n")

    f.write("Optimal-test (avg, std): ")
    f.write(str(opt_tests_avg_std))
    f.write("\n")

    f.write("Optimal-train (avg, std): ")
    f.write(str(opt_trains_avg_std))
    f.write("\n")

    f.write("Sub-Optimal-test (avg, std): ")
    f.write(str(sopt_tests_avg_std))
    f.write("\n")

    f.write("Sub-Optimal-train (avg, std): ")
    f.write(str(sopt_trains_avg_std))
    f.write("\n")
    f.close()