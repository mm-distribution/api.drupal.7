# _update_manager_unique_identifier()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 903–909 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L903-L909)
- **Module/theme:** update

## Signature

```php
function _update_manager_unique_identifier()
```

## Documentation

```text
Returns a short unique identifier for this Drupal installation.

@return
  An eight character string uniquely identifying this Drupal installation.
```

## Code

```php
function _update_manager_unique_identifier() {
  $id = &drupal_static(__FUNCTION__, '');
  if (empty($id)) {
    $id = substr(hash('sha256', drupal_get_hash_salt()), 0, 8);
  }
  return $id;
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
