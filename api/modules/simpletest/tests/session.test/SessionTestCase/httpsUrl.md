# SessionTestCase::httpsUrl()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 543–546 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L543-L546)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function httpsUrl($url)
```

## Documentation

```text
Builds a URL for submitting a mock HTTPS request to HTTP test environments.

@param $url
  A Drupal path such as 'user'.

@return
  An absolute URL.
```

## Code

```php
  protected function httpsUrl($url) {
    global $base_url;
    return $base_url . '/modules/simpletest/tests/https.php?q=' . $url;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
