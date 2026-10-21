# book_block_save()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 349–352 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L349-L352)
- **Module/theme:** book
- **Implements:** [hook_block_save()](../../block/block.api.php/hook_block_save.md)

## Signature

```php
function book_block_save($delta = '', $edit = array())
```

## Documentation

```text
Implements hook_block_save().
```

## Code

```php
function book_block_save($delta = '', $edit = array()) {
  $block = array();
  variable_set('book_block_mode', $edit['book_block_mode']);
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
