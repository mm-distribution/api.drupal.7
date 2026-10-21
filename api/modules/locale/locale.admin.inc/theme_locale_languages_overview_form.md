# theme_locale_languages_overview_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 73–115 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L73-L115)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md), [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_locale_languages_overview_form($variables)
```

## Documentation

```text
Returns HTML for the language overview form.

@param $variables
  An associative array containing:
  - form: A render element representing the form.

@ingroup themeable
```

## Code

```php
function theme_locale_languages_overview_form($variables) {
  $form = $variables['form'];
  $default = language_default();
  foreach ($form['name'] as $key => $element) {
    // Do not take form control structures.
    if (is_array($element) && element_child($key)) {
      // Disable checkbox for the default language, because it cannot be disabled.
      if ($key == $default->language) {
        $form['enabled'][$key]['#attributes']['disabled'] = 'disabled';
      }

      // Add invisible labels for the checkboxes and radio buttons in the table
      // for accessibility. These changes are only required and valid when the
      // form is themed as a table, so it would be wrong to perform them in the
      // form constructor.
      $title = drupal_render($form['name'][$key]);
      $form['enabled'][$key]['#title'] = t('Enable !title', array('!title' => $title));
      $form['enabled'][$key]['#title_display'] = 'invisible';
      $form['site_default'][$key]['#title'] = t('Set !title as default', array('!title' => $title));
      $form['site_default'][$key]['#title_display'] = 'invisible';
      $rows[] = array(
        'data' => array(
          '<strong>' . $title . '</strong>',
          drupal_render($form['native'][$key]),
          check_plain($key),
          drupal_render($form['direction'][$key]),
          array('data' => drupal_render($form['enabled'][$key]), 'align' => 'center'),
          drupal_render($form['site_default'][$key]),
          drupal_render($form['weight'][$key]),
          l(t('edit'), 'admin/config/regional/language/edit/' . $key) . (($key != 'en' && $key != $default->language) ? ' ' . l(t('delete'), 'admin/config/regional/language/delete/' . $key) : '')
        ),
        'class' => array('draggable'),
      );
    }
  }
  $header = array(array('data' => t('English name')), array('data' => t('Native name')), array('data' => t('Code')), array('data' => t('Direction')), array('data' => t('Enabled')), array('data' => t('Default')), array('data' => t('Weight')), array('data' => t('Operations')));
  $output = theme('table', array('header' => $header, 'rows' => $rows, 'attributes' => array('id' => 'language-order')));
  $output .= drupal_render_children($form);

  drupal_add_tabledrag('language-order', 'order', 'sibling', 'language-order-weight');

  return $output;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
