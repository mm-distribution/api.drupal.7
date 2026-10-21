# block_update_7005()

- **Type:** Function
- **File:** [`modules/block/block.install`](_file.md), lines 411–432 · [local source](../../../../source/modules/block/block.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install#L411-L432)
- **Module/theme:** block
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function block_update_7005()
```

## Documentation

```text
Update the {block_custom}.format column.
```

## Code

```php
function block_update_7005() {
  // For an explanation of these updates, see the code comments in
  // user_update_7010().
  db_change_field('block_custom', 'format', 'format', array(
    'type' => 'int',
    'unsigned' => TRUE,
    'not null' => FALSE,
    'description' => 'The {filter_format}.format of the block body.',
  ));
  db_update('block_custom')
    ->fields(array('format' => NULL))
    ->condition('body', '')
    ->condition('format', 0)
    ->execute();
  $existing_formats = db_query("SELECT format FROM {filter_format}")->fetchCol();
  $default_format = variable_get('filter_default_format', 1);
  db_update('block_custom')
    ->fields(array('format' => $default_format))
    ->isNotNull('format')
    ->condition('format', $existing_formats, 'NOT IN')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/block/block.install](https://github.com/drupal/drupal/blob/7.103/modules/block/block.install) · Licensed GPL-2.0-or-later (see LICENSE)._
