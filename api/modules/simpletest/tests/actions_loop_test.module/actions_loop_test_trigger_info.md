# actions_loop_test_trigger_info()

- **Type:** Function
- **File:** [`modules/simpletest/tests/actions_loop_test.module`](_file.md), lines 6–14 · [local source](../../../../../source/modules/simpletest/tests/actions_loop_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions_loop_test.module#L6-L14)
- **Module/theme:** batch_test
- **Implements:** [hook_trigger_info()](../../../trigger/trigger.api.php/hook_trigger_info.md)

## Signature

```php
function actions_loop_test_trigger_info()
```

## Documentation

```text
Implements hook_trigger_info().
```

## Code

```php
function actions_loop_test_trigger_info() {
  return array(
    'actions_loop_test' => array(
      'watchdog' => array(
        'label' => t('When a message is logged'),
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/actions_loop_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions_loop_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
