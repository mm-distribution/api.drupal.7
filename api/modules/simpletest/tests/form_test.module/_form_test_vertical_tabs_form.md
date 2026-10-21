# _form_test_vertical_tabs_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 707–732 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L707-L732)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_vertical_tabs_form($form, &$form_state)
```

## Documentation

```text
Tests functionality of vertical tabs.
```

## Code

```php
function _form_test_vertical_tabs_form($form, &$form_state) {
  $form['vertical_tabs'] = array(
    '#type' => 'vertical_tabs',
  );
  $form['tab1'] = array(
    '#type' => 'fieldset',
    '#title' => t('Tab 1'),
    '#collapsible' => TRUE,
    '#group' => 'vertical_tabs',
  );
  $form['tab1']['field1'] = array(
    '#title' => t('Field 1'),
    '#type' => 'textfield',
  );
  $form['tab2'] = array(
    '#type' => 'fieldset',
    '#title' => t('Tab 2'),
    '#collapsible' => TRUE,
    '#group' => 'vertical_tabs',
  );
  $form['tab2']['field2'] = array(
    '#title' => t('Field 2'),
    '#type' => 'textfield',
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
