# path_admin_filter_form_submit_filter()

- **Type:** Function
- **File:** [`modules/path/path.admin.inc`](_file.md), lines 307–309 · [local source](../../../../source/modules/path/path.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc#L307-L309)
- **Module/theme:** path

## Signature

```php
function path_admin_filter_form_submit_filter($form, &$form_state)
```

## Documentation

```text
Form submission handler for the path_admin_filter_form() Filter button.

@see path_admin_filter_form_submit_reset()
```

## Code

```php
function path_admin_filter_form_submit_filter($form, &$form_state) {
  $form_state['redirect'] = 'admin/config/search/path/list/' . trim($form_state['values']['filter']);
}
```

---
_Drupal 7.103 · [modules/path/path.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
