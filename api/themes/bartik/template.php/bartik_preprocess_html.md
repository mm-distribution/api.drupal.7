# bartik_preprocess_html()

- **Type:** Function
- **File:** [`themes/bartik/template.php`](_file.md), lines 6–27 · [local source](../../../../source/themes/bartik/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/bartik/template.php#L6-L27)
- **Module/theme:** bartik

## Signature

```php
function bartik_preprocess_html(&$variables)
```

## Documentation

```text
Add body classes if certain regions have content.
```

## Code

```php
function bartik_preprocess_html(&$variables) {
  if (!empty($variables['page']['featured'])) {
    $variables['classes_array'][] = 'featured';
  }

  if (!empty($variables['page']['triptych_first'])
    || !empty($variables['page']['triptych_middle'])
    || !empty($variables['page']['triptych_last'])) {
    $variables['classes_array'][] = 'triptych';
  }

  if (!empty($variables['page']['footer_firstcolumn'])
    || !empty($variables['page']['footer_secondcolumn'])
    || !empty($variables['page']['footer_thirdcolumn'])
    || !empty($variables['page']['footer_fourthcolumn'])) {
    $variables['classes_array'][] = 'footer-columns';
  }

  // Add conditional stylesheets for IE
  drupal_add_css(path_to_theme() . '/css/ie.css', array('group' => CSS_THEME, 'browsers' => array('IE' => 'lte IE 7', '!IE' => FALSE), 'preprocess' => FALSE));
  drupal_add_css(path_to_theme() . '/css/ie6.css', array('group' => CSS_THEME, 'browsers' => array('IE' => 'IE 6', '!IE' => FALSE), 'preprocess' => FALSE));
}
```

---
_Drupal 7.103 · [themes/bartik/template.php](https://github.com/drupal/drupal/blob/7.103/themes/bartik/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
