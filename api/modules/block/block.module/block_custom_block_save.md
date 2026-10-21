# block_custom_block_save()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 561–571 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L561-L571)
- **Module/theme:** block

## Signature

```php
function block_custom_block_save($edit, $delta)
```

## Documentation

```text
Saves a user-created block in the database.

@param $edit
  Associative array of fields to save. Array keys:
  - info: Block description.
  - body: Associative array of body value and format.  Array keys:
    - value: Block contents.
    - format: Filter ID of the filter format for the body.
@param $delta
  Block ID of the block to save.

@return
  Always returns TRUE.
```

## Code

```php
function block_custom_block_save($edit, $delta) {
  db_update('block_custom')
    ->fields(array(
      'body' => $edit['body']['value'],
      'info' => $edit['info'],
      'format' => $edit['body']['format'],
    ))
    ->condition('bid', $delta)
    ->execute();
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
