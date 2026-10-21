# image_update_7001()

- **Type:** Function
- **File:** [`modules/image/image.install`](_file.md), lines 271–278 · [local source](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install#L271-L278)
- **Module/theme:** image
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function image_update_7001()
```

## Documentation

```text
Rename possibly misnamed {image_effect} table to {image_effects}.
```

## Code

```php
function image_update_7001() {
  // Due to a bug in earlier versions of image_update_7000() it is possible
  // to end up with an {image_effect} table where there should be an
  // {image_effects} table.
  if (!db_table_exists('image_effects') && db_table_exists('image_effect')) {
    db_rename_table('image_effect', 'image_effects');
  }
}
```

---
_Drupal 7.103 · [modules/image/image.install](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · Licensed GPL-2.0-or-later (see LICENSE)._
