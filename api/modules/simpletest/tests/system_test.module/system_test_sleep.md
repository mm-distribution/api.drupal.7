# system_test_sleep()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 165–167 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L165-L167)
- **Module/theme:** batch_test

## Signature

```php
function system_test_sleep($seconds)
```

## Documentation

_No docblock in source._

## Code

```php
function system_test_sleep($seconds) {
  sleep($seconds);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
