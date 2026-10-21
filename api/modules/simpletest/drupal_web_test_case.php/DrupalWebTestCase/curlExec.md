# DrupalWebTestCase::curlExec()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 2097–2167 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L2097-L2167)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function curlExec($curl_options, $redirect = FALSE)
```

## Documentation

```text
Initializes and executes a cURL request.

@param $curl_options
  An associative array of cURL options to set, where the keys are constants
  defined by the cURL library. For a list of valid options, see
  http://www.php.net/manual/function.curl-setopt.php
@param $redirect
  FALSE if this is an initial request, TRUE if this request is the result
  of a redirect.

@return
  The content returned from the call to curl_exec().

@see curlInitialize()
```

## Code

```php
  protected function curlExec($curl_options, $redirect = FALSE) {
    $this->curlInitialize();

    if (!empty($curl_options[CURLOPT_URL])) {
      // Forward XDebug activation if present.
      if (isset($_COOKIE['XDEBUG_SESSION'])) {
        $options = drupal_parse_url($curl_options[CURLOPT_URL]);
        $options += array('query' => array());
        $options['query'] += array('XDEBUG_SESSION_START' => $_COOKIE['XDEBUG_SESSION']);
        $curl_options[CURLOPT_URL] = url($options['path'], $options);
      }

      // cURL incorrectly handles URLs with a fragment by including the
      // fragment in the request to the server, causing some web servers
      // to reject the request citing "400 - Bad Request". To prevent
      // this, we strip the fragment from the request.
      // TODO: Remove this for Drupal 8, since fixed in curl 7.20.0.
      if (strpos($curl_options[CURLOPT_URL], '#')) {
        $original_url = $curl_options[CURLOPT_URL];
        $curl_options[CURLOPT_URL] = strtok($curl_options[CURLOPT_URL], '#');
      }
    }

    $url = empty($curl_options[CURLOPT_URL]) ? curl_getinfo($this->curlHandle, CURLINFO_EFFECTIVE_URL) : $curl_options[CURLOPT_URL];

    if (!empty($curl_options[CURLOPT_POST])) {
      // This is a fix for the Curl library to prevent Expect: 100-continue
      // headers in POST requests, that may cause unexpected HTTP response
      // codes from some webservers (like lighttpd that returns a 417 error
      // code). It is done by setting an empty "Expect" header field that is
      // not overwritten by Curl.
      $curl_options[CURLOPT_HTTPHEADER][] = 'Expect:';
    }
    curl_setopt_array($this->curlHandle, $this->additionalCurlOptions + $curl_options);

    if (!$redirect) {
      // Reset headers, the session ID and the redirect counter.
      $this->session_id = NULL;
      $this->headers = array();
      $this->redirect_count = 0;
    }

    $content = curl_exec($this->curlHandle);
    $status = curl_getinfo($this->curlHandle, CURLINFO_HTTP_CODE);

    // cURL incorrectly handles URLs with fragments, so instead of
    // letting cURL handle redirects we take of them ourselves to
    // to prevent fragments being sent to the web server as part
    // of the request.
    // TODO: Remove this for Drupal 8, since fixed in curl 7.20.0.
    if (in_array($status, array(300, 301, 302, 303, 305, 307)) && $this->redirect_count < variable_get('simpletest_maximum_redirects', 5)) {
      if ($this->drupalGetHeader('location')) {
        $this->redirect_count++;
        $curl_options = array();
        $curl_options[CURLOPT_URL] = $this->drupalGetHeader('location');
        $curl_options[CURLOPT_HTTPGET] = TRUE;
        return $this->curlExec($curl_options, TRUE);
      }
    }

    $this->drupalSetContent($content, isset($original_url) ? $original_url : curl_getinfo($this->curlHandle, CURLINFO_EFFECTIVE_URL));
    $message_vars = array(
      '!method' => !empty($curl_options[CURLOPT_NOBODY]) ? 'HEAD' : (empty($curl_options[CURLOPT_POSTFIELDS]) ? 'GET' : 'POST'),
      '@url' => isset($original_url) ? $original_url : $url,
      '@status' => $status,
      '!length' => format_size(strlen($this->drupalGetContent()))
    );
    $message = t('!method @url returned @status (!length).', $message_vars);
    $this->assertTrue($this->drupalGetContent() !== FALSE, $message, t('Browser'));
    return $this->drupalGetContent();
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
