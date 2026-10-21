# SessionHttpsTestCase::httpUrl()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 836–839 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L836-L839)
- **Class:** [SessionHttpsTestCase](../SessionHttpsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function httpUrl($url)
```

## Documentation

```text
Builds a URL for submitting a mock HTTP request to HTTPS test environments.

@param $url
  A Drupal path such as 'user'.

@return
  An absolute URL.
```

## Code

```php
  protected function httpUrl($url) {
    global $base_url;
    return $base_url . '/modules/simpletest/tests/http.php?q=' . $url;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
