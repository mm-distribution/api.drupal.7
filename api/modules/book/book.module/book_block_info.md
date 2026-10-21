# book_block_info()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 261–267 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L261-L267)
- **Module/theme:** book
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function book_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function book_block_info() {
  $block = array();
  $block['navigation']['info'] = t('Book navigation');
  $block['navigation']['cache'] = DRUPAL_CACHE_PER_PAGE | DRUPAL_CACHE_PER_ROLE;

  return $block;
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
