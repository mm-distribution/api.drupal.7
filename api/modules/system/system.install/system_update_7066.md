# system_update_7066()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3137–3141 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3137-L3141)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7066()
```

## Documentation

```text
Migrate the 'file_directory_temp' variable.
```

## Code

```php
function system_update_7066() {
  $d6_file_directory_temp = variable_get('file_directory_temp', file_directory_temp());
  variable_set('file_temporary_path', $d6_file_directory_temp);
  variable_del('file_directory_temp');
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
