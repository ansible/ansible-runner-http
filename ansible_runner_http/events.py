import os
import requests
import requests_unixsocket


def send_request(url, data, headers={}, urlpath=None):
    if os.path.exists(url):
        url_actual = "http+unix://{}".format(url.replace("/", "%2F"))
        if urlpath is not None:
            url_actual += urlpath
        session = requests_unixsocket.Session()
    else:
        url_actual = url
        session = requests.Session()
    print(url_actual)
    return session.post(url_actual, headers=headers, json=(data))


def get_configuration(runner_config):
    runner_url = runner_config.settings.get("runner_http_url", None)
    runner_url = os.getenv("RUNNER_HTTP_URL", runner_url)
    runner_path = runner_config.settings.get("runner_http_path", None)
    runner_path = os.getenv("RUNNER_HTTP_PATH", runner_path)
    runner_headers = runner_config.settings.get("runner_http_headers", None)
    return dict(runner_url=runner_url,
                runner_path=runner_path,
                runner_headers=runner_headers)


def status_handler(runner_config, data):
    plugin_config = get_configuration(runner_config)
    if plugin_config['runner_url'] is not None:
        status = send_request(plugin_config['runner_url'],
                              data=data,
                              headers=plugin_config['headers']
                              urlpath=plugin_config['runner_path'])
        print("runner http {}".format(status))
    else:
        print("HTTP Plugin Skipped")


def event_handler(runner_config, data):
    status_handler(runner_config, data)
