def compute_score(arr):
    evaluation_results = {
        "main_metric": "EM",
        "overall_evaluation": {"EM": 0.},
        "partial_evaluation": [],
    }

    correct = 0
    for item in arr:
        if item is None:
            evaluation_results["partial_evaluation"].append({"EM": 0.})
        else:
            if item['score'] == 1:
                correct += 1
                evaluation_results["partial_evaluation"].append({"EM": 100.})
            else: evaluation_results["partial_evaluation"].append({"EM": 0.})

    evaluation_results['overall_evaluation'][evaluation_results['main_metric']] = (100 * correct) / len(arr)

    return evaluation_results