# SanitizerTestRequest::__construct()

- **Type:** Method
- **File:** [`modules/simpletest/tests/request_sanitizer.test`](../_file.md), lines 319–324 · [local source](../../../../../../source/modules/simpletest/tests/request_sanitizer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test#L319-L324)
- **Class:** [SanitizerTestRequest](../SanitizerTestRequest.md)
- **Module/theme:** batch_test

## Signature

```php
public function __construct(array $query = array(), array $request = array(), array $attributes = array(), array $cookies = array())
```

## Documentation

```text
Constructor.

@param array $query
  The GET parameters.
@param array $request
  The POST parameters.
@param array $attributes
  The request attributes.
@param array $cookies
  The COOKIE parameters.
```

## Code

```php
  public function __construct(array $query = array(), array $request = array(), array $attributes = array(), array $cookies = array()) {
    $this->query = $query;
    $this->request = $request;
    $this->attributes = $attributes;
    $this->cookies = $cookies;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/request_sanitizer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
