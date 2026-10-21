# FileCopyTest::testNormal()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1977–2001 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1977-L2001)
- **Class:** [FileCopyTest](../FileCopyTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testNormal()
```

## Documentation

```text
Test file copying in the normal, base case.
```

## Code

```php
  function testNormal() {
    $contents = $this->randomName(10);
    $source = $this->createFile(NULL, $contents);
    $desired_uri = 'public://' . $this->randomName();

    // Clone the object so we don't have to worry about the function changing
    // our reference copy.
    $result = file_copy(clone $source, $desired_uri, FILE_EXISTS_ERROR);

    // Check the return status and that the contents changed.
    $this->assertTrue($result, 'File copied successfully.');
    $this->assertEqual($contents, file_get_contents($result->uri), 'Contents of file were copied correctly.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('copy', 'insert'));

    $this->assertDifferentFile($source, $result);
    $this->assertEqual($result->uri, $desired_uri, 'The copied file object has the desired filepath.');
    $this->assertTrue(file_exists($source->uri), 'The original file still exists.');
    $this->assertTrue(file_exists($result->uri), 'The copied file exists.');

    // Reload the file from the database and check that the changes were
    // actually saved.
    $this->assertFileUnchanged($result, file_load($result->fid, TRUE));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
