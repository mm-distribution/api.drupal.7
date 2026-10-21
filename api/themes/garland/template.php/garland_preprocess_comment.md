# garland_preprocess_comment()

- **Type:** Function
- **File:** [`themes/garland/template.php`](_file.md), lines 127–129 · [local source](../../../../source/themes/garland/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php#L127-L129)
- **Module/theme:** garland

## Signature

```php
function garland_preprocess_comment(&$variables)
```

## Documentation

```text
Override or insert variables into the comment template.
```

## Code

```php
function garland_preprocess_comment(&$variables) {
  $variables['submitted'] = $variables['created'] . ' — ' . $variables['author'];
}
```

---
_Drupal 7.103 · [themes/garland/template.php](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
