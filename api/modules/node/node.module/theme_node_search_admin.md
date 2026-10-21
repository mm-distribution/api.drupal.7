# theme_node_search_admin()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1862–1879 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1862-L1879)
- **Module/theme:** node
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_node_search_admin($variables)
```

## Documentation

```text
Returns HTML for the content ranking part of the search settings admin page.

@param $variables
  An associative array containing:
  - form: A render element representing the form.

@see node_search_admin()
@ingroup themeable
```

## Code

```php
function theme_node_search_admin($variables) {
  $form = $variables['form'];

  $output = drupal_render($form['info']);

  $header = array(t('Factor'), t('Influence'));
  foreach (element_children($form['factors']) as $key) {
    $row = array();
    $row[] = $form['factors'][$key]['#title'];
    $form['factors'][$key]['#title_display'] = 'invisible';
    $row[] = drupal_render($form['factors'][$key]);
    $rows[] = $row;
  }
  $output .= theme('table', array('header' => $header, 'rows' => $rows));

  $output .= drupal_render_children($form);
  return $output;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
