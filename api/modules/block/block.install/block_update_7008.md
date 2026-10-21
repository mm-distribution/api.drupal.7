# block_update_7008()

- **Type:** Function
- **File:** [`modules/block/block.install`](_file.md), lines 471–473 · [local source](../../../../source/modules/block/block.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install#L471-L473)
- **Module/theme:** block
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function block_update_7008()
```

## Documentation

```text
Update database to match Drupal 7 schema.
```

## Code

```php
function block_update_7008() {
  db_drop_field('block', 'throttle');
}
```

---
_Drupal 7.103 · [modules/block/block.install](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install) · Licensed GPL-2.0-or-later (see LICENSE)._
