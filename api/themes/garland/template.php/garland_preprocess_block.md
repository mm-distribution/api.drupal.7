# garland_preprocess_block()

- **Type:** Function
- **File:** [`themes/garland/template.php`](_file.md), lines 134–137 · [local source](../../../../source/themes/garland/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php#L134-L137)
- **Module/theme:** garland

## Signature

```php
function garland_preprocess_block(&$variables)
```

## Documentation

```text
Override or insert variables into the block template.
```

## Code

```php
function garland_preprocess_block(&$variables) {
  $variables['title_attributes_array']['class'][] = 'title';
  $variables['classes_array'][] = 'clearfix';
}
```

---
_Drupal 7.103 · [themes/garland/template.php](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
