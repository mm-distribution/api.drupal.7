# search_admin_reindex_submit()

- **Type:** Function
- **File:** [`modules/search/search.admin.inc`](_file.md), lines 193–196 · [local source](../../../../source/modules/search/search.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.admin.inc#L193-L196)
- **Module/theme:** search

## Signature

```php
function search_admin_reindex_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for reindex button on search_admin_settings_form().
```

## Code

```php
function search_admin_reindex_submit($form, &$form_state) {
  // send the user to the confirmation page
  $form_state['redirect'] = 'admin/config/search/settings/reindex';
}
```

---
_Drupal 7.103 · [modules/search/search.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
