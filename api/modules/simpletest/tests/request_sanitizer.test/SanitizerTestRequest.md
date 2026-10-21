# SanitizerTestRequest

- **Type:** Class
- **File:** [`modules/simpletest/tests/request_sanitizer.test`](_file.md), lines 277–354 · [local source](../../../../../source/modules/simpletest/tests/request_sanitizer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test#L277-L354)
- **Module/theme:** batch_test

## Signature

```php
class SanitizerTestRequest
```

## Documentation

```text
Basic HTTP Request class.
```

## Properties

### $query

```php
protected $query;
```

```text
The query (GET).

@var array
```

### $request

```php
protected $request;
```

```text
The request (POST).

@var array
```

### $attributes

```php
protected $attributes;
```

```text
The request attributes.

@var array
```

### $cookies

```php
protected $cookies;
```

```text
The request cookies.

@var array
```

## Methods (derived index)

- [__construct()](SanitizerTestRequest/__construct.md) — Constructor.
- [getQuery()](SanitizerTestRequest/getQuery.md) — Getter for $query.
- [getRequest()](SanitizerTestRequest/getRequest.md) — Getter for $request.
- [getAttributes()](SanitizerTestRequest/getAttributes.md) — Getter for $attributes.
- [getCookies()](SanitizerTestRequest/getCookies.md) — Getter for $cookies.

---
_Drupal 7.103 · [modules/simpletest/tests/request_sanitizer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
