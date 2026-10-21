# search_reindex_confirm_submit()

- **Type:** Function
- **File:** [`modules/search/search.admin.inc`](_file.md), lines 19–26 · [local source](../../../../source/modules/search/search.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.admin.inc#L19-L26)
- **Module/theme:** search

## Signature

```php
function search_reindex_confirm_submit(&$form, &$form_state)
```

## Documentation

```text
Handler for wipe confirmation
```

## Code

```php
function search_reindex_confirm_submit(&$form, &$form_state) {
  if ($form['confirm']) {
    search_reindex();
    drupal_set_message(t('The index will be rebuilt.'));
    $form_state['redirect'] = 'admin/config/search/settings';
    return;
  }
}
```

---
_Drupal 7.103 · [modules/search/search.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
