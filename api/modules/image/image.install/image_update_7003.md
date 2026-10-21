# image_update_7003()

- **Type:** Function
- **File:** [`modules/image/image.install`](_file.md), lines 417–420 · [local source](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install#L417-L420)
- **Module/theme:** image
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function image_update_7003()
```

## Documentation

```text
Remove the variables that set alt and title length since they were not
used for database column size and could cause PDO exceptions.
```

## Code

```php
function image_update_7003() {
  variable_del('image_alt_length');
  variable_del('image_title_length');
}
```

---
_Drupal 7.103 · [modules/image/image.install](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · Licensed GPL-2.0-or-later (see LICENSE)._
