# seven_tablesort_indicator()

- **Type:** Function
- **File:** [`themes/seven/template.php`](_file.md), lines 89–98 · [local source](../../../../source/themes/seven/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/seven/template.php#L89-L98)
- **Module/theme:** seven

## Signature

```php
function seven_tablesort_indicator($variables)
```

## Documentation

```text
Override of theme_tablesort_indicator().

Use our own image versions, so they show up as black and not gray on gray.
```

## Code

```php
function seven_tablesort_indicator($variables) {
  $style = $variables['style'];
  $theme_path = drupal_get_path('theme', 'seven');
  if ($style == 'asc') {
    return theme('image', array('path' => $theme_path . '/images/arrow-asc.png', 'alt' => t('sort ascending'), 'width' => 13, 'height' => 13, 'title' => t('sort ascending')));
  }
  else {
    return theme('image', array('path' => $theme_path . '/images/arrow-desc.png', 'alt' => t('sort descending'), 'width' => 13, 'height' => 13, 'title' => t('sort descending')));
  }
}
```

---
_Drupal 7.103 · [themes/seven/template.php](https://github.com/drupal/drupal/blob/7.103/themes/seven/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
