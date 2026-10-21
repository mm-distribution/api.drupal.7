# seven_preprocess_html()

- **Type:** Function
- **File:** [`themes/seven/template.php`](_file.md), lines 18–25 · [local source](../../../../source/themes/seven/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/seven/template.php#L18-L25)
- **Module/theme:** seven

## Signature

```php
function seven_preprocess_html(&$vars)
```

## Documentation

```text
Override or insert variables into the html template.
```

## Code

```php
function seven_preprocess_html(&$vars) {
  // Add conditional CSS for IE8 and below.
  drupal_add_css(path_to_theme() . '/ie.css', array('group' => CSS_THEME, 'browsers' => array('IE' => 'lte IE 8', '!IE' => FALSE), 'weight' => 999, 'preprocess' => FALSE));
  // Add conditional CSS for IE7 and below.
  drupal_add_css(path_to_theme() . '/ie7.css', array('group' => CSS_THEME, 'browsers' => array('IE' => 'lte IE 7', '!IE' => FALSE), 'weight' => 999, 'preprocess' => FALSE));
  // Add conditional CSS for IE6.
  drupal_add_css(path_to_theme() . '/ie6.css', array('group' => CSS_THEME, 'browsers' => array('IE' => 'lte IE 6', '!IE' => FALSE), 'weight' => 999, 'preprocess' => FALSE));
}
```

---
_Drupal 7.103 · [themes/seven/template.php](https://github.com/drupal/drupal/blob/7.103/themes/seven/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
