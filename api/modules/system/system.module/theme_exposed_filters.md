# theme_exposed_filters()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 4074–4089 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L4074-L4089)
- **Module/theme:** system
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_exposed_filters($variables)
```

## Documentation

```text
Returns HTML for an exposed filter form.

@param $variables
  An associative array containing:
  - form: An associative array containing the structure of the form.

@return
  A string containing an HTML-formatted form.

@ingroup themeable
```

## Code

```php
function theme_exposed_filters($variables) {
  $form = $variables['form'];
  $output = '';

  if (isset($form['current'])) {
    $items = array();
    foreach (element_children($form['current']) as $key) {
      $items[] = drupal_render($form['current'][$key]);
    }
    $output .= theme('item_list', array('items' => $items, 'attributes' => array('class' => array('clearfix', 'current-filters'))));
  }

  $output .= drupal_render_children($form);

  return '<div class="exposed-filters">' . $output . '</div>';
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
