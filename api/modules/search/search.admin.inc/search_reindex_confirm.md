# search_reindex_confirm()

- **Type:** Function
- **File:** [`modules/search/search.admin.inc`](_file.md), lines 11–14 · [local source](../../../../source/modules/search/search.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.admin.inc#L11-L14)
- **Module/theme:** search

## Signature

```php
function search_reindex_confirm()
```

## Documentation

```text
Menu callback: confirm wiping of the index.
```

## Code

```php
function search_reindex_confirm() {
  return confirm_form(array(), t('Are you sure you want to re-index the site?'),
                  'admin/config/search/settings', t('The search index is not cleared but systematically updated to reflect the new settings. Searching will continue to work but new content won\'t be indexed until all existing content has been re-indexed. This action cannot be undone.'), t('Re-index site'), t('Cancel'));
}
```

---
_Drupal 7.103 · [modules/search/search.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
