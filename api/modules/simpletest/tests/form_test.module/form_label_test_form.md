# form_label_test_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 942–1037 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L942-L1037)
- **Module/theme:** batch_test

## Signature

```php
function form_label_test_form()
```

## Documentation

```text
A form for testing form labels and required marks.
```

## Code

```php
function form_label_test_form() {
  $form['form_checkboxes_test'] = array(
    '#type' => 'checkboxes',
    '#title' => t('Checkboxes test'),
    '#options' => array(
      'first-checkbox' => t('First checkbox'),
      'second-checkbox' => t('Second checkbox'),
      'third-checkbox' => t('Third checkbox'),
      '0' => t('0'),
    ),
  );
  $form['form_radios_test'] = array(
    '#type' => 'radios',
    '#title' => t('Radios test'),
    '#options' => array(
      'first-radio' => t('First radio'),
      'second-radio' => t('Second radio'),
      'third-radio' => t('Third radio'),
      '0' => t('0'),
    ),
    // Test #field_prefix and #field_suffix placement.
    '#field_prefix' => '<span id="form-test-radios-field-prefix">' . t('Radios #field_prefix element') . '</span>',
    '#field_suffix' => '<span id="form-test-radios-field-suffix">' . t('Radios #field_suffix element') . '</span>',
  );
  $form['form_checkbox_test'] = array(
    '#type' => 'checkbox',
    '#title' => t('Checkbox test'),
  );
  $form['form_textfield_test_title_and_required'] = array(
    '#type' => 'textfield',
    '#title' => t('Textfield test for required with title'),
    '#required' => TRUE,
  );
  $form['form_textfield_test_no_title_required'] = array(
    '#type' => 'textfield',
    // We use an empty title, since not setting #title suppresses the label
    // and required marker.
    '#title' => '',
    '#required' => TRUE,
  );
  $form['form_textfield_test_title'] = array(
    '#type' => 'textfield',
    '#title' => t('Textfield test for title only'),
    // Not required.
    // Test #prefix and #suffix placement.
    '#prefix' => '<div id="form-test-textfield-title-prefix">' . t('Textfield #prefix element') . '</div>',
    '#suffix' => '<div id="form-test-textfield-title-suffix">' . t('Textfield #suffix element') . '</div>',
  );
  $form['form_textfield_test_title_after'] = array(
    '#type' => 'textfield',
    '#title' => t('Textfield test for title after element'),
    '#title_display' => 'after',
  );
  $form['form_textfield_test_title_invisible'] = array(
    '#type' => 'textfield',
    '#title' => t('Textfield test for invisible title'),
    '#title_display' => 'invisible',
  );
  // Textfield test for title set not to display.
  $form['form_textfield_test_title_no_show'] = array(
    '#type' => 'textfield',
  );
  // Checkboxes & radios with title as attribute.
  $form['form_checkboxes_title_attribute'] = array(
    '#type' => 'checkboxes',
    '#title' => 'Checkboxes test',
    '#options' => array(
      'first-checkbox' => 'First checkbox',
      'second-checkbox' => 'Second checkbox',
    ),
    '#title_display' => 'attribute',
    '#required' => TRUE,
  );
  $form['form_radios_title_attribute'] = array(
    '#type' => 'radios',
    '#title' => 'Radios test',
    '#options' => array(
      'first-radio' => 'First radio',
      'second-radio' => 'Second radio',
    ),
    '#title_display' => 'attribute',
    '#required' => TRUE,
  );
  // Button elements with and without name attribute.
  $form['form_button_with_name'] = array(
    '#type' => 'button',
    '#value' => t('Button with name'),
  );
  $form['form_button_without_name'] = array(
    '#type' => 'button',
    '#value' => t('Button without name'),
    '#name' => '',
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
