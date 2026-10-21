# system_update_7073()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3235–3254 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3235-L3254)
- **Module/theme:** system
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function system_update_7073()
```

## Documentation

```text
Add binary to {file_managed}, in case system_update_7034() was run without
it.
```

## Code

```php
function system_update_7073() {
  db_change_field('file_managed', 'filename', 'filename', array(
    'description' => 'Name of the file with no path components. This may differ from the basename of the URI if the file is renamed to avoid overwriting an existing file.',
    'type' => 'varchar',
    'length' => 255,
    'not null' => TRUE,
    'default' => '',
    'binary' => TRUE,
  ));
  db_drop_unique_key('file_managed', 'uri');
  db_change_field('file_managed', 'uri', 'uri', array(
    'description' => 'The URI to access the file (either local or remote).',
    'type' => 'varchar',
    'length' => 255,
    'not null' => TRUE,
    'default' => '',
    'binary' => TRUE,
  ));
  db_add_unique_key('file_managed', 'uri', array('uri'));
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
