# FileNameMungingTest::testMunging()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2830–2837 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2830-L2837)
- **Class:** [FileNameMungingTest](../FileNameMungingTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testMunging()
```

## Documentation

```text
Create a file and munge/unmunge the name.
```

## Code

```php
  function testMunging() {
    // Disable insecure uploads.
    variable_set('allow_insecure_uploads', 0);
    $munged_name = file_munge_filename($this->name, '', TRUE);
    $messages = drupal_get_messages();
    $this->assertTrue(in_array(t('For security reasons, your upload has been renamed to %filename.', array('%filename' => $munged_name)), $messages['status']), 'Alert properly set when a file is renamed.');
    $this->assertNotEqual($munged_name, $this->name, format_string('The new filename (%munged) has been modified from the original (%original)', array('%munged' => $munged_name, '%original' => $this->name)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
