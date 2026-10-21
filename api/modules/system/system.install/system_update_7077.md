# system_update_7077()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3290–3298 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3290-L3298)
- **Module/theme:** system
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function system_update_7077()
```

## Documentation

```text
Revert {file_managed}.filename changed to a binary column.
```

## Code

```php
function system_update_7077() {
  db_change_field('file_managed', 'filename', 'filename', array(
    'description' => 'Name of the file with no path components. This may differ from the basename of the URI if the file is renamed to avoid overwriting an existing file.',
    'type' => 'varchar',
    'length' => 255,
    'not null' => TRUE,
    'default' => '',
  ));
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
