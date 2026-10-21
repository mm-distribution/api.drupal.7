# search_block_info()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 141–147 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L141-L147)
- **Module/theme:** search
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function search_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function search_block_info() {
  $blocks['form']['info'] = t('Search form');
  // Not worth caching.
  $blocks['form']['cache'] = DRUPAL_NO_CACHE;
  $blocks['form']['properties']['administrative'] = TRUE;
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
