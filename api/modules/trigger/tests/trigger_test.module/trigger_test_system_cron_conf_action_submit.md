# trigger_test_system_cron_conf_action_submit()

- **Type:** Function
- **File:** [`modules/trigger/tests/trigger_test.module`](_file.md), lines 112–120 · [local source](../../../../../source/modules/trigger/tests/trigger_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module#L112-L120)
- **Module/theme:** trigger_test

## Signature

```php
function trigger_test_system_cron_conf_action_submit($form, $form_state)
```

## Documentation

```text
Form submission handler for configurable test action.
```

## Code

```php
function trigger_test_system_cron_conf_action_submit($form, $form_state) {
  $form_values = $form_state['values'];
  // Process the HTML form to store configuration. The keyed array that
  // we return will be serialized to the database.
  $params = array(
    'subject' => $form_values['subject'],
  );
  return $params;
}
```

---
_Drupal 7.103 · [modules/trigger/tests/trigger_test.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
