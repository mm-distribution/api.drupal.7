# form_test_clicked_button()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1782–1836 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1782-L1836)
- **Module/theme:** batch_test

## Signature

```php
function form_test_clicked_button($form, &$form_state)
```

## Documentation

```text
Form builder to test button click detection.
```

## Code

```php
function form_test_clicked_button($form, &$form_state) {
  // A single text field. In IE, when a form has only one non-button input field
  // and the ENTER key is pressed while that field has focus, the form is
  // submitted without any information identifying the button responsible for
  // the submission. In other browsers, the form is submitted as though the
  // first button were clicked.
  $form['text'] = array(
    '#title' => 'Text',
    '#type' => 'textfield',
  );

  // Loop through each path argument, addding buttons based on the information
  // in the argument. For example, if the path is
  // form-test/clicked-button/s/i/rb, then 3 buttons are added: a 'submit', an
  // 'image_button', and a 'button' with #access=FALSE. This enables form.test
  // to test a variety of combinations.
  $i=0;
  $args = array_slice(arg(), 2);
  foreach ($args as $arg) {
    $name = 'button' . ++$i;
    // 's', 'b', or 'i' in the argument define the button type wanted.
    if (strpos($arg, 's') !== FALSE) {
      $type = 'submit';
    }
    elseif (strpos($arg, 'b') !== FALSE) {
      $type = 'button';
    }
    elseif (strpos($arg, 'i') !== FALSE) {
      $type = 'image_button';
    }
    else {
      $type = NULL;
    }
    if (isset($type)) {
      $form[$name] = array(
        '#type' => $type,
        '#name' => $name,
      );
      // Image buttons need a #src; the others need a #value.
      if ($type == 'image_button') {
        $form[$name]['#src'] = 'misc/druplicon.png';
      }
      else {
        $form[$name]['#value'] = $name;
      }
      // 'r' for restricted, so we can test that button click detection code
      // correctly takes #access security into account.
      if (strpos($arg, 'r') !== FALSE) {
        $form[$name]['#access'] = FALSE;
      }
    }
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
