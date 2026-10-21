# FormsElementsValidationTestCase::testMaxlengthValidation()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 792–829 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L792-L829)
- **Class:** [FormsElementsValidationTestCase](../FormsElementsValidationTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testMaxlengthValidation()
```

## Documentation

```text
Tests #maxlength validation.
```

## Code

```php
  public function testMaxlengthValidation() {
    $max_length = 5;
    // The field types that support #maxlength.
    $form = array(
      'textfield' => array(
        '#type' => 'textfield',
        '#title' => 'Textfield',
        '#required' => FALSE,
        '#maxlength' => $max_length,
      ),
      'password' => array(
        '#type' => 'password',
        '#title' => 'Password',
        '#maxlength' => $max_length,
      ),
    );

    $edit = array(
      'textfield' => $this->randomString($max_length + 1),
      'password' => $this->randomString($max_length + 1),
    );
    list($processed_form, $form_state, $errors) = $this->formSubmitHelper($form, $edit);
    $this->assertFalse(empty($errors), 'Form with overly long inputs returned errors.');
    $this->assertTrue(isset($errors['textfield']) && strpos($errors['textfield'], 'cannot be longer than') !== FALSE, 'Long input error in textfield.');
    $this->assertTrue(isset($errors['password']) && strpos($errors['password'], 'cannot be longer than') !== FALSE, 'Long input error in password.');

    // This test for NULL inputs cannot be performed using the drupalPost() method.
    $edit['textfield'] = NULL;
    $edit['password'] = NULL;
    list($processed_form, $form_state, $errors) = $this->formSubmitHelper($form, $edit);
    $this->assertTrue(empty($errors), 'Form with NULL inputs did not return errors.');

    $edit['textfield'] = $this->randomString($max_length);
    $edit['password'] = $this->randomString($max_length);
    list($processed_form, $form_state, $errors) = $this->formSubmitHelper($form, $edit);
    $this->assertTrue(empty($errors), 'Form with maxlength inputs did not return errors.');

  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
