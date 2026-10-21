# DrupalWebTestCase::assertNoResponse()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3960–3964 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3960-L3964)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertNoResponse($code, $message = '')
```

## Documentation

```text
Asserts the page did not return the specified response code.

@param $code
  Response code. For example 200 is a successful page request. For a list
  of all codes see http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html.
@param $message
  Message to display.

@return
  Assertion result.
```

## Code

```php
  protected function assertNoResponse($code, $message = '') {
    $curl_code = curl_getinfo($this->curlHandle, CURLINFO_HTTP_CODE);
    $match = is_array($code) ? in_array($curl_code, $code) : $curl_code == $code;
    return $this->assertFalse($match, $message ? $message : t('HTTP response not expected !code, actual !curl_code', array('!code' => $code, '!curl_code' => $curl_code)), t('Browser'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
