# FormsTestCase::testDisabledMarkup()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 407–459 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L407-L459)
- **Class:** [FormsTestCase](../FormsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDisabledMarkup()
```

## Documentation

```text
Verify markup for disabled form elements.

@see _form_test_disabled_elements()
```

## Code

```php
  function testDisabledMarkup() {
    $this->drupalGet('form-test/disabled-elements');
    $form_state = array();
    $form = _form_test_disabled_elements(array(), $form_state);
    $type_map = array(
      'textarea' => 'textarea',
      'select' => 'select',
      'weight' => 'select',
      'date' => 'select',
    );

    foreach ($form as $name => $item) {
      // Skip special #types.
      if (!isset($item['#type']) || in_array($item['#type'], array('hidden', 'text_format'))) {
        continue;
      }
      // Setup XPath and CSS class depending on #type.
      if (in_array($item['#type'], array('image_button', 'button', 'submit'))) {
        $path = "//!type[contains(@class, :div-class) and @value=:value]";
        $class = 'form-button-disabled';
      }
      else {
        // starts-with() required for checkboxes.
        $path = "//div[contains(@class, :div-class)]/descendant::!type[starts-with(@name, :name)]";
        $class = 'form-disabled';
      }
      // Replace DOM element name in $path according to #type.
      $type = 'input';
      if (isset($type_map[$item['#type']])) {
        $type = $type_map[$item['#type']];
      }
      $path = strtr($path, array('!type' => $type));
      // Verify that the element exists.
      $element = $this->xpath($path, array(
        ':name' => check_plain($name),
        ':div-class' => $class,
        ':value' => isset($item['#value']) ? $item['#value'] : '',
      ));
      $this->assertTrue(isset($element[0]), format_string('Disabled form element class found for #type %type.', array('%type' => $item['#type'])));
    }

    // Verify special element #type text-format.
    $element = $this->xpath('//div[contains(@class, :div-class)]/descendant::textarea[@name=:name]', array(
      ':name' => 'text_format[value]',
      ':div-class' => 'form-disabled',
    ));
    $this->assertTrue(isset($element[0]), format_string('Disabled form element class found for #type %type.', array('%type' => 'text_format[value]')));
    $element = $this->xpath('//div[contains(@class, :div-class)]/descendant::select[@name=:name]', array(
      ':name' => 'text_format[format]',
      ':div-class' => 'form-disabled',
    ));
    $this->assertTrue(isset($element[0]), format_string('Disabled form element class found for #type %type.', array('%type' => 'text_format[format]')));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
