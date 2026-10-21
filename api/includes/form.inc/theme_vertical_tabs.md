# theme_vertical_tabs()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3918–3926 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3918-L3926)
- **Topics:** [form_api](../../topics/form_api.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_vertical_tabs($variables)
```

## Documentation

```text
Returns HTML for an element's children fieldsets as vertical tabs.

@param $variables
  An associative array containing:
  - element: An associative array containing the properties and children of
    the fieldset. Properties used: #children.

@ingroup themeable
```

## Code

```php
function theme_vertical_tabs($variables) {
  $element = $variables['element'];
  // Add required JavaScript and Stylesheet.
  drupal_add_library('system', 'drupal.vertical-tabs');

  $output = '<h2 class="element-invisible">' . t('Vertical Tabs') . '</h2>';
  $output .= '<div class="vertical-tabs-panes">' . $element['#children'] . '</div>';
  return $output;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
