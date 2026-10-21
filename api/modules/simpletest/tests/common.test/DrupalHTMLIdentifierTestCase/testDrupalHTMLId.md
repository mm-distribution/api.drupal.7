# DrupalHTMLIdentifierTestCase::testDrupalHTMLId()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1070–1088 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1070-L1088)
- **Class:** [DrupalHTMLIdentifierTestCase](../DrupalHTMLIdentifierTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalHTMLId()
```

## Documentation

```text
Tests that drupal_html_id() cleans the ID properly.
```

## Code

```php
  function testDrupalHTMLId() {
    // Verify that letters, digits, and hyphens are not stripped from the ID.
    $id = 'abcdefghijklmnopqrstuvwxyz-0123456789';
    $this->assertIdentical(drupal_html_id($id), $id, 'Verify valid characters pass through.');

    // Verify that invalid characters are stripped from the ID.
    $this->assertIdentical(drupal_html_id('invalid,./:@\\^`{Üidentifier'), 'invalididentifier', 'Strip invalid characters.');

    // Verify Drupal coding standards are enforced.
    $this->assertIdentical(drupal_html_id('ID NAME_[1]'), 'id-name-1', 'Enforce Drupal coding standards.');

    // Reset the static cache so we can ensure the unique id count is at zero.
    drupal_static_reset('drupal_html_id');

    // Clean up IDs with invalid starting characters.
    $this->assertIdentical(drupal_html_id('test-unique-id'), 'test-unique-id', 'Test the uniqueness of IDs #1.');
    $this->assertIdentical(drupal_html_id('test-unique-id'), 'test-unique-id--2', 'Test the uniqueness of IDs #2.');
    $this->assertIdentical(drupal_html_id('test-unique-id'), 'test-unique-id--3', 'Test the uniqueness of IDs #3.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
