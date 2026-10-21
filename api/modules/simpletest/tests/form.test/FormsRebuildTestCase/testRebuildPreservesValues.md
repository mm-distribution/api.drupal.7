# FormsRebuildTestCase::testRebuildPreservesValues()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1747–1764 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1747-L1764)
- **Class:** [FormsRebuildTestCase](../FormsRebuildTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRebuildPreservesValues()
```

## Documentation

```text
Tests preservation of values.
```

## Code

```php
  function testRebuildPreservesValues() {
    $edit = array(
      'checkbox_1_default_off' => TRUE,
      'checkbox_1_default_on' => FALSE,
      'text_1' => 'foo',
    );
    $this->drupalPost('form-test/form-rebuild-preserve-values', $edit, 'Add more');

    // Verify that initial elements retained their submitted values.
    $this->assertFieldChecked('edit-checkbox-1-default-off', 'A submitted checked checkbox retained its checked state during a rebuild.');
    $this->assertNoFieldChecked('edit-checkbox-1-default-on', 'A submitted unchecked checkbox retained its unchecked state during a rebuild.');
    $this->assertFieldById('edit-text-1', 'foo', 'A textfield retained its submitted value during a rebuild.');

    // Verify that newly added elements were initialized with their default values.
    $this->assertFieldChecked('edit-checkbox-2-default-on', 'A newly added checkbox was initialized with a default checked state.');
    $this->assertNoFieldChecked('edit-checkbox-2-default-off', 'A newly added checkbox was initialized with a default unchecked state.');
    $this->assertFieldById('edit-text-2', 'DEFAULT 2', 'A newly added textfield was initialized with its default value.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
