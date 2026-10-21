# aggregator_admin_form_submit()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 529–534 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L529-L534)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_admin_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for aggregator_admin_form().
```

## Code

```php
function aggregator_admin_form_submit($form, &$form_state) {
  if (isset($form_state['values']['aggregator_processors'])) {
    $form_state['values']['aggregator_processors'] = array_filter($form_state['values']['aggregator_processors']);
  }
  system_settings_form_submit($form, $form_state);
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
