# update_extra_requirements()

- **Type:** Function
- **File:** [`update.php`](_file.md), lines 337–343 · [local source](../../source/update.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/update.php#L337-L343)

## Signature

```php
function update_extra_requirements($requirements = NULL)
```

## Documentation

```text
Returns and stores extra requirements that apply during the update process.
```

## Code

```php
function update_extra_requirements($requirements = NULL) {
  static $extra_requirements = array();
  if (isset($requirements)) {
    $extra_requirements += $requirements;
  }
  return $extra_requirements;
}
```

---
_Drupal 7.103 · [update.php](https://github.com/drupal/drupal/blob/7.103/update.php) · Licensed GPL-2.0-or-later (see LICENSE)._
