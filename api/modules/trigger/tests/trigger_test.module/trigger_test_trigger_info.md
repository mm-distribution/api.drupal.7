# trigger_test_trigger_info()

- **Type:** Function
- **File:** [`modules/trigger/tests/trigger_test.module`](_file.md), lines 57–76 · [local source](../../../../../source/modules/trigger/tests/trigger_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module#L57-L76)
- **Module/theme:** trigger_test
- **Implements:** [hook_trigger_info()](../../trigger.api.php/hook_trigger_info.md)

## Signature

```php
function trigger_test_trigger_info()
```

## Documentation

```text
Implements hook_trigger_info().
```

## Code

```php
function trigger_test_trigger_info() {
  // Register triggers that this module provides. The first is an additional
  // node trigger and the second is our own, which should create a new tab
  // on the trigger assignment page. The last tests long trigger names.
  return array(
    'node' => array(
      'node_triggertest' => array(
        'label' => t('A test trigger is fired'),
      ),
    ),
    'trigger_test' => array(
      'trigger_test_triggertest' => array(
        'label' => t('Another test trigger is fired'),
      ),
      'trigger_test_we_sweat_it_out_in_the_streets_of_a_runaway_american_dream' => array(
        'label' => t('A test trigger with a name over 64 characters'),
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/trigger/tests/trigger_test.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
