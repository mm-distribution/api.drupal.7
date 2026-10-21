# SanitizerTestRequest::getQuery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/request_sanitizer.test`](../_file.md), lines 329–331 · [local source](../../../../../../source/modules/simpletest/tests/request_sanitizer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test#L329-L331)
- **Class:** [SanitizerTestRequest](../SanitizerTestRequest.md)
- **Module/theme:** batch_test

## Signature

```php
public function getQuery()
```

## Documentation

```text
Getter for $query.
```

## Code

```php
  public function getQuery() {
    return $this->query;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/request_sanitizer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
