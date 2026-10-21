# bartik_preprocess_node()

- **Type:** Function
- **File:** [`themes/bartik/template.php`](_file.md), lines 111–115 · [local source](../../../../source/themes/bartik/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/bartik/template.php#L111-L115)
- **Module/theme:** bartik

## Signature

```php
function bartik_preprocess_node(&$variables)
```

## Documentation

```text
Override or insert variables into the node template.
```

## Code

```php
function bartik_preprocess_node(&$variables) {
  if ($variables['view_mode'] == 'full' && node_is_page($variables['node'])) {
    $variables['classes_array'][] = 'node-full';
  }
}
```

---
_Drupal 7.103 · [themes/bartik/template.php](https://github.com/drupal/drupal/blob/7.103/themes/bartik/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
