# form_test_checkboxes_radios()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1305–1359 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1305-L1359)
- **Module/theme:** batch_test

## Signature

```php
function form_test_checkboxes_radios($form, &$form_state, $customize = FALSE)
```

## Documentation

```text
Form constructor to test expansion of #type checkboxes and radios.
```

## Code

```php
function form_test_checkboxes_radios($form, &$form_state, $customize = FALSE) {
  $form['#submit'] = array('_form_test_submit_values_json');

  // Expand #type checkboxes, setting custom element properties for some but not
  // all options.
  $form['checkboxes'] = array(
    '#type' => 'checkboxes',
    '#title' => 'Checkboxes',
    '#options' => array(
      0 => 'Zero',
      'foo' => 'Foo',
      1 => 'One',
      'bar' => 'Bar',
      '>' => 'Special Char',
    ),
  );
  if ($customize) {
    $form['checkboxes'] += array(
      'foo' => array(
        '#description' => 'Enable to foo.',
      ),
      1 => array(
        '#weight' => 10,
      ),
    );
  }

  // Expand #type radios, setting custom element properties for some but not
  // all options.
  $form['radios'] = array(
    '#type' => 'radios',
    '#title' => 'Radios',
    '#options' => array(
      0 => 'Zero',
      'foo' => 'Foo',
      1 => 'One',
      'bar' => 'Bar',
      '>' => 'Special Char',
    ),
  );
  if ($customize) {
    $form['radios'] += array(
      'foo' => array(
        '#description' => 'Enable to foo.',
      ),
      1 => array(
        '#weight' => 10,
      ),
    );
  }

  $form['submit'] = array('#type' => 'submit', '#value' => 'Submit');

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
