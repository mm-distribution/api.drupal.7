# system_test_exit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 335–337 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L335-L337)
- **Module/theme:** batch_test
- **Implements:** [hook_exit()](../../../system/system.api.php/hook_exit.md)

## Signature

```php
function system_test_exit()
```

## Documentation

```text
Implements hook_exit().
```

## Code

```php
function system_test_exit() {
  watchdog('system_test', 'hook_exit');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
