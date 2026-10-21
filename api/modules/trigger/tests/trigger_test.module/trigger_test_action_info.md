# trigger_test_action_info()

- **Type:** Function
- **File:** [`modules/trigger/tests/trigger_test.module`](_file.md), lines 11–52 · [local source](../../../../../source/modules/trigger/tests/trigger_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module#L11-L52)
- **Module/theme:** trigger_test
- **Implements:** [hook_action_info()](../../../system/system.api.php/hook_action_info.md)

## Signature

```php
function trigger_test_action_info()
```

## Documentation

```text
Implements hook_action_info().
```

## Code

```php
function trigger_test_action_info() {
  // Register an action that can be assigned to the trigger "cron".
  return array(
    'trigger_test_system_cron_action' => array(
      'type' => 'system',
      'label' => t('Cron test action'),
      'configurable' => FALSE,
      'triggers' => array('cron'),
    ),
    'trigger_test_system_cron_conf_action' => array(
      'type' => 'system',
      'label' => t('Cron test configurable action'),
      'configurable' => TRUE,
      'triggers' => array('cron'),
    ),
    'trigger_test_generic_action' => array(
      'type' => 'system',
      'label' => t('Generic test action'),
      'configurable' => FALSE,
      'triggers' => array(
        'taxonomy_term_insert',
        'taxonomy_term_update',
        'taxonomy_delete',
        'comment_insert',
        'comment_update',
        'comment_delete',
        'user_insert',
        'user_update',
        'user_delete',
        'user_login',
        'user_logout',
        'user_view',
      ),
    ),
    'trigger_test_generic_any_action' => array(
      'type' => 'system',
      'label' => t('Generic test action for any trigger'),
      'configurable' => FALSE,
      'triggers' => array('any'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/trigger/tests/trigger_test.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
