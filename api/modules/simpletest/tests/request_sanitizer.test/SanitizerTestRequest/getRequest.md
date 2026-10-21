# SanitizerTestRequest::getRequest()

- **Type:** Method
- **File:** [`modules/simpletest/tests/request_sanitizer.test`](../_file.md), lines 336–338 · [local source](../../../../../../source/modules/simpletest/tests/request_sanitizer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test#L336-L338)
- **Class:** [SanitizerTestRequest](../SanitizerTestRequest.md)
- **Module/theme:** batch_test

## Signature

```php
public function getRequest()
```

## Documentation

```text
Getter for $request.
```

## Code

```php
  public function getRequest() {
    return $this->request;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/request_sanitizer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
