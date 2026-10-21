# theme_locale_date_format_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 1285–1305 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L1285-L1305)
- **Module/theme:** locale
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_locale_date_format_form($variables)
```

## Documentation

```text
Returns HTML for a locale date format form.

@param $variables
  An associative array containing:
  - form: A render element representing the form.

@ingroup themeable
```

## Code

```php
function theme_locale_date_format_form($variables) {
  $form = $variables['form'];
  $header = array(
    t('Date type'),
    t('Format'),
  );

  foreach (element_children($form['date_formats']) as $key) {
    $row = array();
    $row[] = $form['date_formats'][$key]['#title'];
    unset($form['date_formats'][$key]['#title']);
    $row[] = array('data' => drupal_render($form['date_formats'][$key]));
    $rows[] = $row;
  }

  $output = drupal_render($form['language']);
  $output .= theme('table', array('header' => $header, 'rows' => $rows));
  $output .= drupal_render_children($form);

  return $output;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
