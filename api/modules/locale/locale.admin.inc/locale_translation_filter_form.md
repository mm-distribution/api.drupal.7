# locale_translation_filter_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 843–892 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L843-L892)
- **Module/theme:** locale
- **Topics:** [locale-translate-administration-screens](../../../topics/locale-translate-administration-screens.md), [forms](../../../topics/forms.md)

## Signature

```php
function locale_translation_filter_form()
```

## Documentation

```text
Return form for locale translation filters.

@ingroup forms
```

## Code

```php
function locale_translation_filter_form() {
  $filters = locale_translation_filters();

  $form['filters'] = array(
    '#type' => 'fieldset',
    '#title' => t('Filter translatable strings'),
    '#collapsible' => TRUE,
    '#collapsed' => FALSE,
  );
  foreach ($filters as $key => $filter) {
    // Special case for 'string' filter.
    if ($key == 'string') {
      $form['filters']['status']['string'] = array(
        '#type' => 'textfield',
        '#title' => $filter['title'],
        '#description' => $filter['description'],
      );
    }
    else {
      $form['filters']['status'][$key] = array(
        '#title' => $filter['title'],
        '#type' => 'select',
        '#empty_value' => 'all',
        '#empty_option' => $filter['options']['all'],
        '#size' => 0,
        '#options' => $filter['options'],
      );
    }
    if (!empty($_SESSION['locale_translation_filter'][$key])) {
      $form['filters']['status'][$key]['#default_value'] = $_SESSION['locale_translation_filter'][$key];
    }
  }

  $form['filters']['actions'] = array(
    '#type' => 'actions',
    '#attributes' => array('class' => array('container-inline')),
  );
  $form['filters']['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Filter'),
  );
  if (!empty($_SESSION['locale_translation_filter'])) {
    $form['filters']['actions']['reset'] = array(
      '#type' => 'submit',
      '#value' => t('Reset')
    );
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
