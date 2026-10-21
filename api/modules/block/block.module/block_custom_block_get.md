# block_custom_block_get()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 503–505 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L503-L505)
- **Module/theme:** block

## Signature

```php
function block_custom_block_get($bid)
```

## Documentation

```text
Returns information from database about a user-created (custom) block.

@param $bid
  ID of the block to get information for.

@return
  Associative array of information stored in the database for this block.
  Array keys:
  - bid: Block ID.
  - info: Block description.
  - body: Block contents.
  - format: Filter ID of the filter format for the body.
```

## Code

```php
function block_custom_block_get($bid) {
  return db_query("SELECT * FROM {block_custom} WHERE bid = :bid", array(':bid' => $bid))->fetchAssoc();
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
