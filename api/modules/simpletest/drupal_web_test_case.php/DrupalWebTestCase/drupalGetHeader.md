# DrupalWebTestCase::drupalGetHeader()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3178–3196 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3178-L3196)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalGetHeader($name, $all_requests = FALSE)
```

## Documentation

```text
Gets the value of an HTTP response header. If multiple requests were
required to retrieve the page, only the headers from the last request will
be checked by default. However, if TRUE is passed as the second argument,
all requests will be processed from last to first until the header is
found.

@param $name
  The name of the header to retrieve. Names are case-insensitive (see RFC
  2616 section 4.2).
@param $all_requests
  Boolean value specifying whether to check all requests if the header is
  not found in the last request. Defaults to FALSE.
@return
  The HTTP header value or FALSE if not found.
```

## Code

```php
  protected function drupalGetHeader($name, $all_requests = FALSE) {
    $name = strtolower($name);
    $header = FALSE;
    if ($all_requests) {
      foreach (array_reverse($this->drupalGetHeaders(TRUE)) as $headers) {
        if (isset($headers[$name])) {
          $header = $headers[$name];
          break;
        }
      }
    }
    else {
      $headers = $this->drupalGetHeaders();
      if (isset($headers[$name])) {
        $header = $headers[$name];
      }
    }
    return $header;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
