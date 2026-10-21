# cron_queue_test_exception()

- **Type:** Function
- **File:** [`modules/system/tests/cron_queue_test.module`](_file.md), lines 17–19 · [local source](../../../../../source/modules/system/tests/cron_queue_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/tests/cron_queue_test.module#L17-L19)
- **Module/theme:** cron_queue_test

## Signature

```php
function cron_queue_test_exception($item)
```

## Documentation

_No docblock in source._

## Code

```php
function cron_queue_test_exception($item) {
  throw new Exception('That is not supposed to happen.');
}
```

---
_Drupal 7.103 · [modules/system/tests/cron_queue_test.module](https://github.com/drupal/drupal/blob/7.103/modules/system/tests/cron_queue_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
