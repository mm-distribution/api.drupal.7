# system_update_7048()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2529–2534 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2529-L2534)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7048()
```

## Documentation

```text
Convert path languages from the empty string to LANGUAGE_NONE.
```

## Code

```php
function system_update_7048() {
  db_update('url_alias')
    ->fields(array('language' => LANGUAGE_NONE))
    ->condition('language', '')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
