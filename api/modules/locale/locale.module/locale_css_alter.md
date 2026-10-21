# locale_css_alter()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 965–984 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L965-L984)
- **Module/theme:** locale
- **Implements:** [hook_css_alter()](../../system/system.api.php/hook_css_alter.md)

## Signature

```php
function locale_css_alter(&$css)
```

## Documentation

```text
Implements hook_css_alter().

This function checks all CSS files currently added via drupal_add_css() and
and checks to see if a related right to left CSS file should be included.
```

## Code

```php
function locale_css_alter(&$css) {
  global $language;

  // If the current language is RTL, add the CSS file with the RTL overrides.
  if ($language->direction == LANGUAGE_RTL) {
    foreach ($css as $data => $item) {
      // Only provide RTL overrides for files.
      if ($item['type'] == 'file') {
        $rtl_path = str_replace('.css', '-rtl.css', $item['data']);
        if (file_exists($rtl_path) && !isset($css[$rtl_path])) {
          // Replicate the same item, but with the RTL path and a little larger
          // weight so that it appears directly after the original CSS file.
          $item['data'] = $rtl_path;
          $item['weight'] += 0.0001;
          $css[$rtl_path] = $item;
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
