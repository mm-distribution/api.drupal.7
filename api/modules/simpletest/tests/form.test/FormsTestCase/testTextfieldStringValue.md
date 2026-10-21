# FormsTestCase::testTextfieldStringValue()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 477–495 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L477-L495)
- **Class:** [FormsTestCase](../FormsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testTextfieldStringValue()
```

## Documentation

```text
Tests that submitted values are converted to scalar strings for textfields.
```

## Code

```php
  public function testTextfieldStringValue() {
    // Check multivalued submissions.
    $multivalue = array('evil' => 'multivalue', 'not so' => 'good');
    $this->checkFormValue('textfield', $multivalue, '');
    $this->checkFormValue('password', $multivalue, '');
    $this->checkFormValue('textarea', $multivalue, '');
    $this->checkFormValue('machine_name', $multivalue, '');
    $this->checkFormValue('password_confirm', $multivalue, array('pass1' => '', 'pass2' => ''));
    // Check integer submissions.
    $integer = 5;
    $string = '5';
    $this->checkFormValue('textfield', $integer, $string);
    $this->checkFormValue('password', $integer, $string);
    $this->checkFormValue('textarea', $integer, $string);
    $this->checkFormValue('machine_name', $integer, $string);
    $this->checkFormValue('password_confirm', array('pass1' => $integer, 'pass2' => $integer), array('pass1' => $string, 'pass2' => $string));
    // Check that invalid array keys are ignored for password confirm elements.
    $this->checkFormValue('password_confirm', array('pass1' => 'test', 'pass2' => 'test', 'extra' => 'invalid'), array('pass1' => 'test', 'pass2' => 'test'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
