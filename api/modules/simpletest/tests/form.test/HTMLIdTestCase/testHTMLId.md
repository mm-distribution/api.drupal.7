# HTMLIdTestCase::testHTMLId()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 2301–2309 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L2301-L2309)
- **Class:** [HTMLIdTestCase](../HTMLIdTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testHTMLId()
```

## Documentation

```text
Tests that HTML IDs do not get duplicated when form validation fails.
```

## Code

```php
  function testHTMLId() {
    $this->drupalGet('form-test/double-form');
    $this->assertNoDuplicateIds('There are no duplicate IDs');

    // Submit second form with empty title.
    $edit = array();
    $this->drupalPost(NULL, $edit, 'Save', array(), array(), 'form-test-html-id--2');
    $this->assertNoDuplicateIds('There are no duplicate IDs');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
