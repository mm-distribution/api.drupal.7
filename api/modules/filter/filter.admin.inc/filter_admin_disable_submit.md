# filter_admin_disable_submit()

- **Type:** Function
- **File:** [`modules/filter/filter.admin.inc`](_file.md), lines 402–408 · [local source](../../../../source/modules/filter/filter.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc#L402-L408)
- **Module/theme:** filter

## Signature

```php
function filter_admin_disable_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for filter_admin_disable().
```

## Code

```php
function filter_admin_disable_submit($form, &$form_state) {
  $format = $form['#format'];
  filter_format_disable($format);
  drupal_set_message(t('Disabled text format %format.', array('%format' => $format->name)));

  $form_state['redirect'] = 'admin/config/content/formats';
}
```

---
_Drupal 7.103 · [modules/filter/filter.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
