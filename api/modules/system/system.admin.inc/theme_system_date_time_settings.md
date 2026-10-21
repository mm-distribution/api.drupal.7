# theme_system_date_time_settings()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2101–2123 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2101-L2123)
- **Module/theme:** system
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_system_date_time_settings($variables)
```

## Documentation

```text
Returns HTML for the date settings form.

@param $variables
  An associative array containing:
  - form: A render element representing the form.

@ingroup themeable
```

## Code

```php
function theme_system_date_time_settings($variables) {
  $form = $variables['form'];
  $header = array(
    t('Date type'),
    t('Format'),
    t('Operations'),
  );

  foreach (element_children($form['format']) as $key) {
    $delete_key = $key . '_delete';
    $row = array();
    $row[] = $form['format'][$key]['#title'];
    $form['format'][$key]['#title_display'] = 'invisible';
    $row[] = array('data' => drupal_render($form['format'][$key]));
    $row[] = array('data' => drupal_render($form['delete'][$delete_key]));
    $rows[] = $row;
  }

  $output = theme('table', array('header' => $header, 'rows' => $rows, 'attributes' => array('id' => 'system-date-types')));
  $output .= drupal_render_children($form);

  return $output;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
