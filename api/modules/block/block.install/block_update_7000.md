# block_update_7000()

- **Type:** Function
- **File:** [`modules/block/block.install`](_file.md), lines 215–220 · [local source](../../../../source/modules/block/block.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install#L215-L220)
- **Module/theme:** block
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function block_update_7000()
```

## Documentation

```text
Set system.weight to a low value for block module.

Block should go first so that other modules can alter its output
during hook_page_alter(). Almost everything on the page is a block,
so before block module runs, there will not be much to alter.
```

## Code

```php
function block_update_7000() {
  db_update('system')
    ->fields(array('weight' => '-5'))
    ->condition('name', 'block')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/block/block.install](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install) · Licensed GPL-2.0-or-later (see LICENSE)._
