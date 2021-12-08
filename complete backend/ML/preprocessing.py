def test():
    return ("INSIDE preprocessing")

from redis import Redis

# connecting to redis instance
redis = Redis(host="127.0.0.1", port=6379, decode_responses=True)

from collections import Counter
import numpy as np
#from ML import model.joblib

import joblib



def extract_features(url):
    for prefix in ['https://', 'http://', 'www.']:
        if prefix in url:
            url = url.replace(prefix, '')
    link_len = len(url)
    n_perc20 = url.count('%20')

    counter = Counter(url)

    n_semi = counter[';']
    n_colo = counter[':']
    n_at = counter['@']
    n_amp = counter['&']
    n_perc = counter['%']
    n_eq = counter['=']
    n_slash = counter['/']

    n_ascii = 0
    n_nonascii = 0
    n_numbers = 0
    n_alpha = 0
    n_nonalpha = 0

    for c in url:
        if c.isalpha():
            n_alpha += 1
        elif c.isnumeric():
            n_numbers += 1
        elif not c.isalpha():
            n_nonalpha += 1
        elif c.isascii():
            n_ascii += 1
        elif not c.isascii():
            n_nonascii += 1
        else:
            print(f"Shouldn't really be here.. input: {c}")

    url_s = url.split('/')
    domain_name = url_s[0]
    n_hyph = domain_name.count('-')
    domain_name_len = len(domain_name)

    n_num_in_domain = 0
    domain_len = len(domain_name)
    n_subdomains = domain_name.count('.')
    for c in domain_name:
        if c.isnumeric():
            n_num_in_domain += 1
    n_dot_js = url.count('.js')

    return np.array([
        # domain_len,
        n_dot_js,
        n_subdomains,
        n_perc,
        n_hyph,
        n_amp,
        n_perc,
        n_numbers,
        n_alpha,
        n_nonalpha,
        n_num_in_domain,
        counter['a'],
        counter['b'],
        counter['c'],
        counter['d'],
        counter['e'],
        counter['f'],
        counter['g'],
        counter['h'],
        counter['i'],
        counter['j'],
        counter['k'],
        counter['l'],
        counter['m'],
        counter['n'],
        counter['o'],
        counter['p'],
        counter['q'],
        counter['r'],
        counter['s'],
        counter['t'],
        counter['u'],
        counter['v'],
        counter['w'],
        counter['x'],
        counter['y'],
        counter['z'],
    ], dtype=np.float).reshape(1, -1)  # convert from shape (16,) to (1, 16)


def url_pass( URL ):
    #url_example = ["https://github.com/sjsucmpe272-fall21/PhishBlocker","https://colab.research.google.com/drive/1Jx0RNrAitMAmM4DxILlt-FMImixvviVk#scrollTo=9kcFjZF_v8DB"]

    url_example= URL
    print("BEFORE!!!")
    model = joblib.load('/home/ubuntu/ML/model.joblib')
    print("AFTER!!!!")
    results = list()

    for url in url_example:
        if(redis.exists(url)==1):
            #results.append(int(redis.get(url)))
            val=redis.lrange(url,0,1)
            #print(val)
            pred=int(val[1])
            prob=float(val[0])
            results.append((pred,prob))
            print("INSIDE REDIS ")
            continue
        features_array = extract_features(url)
        probability_good_url, probability_bad_url = model.predict_proba(features_array)[0]
        prediction, probability = 0, 0
        if probability_good_url >= probability_bad_url:
            prediction = 0
            probability = probability_good_url
        else:
            prediction = 1
            probability = probability_bad_url

        results.append((prediction,probability))
        #res=model.predict(features_array).item()
        #results.append(res)
        #val=str((prediction,probability))
        #print(val)
        redis.lpush(url,prediction,probability)

    #print(results)
    return results


