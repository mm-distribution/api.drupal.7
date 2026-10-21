# block_update_7003()

- **Type:** Function
- **File:** [`modules/block/block.install`](_file.md), lines 236–247 · [local source](../../../../source/modules/block/block.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install#L236-L247)
- **Module/theme:** block
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function block_update_7003()
```

## Documentation

```text
Change the weight column to normal int.
```

## Code

```php
function block_update_7003() {
  db_change_field('block', 'weight', 'weight', array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'description' => 'Block weight within region.',
  ), array(
    'indexes' => array(
      'list' => array('theme', 'status', 'region', 'weight', 'module'),
    ),
  ));
}
```

---
_Drupal 7.103 · [modules/block/block.install](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install) · Licensed GPL-2.0-or-later (see LICENSE)._
