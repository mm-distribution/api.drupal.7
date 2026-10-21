# theme_menu_local_tasks()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2304–2321 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2304-L2321)
- **Topics:** [menu](../../topics/menu.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_menu_local_tasks(&$variables)
```

## Documentation

```text
Returns HTML for primary and secondary local tasks.

@param $variables
  An associative array containing:
    - primary: (optional) An array of local tasks (tabs).
    - secondary: (optional) An array of local tasks (tabs).

@ingroup themeable
@see menu_local_tasks()
```

## Code

```php
function theme_menu_local_tasks(&$variables) {
  $output = '';

  if (!empty($variables['primary'])) {
    $variables['primary']['#prefix'] = '<h2 class="element-invisible">' . t('Primary tabs') . '</h2>';
    $variables['primary']['#prefix'] .= '<ul class="tabs primary">';
    $variables['primary']['#suffix'] = '</ul>';
    $output .= drupal_render($variables['primary']);
  }
  if (!empty($variables['secondary'])) {
    $variables['secondary']['#prefix'] = '<h2 class="element-invisible">' . t('Secondary tabs') . '</h2>';
    $variables['secondary']['#prefix'] .= '<ul class="tabs secondary">';
    $variables['secondary']['#suffix'] = '</ul>';
    $output .= drupal_render($variables['secondary']);
  }

  return $output;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
