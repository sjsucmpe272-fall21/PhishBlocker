import joblib
from preprecoessing import extract_features

def main():
    
    url_example = ["https://github.com/sjsucmpe272-fall21/PhishBlocker", "https://colab.research.google.com/drive/1Jx0RNrAitMAmM4DxILlt-FMImixvviVk#scrollTo=9kcFjZF_v8DB"]

    model = joblib.load('model.joblib')

    results = list()

    for url in url_example:
        features_array = extract_features(url)
        results.append(model.predict(features_array).item())

    print(results)
    return results

if __name__ == "__main__":
    main()