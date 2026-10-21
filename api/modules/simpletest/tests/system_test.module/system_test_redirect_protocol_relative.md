# system_test_redirect_protocol_relative()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 234–237 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L234-L237)
- **Module/theme:** batch_test

## Signature

```php
function system_test_redirect_protocol_relative()
```

## Documentation

_No docblock in source._

## Code

```php
function system_test_redirect_protocol_relative() {
  header("Location: //example.com/path", TRUE, 301);
  exit;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
