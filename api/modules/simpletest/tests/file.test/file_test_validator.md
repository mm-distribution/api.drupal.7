# file_test_validator()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file.test`](_file.md), lines 12–14 · [local source](../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L12-L14)
- **Module/theme:** batch_test

## Signature

```php
function file_test_validator($file, $errors)
```

## Documentation

```text
Helper validator that returns the $errors parameter.
```

## Code

```php
function file_test_validator($file, $errors) {
  return $errors;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
