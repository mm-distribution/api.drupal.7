# block_block_view()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 244–249 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L244-L249)
- **Module/theme:** block
- **Implements:** [hook_block_view()](../block.api.php/hook_block_view.md)

## Signature

```php
function block_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().

Generates the administrator-defined blocks for display.
```

## Code

```php
function block_block_view($delta = '') {
  $block = db_query('SELECT body, format FROM {block_custom} WHERE bid = :bid', array(':bid' => $delta))->fetchObject();
  $data['subject'] = NULL;
  $data['content'] = check_markup($block->body, $block->format, '', TRUE);
  return $data;
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
