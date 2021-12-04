import joblib
from preprecoessing import extract_features

def main():
    
    url_example = ["https://github.com/sjsucmpe272-fall21/PhishBlocker", "https://colab.research.google.com/drive/1Jx0RNrAitMAmM4DxILlt-FMImixvviVk#scrollTo=9kcFjZF_v8DB"]

    model = joblib.load('model.joblib')

    results = list()

    for url in url_example:
        features_array = extract_features(url)
        probability_good_url, probability_bad_url = model.predict_proba(features_array)[0]
        prediction, probability = 0, 0
        
        if probability_good_url >= probability_bad_url:
            prediction = 0
            probability = probability_good_url
        else:
            prediction = 1
            probability = probability_bad_url

        results.append((prediction, probability))

    print(results)
    return results

if __name__ == "__main__":
    main()