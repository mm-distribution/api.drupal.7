# bartik_preprocess_block()

- **Type:** Function
- **File:** [`themes/bartik/template.php`](_file.md), lines 120–125 · [local source](../../../../source/themes/bartik/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/bartik/template.php#L120-L125)
- **Module/theme:** bartik

## Signature

```php
function bartik_preprocess_block(&$variables)
```

## Documentation

```text
Override or insert variables into the block template.
```

## Code

```php
function bartik_preprocess_block(&$variables) {
  // In the header region visually hide block titles.
  if ($variables['block']->region == 'header') {
    $variables['title_attributes_array']['class'][] = 'element-invisible';
  }
}
```

---
_Drupal 7.103 · [themes/bartik/template.php](https://github.com/drupal/drupal/blob/7.103/themes/bartik/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
