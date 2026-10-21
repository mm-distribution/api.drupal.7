# FileValidateTest::testInsecureExtensions()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2415–2429 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2415-L2429)
- **Class:** [FileValidateTest](../FileValidateTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function testInsecureExtensions()
```

## Documentation

```text
Tests hard-coded security check in file_validate().
```

## Code

```php
  public function testInsecureExtensions() {
    $file = $this->createFile('test.php', 'Invalid PHP');

    // Test that file_validate() will check for insecure extensions by default.
    $errors = file_validate($file, array());
    $this->assertEqual('For security reasons, your upload has been rejected.', $errors[0]);
    $this->assertFileHooksCalled(array('validate'));
    file_test_reset();

    // Test that the 'allow_insecure_uploads' is respected.
    variable_set('allow_insecure_uploads', 1);
    $errors = file_validate($file, array());
    $this->assertEqual(array(), $errors);
    $this->assertFileHooksCalled(array('validate'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
