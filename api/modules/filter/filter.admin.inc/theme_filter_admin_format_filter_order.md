# theme_filter_admin_format_filter_order()

- **Type:** Function
- **File:** [`modules/filter/filter.admin.inc`](_file.md), lines 303–323 · [local source](../../../../source/modules/filter/filter.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc#L303-L323)
- **Module/theme:** filter
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_filter_admin_format_filter_order($variables)
```

## Documentation

```text
Returns HTML for a text format's filter order form.

@param $variables
  An associative array containing:
  - element: A render element representing the form.

@ingroup themeable
```

## Code

```php
function theme_filter_admin_format_filter_order($variables) {
  $element = $variables['element'];

  // Filter order (tabledrag).
  $rows = array();
  foreach (element_children($element, TRUE) as $name) {
    $element[$name]['weight']['#attributes']['class'][] = 'filter-order-weight';
    $rows[] = array(
      'data' => array(
        drupal_render($element[$name]['filter']),
        drupal_render($element[$name]['weight']),
      ),
      'class' => array('draggable'),
    );
  }
  $output = drupal_render_children($element);
  $output .= theme('table', array('rows' => $rows, 'attributes' => array('id' => 'filter-order')));
  drupal_add_tabledrag('filter-order', 'order', 'sibling', 'filter-order-weight', NULL, NULL, TRUE);

  return $output;
}
```

---
_Drupal 7.103 · [modules/filter/filter.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
