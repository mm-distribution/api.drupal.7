# DrupalWebTestCase::drupalGetHeaders()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3131–3160 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3131-L3160)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalGetHeaders($all_requests = FALSE)
```

## Documentation

```text
Gets the HTTP response headers of the requested page. Normally we are only
interested in the headers returned by the last request. However, if a page
is redirected or HTTP authentication is in use, multiple requests will be
required to retrieve the page. Headers from all requests may be requested
by passing TRUE to this function.

@param $all_requests
  Boolean value specifying whether to return headers from all requests
  instead of just the last request. Defaults to FALSE.
@return
  A name/value array if headers from only the last request are requested.
  If headers from all requests are requested, an array of name/value
  arrays, one for each request.

  The pseudonym ":status" is used for the HTTP status line.

  Values for duplicate headers are stored as a single comma-separated list.
```

## Code

```php
  protected function drupalGetHeaders($all_requests = FALSE) {
    $request = 0;
    $headers = array($request => array());
    foreach ($this->headers as $header) {
      $header = trim($header);
      if ($header === '') {
        $request++;
      }
      else {
        if (strpos($header, 'HTTP/') === 0) {
          $name = ':status';
          $value = $header;
        }
        else {
          list($name, $value) = explode(':', $header, 2);
          $name = strtolower($name);
        }
        if (isset($headers[$request][$name])) {
          $headers[$request][$name] .= ',' . trim($value);
        }
        else {
          $headers[$request][$name] = trim($value);
        }
      }
    }
    if (!$all_requests) {
      $headers = array_pop($headers);
    }
    return $headers;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
