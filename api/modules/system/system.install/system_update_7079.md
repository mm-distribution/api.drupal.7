# system_update_7079()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3318–3328 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3318-L3328)
- **Module/theme:** system
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function system_update_7079()
```

## Documentation

```text
Convert the 'filesize' column in {file_managed} to a bigint.
```

## Code

```php
function system_update_7079() {
  $spec = array(
    'description' => 'The size of the file in bytes.',
    'type' => 'int',
    'size' => 'big',
    'unsigned' => TRUE,
    'not null' => TRUE,
    'default' => 0,
  );
  db_change_field('file_managed', 'filesize', 'filesize', $spec);
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
