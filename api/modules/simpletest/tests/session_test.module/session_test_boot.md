# session_test_boot()

- **Type:** Function
- **File:** [`modules/simpletest/tests/session_test.module`](_file.md), lines 83–85 · [local source](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module#L83-L85)
- **Module/theme:** batch_test
- **Implements:** [hook_boot()](../../../system/system.api.php/hook_boot.md)

## Signature

```php
function session_test_boot()
```

## Documentation

```text
Implements hook_boot().
```

## Code

```php
function session_test_boot() {
  header('X-Session-Empty: ' . intval(empty($_SESSION)));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
