# actions_loop_test_action_info()

- **Type:** Function
- **File:** [`modules/simpletest/tests/actions_loop_test.module`](_file.md), lines 49–58 · [local source](../../../../../source/modules/simpletest/tests/actions_loop_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions_loop_test.module#L49-L58)
- **Module/theme:** batch_test
- **Implements:** [hook_action_info()](../../../system/system.api.php/hook_action_info.md)

## Signature

```php
function actions_loop_test_action_info()
```

## Documentation

```text
Implements hook_action_info().
```

## Code

```php
function actions_loop_test_action_info() {
  return array(
    'actions_loop_test_log' => array(
      'label' => t('Write a message to the log.'),
      'type' => 'system',
      'configurable' => FALSE,
      'triggers' => array('any'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/actions_loop_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions_loop_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
