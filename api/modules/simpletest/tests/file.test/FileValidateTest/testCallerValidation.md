# FileValidateTest::testCallerValidation()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2389–2410 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2389-L2410)
- **Class:** [FileValidateTest](../FileValidateTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testCallerValidation()
```

## Documentation

```text
Test that the validators passed into are checked.
```

## Code

```php
  function testCallerValidation() {
    $file = $this->createFile();

    // Empty validators.
    $this->assertEqual(file_validate($file, array()), array(), 'Validating an empty array works successfully.');
    $this->assertFileHooksCalled(array('validate'));

    // Use the file_test.module's test validator to ensure that passing tests
    // return correctly.
    file_test_reset();
    file_test_set_return('validate', array());
    $passing = array('file_test_validator' => array(array()));
    $this->assertEqual(file_validate($file, $passing), array(), 'Validating passes.');
    $this->assertFileHooksCalled(array('validate'));

    // Now test for failures in validators passed in and by hook_validate.
    file_test_reset();
    file_test_set_return('validate', array('Epic fail'));
    $failing = array('file_test_validator' => array(array('Failed', 'Badly')));
    $this->assertEqual(file_validate($file, $failing), array('Failed', 'Badly', 'Epic fail'), 'Validating returns errors.');
    $this->assertFileHooksCalled(array('validate'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
