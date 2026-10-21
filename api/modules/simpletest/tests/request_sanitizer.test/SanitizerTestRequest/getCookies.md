# SanitizerTestRequest::getCookies()

- **Type:** Method
- **File:** [`modules/simpletest/tests/request_sanitizer.test`](../_file.md), lines 350–352 · [local source](../../../../../../source/modules/simpletest/tests/request_sanitizer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test#L350-L352)
- **Class:** [SanitizerTestRequest](../SanitizerTestRequest.md)
- **Module/theme:** batch_test

## Signature

```php
public function getCookies()
```

## Documentation

```text
Getter for $cookies.
```

## Code

```php
  public function getCookies() {
    return $this->cookies;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/request_sanitizer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
