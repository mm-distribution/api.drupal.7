# trigger_test_system_cron_conf_action_form()

- **Type:** Function
- **File:** [`modules/trigger/tests/trigger_test.module`](_file.md), lines 98–107 · [local source](../../../../../source/modules/trigger/tests/trigger_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module#L98-L107)
- **Module/theme:** trigger_test

## Signature

```php
function trigger_test_system_cron_conf_action_form($context)
```

## Documentation

```text
Form for configurable test action.
```

## Code

```php
function trigger_test_system_cron_conf_action_form($context) {
  if (!isset($context['subject'])) {
    $context['subject'] = '';
  }
  $form['subject'] = array(
    '#type' => 'textfield',
    '#default_value' => $context['subject'],
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/trigger/tests/trigger_test.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/tests/trigger_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
