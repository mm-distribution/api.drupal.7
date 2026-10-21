# path_admin_filter_form()

- **Type:** Function
- **File:** [`modules/path/path.admin.inc`](_file.md), lines 273–300 · [local source](../../../../source/modules/path/path.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc#L273-L300)
- **Module/theme:** path
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function path_admin_filter_form($form, &$form_state, $keys = '')
```

## Documentation

```text
Form constructor for the path admin overview filter form.

@ingroup forms
@see path_admin_filter_form_submit_filter()
@see path_admin_filter_form_submit_reset()
```

## Code

```php
function path_admin_filter_form($form, &$form_state, $keys = '') {
  $form['#attributes'] = array('class' => array('search-form'));
  $form['basic'] = array('#type' => 'fieldset',
    '#title' => t('Filter aliases'),
    '#attributes' => array('class' => array('container-inline')),
  );
  $form['basic']['filter'] = array(
    '#type' => 'textfield',
    '#title' => 'Path alias',
    '#title_display' => 'invisible',
    '#default_value' => $keys,
    '#maxlength' => 128,
    '#size' => 25,
  );
  $form['basic']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Filter'),
    '#submit' => array('path_admin_filter_form_submit_filter'),
    );
  if ($keys) {
    $form['basic']['reset'] = array(
      '#type' => 'submit',
      '#value' => t('Reset'),
      '#submit' => array('path_admin_filter_form_submit_reset'),
    );
  }
  return $form;
}
```

---
_Drupal 7.103 · [modules/path/path.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
