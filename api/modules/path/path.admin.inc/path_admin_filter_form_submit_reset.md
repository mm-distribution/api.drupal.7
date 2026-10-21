# path_admin_filter_form_submit_reset()

- **Type:** Function
- **File:** [`modules/path/path.admin.inc`](_file.md), lines 316–318 · [local source](../../../../source/modules/path/path.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc#L316-L318)
- **Module/theme:** path

## Signature

```php
function path_admin_filter_form_submit_reset($form, &$form_state)
```

## Documentation

```text
Form submission handler for the path_admin_filter_form() Reset button.

@see path_admin_filter_form_submit_filter()
```

## Code

```php
function path_admin_filter_form_submit_reset($form, &$form_state) {
  $form_state['redirect'] = 'admin/config/search/path/list';
}
```

---
_Drupal 7.103 · [modules/path/path.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
