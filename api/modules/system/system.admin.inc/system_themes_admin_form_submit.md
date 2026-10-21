# system_themes_admin_form_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 287–291 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L287-L291)
- **Module/theme:** system

## Signature

```php
function system_themes_admin_form_submit($form, &$form_state)
```

## Documentation

```text
Process system_themes_admin_form form submissions.
```

## Code

```php
function system_themes_admin_form_submit($form, &$form_state) {
  drupal_set_message(t('The configuration options have been saved.'));
  variable_set('admin_theme', $form_state['values']['admin_theme']);
  variable_set('node_admin_theme', $form_state['values']['node_admin_theme']);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
