# theme_filter_admin_overview()

- **Type:** Function
- **File:** [`modules/filter/filter.admin.inc`](_file.md), lines 75–99 · [local source](../../../../source/modules/filter/filter.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc#L75-L99)
- **Module/theme:** filter
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_filter_admin_overview($variables)
```

## Documentation

```text
Returns HTML for the text format administration overview form.

@param $variables
  An associative array containing:
  - form: A render element representing the form.

@ingroup themeable
```

## Code

```php
function theme_filter_admin_overview($variables) {
  $form = $variables['form'];

  $rows = array();
  foreach (element_children($form['formats']) as $id) {
    $form['formats'][$id]['weight']['#attributes']['class'] = array('text-format-order-weight');
    $rows[] = array(
      'data' => array(
        drupal_render($form['formats'][$id]['name']),
        drupal_render($form['formats'][$id]['roles']),
        drupal_render($form['formats'][$id]['weight']),
        drupal_render($form['formats'][$id]['configure']),
        drupal_render($form['formats'][$id]['disable']),
      ),
      'class' => array('draggable'),
    );
  }
  $header = array(t('Name'), t('Roles'), t('Weight'), array('data' => t('Operations'), 'colspan' => 2));
  $output = theme('table', array('header' => $header, 'rows' => $rows, 'attributes' => array('id' => 'text-format-order')));
  $output .= drupal_render_children($form);

  drupal_add_tabledrag('text-format-order', 'order', 'sibling', 'text-format-order-weight');

  return $output;
}
```

---
_Drupal 7.103 · [modules/filter/filter.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
