# block_install()

- **Type:** Function
- **File:** [`modules/block/block.install`](_file.md), lines 178–187 · [local source](../../../../source/modules/block/block.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install#L178-L187)
- **Module/theme:** block
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function block_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function block_install() {

  // Block should go first so that other modules can alter its output
  // during hook_page_alter(). Almost everything on the page is a block,
  // so before block module runs, there will not be much to alter.
  db_update('system')
    ->fields(array('weight' => -5))
    ->condition('name', 'block')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/block/block.install](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install) · Licensed GPL-2.0-or-later (see LICENSE)._
