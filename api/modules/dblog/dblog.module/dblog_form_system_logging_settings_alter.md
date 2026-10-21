# dblog_form_system_logging_settings_alter()

- **Type:** Function
- **File:** [`modules/dblog/dblog.module`](_file.md), lines 176–185 · [local source](../../../../source/modules/dblog/dblog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module#L176-L185)
- **Module/theme:** dblog
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function dblog_form_system_logging_settings_alter(&$form, $form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter() for system_logging_settings().
```

## Code

```php
function dblog_form_system_logging_settings_alter(&$form, $form_state) {
  $form['dblog_row_limit'] = array(
    '#type' => 'select',
    '#title' => t('Database log messages to keep'),
    '#default_value' => variable_get('dblog_row_limit', 1000),
    '#options' => array(0 => t('All')) + drupal_map_assoc(array(100, 1000, 10000, 100000, 1000000)),
    '#description' => t('The maximum number of messages to keep in the database log. Requires a <a href="@cron">cron maintenance task</a>.', array('@cron' => url('admin/reports/status')))
  );
  $form['actions']['#weight'] = 1;
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.module](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
