# garland_preprocess_html()

- **Type:** Function
- **File:** [`themes/garland/template.php`](_file.md), lines 34–41 · [local source](../../../../source/themes/garland/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php#L34-L41)
- **Module/theme:** garland

## Signature

```php
function garland_preprocess_html(&$variables)
```

## Documentation

```text
Override or insert variables into the html template.
```

## Code

```php
function garland_preprocess_html(&$variables) {
  // Toggle fixed or fluid width.
  if (theme_get_setting('garland_width') == 'fluid') {
    $variables['classes_array'][] = 'fluid-width';
  }
  // Add conditional CSS for IE6.
  drupal_add_css(path_to_theme() . '/fix-ie.css', array('group' => CSS_THEME, 'browsers' => array('IE' => 'lt IE 7', '!IE' => FALSE), 'preprocess' => FALSE));
}
```

---
_Drupal 7.103 · [themes/garland/template.php](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
