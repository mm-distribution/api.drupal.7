# DrupalWebTestCase::curlInitialize()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 2038–2079 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L2038-L2079)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function curlInitialize()
```

## Documentation

```text
Initializes the cURL connection.

If the simpletest_httpauth_credentials variable is set, this function will
add HTTP authentication headers. This is necessary for testing sites that
are protected by login credentials from public access.
See the description of $curl_options for other options.
```

## Code

```php
  protected function curlInitialize() {
    global $base_url;

    if (!isset($this->curlHandle)) {
      $this->curlHandle = curl_init();

      // Some versions/configurations of cURL break on a NULL cookie jar, so
      // supply a real file.
      if (empty($this->cookieFile)) {
        $this->cookieFile = $this->public_files_directory . '/cookie.jar';
      }

      $curl_options = array(
        CURLOPT_COOKIEJAR => $this->cookieFile,
        CURLOPT_URL => $base_url,
        CURLOPT_FOLLOWLOCATION => FALSE,
        CURLOPT_RETURNTRANSFER => TRUE,
        CURLOPT_SSL_VERIFYPEER => FALSE, // Required to make the tests run on HTTPS.
        CURLOPT_SSL_VERIFYHOST => FALSE, // Required to make the tests run on HTTPS.
        CURLOPT_HEADERFUNCTION => array(&$this, 'curlHeaderCallback'),
        CURLOPT_USERAGENT => $this->databasePrefix,
      );
      if (isset($this->httpauth_credentials)) {
        $curl_options[CURLOPT_HTTPAUTH] = $this->httpauth_method;
        $curl_options[CURLOPT_USERPWD] = $this->httpauth_credentials;
      }
      // curl_setopt_array() returns FALSE if any of the specified options
      // cannot be set, and stops processing any further options.
      $result = curl_setopt_array($this->curlHandle, $this->additionalCurlOptions + $curl_options);
      if (!$result) {
        throw new Exception('One or more cURL options could not be set.');
      }

      // By default, the child session name should be the same as the parent.
      $this->session_name = session_name();
    }
    // We set the user agent header on each request so as to use the current
    // time and a new uniqid.
    if (preg_match('/simpletest\d+/', $this->databasePrefix, $matches)) {
      curl_setopt($this->curlHandle, CURLOPT_USERAGENT, drupal_generate_test_ua($matches[0]));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
